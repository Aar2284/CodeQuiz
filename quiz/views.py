from django.conf import settings
from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from django.http import HttpResponse
from reportlab.pdfgen import canvas
import random
import string

from .forms import QuizForm, QuestionForm, OptionForm
from .models import Option, Question, Quiz, Attempt

def generate_quiz_code():
    return ''.join(random.choices(string.ascii_uppercase + string.digits, k=6))

@login_required
def create_quiz(request):
    if request.user.role != 'teacher':
        return redirect('login')

    if request.method == "POST":
        form = QuizForm(request.POST)
        if form.is_valid():
            quiz = form.save(commit=False) 
            quiz.created_by = request.user 
            quiz.save() # quiz_code generated in model save()
            return redirect('add_question', quiz_id=quiz.id)
    else:
        form = QuizForm()

    return render(request, 'quiz/create_quiz.html', {'form': form})

@login_required
def add_question(request, quiz_id):
    quiz = get_object_or_404(Quiz, id=quiz_id)

    if request.method == "POST":
        question_text = request.POST.get("question_text")
        marks = request.POST.get("marks")
        correct_index = request.POST.get("correct_option")

        if not question_text or correct_index is None:
            return render(request, "quiz/add_question.html", {
                "quiz": quiz,
                "error": "Question text and correct option are required"
            })

        question = Question.objects.create(
            quiz=quiz,
            text=question_text,
            marks=marks
        )

        options = [
            request.POST.get("option1"),
            request.POST.get("option2"),
            request.POST.get("option3"),
            request.POST.get("option4"),
        ]

        correct_index = int(correct_index)

        for i, option_text in enumerate(options):
            if option_text:
                Option.objects.create(
                    question=question,
                    text=option_text,
                    is_correct=(i == correct_index)
                )

        return redirect("add_question", quiz_id=quiz.id)

    return render(request, "quiz/add_question.html", {"quiz": quiz})

@login_required
def add_option(request):
    if request.method == "POST":
        form = OptionForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Option added successfully!")
            return redirect('teacher_dashboard')
    else:
        form = OptionForm()
    return render(request, 'quiz/add_option.html', {'form': form})

@login_required
def publish_quiz(request, quiz_id):
    quiz = get_object_or_404(Quiz, id=quiz_id)
    quiz.is_published = True
    quiz.save()
    messages.success(request, f"Quiz '{quiz.title}' published successfully!")
    return redirect('teacher_dashboard')

@login_required
def view_attempts(request):
    attempts = Attempt.objects.filter(
        quiz__created_by=request.user
    ).order_by('-submitted_at')
    return render(request, 'quiz/view_attempts.html', {'attempts': attempts})

@login_required
def download_pdf(request):
    attempts = Attempt.objects.filter(quiz__created_by=request.user)
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="results.pdf"'
    p = canvas.Canvas(response)
    y = 800
    p.drawString(100, y, "Quiz Results Summary")
    y -= 30
    for attempt in attempts:
        text = f"{attempt.student.username} - {attempt.quiz.title} - Score: {attempt.score}/{attempt.total_marks}"
        p.drawString(50, y, text)
        y -= 20
        if y < 50:
            p.showPage()
            y = 800
    p.save()
    return response

@login_required
def enter_quiz_code(request):
    if request.user.role != 'student':
        return redirect('login')

    if request.method == "POST":
        code = request.POST.get('quiz_code')
        quiz = Quiz.objects.filter(quiz_code=code, is_published=True).first()

        if quiz:
            return redirect('attempt_quiz', quiz_id=quiz.id)
        else:
            messages.error(request, 'Invalid or Unpublished Quiz Code')
            return render(request, 'quiz/enter_code.html')

    return render(request, 'quiz/enter_code.html')

@login_required
def attempt_quiz(request, quiz_id):
    quiz = get_object_or_404(Quiz, id=quiz_id)
    questions = Question.objects.filter(quiz=quiz)

    if request.method == "POST":
        score = 0
        total_marks = 0

        for question in questions:
            total_marks += question.marks
            selected_option_id = request.POST.get(str(question.id))

            if selected_option_id:
                try:
                    option = Option.objects.get(id=selected_option_id)
                    if option.is_correct:
                        score += question.marks
                    else:
                        score -= quiz.negative_marking
                except Option.DoesNotExist:
                    pass

        percentage = (score / total_marks) * 100 if total_marks > 0 else 0
        attempt = Attempt.objects.create(
            quiz=quiz,
            student=request.user,
            score=max(0, score),
            total_marks=total_marks,
            percentage=percentage
        )

        # Recalculate ranks for this quiz
        attempts = Attempt.objects.filter(quiz=quiz).order_by('-score')
        for index, attempt_obj in enumerate(attempts):
            attempt_obj.rank = index + 1
            attempt_obj.save()

        return redirect('view_result', attempt_id=attempt.id)

    return render(request, 'attempt_quiz.html', {
        'quiz': quiz,
        'questions': questions
    })

@login_required
def view_result(request, attempt_id):
    attempt = get_object_or_404(Attempt, id=attempt_id)
    return render(request, 'accounts/results.html', {
        'attempt': attempt
    })

@login_required
def past_attempts(request):
    attempts = Attempt.objects.filter(student=request.user).order_by('-submitted_at')
    return render(request, 'quiz/past_attempts.html', {
        'attempts': attempts
    })

@login_required
def available_quizzes(request):
    quizzes = Quiz.objects.filter(is_published=True)
    return render(request, 'available_quizzes.html', {
        'quizzes': quizzes
    })

@login_required
def join_quiz(request):
    if request.method == "POST":
        quiz_id = request.POST.get("quiz_id")
        try:
            quiz = Quiz.objects.get(id=quiz_id, is_published=True)
            return redirect('attempt_quiz', quiz_id=quiz.id)
        except Quiz.DoesNotExist:
            messages.error(request, "Invalid Quiz ID or Quiz not published.")
            return redirect('student_dashboard')
    return redirect('student_dashboard')

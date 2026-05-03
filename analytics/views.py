from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.db.models import Avg, Max, Count
from quiz.models import Quiz, Attempt, Question
from django.contrib.auth import get_user_model

User = get_user_model()

@login_required
def teacher_analytics(request):
    # Ensure only teachers can view this page
    if request.user.role != 'teacher':
        return redirect('student_dashboard')

    # Get all quizzes created by this teacher
    quizzes = Quiz.objects.filter(created_by=request.user)

    # Get all student attempts on these quizzes
    attempts = Attempt.objects.filter(quiz__in=quizzes)

    # Handle quiz filtering
    selected_quiz_id = request.GET.get('quiz_id')
    selected_quiz = None
    if selected_quiz_id:
        try:
            selected_quiz = quizzes.get(id=selected_quiz_id)
            filtered_attempts = attempts.filter(quiz=selected_quiz)
        except (Quiz.DoesNotExist, ValueError):
            filtered_attempts = attempts
    else:
        filtered_attempts = attempts

    # 1. Top 5 student results (highest percentage individual attempts) for the leaderboard
    top_attempts = filtered_attempts.select_related('student', 'quiz').order_by('-percentage')[:5]

    # 2. General statistics
    total_quizzes = quizzes.count()
    total_attempts = attempts.count()
    average_score = attempts.aggregate(Avg('percentage'))['percentage__avg'] or 0
    average_score = round(average_score, 2)

    # Find the most attempted quiz
    most_attempted_quiz = None
    max_attempts = -1
    for quiz in quizzes:
        count = attempts.filter(quiz=quiz).count()
        if count > max_attempts and count > 0:
            max_attempts = count
            most_attempted_quiz = quiz

    # 3. Data for the Quiz Performance Chart (average percentage and attempt counts per quiz)
    quiz_stats = []
    for quiz in quizzes:
        q_attempts = attempts.filter(quiz=quiz)
        q_avg = q_attempts.aggregate(Avg('percentage'))['percentage__avg'] or 0
        quiz_stats.append({
            'title': quiz.title,
            'avg_percentage': round(q_avg, 2),
            'attempts_count': q_attempts.count(),
        })

    # 4. Top 5 consistently high-performing students (by their overall average percentage across all quizzes)
    top_students_avg = attempts.values('student__username').annotate(
        avg_percentage=Avg('percentage'),
        attempts_count=Count('id')
    ).order_by('-avg_percentage')[:5]

    context = {
        'quizzes': quizzes,
        'selected_quiz': selected_quiz,
        'top_attempts': top_attempts,
        'total_quizzes': total_quizzes,
        'total_attempts': total_attempts,
        'average_score': average_score,
        'most_attempted_quiz': most_attempted_quiz,
        'quiz_stats': quiz_stats,
        'top_students_avg': top_students_avg,
    }

    return render(request, 'analytics/teacher_analytics.html', context)

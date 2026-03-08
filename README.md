# 📝 CodeQuiz - Advanced Quiz Management System

<div align="center">

  <img src="https://img.shields.io/badge/CodeQuiz-1E293B?style=for-the-badge&logo=codeforces&logoColor=white" alt="Logo" />

  <p align="center">
    A robust, role-based quiz platform built with Django, featuring automated grading, real-time timers, and performance analytics.
    <br />
    <a href="#-key-features"><strong>Explore the features »</strong></a>
    <br />
    <br />
    <a href="#-quick-start">Quick Start</a>
    ·
    <a href="#-screens">Screenshots</a>
    ·
    <a href="#-contribution">Contribution</a>
  </p>
</div>

---

## 🚀 Tech Stack

### 🌐 Languages Used
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![HTML5](https://img.shields.io/badge/html5-%23E34F26.svg?style=for-the-badge&logo=html5&logoColor=white)
![CSS3](https://img.shields.io/badge/css3-%231572B6.svg?style=for-the-badge&logo=css3&logoColor=white)
![JavaScript](https://img.shields.io/badge/javascript-%23F7DF1E.svg?style=for-the-badge&logo=javascript&logoColor=black)

### ⚙️ Frameworks & Libraries
![Django](https://img.shields.io/badge/django-%23092E20.svg?style=for-the-badge&logo=django&logoColor=white)
![Bootstrap](https://img.shields.io/badge/bootstrap-%238511FA.svg?style=for-the-badge&logo=bootstrap&logoColor=white)
![SQLite](https://img.shields.io/badge/sqlite-%2307405e.svg?style=for-the-badge&logo=sqlite&logoColor=white)

---

## ✨ Key Features

<details>
<summary><b>👨‍🏫 For Teachers</b> (Click to expand)</summary>
<br>

- **Dynamic Quiz Creation:** Create quizzes with titles, descriptions, and custom timers.
- **Question Management:** Add multiple-choice questions with weighted marks.
- **Unique Quiz Codes:** Automatically generate 6-digit alphanumeric codes for secure quiz access.
- **Student Monitoring:** View all student attempts, scores, and rankings in real-time.
- **PDF Report Generation:** Export quiz results and student performance data into professional PDF reports.
- **Negative Marking:** Optional support for negative marking to ensure academic integrity.
</details>

<details>
<summary><b>👨‍🎓 For Students</b> (Click to expand)</summary>
<br>

- **Seamless Access:** Join any quiz instantly using a unique access code.
- **Timed Environment:** Real-time countdown timers to simulate exam conditions.
- **Instant Grading:** Get immediate feedback and results after submission.
- **Performance Analytics:** View percentages, total marks, and global rankings.
- **History Tracking:** Access past attempts and review performance trends.
</details>

---

## 🛠️ Installation & Setup

### 📋 Prerequisites
* Python 3.10+
* pip (Python Package Manager)

### ⚙️ Quick Start

1. **Clone the Repository**
   ```bash
   git clone https://github.com/yourusername/CodeQuiz.git
   cd CodeQuiz
   ```

2. **Setup Virtual Environment**
   ```bash
   python -m venv venv
   # Windows
   .\venv\Scripts\activate
   # Linux/Mac
   source venv/bin/activate
   ```

3. **Configure Environment Variables**
   ```bash
   cp .env.example .env
   # Edit .env with your configuration
   ```

4. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

5. **Database Migrations**
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

6. **Create Superuser (Optional)**
   ```bash
   python manage.py createsuperuser
   ```

7. **Run Server**
   ```bash
   python manage.py runserver
   ```

The application will be available at `http://127.0.0.1:8000`

---

## 📂 Project Structure

```text
CodeQuiz/
├── accounts/          # User management, Roles & Authentication
├── quiz/              # Quiz core logic, Models, Views & PDF Logic
├── templates/         # UI Components & Dashboard Layouts
├── quizz/             # Project Settings & Root Configurations
├── manage.py          # Django management script
├── requirements.txt   # Project dependencies
└── .env.example       # Template for environment variables
```

---

## 🎨 UI & Aesthetics

The project features a **modern dark-themed UI** inspired by enterprise-level dashboards.

*   **Color Palette:** `#0F172A` (Background), `#1E293B` (Cards), `#2563EB` (Primary Accents)
*   **Typography:** 'Poppins', sans-serif
*   **Interactivity:** Smooth transitions and hover effects for a premium feel.

---

## 🤝 Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

---

## 📄 License

Distributed under the MIT License. See `LICENSE` for more information.

---

<div align="center">
  <p>Made with ❤️ by Aaryan</p>
  <a href="https://github.com/yourusername">
    <img src="https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white" />
  </a>
</div>

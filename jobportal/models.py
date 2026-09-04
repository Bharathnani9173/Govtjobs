from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


# =========================================================
# JOB
# =========================================================

class Job(models.Model):

    JOB_TYPE_CHOICES = [
        ("Central", "Central Government"),
        ("Telangana", "Telangana Government"),
    ]

    CATEGORY_CHOICES = [
        ("SSC", "SSC"),
        ("UPSC", "UPSC"),
        ("Railway", "Railway"),
        ("Bank", "Bank"),
        ("Police", "Police"),
        ("Defence", "Defence"),
        ("Teaching", "Teaching"),
        ("PSU", "PSU"),
        ("State PSC", "State PSC"),
        ("High Court", "High Court"),
        ("Health", "Health"),
        ("Other", "Other"),
    ]

    APPLICATION_MODE_CHOICES = [
        ("Online", "Online"),
        ("Offline", "Offline"),
    ]

    title = models.CharField(max_length=200)

    organization = models.CharField(max_length=200)

    job_type = models.CharField(
        max_length=30,
        choices=JOB_TYPE_CHOICES,
        default="Central"
    )

    category = models.CharField(
        max_length=50,
        choices=CATEGORY_CHOICES,
        default="Other"
    )

    state = models.CharField(
        max_length=100,
        default="All India"
    )

    location = models.CharField(
        max_length=150,
        default="All India"
    )

    qualification = models.CharField(
        max_length=200
    )

    age_limit = models.CharField(
        max_length=100,
        default="18-35 Years"
    )

    vacancies = models.PositiveIntegerField(
        default=0
    )

    salary = models.CharField(
        max_length=100,
        default="As Per Rules"
    )

    application_mode = models.CharField(
        max_length=20,
        choices=APPLICATION_MODE_CHOICES,
        default="Online"
    )

    notification_date = models.DateField(
        default=timezone.now
    )

    last_date = models.DateField()

    official_link = models.URLField(
        max_length=500
    )

    description = models.TextField()

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    updated_at = models.DateTimeField(
        auto_now=True
    )

    class Meta:
        ordering = ["-notification_date"]

    def __str__(self):
        return self.title


# =========================================================
# RESULT
# =========================================================

class Result(models.Model):

    exam_name = models.CharField(
        max_length=200
    )

    result_date = models.DateField()

    official_link = models.URLField()

    def __str__(self):
        return self.exam_name


# =========================================================
# ADMIT CARD
# =========================================================

class AdmitCard(models.Model):

    exam_name = models.CharField(
        max_length=200
    )

    release_date = models.DateField()

    official_link = models.URLField()

    def __str__(self):
        return self.exam_name


# =========================================================
# PREVIOUS PAPERS
# =========================================================

class PreviousPaper(models.Model):

    CATEGORY_CHOICES = Job.CATEGORY_CHOICES

    job = models.ForeignKey(
        Job,
        on_delete=models.CASCADE,
        related_name="previous_papers",
        null=True,
        blank=True
    )

    exam_name = models.CharField(
        max_length=200
    )

    category = models.CharField(
        max_length=50,
        choices=CATEGORY_CHOICES,
        default="Other"
    )

    year = models.IntegerField()

    pdf_link = models.CharField(max_length=500)

    def __str__(self):
        return f"{self.exam_name} ({self.year})"


# =========================================================
# ANSWER KEYS
# =========================================================

class AnswerKey(models.Model):

    CATEGORY_CHOICES = Job.CATEGORY_CHOICES

    job = models.ForeignKey(
        Job,
        on_delete=models.CASCADE,
        related_name="answer_keys",
        null=True,
        blank=True
    )

    exam_name = models.CharField(
        max_length=200
    )

    category = models.CharField(
        max_length=50,
        choices=CATEGORY_CHOICES,
        default="Other"
    )

    release_date = models.DateField()

    official_link = models.URLField()

    def __str__(self):
        return self.exam_name


# =========================================================
# CURRENT AFFAIRS
# =========================================================

class CurrentAffair(models.Model):

    CATEGORY_CHOICES = Job.CATEGORY_CHOICES

    job = models.ForeignKey(
        Job,
        on_delete=models.CASCADE,
        related_name="current_affairs",
        null=True,
        blank=True
    )

    title = models.CharField(
        max_length=200
    )

    category = models.CharField(
        max_length=50,
        choices=CATEGORY_CHOICES,
        default="Other"
    )

    date = models.DateField()

    description = models.TextField()

    pdf_link = models.CharField(
    max_length=500,
    blank=True
    )

    def __str__(self):
        return self.title


# =========================================================
# NOTIFICATIONS
# =========================================================

class Notification(models.Model):

    title = models.CharField(
        max_length=200
    )

    organization = models.CharField(
        max_length=200
    )

    last_date = models.DateField()

    official_link = models.URLField()

    def __str__(self):
        return self.title


# =========================================================
# FEEDBACK
# =========================================================

class Feedback(models.Model):

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )

    name = models.CharField(
        max_length=100
    )

    email = models.EmailField()

    rating = models.IntegerField(
        default=5
    )

    message = models.TextField()

    admin_reply = models.TextField(
        blank=True,
        null=True
    )

    status = models.CharField(
        max_length=20,
        default="Acknowledged"
    )

    category = models.CharField(
        max_length=100,
        default="General"
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
        null=True,
        blank=True
    )

    def __str__(self):
        return self.name


# =========================================================
# CONTACT MESSAGES
# =========================================================

class ContactMessage(models.Model):

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )

    name = models.CharField(
        max_length=100
    )

    email = models.EmailField()

    mobile = models.CharField(
        max_length=15
    )

    subject = models.CharField(
        max_length=200
    )

    message = models.TextField()

    admin_reply = models.TextField(
        blank=True,
        null=True
    )

    status = models.CharField(
        max_length=20,
        default="Pending"
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return self.subject


# =========================================================
# SAVED JOBS
# =========================================================

class SavedJob(models.Model):

    job = models.ForeignKey(
        Job,
        on_delete=models.CASCADE
    )

    saved_on = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return self.job.title


# =========================================================
# STUDY MATERIAL
# =========================================================

class StudyMaterial(models.Model):

    SUBJECTS = [
        ("Aptitude", "Aptitude"),
        ("Reasoning", "Reasoning"),
        ("English", "English"),
        ("GK", "General Knowledge"),
        ("Telangana GK", "Telangana GK"),
        ("Computer", "Computer Awareness"),
    ]

    title = models.CharField(
        max_length=200
    )

    subject = models.CharField(
        max_length=50,
        choices=SUBJECTS
    )

    pdf = models.FileField(
        upload_to="study_materials/"
    )

    uploaded_on = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return self.title


# =========================================================
# SUBSCRIBER
# =========================================================

class Subscriber(models.Model):

    email = models.EmailField(
        unique=True
    )

    name = models.CharField(
        max_length=100,
        blank=True
    )

    subscribed_date = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return self.email


# =========================================================
# DAILY QUIZ
# =========================================================

class DailyQuiz(models.Model):

    title = models.CharField(
        max_length=200
    )

    quiz_date = models.DateField(
        unique=True
    )

    def __str__(self):
        return f"{self.title} ({self.quiz_date})"


# =========================================================
# MOCK TEST
# =========================================================

class MockTest(models.Model):

    EXAM_CATEGORIES = [
        ("SSC CGL", "SSC CGL"),
        ("SSC CHSL", "SSC CHSL"),

        ("RRB NTPC", "RRB NTPC"),
        ("RRB Group D", "RRB Group D"),
        ("RRB ALP", "RRB ALP"),
        ("RRB Technician", "RRB Technician"),
        ("RRB JE", "RRB JE"),
        ("Railway Constable", "Railway Constable"),
        ("Railway SI", "Railway SI"),

        ("Banking", "Banking"),

        ("UPSC", "UPSC"),

        ("TGPSC Group 1", "TGPSC Group 1"),
        ("TGPSC Group 2", "TGPSC Group 2"),
        ("TGPSC Group 3", "TGPSC Group 3"),
        ("TGPSC Group 4", "TGPSC Group 4"),

        ("Forest Range Officer", "Forest Range Officer"),

        ("Telangana AE", "Telangana AE"),
        ("Telangana AEE", "Telangana AEE"),

        ("Telangana Police Constable", "Telangana Police Constable"),
        ("Telangana Police SI", "Telangana Police SI"),

        ("DSC", "DSC"),

        ("High Court", "High Court"),
        ("District Court", "District Court"),

        ("Health Department", "Health Department"),
        ("Revenue Department", "Revenue Department"),
    ]

    exam = models.ForeignKey(
        "Exam",
        on_delete=models.CASCADE,
        related_name="mock_tests",
        null=True,
        blank=True
    )

    exam_name = models.CharField(
       max_length=200,
       blank=True,
       null=True
    )

    title = models.CharField(
        max_length=200
    )

    description = models.TextField(
        blank=True
    )

    duration = models.PositiveIntegerField(
        default=60
    )

    questions_per_test = models.PositiveIntegerField(
        default=50
    )

    is_daily = models.BooleanField(
        default=True
    )

    active = models.BooleanField(
        default=True
    )

    created_at = models.DateTimeField(
        null=True,
        blank=True
    )
    
    def __str__(self):
        return f"{self.exam_name} - {self.title}"


# =========================================================
# MOCK TEST QUESTION BANK
# =========================================================

class MockTestQuestion(models.Model):

    SUBJECT_CHOICES = [
        ("Aptitude", "Aptitude"),
        ("Reasoning", "Reasoning"),
        ("English", "English"),
        ("General Knowledge", "General Knowledge"),
        ("Current Affairs", "Current Affairs"),
        ("Computer", "Computer"),
        ("General Science", "General Science"),
        ("Indian Polity", "Indian Polity"),
        ("History", "History"),
        ("Geography", "Geography"),
        ("Economics", "Economics"),
        ("Telangana GK", "Telangana GK"),
        ("Law", "Law"),
        ("Technical", "Technical"),
    ]

    DIFFICULTY_CHOICES = [
        ("Easy", "Easy"),
        ("Medium", "Medium"),
        ("Hard", "Hard"),
    ]

    exam_name = models.CharField(
        max_length=200,
        db_index=True,
        blank=True,
        null=True
    )

    exam = models.ForeignKey(
        "Exam",
        on_delete=models.CASCADE,
        related_name="mock_questions",
        null=True,
        blank=True
    )

    subject = models.CharField(
       max_length=50,
       choices=SUBJECT_CHOICES,
       null=True,
       blank=True
    )
    question = models.TextField()

    option1 = models.CharField(
        max_length=500
    )

    option2 = models.CharField(
        max_length=500
    )

    option3 = models.CharField(
        max_length=500
    )

    option4 = models.CharField(
        max_length=500
    )

    answer = models.CharField(
        max_length=500
    )

    explanation = models.TextField(
        blank=True
    )

    difficulty = models.CharField(
        max_length=20,
        choices=DIFFICULTY_CHOICES,
        default="Medium"
    )

    source = models.CharField(
        max_length=200,
        blank=True
    )

    is_active = models.BooleanField(
        default=True
    )

    created_at = models.DateTimeField(
        null=True,
        blank=True
    )

    def __str__(self):
        return f"{self.exam_name} - {self.question[:60]}"

    class Meta:
        indexes = [
            models.Index(fields=["exam_name"]),
            models.Index(fields=["subject"]),
        ]

# =========================================================
# DAILY MOCK TEST
# =========================================================

class DailyMockTest(models.Model):

    exam_name = models.CharField(
        max_length=200,
        db_index=True
    )

    exam = models.ForeignKey(
        "Exam",
        on_delete=models.CASCADE,
        related_name="daily_mock_tests",
        null=True,
        blank=True
    )

    test_date = models.DateField(
        default=timezone.now
    )

    title = models.CharField(
        max_length=200
    )

    duration = models.PositiveIntegerField(
        default=60
    )

    total_questions = models.PositiveIntegerField(
        default=50
    )

    questions = models.ManyToManyField(
        MockTestQuestion,
        related_name="daily_tests"
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["exam_name", "test_date"],
                name="unique_daily_mock_per_exam"
            )
        ]

    def __str__(self):
        return f"{self.exam_name} - {self.test_date}"

# =========================================================
# QUIZ QUESTIONS
# =========================================================

class QuizQuestion(models.Model):

    job = models.ForeignKey(
        Job,
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )

    exam = models.ForeignKey(
        "Exam",
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )

    question = models.CharField(
        max_length=1000
    )

    option1 = models.CharField(
        max_length=500
    )

    option2 = models.CharField(
        max_length=500
    )

    option3 = models.CharField(
        max_length=500
    )

    option4 = models.CharField(
        max_length=500
    )

    answer = models.CharField(
        max_length=500
    )

    subject = models.CharField(
        max_length=100
    )

    difficulty = models.CharField(
        max_length=20,
        choices=[
            ("Medium", "Medium"),
            ("Tough", "Tough"),
        ],
        default="Medium"
    )

    source = models.CharField(
        max_length=200,
        blank=True,
        default="Practice"
    )

    def __str__(self):
        return self.question[:100]

class QuizQuestionHistory(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="quiz_question_history"
    )

    question = models.ForeignKey(
        QuizQuestion,
        on_delete=models.CASCADE,
        related_name="history"
    )

    exam = models.ForeignKey(
        "Exam",
        on_delete=models.CASCADE,
        related_name="question_history",
        null=True,
        blank=True
    )

    seen_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - Question {self.question.id}"


# =========================================================
# MOCK TEST ATTEMPT
# =========================================================

class MockTestAttempt(models.Model):

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="mock_test_attempts"
    )

    exam = models.ForeignKey(
        "Exam",
        on_delete=models.CASCADE,
        related_name="mock_attempts",
        null=True,
        blank=True
    )

    daily_test = models.ForeignKey(
        DailyMockTest,
        on_delete=models.CASCADE,
        related_name="attempts",
        null=True,
        blank=True
    )

    score = models.PositiveIntegerField(default=0)
    total_questions = models.PositiveIntegerField(default=100)
    correct_answers = models.PositiveIntegerField(default=0)
    wrong_answers = models.PositiveIntegerField(default=0)
    unanswered = models.PositiveIntegerField(default=0)
    time_taken = models.PositiveIntegerField(default=0)

    attempted_at = models.DateTimeField(auto_now_add=True)

    question_ids = models.JSONField(default=list, blank=True)
    answers = models.JSONField(default=dict, blank=True)

    class Meta:
        ordering = ["-attempted_at"]
    def __str__(self):
        if self.daily_test:
            return f"{self.user.username} - {self.daily_test.exam_name} - {self.score}"
        return f"{self.user.username} - Mock Test - {self.score}"

class QuizAttempt(models.Model):

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )

    score = models.IntegerField()

    total_questions = models.IntegerField(
        default=20
    )

    attempted_date = models.DateField(
        auto_now_add=True
    )

    time_taken = models.IntegerField(
        default=0
    )

    question_ids = models.JSONField(
        default=list,
        blank=True
    )

    def __str__(self):
        return f"{self.user.username} - {self.score}"

        
# =========================================================
# EXAM
# =========================================================

class Exam(models.Model):

    STATUS_CHOICES = [
        ("Upcoming", "Upcoming"),
        ("Application Open", "Application Open"),
        ("Application Closed", "Application Closed"),
        ("Exam Soon", "Exam Soon"),
        ("Exam Completed", "Exam Completed"),
        ("Result Released", "Result Released"),
    ]

    name = models.CharField(
        max_length=200
    )

    organization = models.CharField(
        max_length=200,
        blank=True
    )

    state = models.CharField(
        max_length=100,
        default="Telangana"
    )

    vacancies = models.PositiveIntegerField(
        null=True,
        blank=True
    )

    application_start = models.DateField(
        null=True,
        blank=True
    )

    application_end = models.DateField(
        null=True,
        blank=True
    )

    exam_date = models.DateField(
        null=True,
        blank=True
    )

    status = models.CharField(
        max_length=50,
        choices=STATUS_CHOICES,
        default="Upcoming"
    )

    eligibility = models.TextField(
        blank=True
    )

    syllabus = models.TextField(
        blank=True
    )

    official_link = models.URLField(
        blank=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return self.name


# =========================================================
# SYLLABUS
# =========================================================

class Syllabus(models.Model):

    job = models.OneToOneField(
        Job,
        on_delete=models.CASCADE,
        related_name="syllabus"
    )

    title = models.CharField(
        max_length=200
    )

    description = models.TextField(
        blank=True
    )

    pdf_link = models.URLField(
        blank=True
    )

    def __str__(self):
        return f"{self.job.title} Syllabus"
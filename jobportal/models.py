from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

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

    qualification = models.CharField(max_length=200)

    age_limit = models.CharField(
        max_length=100,
        default="18-35 Years"
    )

    vacancies = models.PositiveIntegerField(default=0)

    salary = models.CharField(
        max_length=100,
        default="As Per Rules"
    )

    application_mode = models.CharField(
        max_length=20,
        choices=APPLICATION_MODE_CHOICES,
        default="Online"
    )

    notification_date = models.DateField(default=timezone.now)

    last_date = models.DateField()

    official_link = models.URLField(max_length=500)

    description = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)

    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-notification_date"]

    def __str__(self):
        return self.title
    
class Result(models.Model):
    exam_name = models.CharField(max_length=200)
    result_date = models.DateField()
    official_link = models.URLField()

    def __str__(self):
        return self.exam_name
       
class AdmitCard(models.Model):
    exam_name = models.CharField(max_length=200)
    release_date = models.DateField()
    official_link = models.URLField()

    def __str__(self):
        return self.exam_name


class AnswerKey(models.Model):
    exam_name = models.CharField(max_length=200)
    release_date = models.DateField()
    official_link = models.URLField()

    def __str__(self):
        return self.exam_name


class PreviousPaper(models.Model):
    exam_name = models.CharField(max_length=200)
    year = models.IntegerField()
    pdf_link = models.URLField()

    def __str__(self):
        return f"{self.exam_name} ({self.year})"


class CurrentAffair(models.Model):
    title = models.CharField(max_length=200)
    category = models.CharField(max_length=100)
    date = models.DateField()
    description = models.TextField()

    def __str__(self):
        return self.title


class Notification(models.Model):
    title = models.CharField(max_length=200)
    organization = models.CharField(max_length=200)
    last_date = models.DateField()
    official_link = models.URLField()

    def __str__(self):
        return self.title


class Feedback(models.Model):

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )

    name = models.CharField(max_length=100)
    email = models.EmailField()
    rating = models.IntegerField(default=5)
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

class ContactMessage(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )

    name = models.CharField(max_length=100)
    email = models.EmailField()
    mobile = models.CharField(max_length=15)
    subject = models.CharField(max_length=200)
    message = models.TextField()

    admin_reply = models.TextField(
        blank=True,
        null=True
    )

    status = models.CharField(
        max_length=20,
        default="Pending"
    )

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.subject


class SavedJob(models.Model):
    job = models.ForeignKey(Job, on_delete=models.CASCADE)
    saved_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.job.title


class StudyMaterial(models.Model):
    SUBJECTS = [
        ('Aptitude', 'Aptitude'),
        ('Reasoning', 'Reasoning'),
        ('English', 'English'),
        ('GK', 'General Knowledge'),
        ('Telangana GK', 'Telangana GK'),
        ('Computer', 'Computer Awareness'),
    ]

    title = models.CharField(max_length=200)
    subject = models.CharField(max_length=50, choices=SUBJECTS)
    pdf = models.FileField(upload_to='study_materials/')
    uploaded_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Subscriber(models.Model):
    email = models.EmailField(unique=True)
    name = models.CharField(max_length=100, blank=True)
    subscribed_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email


# ===========================
# DAILY QUIZ
# ===========================

class DailyQuiz(models.Model):
    title = models.CharField(max_length=200)
    quiz_date = models.DateField(unique=True)

    def __str__(self):
        return f"{self.title} ({self.quiz_date})"


class QuizQuestion(models.Model):
    SUBJECTS = [
        ("Aptitude", "Aptitude"),
        ("Reasoning", "Reasoning"),
        ("English", "English"),
        ("GK", "General Knowledge"),
        ("Computer", "Computer"),
    ]

    question = models.CharField(max_length=500)
    option1 = models.CharField(max_length=200)
    option2 = models.CharField(max_length=200)
    option3 = models.CharField(max_length=200)
    option4 = models.CharField(max_length=200)
    answer = models.CharField(max_length=200)
    subject = models.CharField(max_length=50, choices=SUBJECTS)

    def __str__(self):
        return self.question


class QuizAttempt(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    score = models.IntegerField()
    total_questions = models.IntegerField(default=20)
    attempted_date = models.DateField(auto_now_add=True)
    time_taken = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.user.username} - {self.score}"
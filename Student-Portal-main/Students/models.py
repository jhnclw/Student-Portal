from django.db import models

class Student(models.Model):
    COURSE_CHOICES = [
        ("BSIT", "BS in Information Technology"),
        ("BSCS", "BS in Computer Science"),
        ("BSEE", "BS in Electrical Engineering"),
        ("BSTM", "BS in Technology Management"),
    ]

    YEAR_CHOICES = [
        (1, "1st Year"),
        (2, "2nd Year"),
        (3, "3rd Year"),
        (4, "4th Year"),
    ]

    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    age = models.PositiveSmallIntegerField()
    course = models.CharField(max_length=10, choices=COURSE_CHOICES, default="BS in Information Technology")
    year_level = models.PositiveSmallIntegerField(choices=YEAR_CHOICES, default='1st Year')
    grade = models.CharField(max_length=10)

    def __str__(self):
        return f"{self.name} — {self.get_course_display()} ({self.get_year_level_display()})"

    class Meta:
        ordering = ["name"]
        verbose_name = "Student"
        verbose_name_plural = "Students"

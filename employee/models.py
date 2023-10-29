from django.db import models
from django.utils.translation import gettext_lazy as _

# Create your models here.


class Gender(models.TextChoices):
    NAM = "NAM", _("Nam")
    NU = "NU", _("Nữ")


class Employee(models.Model):
    name = models.CharField(null=False, max_length=100)
    code = models.CharField(null=False, max_length=100, unique=True)
    birthday = models.DateField(null=False)
    gender = models.CharField(choices=Gender.choices)
    supervisor = models.ForeignKey(
        "self", on_delete=models.CASCADE, null=True, blank=True
    )

    def __str__(self):
        return f"{self.name} ({self.code})"


class Student(models.Model):
    name = models.CharField(null=False, max_length=100)
    code = models.CharField(null=False, max_length=100, unique=True)
    birthday = models.DateField(null=False)
    gender = models.CharField(choices=Gender.choices)

    def __str__(self):
        return f"{self.name} ({self.code})"


class Program(models.Model):
    name = models.CharField(null=False, max_length=100)
    code = models.CharField(null=False, max_length=100, unique=True)
    employee = models.ForeignKey("Employee", on_delete=models.CASCADE, null=True)
    subjects = models.ManyToManyField(
        "Subject", through="ProgramSubject", through_fields=("program", "subject")
    )

    def __str__(self):
        return f"{self.name} ({self.code})"


class Subject(models.Model):
    name = models.CharField(null=False, max_length=100)
    code = models.CharField(null=False, max_length=100, unique=True)
    total_hours = models.IntegerField(null=False)
    room = models.ForeignKey("Room", on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f"{self.name} ({self.code})"


class ProgramSubject(models.Model):
    program = models.ForeignKey("Program", on_delete=models.CASCADE, null=False)
    subject = models.ForeignKey("Subject", on_delete=models.CASCADE, null=False)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["program", "subject"], name="program_subject_unique"
            ),
        ]


class ProgramStudent(models.Model):
    program = models.ForeignKey("Program", on_delete=models.CASCADE, null=False)
    student = models.ForeignKey("Student", on_delete=models.CASCADE, null=False)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["program", "student"], name="program_student_unique"
            ),
        ]


class SubjectStudent(models.Model):
    subject = models.ForeignKey("Subject", on_delete=models.CASCADE, null=False)
    student = models.ForeignKey("Student", on_delete=models.CASCADE, null=False)
    score = models.FloatField(null=False)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["subject", "student"], name="subject_student_unique"
            ),
        ]


class Lecturer(models.Model):
    name = models.CharField(null=False, max_length=100)
    code = models.CharField(null=False, max_length=100, unique=True)
    birthday = models.DateField(null=False)
    gender = models.CharField(choices=Gender.choices)
    subjects = models.ManyToManyField(
        "Subject", through="SubjectLecturer", through_fields=("lecturer", "subject")
    )

    def __str__(self):
        return f"{self.name} ({self.code})"


class Room(models.Model):
    name = models.CharField(null=False, max_length=100)
    code = models.CharField(null=False, max_length=100, unique=True)
    address = models.CharField(null=False)

    def __str__(self):
        return f"{self.name} ({self.code})"


class SubjectLecturer(models.Model):
    lecturer = models.ForeignKey(
        "Lecturer", on_delete=models.CASCADE, null=False, related_name="lecturer"
    )
    tutor = models.ForeignKey(
        "Lecturer", on_delete=models.CASCADE, null=True, blank=True
    )
    subject = models.ForeignKey("Subject", on_delete=models.CASCADE, null=False)

    def __str__(self):
        return f"{self.subject.code} - {self.lecturer.code}"

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["subject", "lecturer"], name="subject_lecturer_unique"
            ),
        ]

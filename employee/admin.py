from django.contrib import admin
from .models import (
    Employee,
    Program,
    Subject,
    ProgramSubject,
    Lecturer,
    Room,
    SubjectLecturer,
    ProgramStudent,
    SubjectStudent,
    Student,
)


# Register your models here.
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ["name", "code"]
    search_fields = ["name", "code"]


class ProgramAdmin(admin.ModelAdmin):
    list_display = ["name", "code"]
    search_fields = ["name", "code"]


class StudentAdmin(admin.ModelAdmin):
    list_display = ["name", "code"]
    search_fields = ["name", "code"]


class LecturerAdmin(admin.ModelAdmin):
    list_display = ["name", "code"]
    search_fields = ["name", "code"]


class SubjectAdmin(admin.ModelAdmin):
    list_display = ["name", "code"]
    search_fields = ["name", "code"]


class ProgramSubjectAdmin(admin.ModelAdmin):
    list_display = ["program", "subject"]
    search_fields = ["program", "subject"]


class SubjectLecturerAdmin(admin.ModelAdmin):
    list_display = ["lecturer", "subject"]
    search_fields = ["lecturer", "subject"]


class ProgramStudentAdmin(admin.ModelAdmin):
    list_display = ["program", "student"]
    search_fields = ["program", "student"]


class SubjectStudentAdmin(admin.ModelAdmin):
    list_display = ["student", "subject"]
    search_fields = ["student", "subject"]


class RoomAdmin(admin.ModelAdmin):
    list_display = ["name", "code"]
    search_fields = ["name", "code"]


admin.site.register(Employee, EmployeeAdmin)
admin.site.register(Program, ProgramAdmin)
admin.site.register(Student, StudentAdmin)
admin.site.register(Subject, SubjectAdmin)
admin.site.register(ProgramSubject, ProgramSubjectAdmin)
admin.site.register(Lecturer, LecturerAdmin)
admin.site.register(Room, RoomAdmin)
admin.site.register(SubjectLecturer, SubjectLecturerAdmin)
admin.site.register(ProgramStudent, ProgramStudentAdmin)
admin.site.register(SubjectStudent, SubjectStudentAdmin)

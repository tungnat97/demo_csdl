"""
URL configuration for demo_csdl project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from employee.views import (
    calculate_view,
    calculate_lecturer,
    calculate_employee,
    get_student_score,
    get_unfinished_students,
)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("calculate/", calculate_view, name="calculate_view"),
    path("calculate/lecturer_salary/<str:code>/<int:base>", calculate_lecturer),
    path("calculate/employee_salary/<str:code>", calculate_employee),
    path(
        "calculate/student_score/<str:student_code>/<str:program_code>",
        get_student_score,
    ),
    path(
        "calculate/unfinished_students/<str:program_code>",
        get_unfinished_students,
    ),
]

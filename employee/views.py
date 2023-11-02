from django.shortcuts import render
from django.http import HttpResponse
from django.db import connection


# Create your views here.
def calculate_view(request):
    return render(request, "calculate_view.html", {})


def calculate_employee(request, code):
    with connection.cursor() as cursor:
        cursor.execute(
            f"""
                SELECT em.code, p.stu_num as total_student, em1.em_num as total_employees, p.stu_num + 5000000 + em1.em_num * 250000 as salary 
                from employee_employee as em
                LEFT JOIN (
                    SELECT e.code as ecode, ps.count as stu_num from employee_program as p 
                    LEFT JOIN employee_employee as e
                    on p.employee_id = e.id
                    LEFT JOIN (SELECT count(*), program_id from employee_programstudent group by program_id) ps on ps.program_id = p.id
                ) p on p.ecode = em.code
                LEFT JOIN (
                    SELECT count(*) as em_num, em2.code as code from employee_employee as em1
                    left join employee_employee as em2 on em2.id = em1.supervisor_id  where em2.code = '{code}' group by em2.code
                ) em1 on em1.code = em.code WHERE em.code = '{code}';
            """
        )
        row = cursor.fetchone()
        return HttpResponse(row[-1])


def calculate_lecturer(request, code, base):
    with connection.cursor() as cursor:
        cursor.execute(
            f"""
                SELECT SUM(agg.total_hours * agg.case * {float(base)}) FROM (
                    SELECT
                    sub.total_hours AS total_hours,
                    CASE lec.code WHEN '{code}' THEN 1
                        ELSE 0.5
                    END

                FROM employee_subjectlecturer AS sl
                LEFT JOIN employee_lecturer AS lec ON lec.id = sl.lecturer_id
                LEFT JOIN employee_lecturer AS tut ON tut.id = sl.tutor_id
                LEFT JOIN employee_subject AS sub ON sub.id = sl.subject_id WHERE lec.code = '{code}' OR tut.code = '{code}'
                ) agg
            """
        )
        row = cursor.fetchone()
        return HttpResponse(row[0])


def get_student_score(request, student_code, program_code):
    with connection.cursor() as cursor:
        cursor.execute(
            f"""
                select sb.code as code, ss.score as score from employee_subjectstudent as ss
                LEFT JOIN employee_student as s on s.id = ss.student_id
                LEFT JOIN employee_subject as sb on sb.id = ss.subject_id
                WHERE s.code = '{student_code}' and sb.id in (
                    select subject_id from employee_programsubject as ps
                    left join employee_program as p on p.id = ps.program_id
                    WHERE p.code = '{program_code}'
                )
            """
        )
        row = cursor.fetchall()
        return HttpResponse(row)


def get_unfinished_students(request, program_code):
    with connection.cursor() as cursor:
        cursor.execute(
            f"""
                SELECT
                s.name || ' - '|| s.code
                FROM employee_programstudent as ps
                LEFT JOIN employee_program as p on p.id = ps.program_id
                LEFT JOIN employee_student as s on s.id = ps.student_id
                LEFT JOIN (
                    SELECT student_id, count(*) as count from employee_subjectstudent as ss
                    WHERE ss.subject_id in (
                        SELECT
                            subject_id
                        FROM employee_programsubject as ps
                        LEFT JOIN employee_program as p on p.id = ps.program_id
                        WHERE p.code = '{program_code}'
                    ) 
                    GROUP BY student_id 
                ) scount on scount.student_id = ps.student_id
                WHERE p.code = '{program_code}' and 
                    (scount.count is null
                        or scount.count < (
                            SELECT count(*) from employee_programsubject as ps
                            left join employee_program as p on p.id = ps.program_id
                            where p.code = '{program_code}'
                        )
                    )
            """
        )
        row = cursor.fetchall()
        return HttpResponse(row)

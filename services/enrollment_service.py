"""Enrollment service for enrolling students in courses and creating module progress entries."""
from services.student_service import get_student
from services.moduleprogress_service import create_moduleprogress_entries
from data.student import enroll_student_in_course_db


def enrollment_student_in_course(student_id, course_id, gradetarget):
    """Enrolls a student in a course and creates module progress entries for the student."""
    student = get_student(student_id)
    student.enroll_student_in_course(course_id, gradetarget)
    enroll_student_in_course_db(student_id, course_id, gradetarget)
    create_moduleprogress_entries(student_id, course_id)
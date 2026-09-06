"""Enrollment service for enrolling students in courses and creating module progress entries."""
from data.student import enroll_course as enroll_course_db
from data.moduleprogress import create_moduleprogress_entries

def enroll_student_in_course(student_id, course_id, gradetarget):
    """Enrolls a student in a course and creates module progress entries for the student."""
    enroll_course_db(student_id, course_id, gradetarget)
    create_moduleprogress_entries(student_id, course_id)
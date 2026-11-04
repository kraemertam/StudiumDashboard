from controller.moduleprogress_controller import ModuleProgressController
from data.student_repository import StudentRepository
from domains.student import Student


class StudentController:
    def __init__(self):
        self.student_repository = StudentRepository()
        self.moduleprogress_controller = ModuleProgressController()


    def create_new_student(self, student_id, student_name, student_lastname) -> Student | None:
        """Create an new Student in database & as objekt."""
        try:
            new_student = Student(id=student_id, name=student_name, lastname=student_lastname)
        except ValueError as e:
            print(f"Student konnte nicht anlegt werden: {e}")
            raise
        try: 
            self.student_repository.create(student_id, student_name, student_lastname)
        except ValueError as e:
            print(f"Student konnte nicht anlegt werden: {e}")
            raise
        print(f"{new_student.name} {new_student.lastname} wurde als neuer Student angelegt.")
        return new_student

    def get_student(self, student_id: str) -> Student | None:
        """Load an already existing student and create as an Instanz of the object Student."""
        this_student = self.student_repository.get_by_id(student_id)
        if not this_student:
            return None
        student = Student(id= this_student[0], name = this_student[1], lastname=this_student[2], course_id = this_student[3], gradetarget = this_student[4])
        print(f"Student {student.name}, {student.lastname}, {student.id} wurde geladen.")
        return student

    def login(self, student_id: str) -> Student:
        """Load student for login. Raises ValueError if student does not exist or is not enrolled."""
        student = self.get_student(student_id)
        if student is None:
            raise ValueError(f"Kein Student mit der Matrikelnummer {student_id}.")
        if student.course_id is None:
            raise ValueError("Du bist noch in keinem Kurs eingeschrieben.")
        return student

    def enrollment_student_in_course(self, student_id, course_id, gradetarget):
        """Enrolls a student in a course and creates module progress entries for the student."""
        student = self.get_student(student_id)
        if student is None:
            raise ValueError(f"Kein Student mit der Matrikelnummer {student_id} gefunden.")
        student.enroll_student_in_course(course_id, gradetarget)
        self.student_repository.enroll(student_id, course_id, student.gradetarget)
        self.moduleprogress_controller.create_moduleprogress_entries(student_id, course_id)
        return student
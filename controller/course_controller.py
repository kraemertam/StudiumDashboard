from domains.module import Module
from data.course_repository import CourseRepository
from domains.course import Course
from controller.module_controller import ModuleController


class CourseController:
    """Coordinates loading, creating and changing courses between UI, domain and database."""
    def __init__(self):
        self.course_repository = CourseRepository()
        self.module_controller = ModuleController()

    def create_new_course(self, course_id: str, course_name: str, course_degree: str, course_ects: int) -> Course | None:
        """Create a new course: validate via the domain class, then save in the database."""
        try:
            new_course = Course(course_id, course_name, course_degree, course_ects)
        except ValueError as e:
            print(f"Kurs konnte nicht angelegt werden: {e}")
            raise
        try:
            self.course_repository.create(course_id, course_name, course_degree, course_ects)
        except ValueError as e:
            print(f"Kurs konnte nicht angelegt werden: {e}")
            raise
        return new_course
    
    def get_course(self, course_id: str) -> Course | None:
        """Load a course including its modules. Returns None if it does not exist."""
        coursedata = self.course_repository.get_by_id(course_id)
        if coursedata is None:
            print("Der Kurs ist nicht in der Datenbank vorhanden.")
            return None
        course_modules = self.course_repository.get_modules(course_id)
        modules = [Module(module[0], module[1], module[2]) for module in course_modules]
        course =Course(coursedata[0], coursedata[1], coursedata[2], coursedata[3], modules)
        return course
                
    def get_all_courses(self) -> list[Course]:
        """Load all courses without their modules."""
        courses_data = self.course_repository.get_all()
        courses = []
        for course_data in courses_data:
            course = Course(course_data[0], course_data[1], course_data[2], course_data[3])
            courses.append(course)
        return courses

    def add_module_to_course(self, course_id: str, module_id: str) -> bool:
        """Add a module to a course after checking it via the domain class. Returns True on success."""
        course = self.get_course(course_id) # Check, if Course in DB. If yes, return Course as Instance.
        if course is None:
            print(f"Der Kurs {course_id} ist nicht in der Datenbank enthalten.")
            return False
        
        module = self.module_controller.get_module(module_id) # Check, if Module in DB. If yes create Instanz.
        if module is None:
            print(f"Das Module {module_id} ist nicht in der Datenbank enthalten.")
            return False
        
        try:
            course.add_module(module) # Check, if Module can add to Course. If yes, add Module to Moduleliste in Instance Course.
            self.course_repository.add_module(course.id, module.id) # Add Module to Course in DB.
        except ValueError as e:
            print(f"{e}")
            return False

        return True


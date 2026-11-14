from data.course_repository import CourseRepository
from data.moduleprogress_repository import ModuleProgressRepository
from domains.module import Module
from domains.moduleprogress import ModuleProgress
from services.metrics_service import DashboardMetrics, MetricsService


class ModuleProgressController:
    _STATUS_ORDER = {
        ModuleProgress.Status.COMPLETED: 0,
        ModuleProgress.Status.FAILED: 1,
        ModuleProgress.Status.IN_PROGRESS: 2,
        ModuleProgress.Status.OPEN: 3,
    }
    def __init__(self):
        self.moduleprogress_repository = ModuleProgressRepository()
        self.course_repository = CourseRepository()
        self.metrics_service = MetricsService()

    def create_moduleprogress_entries(self, student_id: str, course_id: str) ->list[ModuleProgress]:
        modules = self.course_repository.get_modules(course_id)
        moduleprogresslist = [ModuleProgress(student_id, Module(module_id, name, ects)) for module_id, name, ects in modules]
        rows = [(p.student_id, p.module.id, p.status) for p in moduleprogresslist]
        self.moduleprogress_repository.create_entries(rows)
        return moduleprogresslist

    def get_all_moduleprogress(self, student_id: str) -> list[ModuleProgress]:
        """Load all modules from a student as domainobject."""
        all_moduleprogresses = self.moduleprogress_repository.get_for_student(student_id)
        progresses = [
            ModuleProgress(student_id,
                        Module(module_id, name, ects),
                        ModuleProgress.Status(status),
                        grade)
            for module_id, name, ects, status, grade in all_moduleprogresses
        ]
        return sorted(progresses, key=lambda p: (self._STATUS_ORDER[p.status], p.module.name))
        
    def update_moduleprogress(self, moduleprogress: ModuleProgress, new_status: ModuleProgress.Status, grade: float | None = None) -> ModuleProgress | None:
        if grade is not None:
            moduleprogress.grade = grade
        else:
            moduleprogress.change_status(new_status)
        self.moduleprogress_repository.save(moduleprogress.student_id, moduleprogress.module.id, moduleprogress.status, moduleprogress.grade)
        return moduleprogress

    def get_dashboard_metrics(self, student) -> DashboardMetrics:
        moduleprogresses = self.get_all_moduleprogress(student.id) # loads all moduleprogresses for student as domainobject
        dashboard_metrics = self.metrics_service.get_dashboard_metrics(moduleprogresses, float(student.gradetarget)) # calculates the key figures for the dashboard
        return dashboard_metrics

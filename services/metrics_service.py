from collections import Counter
from dataclasses import dataclass
from domains.moduleprogress import ModuleProgress

Status = ModuleProgress.Status
ALL_STATUS: tuple[ModuleProgress.Status, ...] = tuple(Status)

@dataclass
class DashboardMetrics:
    """Container for the key figures that are passed to the dashboard."""
    status_counts: dict[Status, int]
    ects_total: int
    ects_achieved: int
    average_grade: float | None       
    grade_target: float | None
    grade_difference: float | None  

class MetricsService:
     """Calculates the key figures for the dashboard. Has no access to the database."""
     
     def get_dashboard_metrics(self, moduleprogress: list[ModuleProgress], gradetarget: float | None) -> DashboardMetrics:
        """Calculate status counts, ECTS and the ECTS-weighted average grade of all passed modules."""
        number_of_status = Counter(m.status for m in moduleprogress)    # counts number of modules for each status

        status_counts = {s: number_of_status.get(s, 0) for s in ALL_STATUS}  # creates a dictionary with all statuses and their counts
        ects_total = sum(m.module.ects for m in moduleprogress)
        ects_achieved = sum(m.module.ects for m in moduleprogress if m.status == Status.COMPLETED)

        weighted_grades = sum(m.grade * m.module.ects for m in moduleprogress if m.status == Status.COMPLETED and m.grade is not None)
        average_grade = round(weighted_grades / ects_achieved, 2) if ects_achieved else None
        grade_difference = round(average_grade - gradetarget, 2) if average_grade is not None and gradetarget is not None else None

        return DashboardMetrics(
              status_counts=status_counts,
              ects_total=ects_total,
              ects_achieved=ects_achieved,
              average_grade=average_grade,
              grade_target=gradetarget,
              grade_difference=grade_difference,)
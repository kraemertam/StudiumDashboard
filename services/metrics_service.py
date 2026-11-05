from collections import Counter
from dataclasses import dataclass
from domains.moduleprogress import ModuleProgress

Status = ModuleProgress.Status
ALL_STATUS = tuple(Status)

@dataclass
class DashboardMetrics:
    status_counts: dict[str, int]
    ects_total: int
    ects_achieved: int
    average_grade: float | None       
    grade_target: float
    grade_difference: float | None  

class MetricsService:
     """Calculates the key figures for the dashboard. Has no access to the database."""
     
     def get_dashboard_metrics(self, moduleprogress: list[ModuleProgress], gradetarget: float) -> DashboardMetrics:
        number_of_status = Counter(m.status for m in moduleprogress) # counts number of modules for each status
        grades = [m.grade for m in moduleprogress if m.grade is not None] # get all grades for modules as list

        status_counts={s: number_of_status.get(s, 0) for s in ALL_STATUS}
        ects_total=sum(m.module.ects for m in moduleprogress)
        ects_achieved=sum(m.module.ects for m in moduleprogress if m.status == Status.COMPLETED)
        average_grade=round(sum(grades) / len(grades), 2) if grades else None
        grade_difference = round(average_grade - gradetarget, 2) if average_grade is not None else None

        return DashboardMetrics(
              status_counts=status_counts,
              ects_total=ects_total,
              ects_achieved=ects_achieved,
              average_grade=average_grade,
              grade_target=gradetarget,
              grade_difference=grade_difference,)
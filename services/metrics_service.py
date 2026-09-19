from collections import Counter
from dataclasses import dataclass
from data.moduleprogress import get_moduleprogress_data_db, get_grade_data_db
from domains.moduleprogress import ModuleProgress

Status = ModuleProgress.Status
ALL_STATUS = tuple(Status)

@dataclass
class DashboardMetrics:
    status_counts: dict[str, int]     # {"offen": 12, ...}
    ects_total: int
    ects_achieved: int
    average_grade: float | None       
    grade_target: float

def get_dashboard_metrics(student) -> DashboardMetrics:
    modules = get_moduleprogress_data_db(student.id) # all modules | data from Module
    counts = Counter(m[3] for m in modules) # counts all statuse for modules

    grades = [m[3] for m in get_grade_data_db(student.id)]         # Data from Moduleprogress

    return DashboardMetrics(
        status_counts={s: counts.get(s, 0) for s in ALL_STATUS},
        ects_total=sum(m[2] for m in modules),
        ects_achieved=sum(m[2] for m in modules if m[3] == Status.COMPLETED),
        average_grade=round(sum(grades) / len(grades), 2) if grades else None,
        grade_target=float(student.gradetarget),
    )
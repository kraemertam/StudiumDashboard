from data.course import get_modules_of_course_db
from data.moduleprogress import save_grade_changes_db, save_modulestatus_changes_db, get_moduleprogress_data_db, create_moduleprogress_entries_db
from domains.module import Module
from domains.moduleprogress import ModuleProgress


STATUS_ORDER = {
    ModuleProgress.Status.COMPLETED: 0,
    ModuleProgress.Status.FAILED: 1,
    ModuleProgress.Status.IN_PROGRESS: 2,
    ModuleProgress.Status.OPEN: 3,
}

def get_moduleprogress(student_id, module_id):
    pass

def get_all_moduleprogress(student_id):
    """Load all modules from a student as domainobject."""
    all_modules = get_moduleprogress_data_db(student_id)
    progresses = [
        ModuleProgress(student_id,
                       Module(module_id, name, ects),
                       ModuleProgress.Status(status),
                       grade)
        for module_id, name, ects, status, grade in all_modules
    ]
    return sorted(progresses, key=lambda p: (STATUS_ORDER[p.status], p.module.name))

def create_moduleprogress_entries(student_id, course_id) ->list[ModuleProgress]:
    modules = get_modules_of_course_db(course_id)
    moduleprogresslist = [ModuleProgress(student_id, Module(module_id, name, ects)) for module_id, name, ects in modules]
    create_moduleprogress_entries_db([(p.student_id, p.module.id, p.status) for p in moduleprogresslist])
    return moduleprogresslist
    

def update_moduleprogress(moduleprogress, new_status, grade = None):
    if grade is not None:
        moduleprogress.set_grade(grade)
    else:
        moduleprogress.change_status(new_status)
    save_modulestatus_changes_db(moduleprogress.student_id, moduleprogress.module.id, moduleprogress.status)
    save_grade_changes_db(moduleprogress.student_id, moduleprogress.module.id, moduleprogress.grade)
    return moduleprogress

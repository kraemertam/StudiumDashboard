# --- Assignment of the modules to the semesters ---------------------------------------------------------------------
def semester_assign(student, modulliste) -> list:
    etc_per_semester = student.calc_etc_per_semesters()
    number_of_semesters = student.semester + 1 # additional semester for remaining surplus etc

    modules_per_semester = []
    i = 0

    for semester in range(number_of_semesters):
        print(f"Folgendes Semester wird bearbeitet: {semester}")
        semester_etc = 0
        fertig = etc_per_semester
        semestermodule = []

        while i < len(modulliste) and semester_etc + modulliste[i].etc <= fertig:
            module = modulliste[i]
            semestermodule.append(module)
            semester_etc += module.etc
            i += 1
        modules_per_semester.append(semestermodule)


    print(f"Anzahl der Semester mit Modulen: {len(modules_per_semester)}")
    return modules_per_semester
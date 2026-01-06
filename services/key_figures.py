from matplotlib.figure import Figure
from data.student import get_overview_data, get_grade_data, get_gradetarget

def pie_chart(student_id):
    moduleliste = get_overview_data(student_id)

    offen = []
    bearbeitung = []
    abgeschlossen = []

    for module in moduleliste:
        if module[3] == "offen":
            offen.append(module)
        elif module[3] == "in Bearbeitung":
            bearbeitung.append(module)
        else:
            abgeschlossen.append(module)

    labels = ["offen", "in Bearbeitung", "abgeschlossen"]
    sizes = [len(offen), len(bearbeitung), len(abgeschlossen)]

    fig = Figure(figsize=(5,3), dpi=100)
    fig.subplots_adjust(right=0.70)
    ax = fig.add_subplot(111)

    wedges, *_ = ax.pie(sizes, colors=["lightblue", "orange", "lightgreen"], autopct="%1.1f%%", startangle=90)

    ax.legend(wedges, labels, title="Status", loc="center left", bbox_to_anchor=(1, 0.5))


    ax.axis("equal")
    ax.set_title("Übersicht Studienfortschritt")

    return fig

def grade_point_average(student_id):
    moduleliste = get_grade_data(student_id)
    student_gradetarget = get_gradetarget(student_id)
    gradetarget = float(student_gradetarget[0])
    print(gradetarget, type(gradetarget))
    print(moduleliste)

    grades = []
    gradecolor = "black"
    gradetargettext = f"Super, du befindest dich innerhalb deines Notenziels von {gradetarget}!"

    for module in moduleliste:
        grades.append(module[3])

    try:
        grade_point_average = round((sum(grades) / len(grades)), 2)
        print(grade_point_average)
        if grade_point_average > gradetarget:
            gradecolor = "red"
            gradetargettext = f"Achtung: Du hast deine Notenziel von {gradetarget} überschritten!"
    except ZeroDivisionError:
        grade_point_average = " Noch keine Note vorhanden. "
        gradetargettext = f"Dein Notenziel: {gradetarget}"

    return grade_point_average, gradecolor, gradetargettext

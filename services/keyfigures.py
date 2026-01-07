from matplotlib.figure import Figure
from data.student import get_overview_data, get_grade_data, get_gradetarget

def pie_chart(student_id):
    moduleliste = get_overview_data(student_id)

    offen = []
    bearbeitung = []
    abgeschlossen = []
    nicht_bestanden = []

    for module in moduleliste:
        if module[3] == "offen":
            offen.append(module)
        elif module[3] == "in Bearbeitung":
            bearbeitung.append(module)
        elif module[3] == "abgeschlossen":
            abgeschlossen.append(module)
        else:
            nicht_bestanden.append(module)
    sizes = [len(offen), len(bearbeitung), len(abgeschlossen), len(nicht_bestanden)]

    share_offen = round(((sizes[0]/sum(sizes))*100),2)
    share_bearbeitung = round(((sizes[1]/sum(sizes))*100),2)
    share_abgeschlossen = round(((sizes[2]/sum(sizes))*100),2)
    share_nicht_bestanden = round(((sizes[3]/sum(sizes))*100),2)


    labels = [f"offen: {share_offen}",
              f"in Bearbeitung: {share_bearbeitung}%",
              f"abgeschlossen: {share_abgeschlossen}%",
              f"nicht bestanden: {share_nicht_bestanden}%"]

    fig = Figure(figsize=(3,3), dpi=100)
    fig.subplots_adjust(right=0.75)
    ax = fig.add_subplot(111)
    wedges, *_ = ax.pie(sizes, colors=["lightblue", "orange", "lightgreen", "red"], startangle=90)
    ax.legend(wedges, labels, title="Status", loc="center left", bbox_to_anchor=(0.75, 0.5))
    ax.axis("equal")
    ax.set_title("Übersicht über deinen Studienfortschritt")

    return fig

def grade_point_average(student_id):
    moduleliste = get_grade_data(student_id)
    student_gradetarget = get_gradetarget(student_id)

    gradetarget = float(student_gradetarget[0])
    grades = []
    gradecolor = "black"
    gradetargettext = f"Super gemacht! \nDu befindest dich innerhalb deines Notenziels. Weiter so!"

    for module in moduleliste:
        grades.append(module[3])

    try:
        grade_point_average = round((sum(grades) / len(grades)), 2)
        print(grade_point_average)
        if grade_point_average > gradetarget:
            gradecolor = "red"
            grade_difference = round((grade_point_average - gradetarget), 2)
            gradetargettext = f"Achtung! \nDu hast deine Zielnote um {grade_difference} überschritten!"
    except ZeroDivisionError:
        grade_point_average = " Noch keine Note vorhanden. "
        gradetargettext = ""

    return grade_point_average, gradetarget, gradecolor, gradetargettext

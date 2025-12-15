from matplotlib.figure import Figure

import data.query_db

def pie_chart(student_id):
    moduleliste = data.query_db.get_overview_data(student_id)

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

    fig = Figure(figsize=(3,3), dpi=100)
    ax = fig.add_subplot(111)
    ax.pie(sizes, labels=labels, autopct="%1.1f%%", startangle=90)
    ax.axis("equal")
    ax.set_title("Übersicht Studienfortschritt")

    return fig

def grade_point_average(student_id):
    moduleliste = data.query_db.get_grade_data(student_id)
    print(moduleliste)

    grades = []

    for module in moduleliste:
        grades.append(module[3])

    grade_point_average = round((sum(grades) / len(grades)), 2)
    print(grade_point_average)

    return grade_point_average

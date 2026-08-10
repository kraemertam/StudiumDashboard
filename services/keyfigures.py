from matplotlib.figure import Figure
from data.student import get_overview_data, get_grade_data, get_gradetarget
from ui.theme import BG_COLOR, STATUS_OPEN, STATUS_IN_PROGRESS, STATUS_COMPLETED, STATUS_FAILED, STATUS_COLORS

def pie_chart(student_id):
    moduleliste = get_overview_data(student_id)

    status_open = []
    status_in_progress = []
    status_completed = []
    status_failed = []

    for module in moduleliste:
        if module[3] == STATUS_OPEN:
            status_open.append(module)
        elif module[3] == STATUS_IN_PROGRESS:
            status_in_progress.append(module)
        elif module[3] == STATUS_COMPLETED:
            status_completed.append(module)
        else:
            status_failed.append(module)
    sizes = [len(status_open), len(status_in_progress), len(status_completed), len(status_failed)]

    share_offen = round(((sizes[0]/sum(sizes))*100),2)
    share_bearbeitung = round(((sizes[1]/sum(sizes))*100),2)
    share_abgeschlossen = round(((sizes[2]/sum(sizes))*100),2)
    share_nicht_bestanden = round(((sizes[3]/sum(sizes))*100),2)

    labels = [f"{STATUS_OPEN}: {share_offen}%",
              f"{STATUS_IN_PROGRESS}: {share_bearbeitung}%",
              f"{STATUS_COMPLETED}: {share_abgeschlossen}%",
              f"{STATUS_FAILED}: {share_nicht_bestanden}%"]

    fig = Figure(figsize=(3,3), dpi=100)
    fig.patch.set_facecolor(BG_COLOR)
    fig.subplots_adjust(right=0.75)
    ax = fig.add_subplot(111)
    ax.set_facecolor(BG_COLOR) 
    wedges, *_ = ax.pie(sizes, colors=[STATUS_COLORS[STATUS_OPEN], STATUS_COLORS[STATUS_IN_PROGRESS],
                STATUS_COLORS[STATUS_COMPLETED], STATUS_COLORS[STATUS_FAILED]], startangle=90)
    legend = ax.legend(wedges, labels, title="Modulstatus", loc="center left", bbox_to_anchor=(0.75, 0.5))
    legend.get_frame().set_facecolor(BG_COLOR)
    legend.get_frame().set_edgecolor(BG_COLOR)
    ax.axis("equal")
    ax.set_title("Übersicht über deinen Studienfortschritt")

    return fig

def calc_achieved_etcs(student_id):
    moduleliste = get_overview_data(student_id)
    all_etcs = sum(module[2] for module in moduleliste)
    achieved_etcs = 0

    for module in moduleliste:
        if module[3] == STATUS_COMPLETED:
            achieved_etcs += module[2]

    return all_etcs,achieved_etcs

def grade_point_average(student_id):
    moduleliste = get_grade_data(student_id)
    student_gradetarget = get_gradetarget(student_id)

    gradetarget = float(student_gradetarget[0])
    grades = []
    gradecolor = "black"
    gradetargettext = "Super gemacht! \nDu befindest dich innerhalb deines Notenziels. Weiter so!"

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


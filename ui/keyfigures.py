from matplotlib.figure import Figure
from services.metrics_service import get_dashboard_metrics, ALL_STATUS
from ui.theme import BG_COLOR, STATUS_COLORS

def pie_chart(student):
    metrics = get_dashboard_metrics(student)
    sizes = [metrics.status_counts[s] for s in ALL_STATUS]

    total = sum(sizes)
    shares = [round(s/total *100, 2) if total else 0 for s in sizes]

    labels = [f"{status}: {share}%" for status, share in zip(ALL_STATUS, shares)]
    colors = [STATUS_COLORS[s] for s in ALL_STATUS]

    fig = Figure(figsize=(3,3), dpi=100)
    fig.patch.set_facecolor(BG_COLOR)
    fig.subplots_adjust(right=0.75)
    ax = fig.add_subplot(111)
    ax.set_facecolor(BG_COLOR) 
    wedges, *_ = ax.pie(sizes, colors=colors, startangle=90)
    legend = ax.legend(wedges, labels, title="Modulstatus", loc="center left", bbox_to_anchor=(0.75, 0.5))
    legend.get_frame().set_facecolor(BG_COLOR)
    legend.get_frame().set_edgecolor(BG_COLOR)
    ax.axis("equal")
    ax.set_title("Übersicht über deinen Studienfortschritt")

    return fig

def calc_achieved_ects(student):
    metrics = get_dashboard_metrics(student)
    return metrics.ects_total, metrics.ects_achieved


def grade_point_average(student):

    metrics = get_dashboard_metrics(student)

    if metrics.average_grade is None:
        return "Noch keine Note vorhanden.", metrics.grade_target, "black", ""

    if metrics.average_grade > metrics.grade_target:
        diff = round(metrics.average_grade - metrics.grade_target, 2)
        return (metrics.average_grade, metrics.grade_target, "red",
                f"Achtung! \nDu hast deine Zielnote um {diff} überschritten!")

    return (metrics.average_grade, metrics.grade_target, "black",
            "Super gemacht! \nDu befindest dich innerhalb deines Notenziels. Weiter so!")

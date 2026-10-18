from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import SimpleDocTemplate, Paragraph
import os

def generate_report(metrics, insights):

    os.makedirs("outputs", exist_ok=True)

    filename = "outputs/customer_report.pdf"

    doc = SimpleDocTemplate(filename)

    styles = getSampleStyleSheet()

    story = []

    story.append(
        Paragraph("<b>Customer Behavior Analytics Report</b>", styles["Title"])
    )

    story.append(
        Paragraph("<br/>Dashboard Summary", styles["Heading2"])
    )

    for key, value in metrics.items():
        story.append(
            Paragraph(f"<b>{key}</b>: {value}", styles["BodyText"])
        )

    story.append(
        Paragraph("<br/>Business Insights", styles["Heading2"])
    )

    for key, value in insights.items():
        story.append(
            Paragraph(f"<b>{key}</b>: {value}", styles["BodyText"])
        )

    doc.build(story)

    return filename
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render

from mango_pests.models import Pest, PestCheck


@login_required
def summary_view(request):
    pests = Pest.objects.all()
    pest_summaries = []

    for pest in pests:
        checks = PestCheck.objects.filter(pest=pest, num_positive=0)
        total_checked = sum(c.num_trees_checked for c in checks)

        confidence = None
        if total_checked > 0:
            assumed_prevalence = 0.01  # 1%
            confidence = 1 - (1 - assumed_prevalence) ** total_checked

        pest_summaries.append(
            {
                "pest": pest,
                "checks": checks,
                "total_checked": total_checked,
                "confidence": round(confidence * 100, 2) if confidence else None,
            }
        )

    return render(
        request,
        "mango_pests/summary.html",
        {
            "pest_summaries": pest_summaries,
        },
    )


def download_csv(request):
    response = HttpResponse(content_type="text/csv")
    response["Content-Disposition"] = 'attachment; filename="surveillance_summary.csv"'

    writer = csv.writer(response)
    writer.writerow(
        ["Pest", "Part of Plant", "Confidence", "Trees Checked", "Positives", "Date"]
    )

    pest_checks = PestCheck.objects.all()
    for check in pest_checks:
        confidence = (
            check.confidence_score if check.confidence_score is not None else "N/A"
        )
        writer.writerow(
            [
                check.pest.name,
                check.part_of_plant,
                confidence,
                check.num_trees_checked,
                check.num_positive,
                check.date_checked.strftime("%Y-%m-%d"),
            ]
        )

    return response

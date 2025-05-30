# Import Django's render for template rendering and HttpResponse for CSV output
from django.shortcuts import render
from django.http import HttpResponse
# Import PestCheck model for database queries
from .models import PestCheck
# Import csv for generating CSV files
import csv


def recent_checks(request):
    # Display the 10 most recent pest checks with traffic light badges.
    # Query the 10 latest PestCheck records, ordered by date_checked (descending)
    records = PestCheck.objects.order_by('-date_checked')[:10]
    # Pair each record with its traffic light status (🟢, 🟡, 🔴)
    records_with_status = [(record, get_traffic_light(record)) for record in records]
    # Render the recent_checks template with the records
    return render(request, 'surveillance/recent_checks.html', {'records': records_with_status})


def summary(request):
    # Display a summary of pest checks with overall status, totals, and recent checks.
    # Get the 5 most recent PestCheck records for the summary table
    records = PestCheck.objects.order_by('-date_checked')[:5]
    # Pair each record with its traffic light status
    records_with_status = [(record, get_traffic_light(record)) for record in records]
    # Count total number of PestCheck records
    total_checks = PestCheck.objects.count()
    # Count records with pests found (positives > 0), implementing SELECT * FROM pest_check WHERE positives > 0;
    pest_checks = len([record for record in PestCheck.objects.all() if record.positives > 0])
    # Get the latest record for overall status, or None if no records exist
    latest_record = PestCheck.objects.latest('date_checked') if PestCheck.objects.exists() else None
    # Determine overall status (traffic light) based on the latest record
    overall_status = get_traffic_light(latest_record) if latest_record else '🟡'
    # Render the summary template with data
    return render(request, 'surveillance/summary.html', {
        'records': records_with_status,
        'total_checks': total_checks,
        'pest_checks': pest_checks,
        'overall_status': overall_status,
    })


def download_csv(request):
    # Generate and download a CSV file of all pest check records.
    # Create an HttpResponse with CSV content type
    response = HttpResponse(content_type='text/csv')
    # Set the filename for download
    response['Content-Disposition'] = 'attachment; filename="pest_checks.csv"'
    # Initialize CSV writer
    writer = csv.writer(response)
    # Write CSV header row
    writer.writerow(['Date', 'Farm Block', 'Pest', 'Part of Plant', 'Confidence', 'Trees Checked', 'Positives', 'Status'])
    # Query all PestCheck records, ordered by date_checked (descending)
    records = PestCheck.objects.order_by('-date_checked')
    # Write each record's data to the CSV
    for record in records:
        writer.writerow([
            record.date_checked,
            record.farm_block.name,
            record.pest.name,
            record.part_of_plant,
            f"{record.confidence*100:.2f}%" if record.confidence else 'N/A',  # Format confidence as percentage
            record.num_trees,
            record.positives,
            get_traffic_light(record),  # Include traffic light status
        ])
    return response


def get_traffic_light(record):
    # Determine traffic light badge for a PestCheck record.
    # Return yellow (🟡) if no record exists
    if not record:
        return '🟡'
    # Red (🔴) if pests are found (positives > 0)
    if record.positives > 0:
        return '🔴'
    # Green (🟢) if confidence is ≥90% and enough trees checked (≥50)
    if record.confidence and record.confidence >= 0.9 and record.num_trees >= 50:
        return '🟢'
    # Yellow (🟡) for low samples or insufficient confidence
    return '🟡'

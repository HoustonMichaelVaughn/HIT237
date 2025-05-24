rom django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .models import SurveillanceRecord
from .forms import SurveillanceForm
import csv
from datetime import datetime

# Calculate traffic light status for a record
def get_traffic_light(record):
    if record.pests_found:
        return '🔴'  # Red if pests found
    elif record.confidence >= 90:
        return '🟢'  # Green if high confidence and no pests
    elif record.sample_count < 50:
        return '🟡'  # Yellow if low sample count and no pests
    return '🟡'  # Default to yellow

# View to add a new surveillance check
def add_check(request):
    if request.method == 'POST':  # Handle form submission
        form = SurveillanceForm(request.POST)
        if form.is_valid():  # Validate form data
            form.save()  # Save record to database
            return HttpResponseRedirect(reverse('farm:summary'))  # Redirect to summary
        else:
            page_data = {'form': form}  # Pass form with errors
    else:
        page_data = {'form': SurveillanceForm()}  # Display empty form for GET
    return render(request, 'farm/add_check.html', page_data)

# View for summary page with overall status and recent checks
def summary(request):
    records = SurveillanceRecord.objects.all().order_by('-check_date')[:5]  # Get 5 latest records
    total_checks = SurveillanceRecord.objects.count()  # Total number of checks
    pest_checks = SurveillanceRecord.objects.filter(pests_found=True).count()  # Number of pest detections
    sufficient_checks = SurveillanceRecord.objects.filter(confidence__gte=90, pests_found=False).count()  # High-confidence, pest-free checks
    
    # Determine overall farm status
    overall_status = '🟢' if sufficient_checks >= 3 and pest_checks == 0 else '🟡' if pest_checks == 0 else '🔴'
    
    page_data = {
        'overall_status': overall_status,
        'records': [(record, get_traffic_light(record)) for record in records],  # Pair records with status
        'total_checks': total_checks,
        'pest_checks': pest_checks,
    }
    return render(request, 'farm/summary.html', page_data)

# View for listing 10 recent checks
def recent_checks(request):
    records = SurveillanceRecord.objects.all().order_by('-check_date')[:10]  # Get 10 latest records
    page_data = {
        'records': [(record, get_traffic_light(record)) for record in records],  # Pair records with status
    }
    return render(request, 'farm/recent_checks.html', page_data)

# View to download all records as CSV
def download_csv(request):
    response = HttpResponse(content_type='text/csv')  # Set response type to CSV
    response['Content-Disposition'] = f'attachment; filename="surveillance_records_{datetime.now().strftime('%Y%m%d')}.csv"'  # Set filename
    
    writer = csv.writer(response)  # Create CSV writer
    writer.writerow(['Check Date', 'Confidence', 'Sample Count', 'Pests Found', 'Status'])  # Write header
    
    for record in SurveillanceRecord.objects.all():  # Write each record
        status = get_traffic_light(record)
        writer.writerow([
            record.check_date,
            record.confidence,
            record.sample_count,
            'Yes' if record.pests_found else 'No',
            status
        ])
    
    return response

from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Supplier, PurchaseOrder, Docket
from .forms import CSVUploadForm, ExcelUploadForm
import pandas as pd  # Import Pandas if not already imported
import csv

def purchase_order_list(request):
    # Implement logic to retrieve and list purchase orders
    purchase_orders = PurchaseOrder.objects.all()
    return render(request, 'purchase_order_list.html', {'purchase_orders': purchase_orders})

def docket_form(request):
    suppliers = Supplier.objects.all()
    purchase_orders = PurchaseOrder.objects.all()

    if request.method == 'POST':
        # Process and save the docket data
        name = request.POST['name']
        start_time = request.POST['start_time']
        end_time = request.POST['end_time']
        hours_worked = request.POST['hours_worked']
        rate_per_hour = request.POST['rate_per_hour']
        supplier_id = request.POST['supplier']
        purchase_order_id = request.POST['purchase_order']
        
        # Create and save a new Docket instance
        docket = Docket(
            name=name, 
            start_time=start_time, 
            end_time=end_time, 
            num_hours_worked=hours_worked,
            rate_per_hour=rate_per_hour, 
            supplier_id=supplier_id, 
            purchase_order_id=purchase_order_id
        )
        docket.save()
        
        # Redirect to a success page or another view
        return redirect('purchase_order_list')

    return render(request, 'docket_form.html', {'suppliers': suppliers, 'purchase_orders': purchase_orders})

def docket_creation_popup(request):
    suppliers = Supplier.objects.all()
    purchase_orders = PurchaseOrder.objects.all()

    if request.method == 'POST':
        # Process and save the docket data (similar to docket_form)
        # ...
        return redirect('docket_creation_popup')  # Redirect back to the popup or another page

    return render(request, 'docket_creation_popup.html', {'suppliers': suppliers, 'purchase_orders': purchase_orders})

def upload_csv(request):
    if request.method == 'POST':
        form = CSVUploadForm(request.POST, request.FILES)
        if form.is_valid():
            csv_file = form.cleaned_data['csv_file']
            
            # Process the CSV file
            process_csv(csv_file)
            
            # Redirect or return a success response
            return redirect('success_page')
    else:
        form = CSVUploadForm()

    return render(request, 'upload_csv.html', {'form': form})

def process_csv(csv_file):
    # Read the CSV file
    reader = csv.reader(csv_file)

    for row in reader:
        # Create or get a Supplier object based on your data (e.g., using row[0])
        supplier, created = Supplier.objects.get_or_create(name=row[0])

        # Create a PurchaseOrder object for the supplier
        purchase_order = PurchaseOrder.objects.create(supplier=supplier, description=row[1])

        # Create a Docket object for the purchase order
        Docket.objects.create(
            name=row[2],
            start_time=row[3],
            end_time=row[4],
            num_hours_worked=row[5],
            rate_per_hour=row[6],
            supplier=supplier,
            purchase_order=purchase_order
        )

def upload_excel(request):
    if request.method == 'POST':
        form = ExcelUploadForm(request.POST, request.FILES)
        if form.is_valid():
            excel_file = request.FILES['excel_file']

            try:
                df = pd.read_excel(excel_file)
                # Process the DataFrame or save the data to your models

            except pd.errors.ParserError:
                return render(request, 'error.html', {'message': 'Invalid Excel file format'})
        else:
            return render(request, 'error.html', {'message': 'Invalid form data'})
    else:
        form = ExcelUploadForm()

    return render(request, 'upload_excel.html', {'form': form})

from django import forms
from .models import Docket, Supplier, PurchaseOrder

class DocketForm(forms.ModelForm):
    class Meta:
        model = Docket
        fields = ['name', 'start_time', 'end_time', 'num_hours_worked', 'rate_per_hour', 'supplier', 'purchase_order']

    def __init__(self, *args, **kwargs):
        super(DocketForm, self).__init__(*args, **kwargs)

        # Filter the Supplier Name and Purchase Order fields based on the selected PO Number.
        # You can do this using queryset in the form's __init__ method.
        if 'purchase_order' in self.data:
            purchase_order_id = self.data.get('purchase_order')
            self.fields['supplier'].queryset = Supplier.objects.filter(purchaseorder__id=purchase_order_id)

        # Disable the PO Number field until a supplier is selected.
        self.fields['purchase_order'].widget.attrs['disabled'] = True
# forms.py

from django import forms

class CSVUploadForm(forms.Form):
    csv_file = forms.FileField()


# forms.py

from django import forms

class ExcelUploadForm(forms.Form):
    excel_file = forms.FileField()

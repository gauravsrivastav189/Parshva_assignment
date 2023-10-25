# urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('purchase_orders/', views.purchase_order_list, name='purchase_order_list'),
    path('docket_form/', views.docket_form, name='docket_form'),
    path('docket_creation_popup/', views.docket_creation_popup, name='docket_creation_popup'),
    path('upload_csv/', views.upload_csv, name='upload_csv'),
    path('upload_excel/', views.upload_excel, name='upload_excel'),

]

from django.urls import path
from . import views

urlpatterns = [
    path('', views.submit_form, name='form'),
    path('success/', views.success, name='success'),
    path('customers/', views.CustomerListView.as_view(), name='customers'),
    path('customers/<int:pk>', views.CustomersDetailView.as_view(), name='customer-detail'),
    # path('machines/', views.MachineListView.as_view(), name='machines'),
]

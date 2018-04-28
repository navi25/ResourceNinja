from django.shortcuts import render
from .forms import TestForm, RequestForm, RequestOrderForm
from django.http import HttpResponseRedirect
from .models import CustomerModel, MachineModel, OrderModel
from django.views import generic
from .services import *
from Constants import EMAIL
import json

def submit_form(request):
    if request.method == 'POST':

        form = RequestOrderForm(request.POST)

        # check whether it's valid:
        if form.is_valid():
            data = form.cleaned_data
            newOrder = form.save()
            emailData = {
                         EMAIL.FROM : "admin@resourceninja.asu.edu",
                         EMAIL.RECIPIENT_LIST : ["sdasgu11@asu.edu"],
                         EMAIL.SUBJECT : "Testing Email Settings",
                         EMAIL.BODY : "Hi Admin, \nThe following request has been received : \n%s"%json.dumps(data)
                         }
            SendEmail(emailData) # Sends Email
            # redirect to a Success:
            return HttpResponseRedirect('success')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = RequestOrderForm()

    return render(request, 'baseform.html', {'form': form})

def success(request):
    return render(
        request,
        'success.html'
    )



class CustomerListView(generic.ListView):
    model = CustomerModel
    context_object_name = 'customersList'
    queryset = CustomerModel.objects.all()
    template_name = 'customers.html'

class CustomersDetailView(generic.DetailView):
    model = CustomerModel
    template_name = 'customer_detail.html'

from django.shortcuts import render
from .forms import TestForm, RequestForm, RequestOrderForm
from django.http import HttpResponseRedirect
from .models import CustomerModel, MachineModel, OrderModel
from django.views import generic

# Create your views here.
def submit_form(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = RequestOrderForm(request.POST)
        # check whether it's valid:

        if form.is_valid():
            data = form.cleaned_data
            newOrder = form.save()
            print("New Order = " + str(newOrder))
            print("Data = " + str(data))
            firstName = data['firstName']
            lastName = data['lastName']
            dateSubmitted = data['dateSubmitted']
            datePartsNeeded =  data['datePartsNeeded']
            facultyAdvisor = data['facultyAdvisor']
            paymentAccountNo = data['paymentAccountNo']
            className = data['className']
            machineRequested = data['machineRequested']
            listParts = data['listParts']
            maxHeight=data['maxHeight']
            minHeight=data['minHeight']
            maxLength=data['maxLength']
            minLength=data['minLength']
            maxWidth=data['maxWidth']
            minWidth=data['minWidth']
            # redirect to a new URL:
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

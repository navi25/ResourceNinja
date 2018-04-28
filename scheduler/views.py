from django.shortcuts import render
from .forms import TestForm
from django.http import HttpResponseRedirect

# Create your views here.
def submit_form(request):

    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = TestForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect('success')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = TestForm()

    return render(request, 'baseform.html', {'form': form})

def success(request):
    return render(
        request,
        'success.html'
    )

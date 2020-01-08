from django.shortcuts import render
from .models import Emaployee

# Create your views here.

def home(request):

    # creating employee object from the requests.
    employees = Emaployee.objects.all()
    return render(request,'home.html',{'employees':employees})

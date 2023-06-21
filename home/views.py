from django.shortcuts import render
from .models import Our_Media


# Create your views here.
def index(request):
    portfolio = Our_Media.objects.all()
    context = {'portfolio':portfolio,}
    return render(request,'index.html',context)
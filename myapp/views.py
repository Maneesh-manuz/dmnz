import datetime
from django.shortcuts import render, redirect
from myapp.models import *
from datetime import date 




# Create your views here.
def admin_payment_history(request):
    return render(request, 'admin_payment_history.html')

def payment_table(request):
    var= payment.objects.all()
    if request.method == "POST":
            fromdate = request.POST.get('fromdate')
            todate = request.POST.get('todate') 
            var = payment.objects.filter(date__range=[fromdate, todate])
    return render(request, 'payment_table.html',{'var':var})




 




  
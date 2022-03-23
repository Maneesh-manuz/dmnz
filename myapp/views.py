from django.shortcuts import render, redirect
from myapp.models import *



# Create your views here.
def admin_payment_history(request):
    var=payment.objects.all()
    if request.method == 'POST':
            start=request.POST['startdate']
            end=request.POST['enddate']
            var=payment.objects.filter(date_gte=start,date__lte=end)
    return render(request, 'admin_payment_history.html',{'var':var})
def demo(request):
    return render(request, 'demo.html')






    # def BRadmin_promanattendsort(request,id):
    # if 'Adm_id' in request.session:
    #     if request.session.has_key('Adm_id'):
    #         Adm_id = request.session['Adm_id']
    #     else:
    #         variable="dummy"
    #     Adm = user_registration.objects.filter(id=Adm_id)
    #     id = id
    #     if request.method == "POST":
    #         fromdate = request.POST.get('fromdate')
    #         todate = request.POST.get('todate') 
    #         # mem1 = attendance.objects.raw('select * from app_attendance where user_id and date between "'+fromdate+'" and "'+todate+'"')
    #         mem1 = attendance.objects.filter(date__range=[fromdate, todate]).filter(user_id = id)
    #     return render(request, 'BRadmin_promanattendsort.html',{'mem1':mem1,'Adm':Adm,'id':id})
    # else:
    #     return redirect('/')
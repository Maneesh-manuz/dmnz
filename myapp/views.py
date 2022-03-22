from django.shortcuts import render, redirect



# Create your views here.
def admin_payment_history(request):
    return render(request, 'admin_payment_history.html')
def demo(request):
    return render(request, 'demo.html')
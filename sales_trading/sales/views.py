from django.shortcuts import render

def sales_dashboard(request):
    return render(request, 'sales/index.html')

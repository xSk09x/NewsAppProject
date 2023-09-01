from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def start(request):
    data = {
        'title': 'Страница',
        'spisok' : ['123', 'popa', 'penis'],
        'car' :{
            'number' : '4523',
            'type' : 'SUV',
            'manufacture' : 'Range Rover'        
            }  
    }
    return render(request, 'main_app/start_page.html', data)
def SupportPage(request):
    return render(request, 'main_app/support_page.html')
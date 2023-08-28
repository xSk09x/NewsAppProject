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
def SecondPage(request):
    return render(request, 'main_app/test.html')
def menu(request):
    return render(request, 'main_app/menu.html')
def design(request):
    return render(request, 'main_app/design.html')

# def datafunc(request):
#     data ={
#         'title': 'Страница'
#         'values': ['123', 'popa', 'penis']  
#     }
#     return render (request, 'main_app/')
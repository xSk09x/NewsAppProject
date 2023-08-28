from django.urls import path
from . import views

urlpatterns = [
    path('', views.StartPageForAgenda, name='StartPageForAgenda'),
    path('create', views.CreatePage, name= 'create'),
    path('<int:pk>', views.NarrativeDetailView.as_view(), name='agenda-detail'),
    path('<int:pk>/update', views.NarrativeUpdateView.as_view(), name='agenda-update'),
    path('<int:pk>/delete', views.NarrativeDeleteView.as_view(), name='agenda-delete')
]
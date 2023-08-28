from django.shortcuts import render, redirect
from .models import Narrative
from .forms import NarrativeForm
from django.views.generic import DetailView, UpdateView, DeleteView

class NarrativeDetailView(DetailView):
    model = Narrative
    template_name = 'agenda/DetailView.html'
    context_object_name = 'narrative'

class NarrativeUpdateView(UpdateView):
    model = Narrative
    template_name = 'agenda/create.html'
    form_class = NarrativeForm

class NarrativeDeleteView(DeleteView):
    model = Narrative
    template_name = 'agenda/delete.html'
    success_url = '/agenda/'

def StartPageForAgenda(request):
    narratives = Narrative.objects.order_by('id')
    return render(request, 'agenda/StartPageForAgenda.html', {'narratives' : narratives} )
# Create your views here.   

def CreatePage(request):
    error = ''
    if request.method == "POST":
        form = NarrativeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('StartPageForAgenda')
        else:
            error = 'The form is incorrect"' 
    form = NarrativeForm()
    data = {
        'form' : form,
        'error' : error
    }

    return render(request, 'agenda/create.html', data)
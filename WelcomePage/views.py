from django.shortcuts import render
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy

from .models import Event, Project
from .forms import EventForm


def index(request):
    evs = Event.objects.order_by('-date')
    projects = Project.objects.all()
    context = {'evs': evs, 'projects': projects}
    return render(request, 'welcome_page/index.html', context)


def by_project(request, project_id):
    evs = Event.objects.filter(project=project_id)
    projects = Project.objects.all()
    current_project = Project.objects.get(pk=project_id)
    context = {'evs': evs, 'projects': projects, 'current_project': current_project}
    return render(request, 'welcome_page/by_projects.html', context)


class EventCreateView(CreateView):
    template_name = 'welcome_page/create.html'
    form_class = EventForm
    success_url = reverse_lazy('index')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['projects'] = Project.objects.all()
        return context

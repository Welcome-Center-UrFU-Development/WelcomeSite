from django.urls import path

from .views import index, by_project, EventCreateView


urlpatterns = [
    path('', index, name='index'),
    path('<int:project_id>/', by_project, name='by_project'),
    path('add/', EventCreateView.as_view(), name='add'),
]
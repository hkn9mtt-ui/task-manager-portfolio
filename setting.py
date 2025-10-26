from django.urls import path
from . import views

urlpatterns = [
    path('admin/',admin.site.urls),
    path('',include('task_app.urls')),
    path('', views.task_list, name='task_list'),
]





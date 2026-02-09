from django.urls import include, path

from task.views import retrieve_tasks
from task.views import delete_task
from task.views import create_task
from task.views import update_task
from task.views import retrieve_task


urlpatterns = [
    path('list/', retrieve_tasks, name='task-list'),
    path('delete/<int:pk>/', delete_task, name='delete_task'),
    path('create/', create_task, name='create_task'),
    path('update/<int:pk>/', update_task, name="update_task"),
    path('get/<int:pk>/', retrieve_task, name="retrieve_task"),
]

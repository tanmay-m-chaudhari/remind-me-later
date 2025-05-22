from django.urls import path
from .views import ReminderViewSet

urlpatterns = [
    path('get-reminders', 
        ReminderViewSet.as_view({
            'get': 'list',
            'post': 'create'
        }), 
        name='reminder-list-create'
    ),
    path('get-reminder/<int:pk>', 
        ReminderViewSet.as_view({
            'get': 'retrieve',
            'put': 'update',
            'delete': 'destroy'
        }), 
        name='reminder-detail'
    ),
]
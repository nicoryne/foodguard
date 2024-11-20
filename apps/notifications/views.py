from .models import Notification
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

# Notification List View
class NotificationListView(ListView):
    model = Notification
    template_name = 'notification_list.html'
    context_object_name = 'notifications'

# Notification Detail View
class NotificationDetailView(DetailView):
    model = Notification
    template_name = 'notification_detail.html'
    context_object_name = 'notification'

# Notification Create View
class NotificationCreateView(CreateView):
    model = Notification
    fields = ['user', 'title', 'description']
    template_name = 'notification_create_form.html'
    success_url = '/notifications/'

# Notification Update View
class NotificationUpdateView(UpdateView):
    model = Notification
    fields = ['title', 'description']
    template_name = 'notification_update_form.html'
    success_url = '/notifications/'

# Notification Delete View
class NotificationDeleteView(DeleteView):
    model = Notification
    template_name = 'notification_confirm_delete.html'
    success_url = '/notifications/'

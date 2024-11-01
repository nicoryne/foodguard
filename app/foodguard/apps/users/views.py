from django.contrib.auth.hashers import make_password
from .models import User
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

# User List View
class UserListView(ListView):
    model = User
    template_name = 'user_list.html'
    context_object_name = 'users'

# User Detail View
class UserDetailView(DetailView):
    model = User
    template_name = 'user_detail.html'
    context_object_name = 'user'

# Create a New User
class UserCreateView(CreateView):
    model = User
    fields = ['fname', 'lname', 'password', 'email', 'phone_number', 'date_of_birth']
    template_name = 'user_create_form.html'
    success_url = '/users/'

    def form_valid(self, form):
        # Hash the password before saving
        form.instance.password = make_password(form.cleaned_data['password'])
        return super().form_valid(form)

# Update User View
class UserUpdateView(UpdateView):
    model = User
    fields = ['fname', 'lname', 'password', 'email', 'phone_number', 'date_of_birth']
    template_name = 'user_update_form.html'
    success_url = '/users/'

    def form_valid(self, form):
        # Hash the password if it's changed
        if form.cleaned_data['password']:
            form.instance.password = make_password(form.cleaned_data['password'])
        return super().form_valid(form)

# Delete User View
class UserDeleteView(DeleteView):
    model = User
    template_name = 'user_confirm_delete.html'
    success_url = '/users/'



# Create your views here.
from django.shortcuts import render, redirect
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

# Create your views here.
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView

from django.contrib.auth import login
from django.contrib.auth import logout
from django.contrib.auth.views import LogoutView


# Create your views here.
from .models import Todo

class CustomLoginView(LoginView):
    template_name = 'userpage/login.html'
    fields = '__all__'
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('user')
    
class UserLogoutView(LogoutView):
    def get(self, request):
        logout(request)
        return redirect('login')
    
class TodoCreate(CreateView):
    model = Todo
    template_name = 'todo-list/todo_form.html'
    fields = ['title', 'description', 'complete']
    success_url = reverse_lazy('todos')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(TodoCreate, self).form_valid(form)

class TodoUpdate (UpdateView):
    model = Todo
    template_name = 'todo-list/todo_form.html'
    fields = ['title', 'description', 'complete']
    success_url = reverse_lazy('todos')

class DeleteView(DeleteView):
    model = Todo
    template_name = 'todo-list/todo_confirm_delete.html'
    context_object_name = 'todo'
    success_url = reverse_lazy('todos')
    def get_queryset(self):
        owner = self.request.user
        return self.model.objects.filter(user=owner)

def homepage(request):
    if request.user.is_authenticated:
        return redirect(reverse_lazy('user'))
    return render(request, 'userpage/index.html')

def userpage(request):
    return render(request, 'userpage/userpage.html')


class TodoList(ListView):
    model = Todo
    context_object_name = 'todos'
    template_name = 'todo-list/todo_list.html'

class TodoDetail(DetailView):
    model = Todo
    context_object_name = 'todo'
    template_name = 'todo-list/todo.html'
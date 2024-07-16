
from django.urls import path
from .views import TodoList, TodoDetail ,CustomLoginView ,TodoCreate,TodoUpdate,DeleteView
from frontend import views


urlpatterns = [
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', views.UserLogoutView.as_view(http_method_names = ['get', 'post', 'options']), name='logout'),
    
    
    path('', views.homepage, name=""),
    path('user/', views.userpage, name="user"),

    path('todo/', TodoList.as_view(), name='todos'),
    path('todos/<int:pk>/', TodoDetail.as_view(), name='todo'),
    path('todo-create/', TodoCreate.as_view(), name='todo-create'),
    path('todo-update/<int:pk>/', TodoUpdate.as_view(), name='todo-update'),
    path('todo-delete/<int:pk>/', DeleteView.as_view(), name='todo-delete'),
]

from django.urls import path
from .views import TodoList, TodoDetail ,CustomLoginView
from frontend import views


urlpatterns = [
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', views.UserLogoutView.as_view(http_method_names = ['get', 'post', 'options']), name='logout'),
    
    
    path('', views.homepage, name=""),
    path('user/', views.userpage, name="user"),

    path('todo/', TodoList.as_view(), name='todos'),
    path('todos/<int:pk>/', TodoDetail.as_view(), name='todo'),
]
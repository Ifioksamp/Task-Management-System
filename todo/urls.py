from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
	path('signup/', views.SignUpView, name='signup'),
	path('login/', views.LoginView, name='login'),
	path('logout/', auth_views.LogoutView.as_view(), name='logout'),
	path('', views.HomeView, name='home'),
	path('add-task/', views.AddTask, name='add_task'),
	path('task/<int:task_id>/detail/', views.taskDetail, name='task_detail'),
	path('task/<int:task_id>/update/', views.updateTask, name='update_task'),
	path('task/<int:task_id>/delete/', views.deleteTask, name='delete_task'),
	path('join_task/<int:task_id>/', views.joinTask, name='join_task'),
	path('tasks/<int:task_id>/leave/', views.leave_task, name='leave_task'),
	path('profile/<int:user_id>/', views.user_profile, name='user_profile'),
	#path('profile/edit/', views.edit_profile, name='edit_profile'),
]
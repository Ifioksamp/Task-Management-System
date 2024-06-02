from django.shortcuts import render, redirect, get_object_or_404
from .models import Profile, Task
from django.contrib.auth import authenticate, login
from .forms import SignUpForm, TaskForm, CommentForm, TaskUpdate, JoinTaskForm, ProfileForm
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.db.models import Q 


def SignUpView(request):
	if request.method == 'POST':
		form = SignUpForm(request.POST, request.FILES)

		if form.is_valid():
			profile_picture = form.cleaned_data.get('profile_picture')
			gender = form.cleaned_data.get('gender')

			user = form.save(commit=False)

			user.save()

			profile = Profile.objects.create(
				name=user.username,
				created_by=user,
				profile_picture=profile_picture,
				gender=gender
			)

			

			messages.success(request, 'Your account has been created successfully!')

			return redirect('login')
	else:
		form = SignUpForm()

	context = {'form':form}
	return render(request, 'todo/signup.html', context)

def LoginView(request):
	if request.method == 'POST':
		form = AuthenticationForm(request, 	data=request.POST)

		if form.is_valid():
			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password')

			user = authenticate(request, username=username, password=password)

			if user is not None:
				login(request, user)
				messages.success(request, f'You are now logged in as {username}')
				return redirect('home')

			else:
				messages.error(request, 'Invalid username or password')

	else:
		form = AuthenticationForm()
	return render(request, 'todo/login.html', {'form':form})


def HomeView(request):
	search_query = request.GET.get('search', '')

	if search_query:
		tasks = Task.objects.filter(
			Q(title__icontains=search_query)
		)

	else:

		tasks = Task.objects.all().order_by('-created_at')
	return render(request, 'todo/home.html', {'tasks':tasks})

@login_required(login_url='/login')
def AddTask(request):
	if request.method == 'POST':
		form = TaskForm(request.POST)

		if form.is_valid():
			instance = form.save(commit=False)

			instance.user = request.user.profile
			instance.save()
			messages.success(request, 'New Task added!')
			return redirect('home')
	else:
		form = TaskForm()
	return render(request, 'todo/add_task.html', {'form':form})


@login_required(login_url='/login')
def taskDetail(request, task_id):
	task = get_object_or_404(Task, id=task_id)

	comments = task.comments.all()

	is_participant = request.user.profile in task.participants.all() or request.user.profile == task.user

	if request.method == 'POST':
		if not is_participant:
			messages.warning(request, 'You do not have permission to comment on this task.')
			return redirect('task_detail', task_id=task.id)

		form = CommentForm(request.POST)
		if form.is_valid():
			comment = form.save(commit=False)
			comment.user = request.user.profile
			comment.task = task
			comment.save()
			messages.success(request, 'Comment added successfully!')

			return redirect('task_detail', task_id=task.id)

	else:
		form = CommentForm()

	context = {
		'task':task,
		'comments':comments,
		'form':form,
		'is_participant':is_participant
	}

	return render(request, 'todo/task_detail.html', context)


@login_required(login_url='/login')
def updateTask(request, task_id):
	task = get_object_or_404(Task, id=task_id)

	if request.user.profile != task.user:
		messages.warning(request, 'You do not have permission to update this task.')
		return redirect('home')

	if request.method == 'POST':
		form = TaskUpdate(request.POST, instance=task)

		if form.is_valid():
			instance = form.save(commit=False)
			instance.user = request.user.profile
			instance.save()
			messages.success(request, 'Task has been updated!')

			return redirect('home')
	else:
		form = TaskUpdate(instance=task)

	context = {
		'task':task,
		'form':form
	}
	return render(request, 'todo/update_task.html', context)


@login_required(login_url='/login')
def deleteTask(request, task_id):
	task = get_object_or_404(Task, id=task_id)

	if request.user.profile != task.user:
		messages.warning(request, 'You do not have permission to delete this task')
		return redirect('home')

	if request.method == 'POST':
		task.delete()
		messages.success(request, 'Task has been deleted successfully')
		return redirect('home')
	return render(request, 'todo/delete_task.html', {'task':task})


@login_required(login_url='/login')
def joinTask(request, task_id):
	task = get_object_or_404(Task, id=task_id)

	if request.user.profile in task.participants.all():
		messages.warning(request, 'You have already joined this task.')
		return redirect('home')

	if request.method == 'POST':
		task.participants.add(request.user.profile)
		task.save()
		messages.success(request, 'You have successfully joined the task!')
		return redirect('home')

	context = {
		'task':task,
	}

	return redirect('task_detail', task_id=task.id)


@login_required(login_url='/login')
def leave_task(request, task_id):
	task = get_object_or_404(Task, id=task_id)

	profile = request.user.profile

	if profile in task.participants.all():
		task.participants.remove(profile)
		messages.success(request, 'You have left the task')
	else:
		messages.warning(request, 'You are not a participant of this task.')

	return redirect('home')

@login_required(login_url='/login')
def user_profile(request, user_id):
	profile = get_object_or_404(Profile, created_by__id=user_id)
	
	tasks = profile.tasks.all()

	if request.method == 'POST' and request.user == profile.created_by:
		form = ProfileForm(request.POST, request.FILES, instance=profile)
		if form.is_valid():
			form.save()
			messages.success(request, 'Profile updated successfully.')
			return redirect('user_profile', user_id=user_id)
	else:
		form = ProfileForm(instance=profile)

	context = {
		'profile':profile,
		'tasks':tasks,
		'form':form,
	}
	return render(request, 'todo/profile.html', context)
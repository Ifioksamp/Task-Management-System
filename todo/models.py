from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
	GENDER = (
		('Male', 'Male'),
		('Female', 'Female')
	)
	name = models.CharField(max_length=100)
	gender = models.CharField(max_length=6, choices=GENDER)
	created_by = models.OneToOneField(User, related_name='profile', on_delete=models.CASCADE)
	profile_picture = models.ImageField(blank=True, null=True)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now_add=False, auto_now=True)

	def __str__(self):
		return self.name


class Task(models.Model):
	PRIORITY_CHOICES = (
		('High', 'High'),
		('Medium', 'Medium'),
		('Low', 'Low')
	)

	STATUS_CHOICES = (
		('Pending', 'Pending'),
		('In Progress', 'In Progress'),
		('Completed', 'Completed')
	)

	user = models.ForeignKey(Profile, related_name='tasks', on_delete=models.CASCADE)
	title = models.CharField(max_length=100)
	#description = models.TextField()
	priority = models.CharField(max_length=10, choices=PRIORITY_CHOICES)
	created_at = models.DateTimeField(auto_now_add=True)
	due_date = models.DateTimeField()
	is_public = models.BooleanField(default=False)
	participants = models.ManyToManyField(Profile, related_name='tasks_joined', blank=True)
	status = models.CharField(max_length=11, choices=STATUS_CHOICES, default='Pending')

	def __str__(self):
		return self.title


class Comment(models.Model):
	task = models.ForeignKey(Task, related_name='comments', on_delete=models.CASCADE)
	user = models.ForeignKey(Profile, on_delete=models.CASCADE)
	content = models.TextField()
	created_at = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return f'Comment by {self.user.name} on {self.task.title}'
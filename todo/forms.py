from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import Profile, Task, Comment
from django.contrib.auth.models import User


class SignUpForm(UserCreationForm):
	email = forms.EmailField()
	gender = forms.ChoiceField(choices=Profile.GENDER)
	profile_picture = forms.ImageField(required=False)

	class Meta:
		model = User
		fields = ('first_name', 'last_name', 'username', 'email', 'password1', 'password2',
					'gender', 'profile_picture')


class TaskForm(forms.ModelForm):
	due_date = forms.DateTimeField(widget=forms.DateTimeInput(attrs={'type': 'datetime-local'}))
	class Meta:
		model = Task
		fields = ('title', 'priority', 'due_date', 'is_public', 'status')

class TaskUpdate(forms.ModelForm):

	class Meta:
		model = Task 
		fields = ('priority', 'is_public', 'status')

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']
        widgets = {
            'content': forms.Textarea(attrs={'rows': 5, 'placeholder': 'Add a comment...'}),
        }


class JoinTaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = []

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['name', 'gender', 'profile_picture']
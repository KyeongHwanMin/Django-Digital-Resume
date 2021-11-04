from django import forms
from .models import ContactProfile


class ContactForm(forms.ModelForm):

	name = forms.CharField(max_length=100, required=True,
		widget=forms.TextInput(attrs={
			'placeholder': '*Full name..',
			'class': 'form-control'
			}))
<<<<<<< HEAD
	email = forms.EmailField(max_length=254, required=True, 
=======
	email = forms.EmailField(max_length=254, required=True,
>>>>>>> 4c172ba2443b21df26bae70408de9b09d1957031
		widget=forms.TextInput(attrs={
			'placeholder': '*Email..',
			'class': 'form-control'
			}))
<<<<<<< HEAD
	message = forms.CharField(max_length=1000, required=True, 
=======
	message = forms.CharField(max_length=1000, required=True,
>>>>>>> 4c172ba2443b21df26bae70408de9b09d1957031
		widget=forms.Textarea(attrs={
			'placeholder': '*Message..',
			'class': 'form-control',
			'rows': 6,
			}))


	class Meta:
		model = ContactProfile
		fields = ('name', 'email', 'message',)
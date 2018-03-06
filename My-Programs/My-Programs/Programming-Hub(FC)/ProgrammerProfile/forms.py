<<<<<<< HEAD
from django.forms import forms
=======
from django.forms import forms,extras
>>>>>>> 358728481686bb8a7013093aa82f467ab168bf77
from django import forms
#To add a User into the database


class Add(forms.Form):
    Username = forms.CharField(label='Your name', max_length=100,initial=" ")
    Password=forms.CharField(widget=forms.PasswordInput,label="Password",initial=" ")
    Email = forms.EmailField(label="Email Id:", initial="",)
    age=forms.IntegerField(label="Your age")
    Description=forms.CharField(label="Describe Yourself",widget=forms.Textarea)
<<<<<<< HEAD
    
=======
    OPTIONS=(("Java","Java"),("C++","C++"),("C","C"),("Python","Python"),("JavaScript","JavaScript"),("Ruby","Ruby"))
    Languages=forms.MultipleChoiceField(
        required=True,
        widget=forms.CheckboxSelectMultiple,
        choices=OPTIONS,
    )
>>>>>>> 358728481686bb8a7013093aa82f467ab168bf77
    Profile_Picture = forms.FileField(label="Your Profile Picture:")


class Authenticate(forms.Form):
    Username = forms.CharField(label="Username:", initial=" ")
    Password = forms.CharField(widget=forms.PasswordInput(), initial="")
<<<<<<< HEAD
class posts(forms.Form):
    title=forms.CharField(label='Give a title', max_length=100,initial=" ")
    Review=forms.CharField(label="Your Article",max_length=1000000000000000,initial="Type your article",widget=forms.Textarea)
=======


>>>>>>> 358728481686bb8a7013093aa82f467ab168bf77

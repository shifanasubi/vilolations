from django import forms

from complaints.models import User,Road

from django.contrib.auth.forms import UserCreationForm

class SignUpForm(UserCreationForm):
    
    class Meta:
        model=User
        fields=["username","email","password1","password2","phone"]
        widgets={
            "username":forms.TextInput(attrs={"class":"form-control"}),
            "email":forms.EmailInput(attrs={"class":"form-control"}),
            "phone":forms.NumberInput(attrs={"class":"form-control"}),

        }

class SignInForm(forms.Form):

    username=forms.CharField()
    password=forms.CharField()
    

class RoadForm(forms.ModelForm):

    class Meta:

        model=Road

        fields=["vehicle","description","image"]

        # widgets={
        #         "title":forms.TextInput(attrs={"class":"form-control"}),
        #         "category":forms.Select(attrs={"class":"form-control form-select"}),
        #         "Amount":forms.TextInput(attrs={"class":"form-control"}),
        #         "payment_method":forms.Select(attrs={"class":"form-control form-select"}),



        # }




from django import forms
from django.contrib.auth.models import User




class SignUpForm(forms.Form):
    username=forms.CharField(max_length=150,required=True)
    email=forms.EmailField(required=True)
    password1=forms.CharField(widget=forms.PasswordInput,required=True)
    password2=forms.CharField(widget=forms.PasswordInput,required=True)


    def clean_username(self):
        username=self.cleaned_data.get('username')
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError("Bu username allaqochon mavjud iltimos boshqa tanlang ")

        return username

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("Bu email allaqochon mavjud iltimos boshqa tanlang ")

        return email


    def clean(self):
        cleaned_data=super().clean()
        password1=cleaned_data.get('password1')
        password2=cleaned_data.get('password2')

        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Parolni kiritishda muammo iltimos bir xil parol kiriting")

        return cleaned_data





class LoginForm(forms.Form):
    username=forms.CharField(max_length=150,required=True)
    password = forms.CharField(widget=forms.PasswordInput, required=True)









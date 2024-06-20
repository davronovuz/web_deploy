from .models import New,Category,Contact
from django import forms



#Yanngilik qo'shish uchun forma
class AddCategoryForm(forms.ModelForm):
    class Meta:
         model=Category
         fields="__all__"


class AddNewsForm(forms.ModelForm):
    class Meta:
         model=New
         fields="__all__"



class AddContacForm(forms.ModelForm):
    class Meta:
         model=Contact
         fields="__all__"
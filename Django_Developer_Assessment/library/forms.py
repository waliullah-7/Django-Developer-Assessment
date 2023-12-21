# from django.core import validators
from django import forms
from .models import authorm, bookm

class  authorf(forms.ModelForm):
    class Meta:
        model = authorm
        fields = '__all__'
        labels = {'first_name': 'First Name: ' , 'last_name' :'Last Name: ' , 'adress':'Adress: '}


class bookf(forms.ModelForm):
    class Meta:
        model = bookm
        fields = '__all__'
        labels = {'title': 'Title', 'author':'Author' ,'pb_year': 'Publication Year: ', 'isbn': 'ISBN Number: ',  'price': 'Price: '}

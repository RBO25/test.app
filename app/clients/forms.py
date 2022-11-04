from django import forms
from django.forms import SelectDateWidget
from .models import Client
from rest_framework.exceptions import ValidationError
import datetime


class Client(forms.ModelForm):
    # birth = forms.DateField(widget=forms.DateInput(format="%d-%m-%Y", attrs={'type': 'date'}))
    class Meta:
        model = Client
        tg = forms.CharField(required=False)
        email = forms.EmailField(required=False)
        widgets={
            'birth': SelectDateWidget(years=(1940, 2004))
        }


    # def clean_birth(self):
    #     data = self.cleaned_data['birth']
    #     if data > datetime.date.today():
    #         raise ValidationError('Неправильный ввод даты')
    #     if data < datetime.date.today() < datetime.timedelta(years=18):
    #         raise ValidationError('Зарегистрироваться возможно только с 18 лет')
    #     return data
#

    # def year(self):
    #     if self > 2004:
    #         raise ValidationError('Зарегистрироваться возможно только с 18 лет')


    # def clean_fields(self, exclude=None):
    #     super().clean_fields(exclude=exclude)
    #
    #     now = timezone.now()
    #     if self.birth < (now - timedelta(years=30)):
    #         raise ValidationError('Зарегистрироваться возможно только с 18 лет')
    #
    #
    # def birth_log(self):
    #     td = datetime.datetime.now.date("%d-%m-%Y")
    #     tb = self.birth.datetime.date("%d-%m-%Y")
    #     age_years = int((td - tb).days / 365)
    #     if age_years < 18:
    #         raise ValidationError('Зарегистрироваться возможно только с 18 лет')
    #
    # def get_age(self, obj):
    #     if dt.datetime.now().year - obj.birth < 18:
    #         raise ValidationError('Зарегистрироваться возможно только с 18 лет')

# widget=forms.DateInput(format="%d-%m-%Y"))
# widget=forms.DateInput(format="%d-%m-%Y", attrs={
#                                     'data-min': 1/1/1940,
#                                     'data-max': 1/1/2004})),


    # birth = forms.DateField(widget=forms.DateInput(attrs={'min': 1/1/1940, 'max': 1/1/2004}))
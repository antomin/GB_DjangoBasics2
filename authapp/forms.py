from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.forms import forms

from authapp.models import ShopUser


class ShopUserLoginForm(AuthenticationForm):
    class Meta:
        model = ShopUser
        fields = ('username', 'password')

    def __init__(self, *args, **kwargs):
        super(ShopUserLoginForm, self).__init__( *args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control py-4'


class ShopUserRegistrationForm(UserCreationForm):
    class Meta:
        model = ShopUser
        fields = ('first_name', 'last_name', 'username', 'email', 'password1', 'password2', 'age')

    def __init__(self, *args, **kwargs):
        super(ShopUserRegistrationForm, self).__init__( *args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control py-4'

    def clean_age(self):
        data = self.cleaned_data['age']
        if data < 18:
            raise forms.ValidationError('Регистрация с 18 лет.')
        return data


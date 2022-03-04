
from django import forms

from authapp.forms import ShopUserEditForm, ShopUserRegistrationForm
from authapp.models import ShopUser
from mainapp.models import ProductCategory


class UserCreationAdminForm(ShopUserRegistrationForm):
    class Meta:
        model = ShopUser
        fields = (
            'first_name', 'last_name', 'username', 'email', 'password1', 'password2', 'age', 'avatar', 'is_staff'
        )

    def __init__(self, *args, **kwargs):
        super(UserCreationAdminForm, self).__init__( *args, **kwargs)
        self.fields['avatar'].widget.attrs['class'] = 'custom-file-label'


class CategoryCreationAdminForm(forms.ModelForm):
    class Meta:
        model = ProductCategory
        fields = ('name', 'description')

    def __init__(self, *args, **kwargs):
        super(CategoryCreationAdminForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control py-4'


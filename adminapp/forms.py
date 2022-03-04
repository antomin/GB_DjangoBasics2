from django import forms

from authapp.forms import ShopUserRegistrationForm
from authapp.models import ShopUser
from mainapp.models import Product, ProductCategory


class UserCreationAdminForm(ShopUserRegistrationForm):
    class Meta:
        model = ShopUser
        fields = ('first_name', 'last_name', 'username', 'email', 'password1', 'password2', 'age', 'avatar', 'is_staff')

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


class ProductCreationAdminForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ('name', 'category', 'description', 'image_url', 'price', 'quantity')

    def __init__(self, *args, **kwargs):
        super(ProductCreationAdminForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control py-4'
        self.fields['image_url'].widget.attrs['class'] = 'custom-file-label'

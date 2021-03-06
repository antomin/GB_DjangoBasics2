from django import forms
from django.forms import FileInput

from authapp.forms import ShopUserEditForm, ShopUserRegistrationForm
from authapp.models import ShopUser
from mainapp.models import Product, ProductCategory
from ordersapp.models import Order


class ShopUserCreateAdminForm(ShopUserRegistrationForm):
    class Meta:
        model = ShopUser
        fields = ('first_name', 'last_name', 'username', 'email', 'password1', 'password2', 'age', 'avatar', 'is_staff')

    def __init__(self, *args, **kwargs):
        super(ShopUserCreateAdminForm, self).__init__(*args, **kwargs)
        self.fields['avatar'].widget.attrs['class'] = 'custom-file-label'


class ShopUserEditAdminForm(ShopUserEditForm):
    class Meta:
        model = ShopUser
        fields = ('first_name', 'last_name', 'avatar', 'age', 'email', 'username', 'is_active', 'is_staff')
        widgets = {'avatar': FileInput()}

    def __init__(self, *args, **kwargs):
        super(ShopUserEditForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control py-4'
        self.fields['avatar'].widget.attrs['class'] = 'custom-file-label'


class ProductCategoryCreateForm(forms.ModelForm):
    class Meta:
        model = ProductCategory
        fields = ('name', 'description', 'is_active')

    def __init__(self, *args, **kwargs):
        super(ProductCategoryCreateForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control py-4'


class ProductCreateForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ('name', 'category', 'description', 'image_url', 'price', 'quantity', 'is_active')
        widgets = {'image_url': FileInput()}

    def __init__(self, *args, **kwargs):
        super(ProductCreateForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control py-4'
        self.fields['image_url'].widget.attrs['class'] = 'custom-file-label'


class OrderEditForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ('status', 'is_active')

    def __init__(self, *args, **kwargs):
        super(OrderEditForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'

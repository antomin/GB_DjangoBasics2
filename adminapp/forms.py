
from django.forms import FileInput, forms

from authapp.forms import ShopUserEditForm, ShopUserRegistrationForm
from authapp.models import ShopUser


class UserCreationAdminForm(ShopUserRegistrationForm):
    class Meta:
        model = ShopUser
        fields = (
            'first_name', 'last_name', 'username', 'email', 'password1', 'password2', 'age', 'avatar', 'is_staff'
        )

    def __init__(self, *args, **kwargs):
        super(UserCreationAdminForm, self).__init__( *args, **kwargs)
        self.fields['avatar'].widget.attrs['class'] = 'custom-file-label'


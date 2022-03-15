from collections import OrderedDict
from datetime import datetime
from urllib.parse import urlencode, urlunparse

import requests
from django.utils import timezone
from social_core.exceptions import AuthForbidden

from authapp.models import ShopUser, ShopUserProfile


def save_user_profile(backend, user: ShopUser, response, *args, **kwargs):
    if backend.name != 'vk-oauth2':
        return
    api_url = urlunparse(('https', 'api.vk.com', '/method/users.get', None,
                          urlencode(OrderedDict(fields=','.join(('bdate', 'sex', 'about', 'country', 'photo_200_orig')),
                                                access_token=response['access_token'],
                                                v='5.131')),
                          None
                          ))
    resp = requests.get(api_url)
    if resp.status_code != 200:
        return
    data = resp.json()['response'][0]
    if data['sex']:
        user.shopuserprofile.gender = ShopUserProfile.MALE if data['sex'] == 2 else ShopUserProfile.FEMAIL
    if data['about']:
        user.shopuserprofile.about_me = data['about']
    if data['bdate']:
        bdate = datetime.strptime(data['bdate'], '%d.%m.%Y').date()
        age = timezone.now().year - bdate.year
        if age < 18:
            user.delete()
            raise AuthForbidden('social_core.backends.vk.VKOAuth2')
        user.age = age
    if data['country']:
        user.shopuserprofile.country = data['country']['title']
    if data['photo_200_orig']:
        img = requests.get(data['photo_200_orig'])
        with open(f'media/users_avatars/{user.username}.jpg', 'wb') as f:
            f.write(img.content)
        user.avatar = f'users_avatars/{user.username}.jpg'
    user.save()





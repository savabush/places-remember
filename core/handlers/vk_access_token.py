from django.contrib.auth.models import User
from social_django.models import UserSocialAuth


def get_access_token(request):
    """
    Getting VK_TOKEN and OWNER_ID for VK_API using username
     and library python-social-django
    """
    username_vk = User.objects.get(username=f'{request.user.username}')
    owner_id = UserSocialAuth.objects.get(user_id=username_vk.id).extra_data['id']
    access_token = UserSocialAuth.objects.get(user_id=username_vk.id).extra_data['access_token']
    return access_token, owner_id

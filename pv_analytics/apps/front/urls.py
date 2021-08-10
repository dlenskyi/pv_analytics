from django.urls import re_path
from .views import *

urlpatterns = [
    re_path(r"^admin_cabinet", AdminSection.as_view(), name="admin-cabinet"),
    re_path(r"^.*", AnonymousSection.as_view(), name="anonymous-cabinet"),
]

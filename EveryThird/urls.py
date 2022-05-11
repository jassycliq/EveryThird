from django.urls import re_path
from rest_framework.urlpatterns import format_suffix_patterns

import lyft_app.views

urlpatterns = [
    re_path(r'^test/?$', lyft_app.views.Test.as_view(), name='test'),
]

urlpatterns = format_suffix_patterns(urlpatterns)


from django.urls import path

from test_async.views import test_view

urlpatterns = [
    path('test', test_view),
]

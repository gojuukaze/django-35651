from django.urls import path, include

urlpatterns = [
    path('', include('test_async.urls')),
]

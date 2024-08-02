from django.core.cache import cache
from django.http import HttpResponse


async def test_view(request):
    cache.get('key')
    return HttpResponse('Hi')

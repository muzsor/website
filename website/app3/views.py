from django.core.cache import caches
from django.shortcuts import render


def ShowCache(request):
    default_value = caches['default'].get_or_set('keyName', 'Hello, world!')
    primary_value = caches['primary'].get_or_set('keyName', 'Hello, my friend!')
    secondary_value = caches['secondary'].get_or_set('keyName', 'GoodBye, my friend!')

    context = {
        'default_value': default_value,
        'primary_value': primary_value,
        'secondary_value': secondary_value,
    }
    return render(request, 'app3/index.html', context=context)

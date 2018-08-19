from core import rest

async def ls(request):
    return rest.get({}, 'site', 'first')

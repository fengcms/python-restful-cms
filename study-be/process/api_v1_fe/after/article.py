async def ls (response):
    for i in response['list']:
        i.pop('content')
        i.pop('markdown')
    return response

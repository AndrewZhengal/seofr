from aiohttp import web
from modw import Page, objects


async def home_handler(request):
    all_objects = await objects.execute(Page.select().limit(100))
    text = "\n".join([x.title for x in all_objects])
    return web.Response(text=text)


async def category_handler(request):
    name = request.match_info.get('name', 'Anonymous')
    text = 'Hello, ' + name
    return web.Response(text=text)


async def post_handler(request):
    name = request.match_info.get('name', 'Anonymous')
    text = 'Hello, ' + name
    return web.Response(text=text)


app = web.Application()

app.add_routes([
    web.get('/', home_handler),
    web.get('/category', category_handler),
    web.get('/post', post_handler)
])


if __name__ == '__main__':
    web.run_app(app)

import aiohttp
import asyncio
from demo import create_app

try:
    import uvloop
    asyncio.set_event_loop_policy(uvloop.EventLoopPolicy())
except ImportError:
    print('Library uvloop is not available')


app = create_app()
if __name__ == '__main__':
    aiohttp.web.run_app(app)
import argparse
import aiohttp
import asyncio
from demo import create_app

try:
    import uvloop

    asyncio.set_event_loop_policy(uvloop.EventLoopPolicy())
except ImportError:
    print('Library uvloop is not available')

parser = argparse.ArgumentParser(description="Demo project")
parser.add_argument('--host', help='Host to listen', default='127.0.0.1')
parser.add_argument('--port', help='Port to accept connections', default='8080')
parser.add_argument('--reload', action='store_true', help='Auto reloaded')

args = parser.parse_args()

if args.reload:
    print('Start with code reload')
    import aioreloader
    aioreloader.start()

app = create_app()
if __name__ == '__main__':
    aiohttp.web.run_app(app, host=args.host, port=args.port)

import asyncio
import os

import gevent
from gevent.pywsgi import WSGIServer

from src.async_faceit_api import FaceitAPI
from src.async_faceit_api.dataclasses.enums import FaceitEventType
from src.async_faceit_api.webhooks import FaceitWebhooks


async def callback(event_obj):
    print(f"cb called with {event_obj}")



if __name__ == "__main__":
    hooker = FaceitWebhooks()
    # hooker.run()
    https_server = WSGIServer(("127.0.0.1", 5000), hooker)
    https_server.start()

    loop = asyncio.new_event_loop()
    # loop.run_until_complete(test_task())
    print('rdy')
    loop.run_forever()

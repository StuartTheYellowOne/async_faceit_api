import asyncio
import typing
from typing import Tuple, Any

from aiohttp import request
from flask import Flask, abort, request

from .dataclasses.enums import FaceitEventType
from .dataclasses.events import *


class FaceitWebhooks(Flask):

    __EVENT_TO_CLASS = {
        'hub_created': HubCreated,
        'hub_updated': HubUpdated,
        'hub_role_updated': HubRoleUpdated,
        'hub_role_created': HubRoleCreated,
        'hub_role_deleted': HubRoleDeleted,
    }

    def __init__(self, **kwargs):
        super().__init__('FaceitAPIwebhook', **kwargs)
        self.route('/webhook', methods=['POST'])(self.received)
        self.__callbacks = {FaceitEventType(x): set() for x in self.__EVENT_TO_CLASS}

    def __call__(self, *args, **kwargs):
        print("called")

    def subscribe(self, event_type: FaceitEventType, callback: typing.Callable):
        self.__callbacks[event_type].add(callback)

    def unsubscribe(self, event_type: FaceitEventType, callback: typing.Callable):
        self.__callbacks[event_type].remove(callback)

    @classmethod
    async def __create_event(cls, json_response: dict) -> Any:
        payload_class = cls.__EVENT_TO_CLASS.get(json_response["event"], UnknownEvent)
        json_response["payload"] = payload_class(**json_response["payload"])
        return FaceitEvent(**json_response)

    async def received(self):
        if request.method != 'POST':
            abort(400)
            print("hmm")
            return "\n"
        print(f'got {request.json}')
        obj: FaceitEvent = await self.__create_event(request.json)
        await asyncio.gather(*[x(obj) for x in self.__callbacks[obj.event]])
        print(f'got {obj}')
        return "\n"

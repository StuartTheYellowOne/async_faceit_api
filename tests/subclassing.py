import asyncio
import datetime
import os

from dotenv import load_dotenv

from src.async_faceit_api import FaceitAPI
from src.async_faceit_api.dataclasses import MatchStats
from src.async_faceit_api.enums import Game

load_dotenv()


class MyApi(FaceitAPI):
    """
    Api inheriting FaceitAPI
    """
    def __init__(self):
        api_key = os.getenv('faceit_api_key')
        super().__init__(api_key)

    async def get_played_maps(self, player_id):
        matches = await self.player_history(player_id, Game.CS_GO)
        maps = {}
        for match in matches.items:
            map_ = await self.match_stats(match.match_id)
            if map_ in maps:
                maps[map_] += 1
            else:
                maps[map_] = 1
        return maps

    async def get_played_maps_parallel(self, player_id):
        matches = await self.player_history(player_id, Game.CS_GO)
        tasks = [self.match_stats(match.match_id) for match in matches.items]
        all_match_stats = await asyncio.gather(*tasks)
        maps = {}
        for match_stat in all_match_stats:
            match_stat: MatchStats
            map_ = match_stat.rounds[0].round_stats['Map']
            if map_ in maps:
                maps[map_] += 1
            else:
                maps[map_] = 1
        return maps


async def my_task():
    api = MyApi()
    player_id = "a5ae3596-697d-4f08-af16-4584a7c93ab2"
    time = datetime.datetime.now()
    print(await api.get_played_maps(player_id))
    print(datetime.datetime.now() - time)
    time = datetime.datetime.now()
    print(await api.get_played_maps_parallel(player_id))
    print(datetime.datetime.now() - time)


if __name__ == "__main__":
    loop = asyncio.new_event_loop()
    loop.run_until_complete(my_task())
    loop.close()

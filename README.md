# Async faceit API

Async wrapper for the faceit API for csgo.

### Error Handling

Note that the async api methods return an object of type FaceitApiError 
if the request was not successful. To distinguish between a successful 
response and an error, you can easily use the object as a boolean expression:
```
    games = await api.games()
    if games:
        print('success')
    else:
        print('error')
```

### Getting started

If you dont already have a loop in your programm you need to create one. 
Here is a basic example which will search players by the username and
prints out a dict with the nicknames and player_ids: 
```
import asyncio
from src.async_faceit_api import FaceitAPI


async def my_task():
    api_key = "..."
    api = FaceitAPI(api_key)
    players = await api.search_players("username")
    print({player.nickname: player.player_id for player in players.items})


if __name__ == "__main__":
    loop = asyncio.new_event_loop()
    loop.run_until_complete(my_task())
    loop.close()
```
Its recomended to store the api_key somewhere safe (e.g .env file)! 
Here is another example on how you can implement the api:

```
class MyApi(FaceitAPI):
    def __init__(self):
        api_key = os.getenv('faceit_api_key')
        super().__init__(api_key)

    async def get_played_maps_parallel(self, player_id):
        matches = await self.player_history(player_id, Game.CS_GO)
        all_match_stats = await asyncio.gather(*[self.match_stats(match.match_id) for match in matches.items])
        maps = {}
        for match_stat in all_match_stats:
            match_stat: MatchStats
            map = match_stat.rounds[0].round_stats['Map']
            if map in maps:
                maps[map] += 1
            else:
                maps[map] = 1
        return maps


async def my_task():
    api = MyApi()
    player_id = "..."
    print(await api.get_played_maps_parallel(player_id))


if __name__ == "__main__":
    loop = asyncio.new_event_loop()
    loop.run_until_complete(my_task())
    loop.close()
```

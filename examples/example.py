import asyncio
from src.async_faceit_api import FaceitAPI


async def my_task():
    api_key = "..."  # Set your api key here
    api = FaceitAPI(api_key)
    players = await api.search_players("username")
    print({player.nickname: player.player_id for player in players.items})


if __name__ == "__main__":
    loop = asyncio.new_event_loop()
    loop.run_until_complete(my_task())
    loop.close()

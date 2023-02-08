import os
import asyncio

from src.async_faceit_api import FaceitAPI
from dotenv import load_dotenv

from src.async_faceit_api.types.enums import Game

load_dotenv()


async def test_championship(api: FaceitAPI):
    game_id = Game.CS_GO
    championship_id = "3c5121c0-ac3a-4a99-9788-20ee262fca7f"
    champs = await api.championships(game_id)
    await api.championship(championship_id)
    await api.championship_results(championship_id)
    await api.championship_subscriptions(championship_id)


async def test_games(api: FaceitAPI):
    game_id = Game.CS_GO
    await api.games()
    await api.game_details(game_id)
    await api.game_parent_details(game_id)


async def test_hub(api: FaceitAPI):
    hub_id = "bfbb0657-8694-4278-8007-a7dc58f544af"
    await api.hub(hub_id)
    await api.hub_matches(hub_id)
    await api.hub_members(hub_id)
    await api.hub_roles(hub_id)
    await api.hub_rules(hub_id)
    await api.hub_stats(hub_id)


async def test_leaderboards(api: FaceitAPI):
    hub_id = "bfbb0657-8694-4278-8007-a7dc58f544af"
    championship_id = "3c5121c0-ac3a-4a99-9788-20ee262fca7f"
    group = 0
    season = 0
    leaderboard_id = ""
    await api.leaderboards_championship(championship_id)
    await api.leaderboards_championship_groups(championship_id, group)
    await api.leaderboards_hub(hub_id)
    await api.leaderboards_hub_general(hub_id)
    await api.leaderboards_hub_season(hub_id, season)
    await api.leaderboard(leaderboard_id)


async def test_match(api: FaceitAPI):
    match_id = "1-506ad3d0-7266-4d43-8cfc-fdbbac077027"
    await api.match(match_id)
    await api.match_stats(match_id)


async def test_organizer(api: FaceitAPI):
    name = ""
    organizer_id = "faceit"
    await api.organizer_by_name(name)
    await api.organizer_by_id(organizer_id)
    await api.organizer_championships(organizer_id)
    await api.organizer_games(organizer_id)
    await api.organizer_hubs(organizer_id)
    await api.organizer_tournaments(organizer_id)


async def test_player(api: FaceitAPI):
    nickname = "Stuart11"
    game = "csgo"
    player_id = "a5ae3596-697d-4f08-af16-4584a7c93ab2"
    game_player_id = ""
    game_id = "csgo"
    await api.player_by_nickname(nickname)
    await api.player_by_game_player_id(game, game_player_id)
    await api.player_by_player_id(player_id)
    await api.player_history(player_id, game)
    await api.player_hubs(player_id)
    await api.player_game_stats(player_id, game_id)
    await api.player_tournaments(player_id)


async def test_ranking(api: FaceitAPI):
    game_id = Game.CS_GO
    region = "EU"
    player_id = "a5ae3596-697d-4f08-af16-4584a7c93ab2"
    await api.ranking(game_id, region)
    await api.ranking_of_player(game_id, region, player_id)


async def test_search(api: FaceitAPI):
    name = ""
    nickname = "Stuart11"
    await api.search_championships(name)
    await api.search_hubs(name)
    await api.search_organizers(name)
    await api.search_players(nickname)
    await api.search_teams(nickname)
    await api.search_tournaments(name)


async def test_teams(api: FaceitAPI):
    team_id = "90f11a8e-ae27-4d64-9a5f-ba5425e431b5"
    game_id = Game.CS_GO
    await api.team(team_id)
    await api.team_game_stats(team_id, game_id)
    await api.team_tournaments(team_id)


async def test_tournament(api: FaceitAPI):
    tournament_id = ""
    await api.tournaments()
    await api.tournament(tournament_id)
    await api.tournament_brackets(tournament_id)
    await api.tournament_matches(tournament_id)
    await api.tournament_teams(tournament_id)


async def test_task():
    api = FaceitAPI(os.getenv('faceit_api_key'))
    await test_championship(api)
    # await test_games(api)
    # await test_hub(api)
    # await test_leaderboards(api)
    # await test_match(api)
    # await test_organizer(api)
    # await test_player(api)
    # await test_ranking(api)
    # await test_search(api)
    # await test_teams(api)
    # await test_tournament(api)


if __name__ == "__main__":
    loop = asyncio.new_event_loop()
    loop.run_until_complete(test_task())

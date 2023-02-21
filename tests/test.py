import datetime
import os
import asyncio

from src.async_faceit_api import FaceitAPI
from dotenv import load_dotenv

from src.async_faceit_api.dataclasses import Match
from src.async_faceit_api.enums import Game, Region, Country

load_dotenv()


async def test_championship(api: FaceitAPI):
    game_id = Game.CS_GO
    championship_id = "3c5121c0-ac3a-4a99-9788-20ee262fca7f"
    if not await api.championships(game_id):
        print("error championships(game_id)")
    if not await api.championship(championship_id):
        print("error championship(championship_id)")
    if not await api.championship_results(championship_id):
        print("error championship_results(championship_id)")
    if not await api.championship_subscriptions(championship_id):
        print("error championship_subscriptions(championship_id)")


async def test_games(api: FaceitAPI):
    game_id = Game.CS_GO
    if not await api.games():
        print("error games()")
    if not await api.game_details(game_id):
        print("error game_details(game_id)")
    if not await api.game_parent_details(game_id):
        print("error game_parent_details(game_id)")


async def test_hub(api: FaceitAPI):
    hub_id = "bfbb0657-8694-4278-8007-a7dc58f544af"
    if not await api.hub(hub_id):
        print("error hub(hub_id)")
    if not await api.hub_matches(hub_id):
        print("error hub_matches(hub_id)")
    if not await api.hub_members(hub_id):
        print("error hub_members(hub_id)")
    if not await api.hub_roles(hub_id):
        print("error hub_roles(hub_id)")
    if not await api.hub_rules(hub_id):
        print("error hub_rules(hub_id)")
    if not await api.hub_stats(hub_id):
        print("error hub_stats(hub_id)")


async def test_leaderboards(api: FaceitAPI):
    hub_id = "bfbb0657-8694-4278-8007-a7dc58f544af"
    championship_id = "3c5121c0-ac3a-4a99-9788-20ee262fca7f"
    group = 1
    season = 1
    leaderboard_id = '63e107a45ca9066d45af3a26'
    if not await api.leaderboards_championship(championship_id):
        print("error leaderboards_championship(championship_id)")
    if not await api.leaderboards_championship_groups(championship_id, group):
        print("error leaderboards_championship_groups(championship_id, group)")
    if not await api.leaderboards_hub(hub_id):
        print("error leaderboards_hub(hub_id)")
    if not await api.leaderboards_hub_general(hub_id):
        print("error leaderboards_hub_general(hub_id)")
    if not await api.leaderboards_hub_season(hub_id, season):
        print("error leaderboards_hub_season(hub_id, season)")
    if not await api.leaderboard(leaderboard_id):
        print("error leaderboard(leaderboard_id)")


async def test_match(api: FaceitAPI):
    match_id = "1-506ad3d0-7266-4d43-8cfc-fdbbac077027"
    if not await api.match(match_id):
        print("error match(match_id)")
    if not await api.match_stats(match_id):
        print("error match_stats(match_id)")


async def test_organizer(api: FaceitAPI):
    name = "faceit"
    organizer_id = "bedc14d0-8bb7-4738-a240-a09c25723159"
    if not await api.organizer_by_name(name):
        print("error organizer_by_name(name)")
    if not await api.organizer_by_id(organizer_id):
        print("error organizer_by_id(organizer_id)")
    if not await api.organizer_championships(organizer_id):
        print("error organizer_championships(organizer_id)")
    if not await api.organizer_games(organizer_id):
        print("error organizer_games(organizer_id)")
    if not await api.organizer_hubs(organizer_id):
        print("error organizer_hubs(organizer_id)")
    if not await api.organizer_tournaments(organizer_id):
        print("error organizer_tournaments(organizer_id)")


async def test_player(api: FaceitAPI):
    nickname = "Stuart11"
    player_id = "a5ae3596-697d-4f08-af16-4584a7c93ab2"
    game_player_id = "76561198102388493"
    game = Game.CS_GO
    if not await api.player_by_nickname(nickname):
        print("error player_by_nickname(nickname)")
    if not await api.player_by_game_player_id(game, game_player_id):
        print("error player_by_game_player_id(game, game_player_id)")
    if not await api.player_by_player_id(player_id):
        print("error player_by_player_id(player_id)")
    if not await api.player_history(player_id, game):
        print("error player_history(player_id, game)")
    if not await api.player_hubs(player_id):
        print("error player_hubs(player_id)")
    if not await api.player_game_stats(player_id, game):
        print("error player_game_stats(player_id, game)")
    if not await api.player_tournaments(player_id):
        print("error player_tournaments(player_id)")


async def test_ranking(api: FaceitAPI):
    game_id = Game.CS_GO
    region = Region.EU
    player_id = "a5ae3596-697d-4f08-af16-4584a7c93ab2"
    if not await api.ranking(game_id, region):
        print("error ranking(game_id, region)")
    if not await api.ranking_of_player(game_id, region, player_id):
        print("error ranking_of_player(game_id, region, player_id)")


async def test_search(api: FaceitAPI):
    name = "csgo"
    nickname = "Stuart11"
    if not await api.search_championships(name):
        print("error search_championships(name)")
    if not await api.search_hubs(name):
        print("error search_hubs(name)")
    if not await api.search_organizers(name):
        print("error search_organizers(name)")
    if not await api.search_players(nickname):
        print("error search_players(nickname, country=county)")
    if not await api.search_teams(nickname):
        print("error search_teams(nickname)")
    if not await api.search_tournaments(name):
        print("error search_tournaments(name)")


async def test_teams(api: FaceitAPI):
    team_id = "90f11a8e-ae27-4d64-9a5f-ba5425e431b5"
    game_id = Game.CS_GO
    if not await api.team(team_id):
        print("error team(team_id)")
    if not await api.team_game_stats(team_id, game_id):
        print("error team_game_stats(team_id, game_id)")
    if not await api.team_tournaments(team_id):
        print("error team_tournaments(team_id)")


async def test_tournament(api: FaceitAPI):
    tournament_id = "ffffb42e-fce8-4beb-9f6d-feeb1e0cb6b7"
    if not await api.tournaments(Game.CS_GO):
        print("error tournaments()")
    if not await api.tournament(tournament_id):
        print("error tournament(tournament_id)")
    if not await api.tournament_brackets(tournament_id):
        print("error tournament_brackets(tournament_id)")
    if not await api.tournament_matches(tournament_id):
        print("error tournament_matches(tournament_id)")
    if not await api.tournament_teams(tournament_id):
        print("error tournament_teams(tournament_id)")


async def test_task():
    api = FaceitAPI(os.getenv('faceit_api_key'))

    await asyncio.gather(
        test_championship(api),
        test_games(api),
        test_hub(api),
        test_leaderboards(api),
        test_match(api),
        test_organizer(api),
        test_player(api),
        test_ranking(api),
        test_search(api),
        test_teams(api),
        test_tournament(api)
    )


if __name__ == "__main__":
    loop = asyncio.new_event_loop()
    loop.run_until_complete(test_task())
    loop.close()

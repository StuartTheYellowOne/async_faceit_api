from typing import Tuple, Any
from aiohttp import request
from .types.enums import *
from .types.dataclasses import *


class FaceitAPI:
    __BASE_URL: str = 'https://open.faceit.com/data/v4/{}'

    def __init__(self, api_token: str):
        self.__header = {
            'accept': 'application/json',
            'Authorization': 'Bearer {}'.format(api_token)
        }

    async def __make_request(self, method: str, url: str) -> Tuple[int, Any]:
        async with request(method, url, headers=self.__header) as response:
            return response.status, await response.json()

    @staticmethod
    async def __create_object(response: Tuple[int, Any], object_class=None) -> Any:
        status, json_response = response
        if not 200 <= status < 300:
            print("error")
            return FaceitApiError(**json_response, status_code=status)
        if not (object_class is None):
            return object_class(**json_response)
        return json_response

    @staticmethod
    async def __create_collection(response: Tuple[int, Any], object_class, collection_class=Collection) -> Any:
        status, json_response = response
        if not 200 <= status < 300:
            return FaceitApiError(**json_response, status_code=status)
        json_response["items"] = [object_class(**x) for x in json_response["items"]]
        return collection_class(**json_response)

    # region Championships
    async def championships(self, game: Game, type: MatchType = MatchType.ALL, offset: int = 0,
                            limit: int = 10) -> Collection[Championship]:
        url = FaceitAPI.__BASE_URL.format(
            f'championships?game={game.value}&type={type.value}&offset={offset}&limit={limit}')
        retval = await self.__make_request('GET', url)
        return await FaceitAPI.__create_collection(retval, Championship)

    async def championship(self, championship_id: str,
                           expanded: Expansion = Expansion.NONE) -> Championship:
        url = FaceitAPI.__BASE_URL.format(f'championships/{championship_id}')
        if expanded is not Expansion.NONE:
            url += f'?expanded={expanded.value}'
        retval = await self.__make_request('GET', url)
        return await FaceitAPI.__create_object(retval, Championship)

    async def championship_matches(self, championship_id: str, type: MatchType = MatchType.ALL,
                                   offset: int = 0, limit: int = 20) -> Collection[Match]:
        url = FaceitAPI.__BASE_URL.format(
            f'championships/{championship_id}/matches?type={type.value}&offset={offset}&limit={limit}')
        retval = await self.__make_request('GET', url)
        return await FaceitAPI.__create_collection(retval, Match)

    async def championship_results(self, championship_id: str, offset: int = 0,
                                   limit: int = 20) -> Collection[Result]:
        url = FaceitAPI.__BASE_URL.format(
            f'championships/{championship_id}/results?offset={offset}&limit={limit}')
        retval = await self.__make_request('GET', url)
        return await FaceitAPI.__create_collection(retval, Result)

    async def championship_subscriptions(self, championship_id: str, offset: int = 0,
                                         limit: int = 10) -> Collection[Subscription]:
        url = FaceitAPI.__BASE_URL.format(
            f'championships/{championship_id}/subscriptions?offset={offset}&limit={limit}')
        retval = await self.__make_request('GET', url)
        return await FaceitAPI.__create_collection(retval, Subscription)
    # endregion

    # region Games
    async def games(self, offset: int = 0, limit: int = 20) -> Collection[GameData]:
        url = FaceitAPI.__BASE_URL.format(f'games?offset={offset}&limit={limit}')
        retval = await self.__make_request('GET', url)
        return await FaceitAPI.__create_collection(retval, GameData)

    async def game_details(self, game: Game) -> GameData:
        url = FaceitAPI.__BASE_URL.format(f'games/{game.value}')
        retval = await self.__make_request('GET', url)
        return await FaceitAPI.__create_object(retval, GameData)

    async def game_parent_details(self, game: Game) -> GameData:
        url = FaceitAPI.__BASE_URL.format(f'games/{game.value}/parent')
        retval = await self.__make_request('GET', url)
        return await FaceitAPI.__create_object(retval, GameData)
    # endregion

    # region Hubs
    async def hub(self, hub_id: str, expanded: Expansion = Expansion.NONE) -> Hub:
        url = FaceitAPI.__BASE_URL.format(f'hubs/{hub_id}')
        if expanded is not Expansion.NONE:
            url += f'?expanded={expanded.value}'
        retval = await self.__make_request('GET', url)
        return await FaceitAPI.__create_object(retval, Hub)

    async def hub_matches(self, hub_id: str, type: MatchType = MatchType.ALL, offset: int = 0,
                          limit: int = 20) -> Collection[Match]:
        url = FaceitAPI.__BASE_URL.format(f'hubs/{hub_id}/matches?type={type.value}&offset={offset}&limit={limit}')
        retval = await self.__make_request('GET', url)
        return await FaceitAPI.__create_collection(retval, Match)

    async def hub_members(self, hub_id: str, offset: int = 0, limit: int = 20) -> Collection[Member]:
        url = FaceitAPI.__BASE_URL.format(f'hubs/{hub_id}/members?offset={offset}&limit={limit}')
        retval = await self.__make_request('GET', url)
        return await FaceitAPI.__create_collection(retval, Member)

    async def hub_roles(self, hub_id: str, offset: int = 0, limit: int = 20) -> Collection[Role]:
        url = FaceitAPI.__BASE_URL.format(f'hubs/{hub_id}/roles?offset={offset}&limit={limit}')
        retval = await self.__make_request('GET', url)
        return await FaceitAPI.__create_collection(retval, Role)

    async def hub_rules(self, hub_id: str) -> Rule:
        url = FaceitAPI.__BASE_URL.format(f'hubs/{hub_id}/rules')
        retval = await self.__make_request('GET', url)
        return await FaceitAPI.__create_object(retval, Rule)

    async def hub_stats(self, hub_id: str, offset: int = 0, limit: int = 20) -> GameStats:
        url = FaceitAPI.__BASE_URL.format(f'hubs/{hub_id}/stats?offset={offset}&limit={limit}')
        retval = await self.__make_request('GET', url)
        return await FaceitAPI.__create_object(retval, GameStats)
    # endregion

    # region Leaderboards
    async def leaderboards_championship(self, championship_id: str, offset: int = 0,
                                        limit: int = 20) -> Collection[Leaderboard]:
        url = FaceitAPI.__BASE_URL.format(f'leaderboards/championships/{championship_id}?offset={offset}&limit={limit}')
        retval = await self.__make_request('GET', url)
        return await FaceitAPI.__create_collection(retval, Leaderboard)

    async def leaderboards_championship_groups(self, championship_id: str, group: int, offset: int = 0,
                                               limit: int = 20) -> ChampionshipRankingCollection[Ranking]:
        url = FaceitAPI.__BASE_URL.format(
            f'leaderboards/championships/{championship_id}/groups/{group}?offset={offset}&limit={limit}')
        retval = await self.__make_request('GET', url)
        return await FaceitAPI.__create_collection(retval, Ranking, ChampionshipRankingCollection)

    async def leaderboards_hub(self, hub_id: str, offset: int = 0,
                               limit: int = 20) -> Collection[Leaderboard]:
        url = FaceitAPI.__BASE_URL.format(f'leaderboards/hubs/{hub_id}?offset={offset}&limit={limit}')
        retval = await self.__make_request('GET', url)
        return await FaceitAPI.__create_collection(retval, Leaderboard)

    async def leaderboards_hub_general(self, hub_id: str, offset: int = 0,
                                       limit: int = 20) -> ChampionshipRankingCollection[Ranking]:
        url = FaceitAPI.__BASE_URL.format(f'leaderboards/hubs/{hub_id}/general?offset={offset}&limit={limit}')
        retval = await self.__make_request('GET', url)
        return await FaceitAPI.__create_collection(retval, Ranking, ChampionshipRankingCollection)

    async def leaderboards_hub_season(self, hub_id: str, season: int, offset: int = 0,
                                      limit: int = 20) -> ChampionshipRankingCollection[Ranking]:
        url = FaceitAPI.__BASE_URL.format(f'leaderboards/hubs/{hub_id}/seasons/{season}?offset={offset}&limit={limit}')
        retval = await self.__make_request('GET', url)
        return await FaceitAPI.__create_collection(retval, Ranking, ChampionshipRankingCollection)

    async def leaderboard(self, leaderboard_id: str, offset: int = 0,
                          limit: int = 20) -> ChampionshipRankingCollection[Ranking]:
        url = FaceitAPI.__BASE_URL.format(f'leaderboards/{leaderboard_id}?offset={offset}&limit={limit}')
        retval = await self.__make_request('GET', url)
        return await FaceitAPI.__create_collection(retval, Ranking, ChampionshipRankingCollection)
    # endregion

    # region Matches
    async def match(self, match_id: str) -> Match:
        url = FaceitAPI.__BASE_URL.format(f'matches/{match_id}')
        retval = await self.__make_request('GET', url)
        return await FaceitAPI.__create_object(retval, Match)

    async def match_stats(self, match_id: str) -> MatchStats:
        url = FaceitAPI.__BASE_URL.format(f'matches/{match_id}/stats')
        retval = await self.__make_request('GET', url)
        return await FaceitAPI.__create_object(retval, MatchStats)
    # endregion

    # region Organizers
    async def organizer_by_name(self, name: str) -> OrganizerData:
        url = FaceitAPI.__BASE_URL.format(f'organizers?name={name}')
        retval = await self.__make_request('GET', url)
        return await FaceitAPI.__create_object(retval, OrganizerData)

    async def organizer_by_id(self, organizer_id: str) -> OrganizerData:
        url = FaceitAPI.__BASE_URL.format(f'organizers/{organizer_id}')
        retval = await self.__make_request('GET', url)
        return await FaceitAPI.__create_object(retval, OrganizerData)

    async def organizer_championships(self, organizer_id: str, offset: int = 0,
                                      limit: int = 20) -> Collection[Championship]:
        url = FaceitAPI.__BASE_URL.format(f'organizers/{organizer_id}/championships?offset={offset}&limit={limit}')
        retval = await self.__make_request('GET', url)
        return await FaceitAPI.__create_collection(retval, Championship)

    async def organizer_games(self, organizer_id: str) -> Collection[Hub]:
        url = FaceitAPI.__BASE_URL.format(f'organizers/{organizer_id}/games')
        retval = await self.__make_request('GET', url)
        return await FaceitAPI.__create_collection(retval, Hub)

    async def organizer_hubs(self, organizer_id: str, offset: int = 0, limit: int = 20) -> Collection[Hub]:
        url = FaceitAPI.__BASE_URL.format(f'organizers/{organizer_id}/hubs?offset={offset}&limit={limit}')
        retval = await self.__make_request('GET', url)
        return await FaceitAPI.__create_collection(retval, Hub)

    async def organizer_tournaments(self, organizer_id: str, type: MatchType = MatchType.UPCOMING,
                                    offset: int = 0, limit: int = 20) -> Collection[Tournament]:
        url = FaceitAPI.__BASE_URL.format(
            f'organizers/{organizer_id}/tournaments?type={type.value}&offset={offset}&limit={limit}')
        retval = await self.__make_request('GET', url)
        return await FaceitAPI.__create_collection(retval, Tournament)
    # endregion

    # region Players
    async def player_by_nickname(self, nickname: str) -> Player:
        url = FaceitAPI.__BASE_URL.format(f'players?nickname={nickname}')
        retval = await self.__make_request('GET', url)
        return await FaceitAPI.__create_object(retval, Player)

    async def player_by_game_player_id(self, game: str, game_player_id: str) -> Player:
        url = FaceitAPI.__BASE_URL.format(f'players?game={game}&game_player_id={game_player_id}')
        retval = await self.__make_request('GET', url)
        return await FaceitAPI.__create_object(retval, Player)

    async def player_by_player_id(self, player_id: str) -> Player:
        url = FaceitAPI.__BASE_URL.format(f'players/{player_id}')
        retval = await self.__make_request('GET', url)
        return await FaceitAPI.__create_object(retval, Player)

    async def player_history(self, player_id: str, game: str, from_: int = None, to: int = None, offset: int = 0,
                             limit: int = 20) -> FromToCollection[PlayerMatch]:
        url = FaceitAPI.__BASE_URL.format(
            f'players/{player_id}/history?game={game}&offset={offset}&limit={limit}')
        if from_ is not None:
            url += f'&from={from_}'
        if to is not None:
            url += f'&to={to}'
        retval = await self.__make_request('GET', url)
        retval[1]["from_"] = retval[1]["from"]
        del retval[1]["from"]
        return await FaceitAPI.__create_collection(retval, PlayerMatch, FromToCollection)

    async def player_hubs(self, player_id: str, offset: int = 0, limit: int = 20) -> Collection[Hub]:
        url = FaceitAPI.__BASE_URL.format(f'players/{player_id}/hubs?offset={offset}&limit={limit}')
        retval = await self.__make_request('GET', url)
        return await FaceitAPI.__create_collection(retval, Hub)

    async def player_game_stats(self, player_id: str, game: Game) -> PlayerGameStats:
        url = FaceitAPI.__BASE_URL.format(f'players/{player_id}/stats/{game.value}')
        retval = await self.__make_request('GET', url)
        return await FaceitAPI.__create_object(retval, PlayerGameStats)

    async def player_tournaments(self, player_id: str, offset: int = 0,
                                 limit: int = 20) -> Collection[Tournament]:
        url = FaceitAPI.__BASE_URL.format(f'players/{player_id}/tournaments?offset={offset}&limit={limit}')
        retval = await self.__make_request('GET', url)
        return await FaceitAPI.__create_collection(retval, Tournament)
    # endregion

    # region Rankings
    async def ranking(self, game: Game, region: str, country: str = "", offset: int = 0,
                      limit: int = 20) -> Collection[Rank]:
        url = FaceitAPI.__BASE_URL.format(
            f'rankings/games/{game.value}/regions/{region}?country={country}&offset={offset}&limit={limit}')
        retval = await self.__make_request('GET', url)
        return await FaceitAPI.__create_collection(retval, Rank)

    async def ranking_of_player(self, game: Game, region: str, player_id: str, country: str = "",
                                limit: int = 20) -> RankCollection[Rank]:
        url = FaceitAPI.__BASE_URL.format(
            f'rankings/games/{game.value}/regions/{region}/players/{player_id}?country={country}&limit={limit}')
        retval = await self.__make_request('GET', url)
        return await FaceitAPI.__create_collection(retval, Rank, RankCollection)
    # endregion

    # region Search
    async def search_championships(self, name: str, game: Game = None, region: str = None,
                                   type: MatchType = MatchType.ALL, offset: int = 0,
                                   limit: int = 20) -> Collection[ChampionshipSearchResult]:
        url = FaceitAPI.__BASE_URL.format(
            f'search/championships?name={name}&type={type.value}&offset={offset}&limit={limit}')
        if game is not None:
            url += f'&game={game}'
        if region is not None:
            url += f'&region={region}'
        retval = await self.__make_request('GET', url)
        return await FaceitAPI.__create_collection(retval, ChampionshipSearchResult)

    async def search_hubs(self, name: str, game: str = None, region: str = None, offset: int = 0,
                          limit: int = 20) -> Collection[ChampionshipSearchResult]:
        url = FaceitAPI.__BASE_URL.format(f'search/hubs?name={name}&offset={offset}&limit={limit}')
        if game is not None:
            url += f'&game={game}'
        if region is not None:
            url += f'&region={region}'
        retval = await self.__make_request('GET', url)
        return await FaceitAPI.__create_collection(retval, ChampionshipSearchResult)

    async def search_organizers(self, name: str, offset: int = 0,
                                limit: int = 20) -> Collection[OrganizerSearchResult]:
        url = FaceitAPI.__BASE_URL.format(f'search/organizers?name={name}&offset={offset}&limit={limit}')
        retval = await self.__make_request('GET', url)
        return await FaceitAPI.__create_collection(retval, OrganizerSearchResult)

    async def search_players(self, nickname: str, game: str = None, country: str = None, offset: int = 0,
                             limit: int = 20) -> Collection[PlayerSearchResult]:
        url = FaceitAPI.__BASE_URL.format(f'search/players?nickname={nickname}&offset={offset}&limit={limit}')
        if game is not None:
            url += f'&game={game}'
        if country is not None:
            url += f'&country={country}'
        retval = await self.__make_request('GET', url)
        return await FaceitAPI.__create_collection(retval, PlayerSearchResult)

    async def search_teams(self, nickname: str, game: str = None, offset: int = 0,
                           limit: int = 20) -> Collection[TeamSearchResult]:
        url = FaceitAPI.__BASE_URL.format(f'search/teams?nickname={nickname}&offset={offset}&limit={limit}')
        if game is not None:
            url += f'&game={game}'
        retval = await self.__make_request('GET', url)
        return await FaceitAPI.__create_collection(retval, TeamSearchResult)

    async def search_tournaments(self, name: str, game: str = None, region: str = None,
                                 type: MatchType = MatchType.ALL, offset: int = 0,
                                 limit: int = 20) -> Collection[TournamentSearchResult]:
        url = FaceitAPI.__BASE_URL.format(
            f'search/tournaments?name={name}&type={type.value}&offset={offset}&limit={limit}')
        if game is not None:
            url += f'&game={game}'
        if region is not None:
            url += f'&region={region}'
        retval = await self.__make_request('GET', url)
        return await FaceitAPI.__create_collection(retval, TournamentSearchResult)
    # endregion

    # region Teams
    async def team(self, team_id: str) -> Team:
        url = FaceitAPI.__BASE_URL.format(f'teams/{team_id}')
        retval = await self.__make_request('GET', url)
        return await FaceitAPI.__create_object(retval, Team)

    async def team_game_stats(self, team_id: str, game: Game) -> TeamGameStats:
        url = FaceitAPI.__BASE_URL.format(f'teams/{team_id}/stats/{game.value}')
        retval = await self.__make_request('GET', url)
        return await FaceitAPI.__create_object(retval, Tournament)

    async def team_tournaments(self, team_id: str, offset: int = 0,
                               limit: int = 20) -> Collection[Tournament]:
        url = FaceitAPI.__BASE_URL.format(f'teams/{team_id}/tournaments?offset={offset}&limit={limit}')
        retval = await self.__make_request('GET', url)
        return await FaceitAPI.__create_collection(retval, Tournament)
    # endregion

    # region Tournaments
    async def tournaments(self, game: str = None, region: str = None, offset: int = 0, limit: int = 20):
        url = FaceitAPI.__BASE_URL.format(f'tournaments?offset={offset}&limit={limit}')
        if game is not None:
            url += f'&game={game}'
        if region is not None:
            url += f'&region={region}'
        retval = await self.__make_request('GET', url)
        return await FaceitAPI.__create_collection(retval, Tournament)

    async def tournament(self, tournament_id: str,
                         expanded: Expansion = Expansion.NONE) -> TournamentData:
        url = FaceitAPI.__BASE_URL.format(f'tournaments/{tournament_id}')
        if expanded is not Expansion.NONE:
            url += f'?expanded={expanded.value}'
        retval = await self.__make_request('GET', url)
        return await FaceitAPI.__create_object(retval, TournamentData)

    async def tournament_brackets(self, tournament_id: str) -> Brackets:
        url = FaceitAPI.__BASE_URL.format(f'tournaments/{tournament_id}/brackets')
        retval = await self.__make_request('GET', url)
        return await FaceitAPI.__create_object(retval, Brackets)

    async def tournament_matches(self, tournament_id: str, offset: int = 0,
                                 limit: int = 20) -> Collection[Match]:
        url = FaceitAPI.__BASE_URL.format(f'tournaments/{tournament_id}/matches?offset={offset}&limit={limit}')
        retval = await self.__make_request('GET', url)
        return await FaceitAPI.__create_collection(retval, Match)

    async def tournament_teams(self, tournament_id: str, offset: int = 0, limit: int = 20) -> TournamentTeams:
        url = FaceitAPI.__BASE_URL.format(f'tournaments/{tournament_id}/teams?offset={offset}&limit={limit}')
        retval = await self.__make_request('GET', url)
        return await FaceitAPI.__create_object(retval, TournamentTeams)
    # endregion

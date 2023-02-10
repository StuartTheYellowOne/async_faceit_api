import datetime
from typing import Tuple, Any
from aiohttp import request
from .enums import *
from .dataclasses import *


class FaceitAPI:
    """
    See the faceit data-api docs for more information:
    https://developers.faceit.com/docs/tools/data-api
    """

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
        """Retrieve all championships of a game

        :param game: The id of the game
        :type game: :class:`.Game`
        :param type: Kind of matches to return. Can be all(default), upcoming, ongoing or past
        :type type: :class:`.MatchType`, optional
        :param offset: The starting item position
        :type offset: int, optional
        :param limit: The number of items to return
        :type limit: int, optional
        :return: Championships collection
        :rtype: :class:`.Collection[.Championship]`
        """
        url = FaceitAPI.__BASE_URL.format(
            f'championships?game={game.value}&type={type.value}&offset={offset}&limit={limit}')
        retval = await self.__make_request('GET', url)
        return await FaceitAPI.__create_collection(retval, Championship)

    async def championship(self, championship_id: str,
                           expanded: Expansion = Expansion.NONE) -> Championship:
        """Retrieve championship details

        :param championship_id: The id of the championship
        :type championship_id: str
        :param expanded: List of entity names to expand in request
        :type expanded: :class:`.Expansion`, optional
        :return: Championship details
        :rtype: :class:.Championship`
        """
        url = FaceitAPI.__BASE_URL.format(f'championships/{championship_id}')
        if expanded is not Expansion.NONE:
            url += f'?expanded={expanded.value}'
        retval = await self.__make_request('GET', url)
        return await FaceitAPI.__create_object(retval, Championship)

    async def championship_matches(self, championship_id: str, type: MatchType = MatchType.ALL,
                                   offset: int = 0, limit: int = 20) -> Collection[Match]:
        """Retrieve all matches of a championship

        :param championship_id: The id of the championship
        :type championship_id: str
        :param type: Kind of matches to return. Can be all(default), upcoming, ongoing or past
        :type type: :class:`.MatchType`, optional
        :param offset: The starting item position
        :type offset: int, optional
        :param limit: The number of items to return
        :type limit: int, optional
        :return: Matches list
        :rtype: :class:`.Collection[.Match]`
        """
        url = FaceitAPI.__BASE_URL.format(
            f'championships/{championship_id}/matches?type={type.value}&offset={offset}&limit={limit}')
        retval = await self.__make_request('GET', url)
        return await FaceitAPI.__create_collection(retval, Match)

    async def championship_results(self, championship_id: str, offset: int = 0,
                                   limit: int = 20) -> Collection[Result]:
        """Retrieve all results of a championship

        :param championship_id: The id of the championship
        :type championship_id: str
        :param offset: The starting item position
        :type offset: int, optional
        :param limit: The number of items to return
        :type limit: int, optional
        :return: Championship results
        :rtype: :class:`.Collection[.Result]`
        """
        url = FaceitAPI.__BASE_URL.format(
            f'championships/{championship_id}/results?offset={offset}&limit={limit}')
        retval = await self.__make_request('GET', url)
        return await FaceitAPI.__create_collection(retval, Result)

    async def championship_subscriptions(self, championship_id: str, offset: int = 0,
                                         limit: int = 10) -> Collection[Subscription]:
        """Retrieve all subscriptions of a championship

        :param championship_id: The id of the championship
        :type championship_id: str
        :param offset: The starting item position
        :type offset: int, optional
        :param limit: The number of items to return
        :type limit: int, optional
        :return: Subscriptions list
        :rtype: :class:`.Collection[.Subscription]`
        """
        url = FaceitAPI.__BASE_URL.format(
            f'championships/{championship_id}/subscriptions?offset={offset}&limit={limit}')
        retval = await self.__make_request('GET', url)
        return await FaceitAPI.__create_collection(retval, Subscription)
    # endregion

    # region Games
    async def games(self, offset: int = 0, limit: int = 20) -> Collection[GameData]:
        """Retrieve details of all games on FACEIT

        :param offset: The starting item position
        :type offset: int, optional
        :param limit: The number of items to return
        :type limit: int, optional
        :return: Games list
        :rtype: :class:`.Collection[.GameData]`
        """
        url = FaceitAPI.__BASE_URL.format(f'games?offset={offset}&limit={limit}')
        retval = await self.__make_request('GET', url)
        return await FaceitAPI.__create_collection(retval, GameData)

    async def game_details(self, game: Game) -> GameData:
        """Retrieve game details

        :param game: The id of the game
        :type game: :class:`.Game`
        :return: Game detail
        :rtype: :class:`.GameData`
        """
        url = FaceitAPI.__BASE_URL.format(f'games/{game.value}')
        retval = await self.__make_request('GET', url)
        return await FaceitAPI.__create_object(retval, GameData)

    async def game_parent_details(self, game: Game) -> GameData:
        """Retrieve the details of the parent game, if the game is region-specific

        :param game: The id of the game
        :type game: :class:`.Game`
        :return: Game detail
        :rtype: :class:`.GameData`
        """
        url = FaceitAPI.__BASE_URL.format(f'games/{game.value}/parent')
        retval = await self.__make_request('GET', url)
        return await FaceitAPI.__create_object(retval, GameData)
    # endregion

    # region Hubs
    async def hub(self, hub_id: str, expanded: Expansion = Expansion.NONE) -> Hub:
        """Retrieve hub details

        :param hub_id: The id of the hub
        :type hub_id: str
        :param expanded: List of entity names to expand in request
        :type expanded: :class:`.Expansion`
        :return: Hub details
        :rtype: :class:`.Hub`
        """
        url = FaceitAPI.__BASE_URL.format(f'hubs/{hub_id}')
        if expanded is not Expansion.NONE:
            url += f'?expanded={expanded.value}'
        retval = await self.__make_request('GET', url)
        return await FaceitAPI.__create_object(retval, Hub)

    async def hub_matches(self, hub_id: str, type: MatchType = MatchType.ALL, offset: int = 0,
                          limit: int = 20) -> Collection[Match]:
        """Retrieve all matches of a hub

        :param hub_id: The id of the hub
        :type hub_id: str
        :param type: Kind of matches to return. Can be all(default), upcoming, ongoing or past
        :type type: :class:`.MatchType`, optional
        :param offset: The starting item position
        :type offset: int, optional
        :param limit: The number of items to return
        :type limit: int, optional
        :return: Matches list
        :rtype: :class:`.Collection[.Match]`
        """
        url = FaceitAPI.__BASE_URL.format(f'hubs/{hub_id}/matches?type={type.value}&offset={offset}&limit={limit}')
        retval = await self.__make_request('GET', url)
        return await FaceitAPI.__create_collection(retval, Match)

    async def hub_members(self, hub_id: str, offset: int = 0, limit: int = 20) -> Collection[Member]:
        """Retrieve all members of a hub

        :param hub_id: The id of the hub
        :type hub_id: str
        :param offset: The starting item position
        :type offset: int, optional
        :param limit: The number of items to return
        :type limit: int, optional
        :return: Members list
        :rtype: :class:`.Collection[.Member]`
        """
        url = FaceitAPI.__BASE_URL.format(f'hubs/{hub_id}/members?offset={offset}&limit={limit}')
        retval = await self.__make_request('GET', url)
        return await FaceitAPI.__create_collection(retval, Member)

    async def hub_roles(self, hub_id: str, offset: int = 0, limit: int = 20) -> Collection[Role]:
        """Retrieve all roles members can have in a hub

        :param hub_id: The id of the hub
        :type hub_id: str
        :param offset: The starting item position
        :type offset: int, optional
        :param limit: The number of items to return
        :type limit: int, optional
        :return: Roles list
        :rtype: :class:`.Collection[.Role]`
        """
        url = FaceitAPI.__BASE_URL.format(f'hubs/{hub_id}/roles?offset={offset}&limit={limit}')
        retval = await self.__make_request('GET', url)
        return await FaceitAPI.__create_collection(retval, Role)

    async def hub_rules(self, hub_id: str) -> Rule:
        """Retrieve rules of a hub

        :param hub_id: The id of the hub
        :type hub_id: str
        :return: Rules details
        :rtype: :class:`.Rule`
        """
        url = FaceitAPI.__BASE_URL.format(f'hubs/{hub_id}/rules')
        retval = await self.__make_request('GET', url)
        return await FaceitAPI.__create_object(retval, Rule)

    async def hub_stats(self, hub_id: str, offset: int = 0, limit: int = 20) -> GameStats:
        """Retrieve statistics of a hub

        :param hub_id: The id of the hub
        :type hub_id: str
        :param offset: The starting item position
        :type offset: int, optional
        :param limit: The number of items to return
        :type limit: int, optional
        :return: Hub stats
        :rtype: :class:`.GameStats`
        """
        url = FaceitAPI.__BASE_URL.format(f'hubs/{hub_id}/stats?offset={offset}&limit={limit}')
        retval = await self.__make_request('GET', url)
        return await FaceitAPI.__create_object(retval, GameStats)
    # endregion

    # region Leaderboards
    async def leaderboards_championship(self, championship_id: str, offset: int = 0,
                                        limit: int = 20) -> Collection[Leaderboard]:
        """Retrieve all leaderboards of a championship

        :param championship_id: The id of the championship
        :type championship_id: str
        :param offset: The starting item position
        :type offset: int, optional
        :param limit: The number of items to return
        :type limit: int, optional
        :return: Leaderboards list
        :rtype: :class:`.Collection[.Leaderboard]`
        """
        url = FaceitAPI.__BASE_URL.format(f'leaderboards/championships/{championship_id}?offset={offset}&limit={limit}')
        retval = await self.__make_request('GET', url)
        return await FaceitAPI.__create_collection(retval, Leaderboard)

    async def leaderboards_championship_groups(self, championship_id: str, group: int, offset: int = 0,
                                               limit: int = 20) -> ChampionshipRankingCollection[Ranking]:
        """Retrieve group ranking of a championship

        :param championship_id: The id of the championship
        :type championship_id: str
        :param group: A group of the championship
        :type group: int
        :param offset: The starting item position
        :type offset: int, optional
        :param limit: The number of items to return
        :type limit: int, optional
        :return: Leaderboards list
        :rtype: :class:`.ChampionshipRankingCollection[.Ranking]`
        """
        url = FaceitAPI.__BASE_URL.format(
            f'leaderboards/championships/{championship_id}/groups/{group}?offset={offset}&limit={limit}')
        retval = await self.__make_request('GET', url)
        return await FaceitAPI.__create_collection(retval, Ranking, ChampionshipRankingCollection)

    async def leaderboards_hub(self, hub_id: str, offset: int = 0,
                               limit: int = 20) -> Collection[Leaderboard]:
        """Retrieve all leaderboards of a hub

        :param hub_id: The id of the hub
        :type hub_id: str
        :param offset: The starting item position
        :type offset: int, optional
        :param limit: The number of items to return
        :type limit: int, optional
        :return: Leaderboards list
        :rtype: :class:`.Collection[.Leaderboard]`
        """
        url = FaceitAPI.__BASE_URL.format(f'leaderboards/hubs/{hub_id}?offset={offset}&limit={limit}')
        retval = await self.__make_request('GET', url)
        return await FaceitAPI.__create_collection(retval, Leaderboard)

    async def leaderboards_hub_general(self, hub_id: str, offset: int = 0,
                                       limit: int = 20) -> ChampionshipRankingCollection[Ranking]:
        """Retrieve all time ranking of a hub

        :param hub_id: The id of the hub
        :type hub_id: str
        :param offset: The starting item position
        :type offset: int, optional
        :param limit: The number of items to return
        :type limit: int, optional
        :return: Leaderboards list
        :rtype: :class:`.ChampionshipRankingCollection[.Ranking]`
        """
        url = FaceitAPI.__BASE_URL.format(f'leaderboards/hubs/{hub_id}/general?offset={offset}&limit={limit}')
        retval = await self.__make_request('GET', url)
        return await FaceitAPI.__create_collection(retval, Ranking, ChampionshipRankingCollection)

    async def leaderboards_hub_season(self, hub_id: str, season: int, offset: int = 0,
                                      limit: int = 20) -> ChampionshipRankingCollection[Ranking]:
        """Retrieve seasonal ranking of a hub

        :param hub_id: The id of the hub
        :type hub_id: str
        :param season: A season of the hub
        :type season: int
        :param offset: The starting item position
        :type offset: int, optional
        :param limit: The number of items to return
        :type limit: int, optional
        :return: Leaderboards list
        :rtype: :class:`.ChampionshipRankingCollection[.Ranking]`
        """
        url = FaceitAPI.__BASE_URL.format(f'leaderboards/hubs/{hub_id}/seasons/{season}?offset={offset}&limit={limit}')
        retval = await self.__make_request('GET', url)
        return await FaceitAPI.__create_collection(retval, Ranking, ChampionshipRankingCollection)

    async def leaderboard(self, leaderboard_id: str, offset: int = 0,
                          limit: int = 20) -> ChampionshipRankingCollection[Ranking]:
        """Retrieve ranking from a leaderboard id

        :param leaderboard_id: The id of the leaderboard
        :type leaderboard_id: str
        :param season: A season of the hub
        :type season: int
        :param offset: The starting item position
        :type offset: int, optional
        :param limit: The number of items to return
        :type limit: int, optional
        :return: Leaderboards list
        :rtype: :class:`.ChampionshipRankingCollection[.Ranking]`
        """
        url = FaceitAPI.__BASE_URL.format(f'leaderboards/{leaderboard_id}?offset={offset}&limit={limit}')
        retval = await self.__make_request('GET', url)
        return await FaceitAPI.__create_collection(retval, Ranking, ChampionshipRankingCollection)
    # endregion

    # region Matches
    async def match(self, match_id: str) -> Match:
        """Retrieve match details

        :param match_id: The id of the match
        :type match_id: str
        :return: Match details
        :rtype: :class:`.Match`
        """
        url = FaceitAPI.__BASE_URL.format(f'matches/{match_id}')
        retval = await self.__make_request('GET', url)
        return await FaceitAPI.__create_object(retval, Match)

    async def match_stats(self, match_id: str) -> MatchStats:
        """Retrieve statistics of a match

        :param match_id: The id of the match
        :type match_id: str
        :return: Match details
        :rtype: :class:`.MatchStats`
        """
        url = FaceitAPI.__BASE_URL.format(f'matches/{match_id}/stats')
        retval = await self.__make_request('GET', url)
        return await FaceitAPI.__create_object(retval, MatchStats)
    # endregion

    # region Organizers
    async def organizer_by_name(self, name: str) -> OrganizerData:
        """Retrieve organizer details from name

        :param name: The name of the organizer
        :type name: str
        :return: Organizer details
        :rtype: :class:`.OrganizerData`
        """
        url = FaceitAPI.__BASE_URL.format(f'organizers?name={name}')
        retval = await self.__make_request('GET', url)
        return await FaceitAPI.__create_object(retval, OrganizerData)

    async def organizer_by_id(self, organizer_id: str) -> OrganizerData:
        """Retrieve organizer details

        :param organizer_id: The id of the organizer
        :type organizer_id: str
        :return: Organizer details
        :rtype: :class:`.OrganizerData`
        """
        url = FaceitAPI.__BASE_URL.format(f'organizers/{organizer_id}')
        retval = await self.__make_request('GET', url)
        return await FaceitAPI.__create_object(retval, OrganizerData)

    async def organizer_championships(self, organizer_id: str, offset: int = 0,
                                      limit: int = 20) -> Collection[Championship]:
        """Retrieve all championships of an organizer

        :param organizer_id: The id of the organizer
        :type organizer_id: str
        :param offset: The starting item position
        :type offset: int, optional
        :param limit: The number of items to return
        :type limit: int, optional
        :return: Leaderboards list
        :rtype: :class:`.Collection[.Championship]`
        """
        url = FaceitAPI.__BASE_URL.format(f'organizers/{organizer_id}/championships?offset={offset}&limit={limit}')
        retval = await self.__make_request('GET', url)
        return await FaceitAPI.__create_collection(retval, Championship)

    async def organizer_games(self, organizer_id: str) -> Collection[Hub]:
        """Retrieve all games an organizer is involved with

        :param organizer_id: The id of the organizer
        :type organizer_id: str
        :return: Leaderboards list
        :rtype: :class:`.Collection[.Hub]`
        """
        url = FaceitAPI.__BASE_URL.format(f'organizers/{organizer_id}/games')
        retval = await self.__make_request('GET', url)
        return await FaceitAPI.__create_collection(retval, Hub)

    async def organizer_hubs(self, organizer_id: str, offset: int = 0, limit: int = 20) -> Collection[Hub]:
        """Retrieve all hubs of an organizer

        :param organizer_id: The id of the organizer
        :type organizer_id: str
        :param offset: The starting item position
        :type offset: int, optional
        :param limit: The number of items to return
        :type limit: int, optional
        :return: Leaderboards list
        :rtype: :class:`.Collection[.Hub]`
        """
        url = FaceitAPI.__BASE_URL.format(f'organizers/{organizer_id}/hubs?offset={offset}&limit={limit}')
        retval = await self.__make_request('GET', url)
        return await FaceitAPI.__create_collection(retval, Hub)

    async def organizer_tournaments(self, organizer_id: str, type: MatchType = MatchType.UPCOMING,
                                    offset: int = 0, limit: int = 20) -> Collection[Tournament]:
        """Retrieve all tournaments of an organizer

        :param organizer_id: The id of the organizer
        :type organizer_id: str
        :param type: Kind of tournament. Can be upcoming(default) or past
        :type type: :class:`.MatchType`, optional
        :param offset: The starting item position
        :type offset: int, optional
        :param limit: The number of items to return
        :type limit: int, optional
        :return: Leaderboards list
        :rtype: :class:`.Collection[.Tournament]`
        """
        url = FaceitAPI.__BASE_URL.format(
            f'organizers/{organizer_id}/tournaments?type={type.value}&offset={offset}&limit={limit}')
        retval = await self.__make_request('GET', url)
        return await FaceitAPI.__create_collection(retval, Tournament)
    # endregion

    # region Players
    async def player_by_nickname(self, nickname: str) -> Player:
        """Retrieve player details

        :param nickname: The nickname of the player on FACEIT
        :type nickname: str
        :return: Player details
        :rtype: :class:`.Player`
        """
        url = FaceitAPI.__BASE_URL.format(f'players?nickname={nickname}')
        retval = await self.__make_request('GET', url)
        return await FaceitAPI.__create_object(retval, Player)

    async def player_by_game_player_id(self, game: Game, game_player_id: str) -> Player:
        """Retrieve player details

        :param game: A game on FACEIT
        :type game: :class:`.Game`
        :param game_player_id: The ID of a player on game's platform
        :type game_player_id: str
        :return: Player details
        :rtype: :class:`.Player`
        """
        url = FaceitAPI.__BASE_URL.format(f'players?game={game.value}&game_player_id={game_player_id}')
        retval = await self.__make_request('GET', url)
        return await FaceitAPI.__create_object(retval, Player)

    async def player_by_player_id(self, player_id: str) -> Player:
        """Retrieve player details

        :param player_id: The id of the player
        :type player_id: str
        :return: Player details
        :rtype: :class:`.Player`
        """
        url = FaceitAPI.__BASE_URL.format(f'players/{player_id}')
        retval = await self.__make_request('GET', url)
        return await FaceitAPI.__create_object(retval, Player)

    async def player_history(self, player_id: str, game: Game, from_: Union[int, datetime.datetime] = None,
                             to: Union[int, datetime.datetime] = None, offset: int = 0,
                             limit: int = 20) -> FromToCollection[PlayerMatch]:
        """Retrieve all matches of a player

        :param player_id: The id of the player
        :type player_id: str
        :param game: A game on FACEIT
        :type game: :class:`.Game`
        :param from_: The timestamp in sec or datetime as lower bound of the query. 1 month ago if not specified
        :type from_: Union[int, datetime.datetime], optional
        :param to: The timestamp in sec or datetime as higher bound of the query. Current timestamp if not specified
        :type to: Union[int, datetime.datetime], optional
        :param offset: The starting item position
        :type offset: int, optional
        :param limit: The number of items to return
        :type limit: int, optional
        :return: Player matches list
        :rtype: :class:`.FromToCollection[.PlayerMatch]`
        """
        url = FaceitAPI.__BASE_URL.format(
            f'players/{player_id}/history?game={game.value}&offset={offset}&limit={limit}')
        if from_ is not None:
            if type(from_) is datetime.datetime:
                from_ = int(from_.timestamp())
            url += f'&from={from_}'
        if to is not None:
            if type(to) is datetime.datetime:
                to = int(to.timestamp())
            url += f'&to={to}'
        retval = await self.__make_request('GET', url)
        retval[1]["from_"] = retval[1]["from"]
        del retval[1]["from"]
        return await FaceitAPI.__create_collection(retval, PlayerMatch, FromToCollection)

    async def player_hubs(self, player_id: str, offset: int = 0, limit: int = 20) -> Collection[Hub]:
        """Retrieve all hubs of a player

        :param player_id: The id of the player
        :type player_id: str
        :param offset: The starting item position
        :type offset: int, optional
        :param limit: The number of items to return
        :type limit: int, optional
        :return: Hubs list
        :rtype: :class:`.Collection[.Hub]`
        """
        url = FaceitAPI.__BASE_URL.format(f'players/{player_id}/hubs?offset={offset}&limit={limit}')
        retval = await self.__make_request('GET', url)
        return await FaceitAPI.__create_collection(retval, Hub)

    async def player_game_stats(self, player_id: str, game: Game) -> PlayerGameStats:
        """Retrieve statistics of a player

        :param player_id: The id of the player
        :type player_id: str
        :param game: A game on FACEIT
        :type game: :class:`.Game`
        :return: Player stats
        :rtype: :class:`.Collection[.Hub]`
        """
        url = FaceitAPI.__BASE_URL.format(f'players/{player_id}/stats/{game.value}')
        retval = await self.__make_request('GET', url)
        return await FaceitAPI.__create_object(retval, PlayerGameStats)

    async def player_tournaments(self, player_id: str, offset: int = 0, limit: int = 20) -> Collection[Tournament]:
        """Retrieve all tournaments of a player

        :param player_id: The id of the player
        :type player_id: str
        :param offset: The starting item position
        :type offset: int, optional
        :param limit: The number of items to return
        :type limit: int, optional
        :return: Tournaments list
        :rtype: :class:`.Collection[.Tournament]`
        """
        url = FaceitAPI.__BASE_URL.format(f'players/{player_id}/tournaments?offset={offset}&limit={limit}')
        retval = await self.__make_request('GET', url)
        return await FaceitAPI.__create_collection(retval, Tournament)
    # endregion

    # region Rankings
    async def ranking(self, game: Game, region: Region, country: Country = None, offset: int = 0,
                      limit: int = 20) -> Collection[Rank]:
        """Retrieve global ranking of a game

        :param player_id: The id of the player
        :type player_id: str
        :param region: A region of a game
        :type region: :class:`.Region`
        :param country: A country code
        :type country: :class:`.Country`, optional
        :param offset: The starting item position
        :type offset: int, optional
        :param limit: The number of items to return
        :type limit: int, optional
        :return: Tournaments list
        :rtype: :class:`.Collection[.Rank]`
        """
        url = FaceitAPI.__BASE_URL.format(
            f'rankings/games/{game.value}/regions/{region.value}?offset={offset}&limit={limit}')
        if country is not None:
            url += f'&country={country.value}'
        retval = await self.__make_request('GET', url)
        return await FaceitAPI.__create_collection(retval, Rank)

    async def ranking_of_player(self, game: Game, region: Region, player_id: str, country: Country = None,
                                limit: int = 20) -> RankCollection[Rank]:
        """Retrieve global ranking of a game

        :param game: The id of the player
        :type game: str
        :param region: A region of a game
        :type region: :class:`.Region`
        :param player_id: The id of a player
        :type player_id: str
        :param country: A country code
        :type country: :class:`.Country`, optional
        :param limit: The number of items to return
        :type limit: int, optional
        :return: Tournaments list
        :rtype: :class:`.RankCollection[.Rank]`
        """
        url = FaceitAPI.__BASE_URL.format(
            f'rankings/games/{game.value}/regions/{region.value}/players/{player_id}?limit={limit}')
        if country is not None:
            url += f'&country={country.value}'
        retval = await self.__make_request('GET', url)
        return await FaceitAPI.__create_collection(retval, Rank, RankCollection)
    # endregion

    # region Search
    async def search_championships(self, name: str, game: Game = None, region: Region = None,
                                   type: MatchType = MatchType.ALL, offset: int = 0,
                                   limit: int = 20) -> Collection[ChampionshipSearchResult]:
        """Search for championships

        :param name: The name of a championship on FACEIT
        :type name: str
        :param game: A game on FACEIT
        :type game: :class:`.Game`, optional
        :param region: A region of a game
        :type region: :class:`.Region`, optional
        :param type: Kind of competitions to return
        :type type: :class:`.MatchType`, optional
        :param offset: The starting item position
        :type offset: int, optional
        :param limit: The number of items to return
        :type limit: int, optional
        :return: List of championship
        :rtype: :class:`.Collection[.ChampionshipSearchResult]`
        """
        url = FaceitAPI.__BASE_URL.format(
            f'search/championships?name={name}&type={type.value}&offset={offset}&limit={limit}')
        if game is not None:
            url += f'&game={game}'
        if region is not None:
            url += f'&region={region.value}'
        retval = await self.__make_request('GET', url)
        return await FaceitAPI.__create_collection(retval, ChampionshipSearchResult)

    async def search_hubs(self, name: str, game: Game = None, region: Region = None, offset: int = 0,
                          limit: int = 20) -> Collection[ChampionshipSearchResult]:
        """List of hub

        :param name: The name of a hub on FACEIT
        :type name: str
        :param game: A game on FACEIT
        :type game: :class:`.Game`, optional
        :param region: A region of a game
        :type region: :class:`.Region`, optional
        :param offset: The starting item position
        :type offset: int, optional
        :param limit: The number of items to return
        :type limit: int, optional
        :return: List of hub
        :rtype: :class:`.Collection[.ChampionshipSearchResult]`
        """
        url = FaceitAPI.__BASE_URL.format(f'search/hubs?name={name}&offset={offset}&limit={limit}')
        if game is not None:
            url += f'&game={game.value}'
        if region is not None:
            url += f'&region={region.value}'
        retval = await self.__make_request('GET', url)
        return await FaceitAPI.__create_collection(retval, ChampionshipSearchResult)

    async def search_organizers(self, name: str, offset: int = 0,
                                limit: int = 20) -> Collection[OrganizerSearchResult]:
        """Search for organizers

        :param name: The name of a organizer on FACEIT
        :type name: str
        :param offset: The starting item position
        :type offset: int, optional
        :param limit: The number of items to return
        :type limit: int, optional
        :return: List of organizers
        :rtype: :class:`.Collection[.OrganizerSearchResult]`
        """
        url = FaceitAPI.__BASE_URL.format(f'search/organizers?name={name}&offset={offset}&limit={limit}')
        retval = await self.__make_request('GET', url)
        return await FaceitAPI.__create_collection(retval, OrganizerSearchResult)

    async def search_players(self, nickname: str, game: Game = None, country: Country = None, offset: int = 0,
                             limit: int = 20) -> Collection[PlayerSearchResult]:
        """Search for players

        :param nickname: The nickname of a player on FACEIT
        :type nickname: str
        :param game: A game on FACEIT
        :type game: :class:`.Game`, optional
        :param country: A country code
        :type country: :class:`.Country`, optional
        :param offset: The starting item position
        :type offset: int, optional
        :param limit: The number of items to return
        :type limit: int, optional
        :return: List of players
        :rtype: :class:`.Collection[.PlayerSearchResult]`
        """
        url = FaceitAPI.__BASE_URL.format(f'search/players?nickname={nickname}&offset={offset}&limit={limit}')
        if game is not None:
            url += f'&game={game.value}'
        if country is not None:
            url += f'&country={country.value}'
        retval = await self.__make_request('GET', url)
        return await FaceitAPI.__create_collection(retval, PlayerSearchResult)

    async def search_teams(self, nickname: str, game: Game = None, offset: int = 0,
                           limit: int = 20) -> Collection[TeamSearchResult]:
        """Search for teams

        :param nickname: The nickname of a team on FACEIT
        :type nickname: str
        :param game: A game on FACEIT
        :type game: :class:`.Game`, optional
        :param offset: The starting item position
        :type offset: int, optional
        :param limit: The number of items to return
        :type limit: int, optional
        :return: List of teams
        :rtype: :class:`.Collection[.TeamSearchResult]`
        """
        url = FaceitAPI.__BASE_URL.format(f'search/teams?nickname={nickname}&offset={offset}&limit={limit}')
        if game is not None:
            url += f'&game={game.value}'
        retval = await self.__make_request('GET', url)
        return await FaceitAPI.__create_collection(retval, TeamSearchResult)

    async def search_tournaments(self, name: str, game: Game = None, region: Region = None,
                                 type: MatchType = MatchType.ALL, offset: int = 0,
                                 limit: int = 20) -> Collection[TournamentSearchResult]:
        """Search for teams

        :param name: The name of a tournament on FACEIT
        :type name: str
        :param game: A game on FACEIT
        :type game: :class:`.Game`, optional
        :param region: A region of a game
        :type region: :class:`.Region`, optional
        :param type: Kind of competitions to return
        :type type: :class:`.MatchType`, optional
        :param offset: The starting item position
        :type offset: int, optional
        :param limit: The number of items to return
        :type limit: int, optional
        :return: List of tournament
        :rtype: :class:`.Collection[.TournamentSearchResult]`
        """
        url = FaceitAPI.__BASE_URL.format(
            f'search/tournaments?name={name}&type={type.value}&offset={offset}&limit={limit}')
        if game is not None:
            url += f'&game={game.value}'
        if region is not None:
            url += f'&region={region.value}'
        retval = await self.__make_request('GET', url)
        return await FaceitAPI.__create_collection(retval, TournamentSearchResult)
    # endregion

    # region Teams
    async def team(self, team_id: str) -> Team:
        """Retrieve team details

        :param team_id: The id of the team
        :type team_id: str
        :return: Team details
        :rtype: :class:`.Team`
        """
        url = FaceitAPI.__BASE_URL.format(f'teams/{team_id}')
        retval = await self.__make_request('GET', url)
        return await FaceitAPI.__create_object(retval, Team)

    async def team_game_stats(self, team_id: str, game: Game) -> TeamGameStats:
        """Retrieve statistics of a team

        :param team_id: The id of the team
        :type team_id: str
        :param game: A game on FACEIT
        :type game: :class:`.Game`
        :return: Team stats
        :rtype: :class:`.TeamGameStats`
        """
        url = FaceitAPI.__BASE_URL.format(f'teams/{team_id}/stats/{game.value}')
        retval = await self.__make_request('GET', url)
        return await FaceitAPI.__create_object(retval, Tournament)

    async def team_tournaments(self, team_id: str, offset: int = 0, limit: int = 20) -> Collection[Tournament]:
        """Retrieve tournaments of a team

        :param team_id: The id of the team
        :type team_id: str
        :param offset: The starting item position
        :type offset: int, optional
        :param limit: The number of items to return
        :type limit: int, optional
        :return: Tournaments list
        :rtype: :class:`.Collection[.Tournament]`
        """
        url = FaceitAPI.__BASE_URL.format(f'teams/{team_id}/tournaments?offset={offset}&limit={limit}')
        retval = await self.__make_request('GET', url)
        return await FaceitAPI.__create_collection(retval, Tournament)
    # endregion

    # region Tournaments
    async def tournaments(self, game: Game = None, region: Region = None, offset: int = 0,
                          limit: int = 20) -> Collection[Tournament]:
        """Retrieve tournaments v1 (no longer used)

        :param game: A game on FACEIT
        :type game: :class:`.Game`, optional
        :param region: A region of a game
        :type region: :class:`.Region`, optional
        :param offset: The starting item position
        :type offset: int, optional
        :param limit: The number of items to return
        :type limit: int, optional
        :return: Tournaments list
        :rtype: :class:`.Collection[.Tournament]`
        """
        url = FaceitAPI.__BASE_URL.format(f'tournaments?offset={offset}&limit={limit}')
        if game is not None:
            url += f'&game={game.value}'
        if region is not None:
            url += f'&region={region.value}'
        retval = await self.__make_request('GET', url)
        return await FaceitAPI.__create_collection(retval, Tournament)

    async def tournament(self, tournament_id: str, expanded: Expansion = Expansion.NONE) -> TournamentData:
        """Retrieve tournament details

        :param tournament_id: The id of the tournament
        :type tournament_id: str
        :param expanded: List of entity names to expand in request
        :type expanded: :class:`.Expansion`
        :return: Tournament details
        :rtype: :class:`.TournamentData`
        """
        url = FaceitAPI.__BASE_URL.format(f'tournaments/{tournament_id}')
        if expanded is not Expansion.NONE:
            url += f'?expanded={expanded.value}'
        retval = await self.__make_request('GET', url)
        return await FaceitAPI.__create_object(retval, TournamentData)

    async def tournament_brackets(self, tournament_id: str) -> Brackets:
        """Retrieve brackets of a tournament

        :param tournament_id: The id of the tournament
        :type tournament_id: str
        :return: Tournament details
        :rtype: :class:`.Brackets`
        """
        url = FaceitAPI.__BASE_URL.format(f'tournaments/{tournament_id}/brackets')
        retval = await self.__make_request('GET', url)
        return await FaceitAPI.__create_object(retval, Brackets)

    async def tournament_matches(self, tournament_id: str, offset: int = 0, limit: int = 20) -> Collection[Match]:
        """Retrieve all matches of a tournament

        :param tournament_id: The id of the tournament
        :type tournament_id: str
        :param offset: The starting item position
        :type offset: int, optional
        :param limit: The number of items to return
        :type limit: int, optional
        :return: Matches list
        :rtype: :class:`.Collection[.Match]`
        """
        url = FaceitAPI.__BASE_URL.format(f'tournaments/{tournament_id}/matches?offset={offset}&limit={limit}')
        retval = await self.__make_request('GET', url)
        return await FaceitAPI.__create_collection(retval, Match)

    async def tournament_teams(self, tournament_id: str, offset: int = 0, limit: int = 20) -> TournamentTeams:
        """Retrieve all teams of a tournament

        :param tournament_id: The id of the tournament
        :type tournament_id: str
        :param offset: The starting item position
        :type offset: int, optional
        :param limit: The number of items to return
        :type limit: int, optional
        :return: Matches list
        :rtype: :class:`.TournamentTeams`
        """
        url = FaceitAPI.__BASE_URL.format(f'tournaments/{tournament_id}/teams?offset={offset}&limit={limit}')
        retval = await self.__make_request('GET', url)
        return await FaceitAPI.__create_object(retval, TournamentTeams)
    # endregion

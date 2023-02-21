from typing import List, Union, TypeVar, Generic

from .enums import Game, Region, Country, MatchType


class FaceitApiResponse:
    def __init__(self, success: bool = True, **kwargs):
        self.__success = success
        for key, value in kwargs.items():
            setattr(self, key, value)

    def __bool__(self):
        return self.__success


class FaceitApiError(FaceitApiResponse):
    def __init__(self, message: str = 'Bad Request', status_code: int = 400, **kwargs):
        super().__init__(False, **kwargs)
        self.message = message
        self.status_code = status_code


class Assets(FaceitApiResponse):
    def __init__(self,
                 cover: str = None,
                 featured_img_l: str = None,
                 featured_img_m: str = None,
                 featured_img_s: str = None,
                 flag_img_icon: str = None,
                 flag_img_l: str = None,
                 flag_img_m: str = None,
                 flag_img_s: str = None,
                 landing_page: str = None,
                 **kwargs):
        super().__init__(**kwargs)
        self.cover = cover
        self.featured_img_l = featured_img_l
        self.featured_img_m = featured_img_m
        self.featured_img_s = featured_img_s
        self.flag_img_icon = flag_img_icon
        self.flag_img_l = flag_img_l
        self.flag_img_m = flag_img_m
        self.flag_img_s = flag_img_s
        self.landing_page = landing_page


class GameData(FaceitApiResponse):
    def __init__(self,
                 assets: dict,
                 game_id: str = None,
                 long_label: str = None,
                 order: int = None,
                 parent_game_id: str = None,
                 platforms: List[str] = None,
                 regions: List[str] = None,
                 short_label: str = None,
                 **kwargs):
        super().__init__(**kwargs)
        self.assets: Assets = Assets(**assets)
        self.game_id: Game = None if game_id is None else Game(game_id)
        self.long_label = long_label
        self.order = order
        self.parent_game_id = parent_game_id
        self.platforms = [] if platforms is None else platforms
        self.regions = [] if regions is None else regions
        self.short_label = short_label


class JoinChecks(FaceitApiResponse):
    def __init__(self,
                 allowed_team_types: List[str] = None,
                 blacklist_geo_countries: List[str] = None,
                 join_policy: str = None,
                 max_skill_level: int = None,
                 membership_type: str = None,
                 min_skill_level: int = None,
                 whitelist_geo_countries: List[str] = None,
                 whitelist_geo_countries_min_players: int = None,
                 **kwargs):
        super().__init__(**kwargs)
        self.allowed_team_types = [] if allowed_team_types is None else allowed_team_types
        self.blacklist_geo_countries = [] if blacklist_geo_countries is None else blacklist_geo_countries
        self.join_policy = join_policy
        self.max_skill_level = max_skill_level
        self.membership_type = membership_type
        self.min_skill_level = min_skill_level
        self.whitelist_geo_countries = [] if whitelist_geo_countries is None else whitelist_geo_countries
        self.whitelist_geo_countries_min_players = whitelist_geo_countries_min_players


class OrganizerData(FaceitApiResponse):
    def __init__(self,
                 avatar: str = None,
                 cover: str = None,
                 description: str = None,
                 facebook: str = None,
                 faceit_url: str = None,
                 followers_count: int = None,
                 name: str = None,
                 organizer_id: str = None,
                 twitch: str = None,
                 twitter: str = None,
                 type: str = None,
                 vk: str = None,
                 website: str = None,
                 youtube: str = None,
                 **kwargs):
        super().__init__(**kwargs)
        self.avatar = avatar
        self.cover = cover
        self.description = description
        self.facebook = facebook
        self.faceit_url = faceit_url
        self.followers_count = followers_count
        self.name = name
        self.organizer_id = organizer_id
        self.twitch = twitch
        self.twitter = twitter
        self.type = type
        self.vk = vk
        self.website = website
        self.youtube = youtube


class Prize(FaceitApiResponse):
    def __init__(self,
                 faceit_points: int = None,
                 rank: int = None,
                 **kwargs):
        super().__init__(**kwargs)
        self.faceit_points = faceit_points
        self.rank = rank


class Stream(FaceitApiResponse):
    def __init__(self,
                 active: bool = None,
                 platform: str = None,
                 source: str = None,
                 title: str = None,
                 **kwargs):
        super().__init__(**kwargs)
        self.active = active
        self.platform = platform
        self.source = source
        self.title = title


class SubstitutionConfiguration(FaceitApiResponse):
    def __init__(self,
                 max_substitutes: int = None,
                 max_substitutions: int = None,
                 **kwargs):
        super().__init__(**kwargs)
        self.max_substitutes = max_substitutes
        self.max_substitutions = max_substitutions


class Championship(FaceitApiResponse):
    def __init__(self,
                 anticheat_required: bool = None,
                 avatar: str = None,
                 background_image: str = None,
                 championship_id: str = None,
                 championship_start: int = None,
                 checkin_clear: int = None,
                 checkin_enabled: bool = None,
                 checkin_start: int = None,
                 cover_image: str = None,
                 current_subscriptions: int = None,
                 description: str = None,
                 faceit_url: str = None,
                 featured: bool = None,
                 full: bool = None,
                 game_id: str = None,
                 id: str = None,
                 join_checks: dict = None,
                 name: str = None,
                 organizer_id: str = None,
                 prizes: list = None,
                 region: str = None,
                 rules_id: str = None,
                 schedule: dict = None,
                 seeding_strategy: str = None,
                 slots: int = None,
                 status: str = None,
                 stream: dict = None,
                 subscription_end: int = None,
                 subscription_start: int = None,
                 subscriptions_locked: bool = None,
                 substitution_configuration: dict = None,
                 total_groups: int = None,
                 total_prizes: int = None,
                 total_rounds: int = None,
                 type: str = None,
                 game_data: Union[dict, None] = None,
                 organizer_data: Union[dict, None] = None,
                 screening: Union[dict, None] = None,
                 **kwargs):
        super().__init__(**kwargs)
        self.anticheat_required = anticheat_required
        self.avatar = avatar
        self.background_image = background_image
        self.championship_id = championship_id
        self.championship_start = championship_start
        self.checkin_clear = checkin_clear
        self.checkin_enabled = checkin_enabled
        self.checkin_start = checkin_start
        self.cover_image = cover_image
        self.current_subscriptions = current_subscriptions
        self.description = description
        self.faceit_url = faceit_url
        self.featured = featured
        self.full = full
        self.game_data: Union[GameData, None] = None if game_data is None else GameData(**game_data)
        self.game_id: Game = None if game_id is None else Game(game_id)
        self.id = id
        self.join_checks: JoinChecks = None if join_checks is None else JoinChecks(**join_checks)
        self.name = name
        self.organizer_data: Union[OrganizerData, None] = \
            None if organizer_data is None else OrganizerData(**organizer_data)
        self.organizer_id = organizer_id
        self.prizes: List[Prize] = [] if prizes is None else [Prize(**prize) for prize in prizes]
        self.region: Region = None if region is None else Region(region)
        self.rules_id = rules_id
        self.schedule = {} if schedule is None else schedule
        self.seeding_strategy = seeding_strategy
        self.slots = slots
        self.status = status
        self.stream: Stream = None if stream is None else Stream(**stream)
        self.subscription_end = subscription_end
        self.subscription_start = subscription_start
        self.subscriptions_locked = subscriptions_locked
        self.substitution_configuration: SubstitutionConfiguration = None if substitution_configuration is None else \
            SubstitutionConfiguration(**substitution_configuration)
        self.total_groups = total_groups
        self.total_prizes = total_prizes
        self.total_rounds = total_rounds
        self.type = type
        self.screening = {} if screening is None else screening


T = TypeVar("T")


class Collection(FaceitApiResponse, Generic[T]):
    def __init__(self,
                 end: int = None,
                 items: List[T] = None,
                 start: int = None,
                 **kwargs):
        super().__init__(**kwargs)
        self.end = end
        self.items: List[T] = [] if items is None else items
        self.start = start


class RankCollection(Collection, Generic[T]):
    def __init__(self,
                 end: int = None,
                 items: List[T] = None,
                 start: int = None,
                 position: int = None,
                 **kwargs):
        super().__init__(end, items, start, **kwargs)
        self.position = position


class ChampionshipRankingCollection(Collection, Generic[T]):
    def __init__(self,
                 end: int = None,
                 items: List[T] = None,
                 start: int = None,
                 leaderboard: dict = None,
                 **kwargs):
        super().__init__(end, items, start, **kwargs)
        self.leaderboard: Leaderboard = Leaderboard(**leaderboard)


class FromToCollection(Collection, Generic[T]):
    def __init__(self,
                 end: int = None,
                 items: list = None,
                 start: int = None,
                 from_: int = None,
                 to: int = None,
                 **kwargs):
        super().__init__(end, items, start, **kwargs)
        self.from_ = from_
        self.to = to


class Bounds(FaceitApiResponse):
    def __init__(self,
                 left: int = None,
                 right: int = None,
                 **kwargs):
        super().__init__(**kwargs)
        self.left = left
        self.right = right


class Placement(FaceitApiResponse):
    def __init__(self,
                 id: str = None,
                 name: str = None,
                 type: str = None,
                 **kwargs):
        super().__init__(**kwargs)
        self.id = id
        self.name = name
        self.type = type


class Result(FaceitApiResponse):
    def __init__(self,
                 bounds: dict = None,
                 placements: list = None,
                 **kwargs):
        super().__init__(**kwargs)
        self.bounds: Bounds = None if bounds is None else Bounds(**bounds)
        self.placements: List[Placement] = [] if placements is None else [Placement(**x) for x in placements]


class Results(FaceitApiResponse):
    def __init__(self,
                 score: dict = None,
                 winner: str = None,
                 **kwargs):
        super().__init__(**kwargs)
        self.score = {} if score is None else score
        self.winner = winner


class Match(FaceitApiResponse):
    def __init__(self,
                 best_of: int = None,
                 calculate_elo: bool = None,
                 chat_room_id: str = None,
                 competition_id: str = None,
                 competition_name: str = None,
                 competition_type: str = None,
                 faceit_url: str = None,
                 game: str = None,
                 match_id: str = None,
                 organizer_id: str = None,
                 region: str = None,
                 status: str = None,
                 teams: dict = None,
                 version: int = None,
                 broadcast_start_time: int = None,
                 broadcast_start_time_label: str = None,
                 configured_at: int = None,
                 demo_url: list[str] = None,
                 finished_at: int = None,
                 group: int = None,
                 results: dict = None,
                 round: int = None,
                 scheduled_at: int = None,
                 started_at: int = None,
                 voting: dict = None,
                 **kwargs):
        super().__init__(**kwargs)
        self.best_of = best_of
        self.broadcast_start_time = broadcast_start_time
        self.broadcast_start_time_label = broadcast_start_time_label
        self.calculate_elo = calculate_elo
        self.chat_room_id = chat_room_id
        self.competition_id = competition_id
        self.competition_name = competition_name
        self.competition_type = competition_type
        self.configured_at = configured_at
        self.demo_url = [] if demo_url is None else demo_url
        self.faceit_url = faceit_url
        self.finished_at = finished_at
        self.game: Game = None if game is None else Game(game)
        self.group = group
        self.match_id = match_id
        self.organizer_id = organizer_id
        self.region: Region = None if region is None else Region(region)
        self.results: Results = None if results is None else Results(**results)
        self.round = round
        self.scheduled_at = scheduled_at
        self.started_at = started_at
        self.status = status
        self.teams = {} if teams is None else teams
        self.version = version
        self.voting = voting


class Member(FaceitApiResponse):
    def __init__(self,
                 avatar: str = None,
                 faceit_url: str = None,
                 nickname: str = None,
                 roles: List[str] = None,
                 user_id: str = None,
                 **kwargs):
        super().__init__(**kwargs)
        self.avatar = avatar
        self.faceit_url = faceit_url
        self.nickname = nickname
        self.roles = [] if roles is None else roles
        self.user_id = user_id


class TeamMember(FaceitApiResponse):
    def __init__(self,
                 avatar: str = None,
                 country: str = None,
                 faceit_url: str = None,
                 nickname: str = None,
                 user_id: str = None,
                 membership_type: str = None,
                 memberships: List[str] = None,
                 skill_level: int = None,
                 **kwargs):
        super().__init__(**kwargs)
        self.avatar = avatar
        self.country: Country = None if country is None else Country(country)
        self.faceit_url = faceit_url
        self.membership_type = membership_type
        self.memberships = [] if memberships is None else memberships
        self.nickname = nickname
        self.skill_level = skill_level
        self.user_id = user_id


class Team(FaceitApiResponse):
    def __init__(self,
                 avatar: str = None,
                 chat_room_id: str = None,
                 cover_image: str = None,
                 description: str = None,
                 facebook: str = None,
                 faceit_url: str = None,
                 game: str = None,
                 leader: str = None,
                 members: list = None,
                 name: str = None,
                 nickname: str = None,
                 team_id: str = None,
                 team_type: str = None,
                 twitter: str = None,
                 website: str = None,
                 youtube: str = None,
                 **kwargs):
        super().__init__(**kwargs)
        self.avatar = avatar
        self.chat_room_id = chat_room_id
        self.cover_image = cover_image
        self.description = description
        self.facebook = facebook
        self.faceit_url = faceit_url
        self.game: Game = None if game is None else Game(game)
        self.leader = leader
        self.members: List[TeamMember] = [] if members is None else [TeamMember(**x) for x in members]
        self.name = name
        self.nickname = nickname
        self.team_id = team_id
        self.team_type = team_type
        self.twitter = twitter
        self.website = website
        self.youtube = youtube


class Subscription(FaceitApiResponse):
    def __init__(self,
                 coach: str = None,
                 coleader: str = None,
                 group: int = None,
                 leader: str = None,
                 roster: List[str] = None,
                 status: str = None,
                 substitutes: List[str] = None,
                 team: dict = None,
                 **kwargs):
        super().__init__(**kwargs)
        self.coach = coach
        self.coleader = coleader
        self.group = group
        self.leader = leader
        self.roster = [] if roster is None else roster
        self.status = status
        self.substitutes = [] if substitutes is None else substitutes
        self.team: Team = None if team is None else Team(**team)


class Hub(FaceitApiResponse):
    def __init__(self,
                 avatar: str = None,
                 faceit_url: str = None,
                 game_id: str = None,
                 hub_id: str = None,
                 name: str = None,
                 organizer_id: str = None,
                 background_image: str = None,
                 chat_room_id: str = None,
                 cover_image: str = None,
                 description: str = None,
                 game_data: dict = None,
                 join_permission: str = None,
                 max_skill_level: int = None,
                 min_skill_level: int = None,
                 organizer_data: dict = None,
                 players_joined: int = None,
                 region: str = None,
                 rule_id: str = None,
                 **kwargs):
        super().__init__(**kwargs)
        self.avatar = avatar
        self.background_image = background_image
        self.chat_room_id = chat_room_id
        self.cover_image = cover_image
        self.description = description
        self.faceit_url = faceit_url
        self.game_data: Union[GameData, None] = None if game_data is None else GameData(**game_data)
        self.game_id: Game = None if game_id is None else Game(game_id)
        self.hub_id = hub_id
        self.join_permission = join_permission
        self.max_skill_level = max_skill_level
        self.min_skill_level = min_skill_level
        self.name = name
        self.organizer_data: Union[OrganizerData, None] \
            = None if organizer_data is None else OrganizerData(**organizer_data)
        self.organizer_id = organizer_id
        self.players_joined = players_joined
        self.region: Region = None if region is None else Region(region)
        self.rule_id = rule_id


class Role(FaceitApiResponse):
    def __init__(self,
                 color: str = None,
                 name: str = None,
                 ranking: int = None,
                 role_id: str = None,
                 visible_on_chat: bool = None,
                 **kwargs):
        super().__init__(**kwargs)
        self.color = color
        self.name = name
        self.ranking = ranking
        self.role_id = role_id
        self.visible_on_chat = visible_on_chat


class Rule(FaceitApiResponse):
    def __init__(self,
                 body: str = None,
                 game: str = None,
                 name: str = None,
                 organizer: str = None,
                 rule_id: str = None,
                 **kwargs):
        super().__init__(**kwargs)
        self.body = body
        self.game: Game = None if game is None else Game(game)
        self.name = name
        self.organizer = organizer
        self.rule_id = rule_id


class GameStats(FaceitApiResponse):
    def __init__(self,
                 game_id: str = None,
                 players: list = None,
                 **kwargs):
        super().__init__(**kwargs)
        self.game_id: Game = None if game_id is None else Game(game_id)
        self.players: List[GamePlayerStats] = None if players is None else [GamePlayerStats(**p) for p in players]


class GamePlayerStats(FaceitApiResponse):
    def __init__(self,
                 nickname: str = None,
                 player_id: str = None,
                 stats: dict = None,
                 **kwargs):
        super().__init__(**kwargs)
        self.nickname = nickname
        self.player_id = player_id
        self.stats = {} if stats is None else stats


class PlayerStats(FaceitApiResponse):
    def __init__(self,
                 nickname: str = None,
                 player_id: str = None,
                 player_stats: dict = None,
                 **kwargs):
        super().__init__(**kwargs)
        self.nickname = nickname
        self.player_id = player_id
        self.player_stats = {} if player_stats is None else player_stats


class Leaderboard(FaceitApiResponse):
    def __init__(self,
                 competition_id: str = None,
                 competition_type: str = None,
                 end_date: int = None,
                 game_id: str = None,
                 leaderboard_id: str = None,
                 leaderboard_mode: str = None,
                 leaderboard_name: str = None,
                 leaderboard_type: str = None,
                 min_matches: int = None,
                 points_per_draw: int = None,
                 points_per_loss: int = None,
                 points_per_win: int = None,
                 points_type: str = None,
                 ranking_boost: int = None,
                 ranking_type: str = None,
                 region: str = None,
                 start_date: int = None,
                 starting_points: int = None,
                 status: str = None,
                 group: int = None,
                 round: int = None,
                 season: int = None,
                 **kwargs):
        super().__init__(**kwargs)
        self.competition_id = competition_id
        self.competition_type = competition_type
        self.end_date = end_date
        self.game_id: Game = None if game_id is None else Game(game_id)
        self.group = group
        self.leaderboard_id = leaderboard_id
        self.leaderboard_mode = leaderboard_mode
        self.leaderboard_name = leaderboard_name
        self.leaderboard_type = leaderboard_type
        self.min_matches = min_matches
        self.points_per_draw = points_per_draw
        self.points_per_loss = points_per_loss
        self.points_per_win = points_per_win
        self.points_type = points_type
        self.ranking_boost = ranking_boost
        self.ranking_type = ranking_type
        self.region: Region = None if region is None else Region(region)
        self.round = round
        self.season = season
        self.start_date = start_date
        self.starting_points = starting_points
        self.status = status


class Ranking(FaceitApiResponse):
    def __init__(self,
                 current_streak: int = None,
                 draw: int = None,
                 lost: int = None,
                 played: int = None,
                 player: dict = None,
                 points: int = None,
                 position: int = None,
                 win_rate: int = None,
                 won: int = None,
                 **kwargs):
        super().__init__(**kwargs)
        self.current_streak = current_streak
        self.draw = draw
        self.lost = lost
        self.played = played
        self.player: TeamMember = None if player is None else TeamMember(**player)
        self.points = points
        self.position = position
        self.win_rate = win_rate
        self.won = won


class TeamStats(FaceitApiResponse):
    def __init__(self,
                 players: list,
                 premade: dict,
                 team_id: dict,
                 team_stats: dict,
                 **kwargs):
        super().__init__(**kwargs)
        self.players = players
        self.premade = premade
        self.team_id = team_id
        self.team_stats = team_stats


class RoundStats(FaceitApiResponse):
    def __init__(self,
                 best_of: dict,
                 competition_id: dict,
                 game_id: dict,
                 game_mode: dict,
                 match_id: dict,
                 match_round: dict,
                 played: dict,
                 round_stats: dict,
                 teams: list,
                 **kwargs):
        super().__init__(**kwargs)
        self.best_of = best_of
        self.competition_id = competition_id
        self.game_id: Game = None if game_id is None else Game(game_id)
        self.game_mode = game_mode
        self.match_id = match_id
        self.match_round = match_round
        self.played = played
        self.round_stats = round_stats
        self.teams: List[TeamStats] = [TeamStats(**x) for x in teams]


class MatchStats(FaceitApiResponse):
    def __init__(self,
                 rounds: list,
                 **kwargs):
        super().__init__(**kwargs)
        self.rounds: List[RoundStats] = [RoundStats(**x) for x in rounds]


class Tournament(FaceitApiResponse):
    def __init__(self,
                 anticheat_required: bool = None,
                 custom: bool = None,
                 faceit_url: str = None,
                 featured_image: str = None,
                 game_id: str = None,
                 invite_type: str = None,
                 match_type: str = None,
                 max_skill: int = None,
                 membership_type: str = None,
                 min_skill: int = None,
                 name: str = None,
                 number_of_players: int = None,
                 number_of_players_checkedin: int = None,
                 number_of_players_joined: int = None,
                 number_of_players_participants: int = None,
                 organizer_id: str = None,
                 prize_type: str = None,
                 region: str = None,
                 started_at: int = None,
                 status: str = None,
                 subscriptions_count: int = None,
                 team_size: int = None,
                 total_prize: dict = None,
                 tournament_id: str = None,
                 whitelist_countries: list = None,
                 **kwargs):
        super().__init__(**kwargs)
        self.anticheat_required = anticheat_required
        self.custom = custom
        self.faceit_url = faceit_url
        self.featured_image = featured_image
        self.game_id: Game = None if game_id is None else Game(game_id)
        self.invite_type = invite_type
        self.match_type: MatchType = None if match_type is None else MatchType(match_type)
        self.max_skill = max_skill
        self.membership_type = membership_type
        self.min_skill = min_skill
        self.name = name
        self.number_of_players = number_of_players
        self.number_of_players_checkedin = number_of_players_checkedin
        self.number_of_players_joined = number_of_players_joined
        self.number_of_players_participants = number_of_players_participants
        self.organizer_id = organizer_id
        self.prize_type = prize_type
        self.region: Region = None if region is None else Region(region)
        self.started_at = started_at
        self.status = status
        self.subscriptions_count = subscriptions_count
        self.team_size = team_size
        self.total_prize = {} if total_prize is None else total_prize
        self.tournament_id = tournament_id
        self.whitelist_countries = [] if whitelist_countries is None else whitelist_countries


class TournamentData(FaceitApiResponse):
    def __init__(self,
                 anticheat_required: bool = None,
                 best_of: dict = None,
                 calculate_elo: bool = None,
                 competition_id: str = None,
                 cover_image: str = None,
                 custom: bool = None,
                 description: str = None,
                 faceit_url: str = None,
                 featured_image: str = None,
                 game_data: dict = None,
                 game_id: str = None,
                 invite_type: str = None,
                 match_type: str = None,
                 max_skill: int = None,
                 membership_type: str = None,
                 min_skill: int = None,
                 name: str = None,
                 number_of_players: int = None,
                 number_of_players_checkedin: int = None,
                 number_of_players_joined: int = None,
                 number_of_players_participants: int = None,
                 organizer_data: dict = None,
                 organizer_id: str = None,
                 prize_type: str = None,
                 region: str = None,
                 rounds: list = None,
                 rule: str = None,
                 started_at: int = None,
                 status: str = None,
                 substitutes_allowed: int = None,
                 substitutions_allowed: int = None,
                 team_size: int = None,
                 total_prize: dict = None,
                 tournament_id: str = None,
                 voting: dict = None,
                 whitelist_countries: list = None,
                 **kwargs):
        super().__init__(**kwargs)
        self.anticheat_required = anticheat_required
        self.best_of = {} if best_of is None else best_of
        self.calculate_elo = calculate_elo
        self.competition_id = competition_id
        self.cover_image = cover_image
        self.custom = custom
        self.description = description
        self.faceit_url = faceit_url
        self.featured_image = featured_image
        self.game_data = {} if game_data is None else game_data
        self.game_id: Game = None if game_id is None else Game(game_id)
        self.invite_type = invite_type
        self.match_type: MatchType = None if match_type is None else MatchType(match_type)
        self.max_skill = max_skill
        self.membership_type = membership_type
        self.min_skill = min_skill
        self.name = name
        self.number_of_players = number_of_players
        self.number_of_players_checkedin = number_of_players_checkedin
        self.number_of_players_joined = number_of_players_joined
        self.number_of_players_participants = number_of_players_participants
        self.organizer_data = {} if organizer_data is None else organizer_data
        self.organizer_id = organizer_id
        self.prize_type = prize_type
        self.region: Region = None if region is None else Region(region)
        self.rounds = [] if rounds is None else rounds
        self.rule = rule
        self.started_at = started_at
        self.status = status
        self.substitutes_allowed = substitutes_allowed
        self.substitutions_allowed = substitutions_allowed
        self.team_size = team_size
        self.total_prize = {} if total_prize is None else total_prize
        self.tournament_id = tournament_id
        self.voting = {} if voting is None else voting
        self.whitelist_countries = [] if whitelist_countries is None else whitelist_countries


class Player(FaceitApiResponse):
    def __init__(self,
                 avatar: str = None,
                 country: str = None,
                 cover_featured_image: str = None,
                 cover_image: str = None,
                 faceit_url: str = None,
                 friends_ids: List[str] = None,
                 games: dict = None,
                 infractions: dict = None,
                 membership_type: str = None,
                 memberships: List[str] = None,
                 new_steam_id: str = None,
                 nickname: str = None,
                 platforms: dict = None,
                 player_id: str = None,
                 settings: dict = None,
                 steam_id_64: str = None,
                 steam_nickname: str = None,
                 **kwargs):
        super().__init__(**kwargs)
        self.avatar = avatar
        self.country: Country = None if country is None else Country(country)
        self.cover_featured_image = cover_featured_image
        self.cover_image = cover_image
        self.faceit_url = faceit_url
        self.friends_ids = [] if friends_ids is None else friends_ids
        self.games = {} if games is None else games
        self.infractions = {} if infractions is None else infractions
        self.membership_type = membership_type
        self.memberships = [] if memberships is None else memberships
        self.new_steam_id = new_steam_id
        self.nickname = nickname
        self.platforms = {} if platforms is None else platforms
        self.player_id = player_id
        self.settings = {} if settings is None else settings
        self.steam_id_64 = steam_id_64
        self.steam_nickname = steam_nickname


class PlayerMatch(FaceitApiResponse):
    def __init__(self,
                 competition_id: str = None,
                 competition_name: str = None,
                 competition_type: str = None,
                 faceit_url: str = None,
                 finished_at: int = None,
                 game_id: str = None,
                 game_mode: str = None,
                 match_id: str = None,
                 match_type: str = None,
                 max_players: int = None,
                 organizer_id: str = None,
                 playing_players: List[str] = None,
                 region: str = None,
                 results: dict = None,
                 started_at: int = None,
                 status: str = None,
                 teams: dict = None,
                 teams_size: int = None,
                 **kwargs):
        super().__init__(**kwargs)
        self.competition_id = competition_id
        self.competition_name = competition_name
        self.competition_type = competition_type
        self.faceit_url = faceit_url
        self.finished_at = finished_at
        self.game_id: Game = None if game_id is None else Game(game_id)
        self.game_mode = game_mode
        self.match_id = match_id
        self.match_type: MatchType = None if match_type is None else MatchType(match_type)
        self.max_players = max_players
        self.organizer_id = organizer_id
        self.playing_players = [] if playing_players is None else playing_players
        self.region: Region = None if region is None else Region(region)
        self.results: Results = None if results is None else Results(**results)
        self.started_at = started_at
        self.status = status
        self.teams = {} if teams is None else teams
        self.teams_size = teams_size


class PlayerGameStats(FaceitApiResponse):
    def __init__(self,
                 game_id: str = None,
                 lifetime: dict = None,
                 player_id: str = None,
                 segments: list = None,
                 **kwargs):
        super().__init__(**kwargs)
        self.game_id: Game = None if game_id is None else Game(game_id)
        self.lifetime = {} if lifetime is None else lifetime
        self.player_id = player_id
        self.segments = [] if segments is None else segments


class TeamGameStats(FaceitApiResponse):
    def __init__(self,
                 game_id: str = None,
                 lifetime: dict = None,
                 segments: list = None,
                 team_id: str = None,
                 **kwargs):
        super().__init__(**kwargs)
        self.game_id: Game = None if game_id is None else Game(game_id)
        self.lifetime = {} if lifetime is None else lifetime
        self.segments = [] if segments is None else segments
        self.team_id = team_id


class Rank(FaceitApiResponse):
    def __init__(self,
                 country: str = None,
                 faceit_elo: int = None,
                 game_skill_level: int = None,
                 nickname: str = None,
                 player_id: str = None,
                 position: int = None,
                 **kwargs):
        super().__init__(**kwargs)
        self.country: Country = None if country is None else Country(country)
        self.faceit_elo = faceit_elo
        self.game_skill_level = game_skill_level
        self.nickname = nickname
        self.player_id = player_id
        self.position = position


class ChampionshipSearchResult(FaceitApiResponse):
    def __init__(self,
                 competition_id: str = None,
                 competition_type: str = None,
                 game: str = None,
                 name: str = None,
                 number_of_members: int = None,
                 organizer_id: str = None,
                 organizer_name: str = None,
                 organizer_type: str = None,
                 players_checkedin: int = None,
                 players_joined: int = None,
                 prize_type: str = None,
                 region: str = None,
                 slots: int = None,
                 started_at: int = None,
                 status: str = None,
                 total_prize: str = None,
                 **kwargs):
        super().__init__(**kwargs)
        self.competition_id = competition_id
        self.competition_type = competition_type
        self.game: Game = None if game is None else Game(game)
        self.name = name
        self.number_of_members = number_of_members
        self.organizer_id = organizer_id
        self.organizer_name = organizer_name
        self.organizer_type = organizer_type
        self.players_checkedin = players_checkedin
        self.players_joined = players_joined
        self.prize_type = prize_type
        self.region: Region = None if region is None else Region(region)
        self.slots = slots
        self.started_at = started_at
        self.status = status
        self.total_prize = total_prize


class OrganizerSearchResult(FaceitApiResponse):
    def __init__(self,
                 active: bool = None,
                 avatar: str = None,
                 countries: List[str] = None,
                 games: List[str] = None,
                 name: str = None,
                 organizer_id: str = None,
                 partner: bool = None,
                 regions: List[str] = None,
                 **kwargs):
        super().__init__(**kwargs)
        self.active = active
        self.avatar = avatar
        self.countries = [] if countries is None else countries
        self.games = [] if games is None else games
        self.name = name
        self.organizer_id = organizer_id
        self.partner = partner
        self.regions = [] if regions is None else regions


class PlayerSearchResult(FaceitApiResponse):
    def __init__(self,
                 avatar: str = None,
                 country: str = None,
                 games: list = None,
                 nickname: str = None,
                 player_id: str = None,
                 status: str = None,
                 verified: bool = None,
                 **kwargs):
        super().__init__(**kwargs)
        self.avatar = avatar
        self.country: Country = None if country is None else Country(country)
        self.games: List[GameSearchResult] = [] if games is None else [GameSearchResult(**x) for x in games]
        self.nickname = nickname
        self.player_id = player_id
        self.status = status
        self.verified = verified


class GameSearchResult(FaceitApiResponse):
    def __init__(self,
                 name: str = None,
                 skill_level: str = None,
                 **kwargs):
        super().__init__(**kwargs)
        self.name = name
        self.skill_level = skill_level


class TeamSearchResult(FaceitApiResponse):
    def __init__(self,
                 avatar: str = None,
                 chat_room_id: str = None,
                 faceit_url: str = None,
                 game: str = None,
                 name: str = None,
                 team_id: str = None,
                 verified: bool = None,
                 **kwargs):
        super().__init__(**kwargs)
        self.avatar = avatar
        self.chat_room_id = chat_room_id
        self.faceit_url = faceit_url
        self.game: Game = None if game is None else Game(game)
        self.name = name
        self.team_id = team_id
        self.verified = verified


class TournamentSearchResult(FaceitApiResponse):
    def __init__(self,
                 competition_id: str = None,
                 competition_type: str = None,
                 game: str = None,
                 name: str = None,
                 number_of_members: int = None,
                 organizer_id: str = None,
                 organizer_name: str = None,
                 organizer_type: str = None,
                 players_checkedin: int = None,
                 players_joined: int = None,
                 prize_type: str = None,
                 region: str = None,
                 slots: int = None,
                 started_at: int = None,
                 status: str = None,
                 total_prize: str = None,
                 **kwargs):
        super().__init__(**kwargs)
        self.competition_id = competition_id
        self.competition_type = competition_type
        self.game: Game = None if game is None else Game(game)
        self.name = name
        self.number_of_members = number_of_members
        self.organizer_id = organizer_id
        self.organizer_name = organizer_name
        self.organizer_type = organizer_type
        self.players_checkedin = players_checkedin
        self.players_joined = players_joined
        self.prize_type = prize_type
        self.region: Region = None if region is None else Region(region)
        self.slots = slots
        self.started_at = started_at
        self.status = status
        self.total_prize = total_prize


class Brackets(FaceitApiResponse):
    def __init__(self,
                 game: str = None,
                 matches: list = None,
                 name: str = None,
                 rounds: list = None,
                 status: str = None,
                 **kwargs):
        super().__init__(**kwargs)
        self.game: Game = None if game is None else Game(game)
        self.matches: List[BracketMatch] = [] if matches is None else [BracketMatch(**x) for x in matches]
        self.name = name
        self.rounds: List[Round] = [] if rounds is None else [Round(**x) for x in rounds]
        self.status = status


class BracketMatch(FaceitApiResponse):
    def __init__(self,
                 faceit_url: str = None,
                 match_id: str = None,
                 position: int = None,
                 results: dict = None,
                 round: int = None,
                 state: str = None,
                 teams: dict = None,
                 **kwargs):
        super().__init__(**kwargs)
        self.faceit_url = faceit_url
        self.match_id = match_id
        self.position = position
        self.results: Results = None if results is None else Results(**results)
        self.round = round
        self.state = state
        self.teams = {} if teams is None else teams


class Round(FaceitApiResponse):
    def __init__(self,
                 best_of: int = None,
                 label: str = None,
                 matches: int = None,
                 round: int = None,
                 start_time: int = None,
                 starts_asap: bool = None,
                 substitution_time: int = None,
                 substitutions_allowed: bool = None,
                 **kwargs):
        super().__init__(**kwargs)
        self.best_of = best_of
        self.label = label
        self.matches = matches
        self.round = round
        self.start_time = start_time
        self.starts_asap = starts_asap
        self.substitution_time = substitution_time
        self.substitutions_allowed = substitutions_allowed


class TournamentTeams(FaceitApiResponse):
    def __init__(self,
                 checked_in: list,
                 finished: list,
                 joined: list,
                 started: list,
                 **kwargs):
        super().__init__(**kwargs)
        self.checked_in: List[TournamentTeam] = [] if checked_in is None else [TournamentTeam(**x) for x in checked_in]
        self.finished: List[TournamentTeam] = [] if finished is None else [TournamentTeam(**x) for x in finished]
        self.joined: List[TournamentTeam] = [] if joined is None else [TournamentTeam(**x) for x in joined]
        self.started: List[TournamentTeam] = [] if started is None else [TournamentTeam(**x) for x in started]


class TournamentTeam(FaceitApiResponse):
    def __init__(self,
                 nickname: str = None,
                 skill_level: int = None,
                 subs_done: int = None,
                 team_id: str = None,
                 team_leader: str = None,
                 team_type: str = None,
                 **kwargs):
        super().__init__(**kwargs)
        self.nickname = nickname
        self.skill_level = skill_level
        self.subs_done = subs_done
        self.team_id = team_id
        self.team_leader = team_leader
        self.team_type = team_type

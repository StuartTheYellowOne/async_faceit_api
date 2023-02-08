from enum import Enum
from typing import List, Union, TypeVar, Generic, Type, Iterator


class Expansion(Enum):
    NONE = ''
    ORGANIZER = 'organizer'
    GAME = 'game'


class MatchType(Enum):
    ALL = 'all'
    UPCOMING = 'upcoming'
    ONGOING = 'ongoing'
    PAST = 'past'


class Game(Enum):
    RL_XBOX_PC = 'rl_XBOX_PC'
    WOT_XBOX = 'wot_xbox'
    WOT_NA = 'wot_NA'
    WOT_RU = 'wot_RU'
    WOT_EU = 'wot_EU'
    SMITE_XBOX = 'smite_xbox'
    SMITE = 'smite'
    DIRTY_BOMB = 'dirtybomb'
    NHL_20_XBOX = 'nhl_20_xbox'
    NHL_19_XBOX = 'nhl_19_XBOX'
    NHL_18_XBOX = 'nhl_18_XBOX'
    NHL_20_PS4 = 'nhl_20_ps4'
    NHL_19_PS4 = 'nhl_19_PS4'
    NHL_18_PS4 = 'nhl_18_PS4'
    NHL_19 = 'nhl_19'
    NHL_20 = 'nhl_20_parent'
    APEX = 'apex'
    MINION_MASTERS = 'minion_masters'
    HALO_3 = 'halo_3'
    HALO_5_XBOX = 'halo_5'
    HALO_INFINITE = 'halo_infinite'
    HALO_MCC = 'halo_mcc'
    RAINBOW6S_PS4 = 'gs_rainbow_6_ps4'
    RAINBOW6S_XBOX = 'gs_rainbow_6_xbox'
    RAINBOW6S_PC = 'gs_rainbow_6'
    RAINBOW6S = 'rainbow_6'
    WARFACE_EU = 'warface_eu'
    WARFACE_NA = 'warface_na'
    WARFACE_ALPHA = 'warface_alpha'
    WARFACE_PARENT = 'warface_parent'
    WARFACE = 'warface'
    BRAWL_STARS_AUTO = 'brawl_stars_auto'
    BRAWL_STARS = 'brawl_stars'
    OVERWATCH_EU = 'overwatch_EU'
    OVERWATCH_US = 'overwatch_US'
    OVERWATCH_KR = 'overwatch_KR'
    OVERWATCH = 'overwatch'
    CLASH_ROYALE_AUTO = 'clash_royale_auto'
    CLASH_ROYALE = 'clash_royale'
    DESTINY_2_XBOX = 'destiny2_xbox'
    DESTINY_2_PS4 = 'destiny2_ps4'
    DESTINY_2_PC = 'destiny2'
    DESTINY_2 = 'destiny2_parent'
    LOL_TR = 'lol_TR'
    LOL_EUN = 'lol_EUN'
    LOL_EUW = 'lol_EUW'
    LOL_OCE = 'lol_OCE'
    LOL_BR = 'lol_BR'
    LOL_LAN = 'lol_LAN'
    LOL_LAS = 'lol_LAS'
    LOL_NA = 'lol_NA'
    LOL = 'Wild'
    LOL_PARENT = 'lol_parent'
    KRUNKER = 'krunker'
    RING_OF_ELYSIUM = 'ring_of_elysium'
    TF2 = 'tf2'
    CS_DZ = 'csdz'
    VALORANT = 'valorant'
    Dota_2 = 'dota2'
    TEMPERIA = 'temperia'
    HS_BATTLEGROUNDS = 'hearthstone-battlegrounds'
    FIFA22 = 'fifa22'
    FIFA20 = 'fifa20'
    WOW = 'wow'
    QUAKE_CHAMPIONS = 'quake_champions'
    TRACKMANIA = 'trackmania'
    PUBG = 'pubg'
    NEW_STATE_MOBILE = 'newstate'
    RIFT = 'wildrift'
    HEARTHSTONE = 'hearthstone'
    FALLGUYS = 'fallguys'
    TEAMFIGHT_TACTICS = 'teamfight_tactics'
    PUBG_MOBILE = 'pubgmobile'
    ROCKET_LEAGUE = 'rocket_league'
    CS_GO = 'csgo'


class FaceitApiResponse:
    

    def __init__(self, success: bool = True, **kwargs):
        self.__success = success
        for key, value in kwargs.items():
            print(f'WARNING unknown key value pair "{key}: {value}"')
            setattr(self, key, value)

    def __bool__(self):
        return self.__success


class Assets(FaceitApiResponse):
    
    def __init__(self,
                 cover: str,
                 featured_img_l: str,
                 featured_img_m: str,
                 featured_img_s: str,
                 flag_img_icon: str,
                 flag_img_l: str,
                 flag_img_m: str,
                 flag_img_s: str,
                 landing_page: str,
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


class FaceitApiError(FaceitApiResponse):
    
    def __init__(self, message: str = 'Bad Request', status_code: int = 400, **kwargs):
        super().__init__(False, **kwargs)
        self.message = message
        self.status_code = status_code


class GameData(FaceitApiResponse):
    
    def __init__(self,
                 assets: dict,
                 game_id: str,
                 long_label: str,
                 order: int,
                 parent_game_id: str,
                 platforms: List[str],
                 regions: List[str],
                 short_label: str,
                 **kwargs):
        super().__init__(**kwargs)
        self.assets: Assets = Assets(**assets)
        self.game_id = game_id
        self.long_label = long_label
        self.order = order
        self.parent_game_id = parent_game_id
        self.platforms = platforms
        self.regions = regions
        self.short_label = short_label


class JoinChecks(FaceitApiResponse):
    
    def __init__(self,
                 allowed_team_types: List[str],
                 blacklist_geo_countries: List[str],
                 join_policy: str,
                 max_skill_level: int,
                 membership_type: str,
                 min_skill_level: int,
                 whitelist_geo_countries: List[str],
                 whitelist_geo_countries_min_players: int,
                 **kwargs):
        super().__init__(**kwargs)
        self.allowed_team_types = allowed_team_types
        self.blacklist_geo_countries = blacklist_geo_countries
        self.join_policy = join_policy
        self.max_skill_level = max_skill_level
        self.membership_type = membership_type
        self.min_skill_level = min_skill_level
        self.whitelist_geo_countries = whitelist_geo_countries
        self.whitelist_geo_countries_min_players = whitelist_geo_countries_min_players


class OrganizerData(FaceitApiResponse):
    
    def __init__(self,
                 avatar: str,
                 cover: str,
                 description: str,
                 facebook: str,
                 faceit_url: str,
                 followers_count: int,
                 name: str,
                 organizer_id: str,
                 twitch: str,
                 twitter: str,
                 type: str,
                 vk: str,
                 website: str,
                 youtube: str,
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
                 faceit_points: int,
                 rank: int,
                 **kwargs):
        super().__init__(**kwargs)
        self.faceit_points = faceit_points
        self.rank = rank


class Stream(FaceitApiResponse):
    
    def __init__(self,
                 active: bool,
                 platform: str,
                 source: str,
                 title: str,
                 **kwargs):
        super().__init__(**kwargs)
        self.active = active
        self.platform = platform
        self.source = source
        self.title = title


class SubstitutionConfiguration(FaceitApiResponse):
    
    def __init__(self,
                 max_substitutes: int,
                 max_substitutions: int,
                 **kwargs):
        super().__init__(**kwargs)
        self.max_substitutes = max_substitutes
        self.max_substitutions = max_substitutions


class Championship(FaceitApiResponse):
    
    def __init__(self,
                 anticheat_required: bool,
                 avatar: str,
                 background_image: str,
                 championship_id: str,
                 championship_start: int,
                 checkin_clear: int,
                 checkin_enabled: bool,
                 checkin_start: int,
                 cover_image: str,
                 current_subscriptions: int,
                 description: str,
                 faceit_url: str,
                 featured: bool,
                 full: bool,
                 game_id: str,
                 id: str,
                 join_checks: dict,
                 name: str,
                 organizer_id: str,
                 prizes: list,
                 region: str,
                 rules_id: str,
                 schedule: dict,
                 seeding_strategy: str,
                 slots: int,
                 status: str,
                 stream: dict,
                 subscription_end: int,
                 subscription_start: int,
                 subscriptions_locked: bool,
                 substitution_configuration: dict,
                 total_groups: int,
                 total_prizes: int,
                 total_rounds: int,
                 type: str,
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
        self.game_id = game_id
        self.id = id
        self.join_checks: JoinChecks = JoinChecks(**join_checks)
        self.name = name
        self.organizer_data: Union[OrganizerData, None] = \
            None if organizer_data is None else OrganizerData(**organizer_data)
        self.organizer_id = organizer_id
        self.prizes: List[Prize] = [] if prizes is None else [Prize(**prize) for prize in prizes]
        self.region = region
        self.rules_id = rules_id
        self.schedule = schedule
        self.seeding_strategy = seeding_strategy
        self.slots = slots
        self.status = status
        self.stream: Stream = Stream(**stream)
        self.subscription_end = subscription_end
        self.subscription_start = subscription_start
        self.subscriptions_locked = subscriptions_locked
        self.substitution_configuration: SubstitutionConfiguration = \
            SubstitutionConfiguration(**substitution_configuration)
        self.total_groups = total_groups
        self.total_prizes = total_prizes
        self.total_rounds = total_rounds
        self.type = type
        self.screening = {} if screening is None else screening


T = TypeVar("T")


class Collection(FaceitApiResponse, Generic[T]):
    
    def __init__(self,
                 end: int,
                 items: List[T],
                 start: int,
                 **kwargs):
        super().__init__(**kwargs)
        self.end = end
        self.items: List[T] = items
        self.start = start

    def __iter__(self) -> Iterator[T]:
        return self.items.__iter__()

    def __next__(self) -> T:
        return next(self.items)


class RankCollection(Collection, Generic[T]):
    
    def __init__(self,
                 end: int,
                 items: List[T],
                 start: int,
                 position: int,
                 **kwargs):
        super().__init__(end, items, start, **kwargs)
        self.position = position


class ChampionshipRankingCollection(Collection, Generic[T]):
    
    def __init__(self,
                 end: int,
                 items: list,
                 start: int,
                 leaderboard: dict,
                 **kwargs):
        super().__init__(end, items, start, **kwargs)
        self.leaderboard: Leaderboard = Leaderboard(**leaderboard)


class FromToCollection(Collection, Generic[T]):
    
    def __init__(self,
                 end: int,
                 items: list,
                 start: int,
                 from_: int,
                 to: int,
                 **kwargs):
        super().__init__(end, items, start, **kwargs)
        self.from_ = from_
        self.to = to


class Bounds(FaceitApiResponse):
    
    def __init__(self,
                 left: int,
                 right: int,
                 **kwargs):
        super().__init__(**kwargs)
        self.left = left
        self.right = right


class Placement(FaceitApiResponse):
    
    def __init__(self,
                 id: str,
                 name: str,
                 type: str,
                 **kwargs):
        super().__init__(**kwargs)
        self.id = id
        self.name = name
        self.type = type


class Result(FaceitApiResponse):
    
    def __init__(self,
                 bounds: dict,
                 placements: list,
                 **kwargs):
        super().__init__(**kwargs)
        self.bounds: Bounds = Bounds(**bounds)
        self.placements: List[Placement] = [Placement(**x) for x in placements]


class Results(FaceitApiResponse):
    
    def __init__(self,
                 score: dict,
                 winner: str,
                 **kwargs):
        super().__init__(**kwargs)
        self.score = score
        self.winner = winner


class Match(FaceitApiResponse):
    
    def __init__(self,
                 best_of: int,
                 calculate_elo: bool,
                 chat_room_id: str,
                 competition_id: str,
                 competition_name: str,
                 competition_type: str,
                 faceit_url: str,
                 game: str,
                 match_id: str,
                 organizer_id: str,
                 region: str,
                 status: str,
                 teams: dict,
                 version: int,
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
        self.game = game
        self.group = group
        self.match_id = match_id
        self.organizer_id = organizer_id
        self.region = region
        self.results: Results = None if results is None else Results(**results)
        self.round = round
        self.scheduled_at = scheduled_at
        self.started_at = started_at
        self.status = status
        self.teams = teams
        self.version = version
        self.voting = voting


class Member(FaceitApiResponse):
    
    def __init__(self,
                 avatar: str,
                 faceit_url: str,
                 nickname: str,
                 roles: List[str],
                 user_id: str,
                 **kwargs):
        super().__init__(**kwargs)
        self.avatar = avatar
        self.faceit_url = faceit_url
        self.nickname = nickname
        self.roles = roles
        self.user_id = user_id


class TeamMember(FaceitApiResponse):
    
    def __init__(self,
                 avatar: str,
                 country: str,
                 faceit_url: str,
                 nickname: str,
                 user_id: str,
                 membership_type: str = None,
                 memberships: List[str] = None,
                 skill_level: int = None,
                 **kwargs):
        super().__init__(**kwargs)
        self.avatar = avatar
        self.country = country
        self.faceit_url = faceit_url
        self.membership_type = membership_type
        self.memberships = [] if memberships is None else memberships
        self.nickname = nickname
        self.skill_level = skill_level
        self.user_id = user_id


class Team(FaceitApiResponse):
    
    def __init__(self,
                 avatar: str,
                 chat_room_id: str,
                 cover_image: str,
                 description: str,
                 facebook: str,
                 faceit_url: str,
                 game: str,
                 leader: str,
                 members: list,
                 name: str,
                 nickname: str,
                 team_id: str,
                 team_type: str,
                 twitter: str,
                 website: str,
                 youtube: str,
                 **kwargs):
        super().__init__(**kwargs)
        self.avatar = avatar
        self.chat_room_id = chat_room_id
        self.cover_image = cover_image
        self.description = description
        self.facebook = facebook
        self.faceit_url = faceit_url
        self.game = game
        self.leader = leader
        self.members: List[TeamMember] = [TeamMember(**x) for x in members]
        self.name = name
        self.nickname = nickname
        self.team_id = team_id
        self.team_type = team_type
        self.twitter = twitter
        self.website = website
        self.youtube = youtube


class Subscription(FaceitApiResponse):
    
    def __init__(self,
                 coach: str,
                 coleader: str,
                 group: int,
                 leader: str,
                 roster: List[str],
                 status: str,
                 substitutes: List[str],
                 team: dict,
                 **kwargs):
        super().__init__(**kwargs)
        self.coach = coach
        self.coleader = coleader
        self.group = group
        self.leader = leader
        self.roster = roster
        self.status = status
        self.substitutes = substitutes
        self.team: Team = Team(**team)


class Hub(FaceitApiResponse):
    
    def __init__(self,
                 avatar: str,
                 faceit_url: str,
                 game_id: str,
                 hub_id: str,
                 name: str,
                 organizer_id: str,
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
        self.game_id = game_id
        self.hub_id = hub_id
        self.join_permission = join_permission
        self.max_skill_level = max_skill_level
        self.min_skill_level = min_skill_level
        self.name = name
        self.organizer_data: Union[OrganizerData, None] \
            = None if organizer_data is None else OrganizerData(**organizer_data)
        self.organizer_id = organizer_id
        self.players_joined = players_joined
        self.region = region
        self.rule_id = rule_id


class Role(FaceitApiResponse):
    
    def __init__(self,
                 color: str,
                 name: str,
                 ranking: int,
                 role_id: str,
                 visible_on_chat: bool,
                 **kwargs):
        super().__init__(**kwargs)
        self.color = color
        self.name = name
        self.ranking = ranking
        self.role_id = role_id
        self.visible_on_chat = visible_on_chat


class Rule(FaceitApiResponse):
    
    def __init__(self,
                 body: str,
                 game: str,
                 name: str,
                 organizer: str,
                 rule_id: str,
                 **kwargs):
        super().__init__(**kwargs)
        self.body = body
        self.game = game
        self.name = name
        self.organizer = organizer
        self.rule_id = rule_id


class GameStats(FaceitApiResponse):
    
    def __init__(self,
                 game_id: str,
                 players: list,
                 **kwargs):
        super().__init__(**kwargs)
        self.game_id = game_id
        self.players: List[GamePlayerStats] = [GamePlayerStats(**p) for p in players]


class GamePlayerStats(FaceitApiResponse):
    
    def __init__(self,
                 nickname: str,
                 player_id: str,
                 stats: dict,
                 **kwargs):
        super().__init__(**kwargs)
        self.nickname = nickname
        self.player_id = player_id
        self.stats = stats


class PlayerStats(FaceitApiResponse):
    
    def __init__(self,
                 nickname: str,
                 player_id: str,
                 player_stats: dict,
                 **kwargs):
        super().__init__(**kwargs)
        self.nickname = nickname
        self.player_id = player_id
        self.player_stats = player_stats


class Leaderboard(FaceitApiResponse):
    
    def __init__(self,
                 competition_id: str,
                 competition_type: str,
                 end_date: int,
                 game_id: str,
                 leaderboard_id: str,
                 leaderboard_mode: str,
                 leaderboard_name: str,
                 leaderboard_type: str,
                 min_matches: int,
                 points_per_draw: int,
                 points_per_loss: int,
                 points_per_win: int,
                 points_type: str,
                 ranking_boost: int,
                 ranking_type: str,
                 region: str,
                 start_date: int,
                 starting_points: int,
                 status: str,
                 group: int = None,
                 round: int = None,
                 season: int = None,
                 **kwargs):
        super().__init__(**kwargs)
        self.competition_id = competition_id
        self.competition_type = competition_type
        self.end_date = end_date
        self.game_id = game_id
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
        self.region = region
        self.round = round
        self.season = season
        self.start_date = start_date
        self.starting_points = starting_points
        self.status = status


class Ranking(FaceitApiResponse):
    
    def __init__(self,
                 current_streak: int,
                 draw: int,
                 lost: int,
                 played: int,
                 player: dict,
                 points: int,
                 position: int,
                 win_rate: int,
                 won: int,
                 **kwargs):
        super().__init__(**kwargs)
        self.current_streak = current_streak
        self.draw = draw
        self.lost = lost
        self.played = played
        self.player: TeamMember = TeamMember(**player)
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
        self.game_id = game_id
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
                 anticheat_required: bool,
                 custom: bool,
                 faceit_url: str,
                 featured_image: str,
                 game_id: str,
                 invite_type: str,
                 match_type: str,
                 max_skill: int,
                 membership_type: str,
                 min_skill: int,
                 name: str,
                 number_of_players: int,
                 number_of_players_checkedin: int,
                 number_of_players_joined: int,
                 number_of_players_participants: int,
                 organizer_id: str,
                 prize_type: str,
                 region: str,
                 started_at: int,
                 status: str,
                 subscriptions_count: int,
                 team_size: int,
                 total_prize: dict,
                 tournament_id: str,
                 whitelist_countries: list,
                 **kwargs):
        super().__init__(**kwargs)
        self.anticheat_required = anticheat_required
        self.custom = custom
        self.faceit_url = faceit_url
        self.featured_image = featured_image
        self.game_id = game_id
        self.invite_type = invite_type
        self.match_type = match_type
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
        self.region = region
        self.started_at = started_at
        self.status = status
        self.subscriptions_count = subscriptions_count
        self.team_size = team_size
        self.total_prize = total_prize
        self.tournament_id = tournament_id
        self.whitelist_countries = whitelist_countries


class TournamentData(FaceitApiResponse):
    
    def __init__(self,
                 anticheat_required: bool,
                 best_of: dict,
                 calculate_elo: bool,
                 competition_id: str,
                 cover_image: str,
                 custom: bool,
                 description: str,
                 faceit_url: str,
                 featured_image: str,
                 game_data: dict,
                 game_id: str,
                 invite_type: str,
                 match_type: str,
                 max_skill: int,
                 membership_type: str,
                 min_skill: int,
                 name: str,
                 number_of_players: int,
                 number_of_players_checkedin: int,
                 number_of_players_joined: int,
                 number_of_players_participants: int,
                 organizer_data: dict,
                 organizer_id: str,
                 prize_type: str,
                 region: str,
                 rounds: list,
                 rule: str,
                 started_at: int,
                 status: str,
                 substitutes_allowed: int,
                 substitutions_allowed: int,
                 team_size: int,
                 total_prize: dict,
                 tournament_id: str,
                 voting: dict,
                 whitelist_countries: list,
                 **kwargs):
        super().__init__(**kwargs)
        self.anticheat_required = anticheat_required
        self.best_of = best_of
        self.calculate_elo = calculate_elo
        self.competition_id = competition_id
        self.cover_image = cover_image
        self.custom = custom
        self.description = description
        self.faceit_url = faceit_url
        self.featured_image = featured_image
        self.game_data = game_data
        self.game_id = game_id
        self.invite_type = invite_type
        self.match_type = match_type
        self.max_skill = max_skill
        self.membership_type = membership_type
        self.min_skill = min_skill
        self.name = name
        self.number_of_players = number_of_players
        self.number_of_players_checkedin = number_of_players_checkedin
        self.number_of_players_joined = number_of_players_joined
        self.number_of_players_participants = number_of_players_participants
        self.organizer_data = organizer_data
        self.organizer_id = organizer_id
        self.prize_type = prize_type
        self.region = region
        self.rounds = rounds
        self.rule = rule
        self.started_at = started_at
        self.status = status
        self.substitutes_allowed = substitutes_allowed
        self.substitutions_allowed = substitutions_allowed
        self.team_size = team_size
        self.total_prize = total_prize
        self.tournament_id = tournament_id
        self.voting = voting
        self.whitelist_countries = whitelist_countries


class Player(FaceitApiResponse):
    
    def __init__(self,
                 avatar: str,
                 country: str,
                 cover_featured_image: str,
                 cover_image: str,
                 faceit_url: str,
                 friends_ids: List[str],
                 games: dict,
                 infractions: dict,
                 membership_type: str,
                 memberships: List[str],
                 new_steam_id: str,
                 nickname: str,
                 platforms: dict,
                 player_id: str,
                 settings: dict,
                 steam_id_64: str,
                 steam_nickname: str,
                 **kwargs):
        super().__init__(**kwargs)
        self.avatar = avatar
        self.country = country
        self.cover_featured_image = cover_featured_image
        self.cover_image = cover_image
        self.faceit_url = faceit_url
        self.friends_ids = friends_ids
        self.games = games
        self.infractions = infractions
        self.membership_type = membership_type
        self.memberships = memberships
        self.new_steam_id = new_steam_id
        self.nickname = nickname
        self.platforms = platforms
        self.player_id = player_id
        self.settings = settings
        self.steam_id_64 = steam_id_64
        self.steam_nickname = steam_nickname


class PlayerMatch(FaceitApiResponse):
    
    def __init__(self,
                 competition_id: str,
                 competition_name: str,
                 competition_type: str,
                 faceit_url: str,
                 finished_at: int,
                 game_id: str,
                 game_mode: str,
                 match_id: str,
                 match_type: str,
                 max_players: int,
                 organizer_id: str,
                 playing_players: List[str],
                 region: str,
                 results: dict,
                 started_at: int,
                 status: str,
                 teams: dict,
                 teams_size: int,
                 **kwargs):
        super().__init__(**kwargs)
        self.competition_id = competition_id
        self.competition_name = competition_name
        self.competition_type = competition_type
        self.faceit_url = faceit_url
        self.finished_at = finished_at
        self.game_id = game_id
        self.game_mode = game_mode
        self.match_id = match_id
        self.match_type = match_type
        self.max_players = max_players
        self.organizer_id = organizer_id
        self.playing_players = playing_players
        self.region = region
        self.results: Results = Results(**results)
        self.started_at = started_at
        self.status = status
        self.teams = teams
        self.teams_size = teams_size


class PlayerGameStats(FaceitApiResponse):
    
    def __init__(self,
                 game_id: str,
                 lifetime: dict,
                 player_id: str,
                 segments: list,
                 **kwargs):
        super().__init__(**kwargs)
        self.game_id = game_id
        self.lifetime = lifetime
        self.player_id = player_id
        self.segments = segments


class TeamGameStats(FaceitApiResponse):
    
    def __init__(self,
                 game_id: str,
                 lifetime: dict,
                 segments: list,
                 team_id: str,
                 **kwargs):
        super().__init__(**kwargs)
        self.game_id = game_id
        self.lifetime = lifetime
        self.segments = segments
        self.team_id = team_id


class Rank(FaceitApiResponse):
    
    def __init__(self,
                 country: str,
                 faceit_elo: int,
                 game_skill_level: int,
                 nickname: str,
                 player_id: str,
                 position: int,
                 **kwargs):
        super().__init__(**kwargs)
        self.country = country
        self.faceit_elo = faceit_elo
        self.game_skill_level = game_skill_level
        self.nickname = nickname
        self.player_id = player_id
        self.position = position


class ChampionshipSearchResult(FaceitApiResponse):
    
    def __init__(self,
                 competition_id: str,
                 competition_type: str,
                 game: str,
                 name: str,
                 number_of_members: int,
                 organizer_id: str,
                 organizer_name: str,
                 organizer_type: str,
                 players_checkedin: int,
                 players_joined: int,
                 prize_type: str,
                 region: str,
                 slots: int,
                 started_at: int,
                 status: str,
                 total_prize: str,
                 **kwargs):
        super().__init__(**kwargs)
        self.competition_id = competition_id
        self.competition_type = competition_type
        self.game = game
        self.name = name
        self.number_of_members = number_of_members
        self.organizer_id = organizer_id
        self.organizer_name = organizer_name
        self.organizer_type = organizer_type
        self.players_checkedin = players_checkedin
        self.players_joined = players_joined
        self.prize_type = prize_type
        self.region = region
        self.slots = slots
        self.started_at = started_at
        self.status = status
        self.total_prize = total_prize


class OrganizerSearchResult(FaceitApiResponse):
    
    def __init__(self,
                 active: bool,
                 avatar: str,
                 countries: List[str],
                 games: List[str],
                 name: str,
                 organizer_id: str,
                 partner: bool,
                 regions: List[str],
                 **kwargs):
        super().__init__(**kwargs)
        self.active = active
        self.avatar = avatar
        self.countries = countries
        self.games = games
        self.name = name
        self.organizer_id = organizer_id
        self.partner = partner
        self.regions = regions


class PlayerSearchResult(FaceitApiResponse):
    
    def __init__(self,
                 avatar: str,
                 country: str,
                 games: list,
                 nickname: str,
                 player_id: str,
                 status: str,
                 verified: bool,
                 **kwargs):
        super().__init__(**kwargs)
        self.avatar = avatar
        self.country = country
        self.games: List[GameSearchResult] = [GameSearchResult(**x) for x in games]
        self.nickname = nickname
        self.player_id = player_id
        self.status = status
        self.verified = verified


class GameSearchResult(FaceitApiResponse):
    
    def __init__(self,
                 name: str,
                 skill_level: str,
                 **kwargs):
        super().__init__(**kwargs)
        self.name = name
        self.skill_level = skill_level


class TeamSearchResult(FaceitApiResponse):
    
    def __init__(self,
                 avatar: str,
                 chat_room_id: str,
                 faceit_url: str,
                 game: str,
                 name: str,
                 team_id: str,
                 verified: bool,
                 **kwargs):
        super().__init__(**kwargs)
        self.avatar = avatar
        self.chat_room_id = chat_room_id
        self.faceit_url = faceit_url
        self.game = game
        self.name = name
        self.team_id = team_id
        self.verified = verified


class TournamentSearchResult(FaceitApiResponse):
    
    def __init__(self,
                 competition_id: str,
                 competition_type: str,
                 game: str,
                 name: str,
                 number_of_members: int,
                 organizer_id: str,
                 organizer_name: str,
                 organizer_type: str,
                 players_checkedin: int,
                 players_joined: int,
                 prize_type: str,
                 region: str,
                 slots: int,
                 started_at: int,
                 status: str,
                 total_prize: str,
                 **kwargs):
        super().__init__(**kwargs)
        self.competition_id = competition_id
        self.competition_type = competition_type
        self.game = game
        self.name = name
        self.number_of_members = number_of_members
        self.organizer_id = organizer_id
        self.organizer_name = organizer_name
        self.organizer_type = organizer_type
        self.players_checkedin = players_checkedin
        self.players_joined = players_joined
        self.prize_type = prize_type
        self.region = region
        self.slots = slots
        self.started_at = started_at
        self.status = status
        self.total_prize = total_prize


class Brackets(FaceitApiResponse):
    
    def __init__(self,
                 game: str,
                 matches: list,
                 name: str,
                 rounds: list,
                 status: str,
                 **kwargs):
        super().__init__(**kwargs)
        self.game = game
        self.matches: List[BracketMatch] = [BracketMatch(**x) for x in matches]
        self.name = name
        self.rounds: List[Round] = [Round(**x) for x in rounds]
        self.status = status


class BracketMatch(FaceitApiResponse):
    
    def __init__(self,
                 faceit_url: str,
                 match_id: str,
                 position: int,
                 results: dict,
                 round: int,
                 state: str,
                 teams: dict,
                 **kwargs):
        super().__init__(**kwargs)
        self.faceit_url = faceit_url
        self.match_id = match_id
        self.position = position
        self.results: Results = Results(**results)
        self.round = round
        self.state = state
        self.teams = teams


class Round(FaceitApiResponse):
    
    def __init__(self,
                 best_of: int,
                 label: str,
                 matches: int,
                 round: int,
                 start_time: int,
                 starts_asap: bool,
                 substitution_time: int,
                 substitutions_allowed: bool,
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
        self.checked_in: List[TournamentTeam] = [TournamentTeam(**x) for x in checked_in]
        self.finished: List[TournamentTeam] = [TournamentTeam(**x) for x in finished]
        self.joined: List[TournamentTeam] = [TournamentTeam(**x) for x in joined]
        self.started: List[TournamentTeam] = [TournamentTeam(**x) for x in started]


class TournamentTeam(FaceitApiResponse):
    
    def __init__(self,
                 nickname: str,
                 skill_level: int,
                 subs_done: int,
                 team_id: str,
                 team_leader: str,
                 team_type: str,
                 **kwargs):
        super().__init__(**kwargs)
        self.nickname = nickname
        self.skill_level = skill_level
        self.subs_done = subs_done
        self.team_id = team_id
        self.team_leader = team_leader
        self.team_type = team_type



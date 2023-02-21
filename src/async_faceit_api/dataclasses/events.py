from typing import TypeVar, Generic, List

from src.async_faceit_api.dataclasses.enums import FaceitEventType

T = TypeVar("T")


class FaceitEvent(Generic[T]):
    def __init__(self,
                 transaction_id: str,
                 event: str,
                 event_id: str,
                 third_party_id: str,
                 app_id: str,
                 timestamp: str,
                 retry_count: int,
                 version: int,
                 payload: T):
        self.transaction_id = transaction_id
        self.event: FaceitEventType = FaceitEventType(event)
        self.event_id = event_id
        self.third_party_id = third_party_id
        self.app_id = app_id
        self.timestamp = timestamp
        self.retry_count = retry_count
        self.version = version
        self.payload = payload


class UnknownEvent:
    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)


class HubCreated:
    def __init__(self,
                 id: str,
                 name: str,
                 owner_id: str,
                 organizer_id: str,
                 game: str,
                 region: str,
                 published: bool,
                 check_game: bool,
                 check_region: bool,
                 slots: int,
                 join_permissions: str,
                 min_skill_level: int,
                 max_skill_level: int,
                 owner_roles: List[str],
                 roles: List[dict],
                 app_config: dict,
                 created_at: str,
                 ):
        self.id = id
        self.name = name
        self.owner_id = owner_id
        self.organizer_id = organizer_id
        self.game = game
        self.region = region
        self.published = published
        self.check_game = check_game
        self.check_region = check_region
        self.slots = slots
        self.join_permissions = join_permissions
        self.min_skill_level = min_skill_level
        self.max_skill_level = max_skill_level
        self.owner_roles = owner_roles
        self.roles: List[Role] = [Role(**role) for role in roles]
        self.app_config = app_config
        self.created_at = created_at


class HubUpdated:
    def __init__(self,
                 id: str,
                 organizer_id: str,
                 roles: List[dict]
                 ):
        self.id = id
        self.organizer_id = organizer_id
        self.roles: List[Role] = [Role(**role) for role in roles]


class HubRoleUpdated:
    def __init__(self,
                 id: str,
                 organizer_id: str,
                 role_id: str,
                 role_name: str,
                 type: str,
                 ranking: int,
                 color: str,
                 permissions: List[str]
                 ):
        self.id = id
        self.organizer_id = organizer_id
        self.role_id = role_id
        self.role_name = role_name
        self.type = type
        self.ranking = ranking
        self.color = color
        self.permissions = permissions


class HubRoleCreated(HubRoleUpdated):
    pass


class HubRoleDeleted:
    def __init__(self,
                 id: str,
                 organizer_id: str,
                 role_id: str,
                 role_name: str,
                 type: str,
                 ):
        self.id = id
        self.organizer_id = organizer_id
        self.role_id = role_id
        self.role_name = role_name
        self.type = type


class Role:
    def __init__(self,
                 id: str,
                 name: str,
                 permissions: List[str],
                 ranking: int,
                 color: str,
                 type: str,
                 visible_on_chat: bool):
        self.id = id
        self.name = name
        self.permissions = permissions
        self.ranking = ranking
        self.color = color
        self.type = type
        self.visible_on_chat = visible_on_chat

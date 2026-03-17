from dataclasses import dataclass, field
from enum import Enum
from typing import Dict, Any, NewType

from cmdb_watch.domain.entities.watcher import Watcher, Cursor, WatcherId, WatcherRule, WatcherRuleId, WatcherRuleModel

InstanceID = NewType("InstanceID", str)


@dataclass(slots=True, frozen=True)
class FieldChange:
    field: str
    old_value: Any
    new_value: Any


class ChangeEventType(str, Enum):
    CREATE = "create"
    UPDATE = "update"
    DELETE = "delete"


@dataclass(slots=True, frozen=True)
class ChangedEvent:
    watcher_id: WatcherId
    model: WatcherRuleModel
    instance_id: InstanceID
    event_type: ChangeEventType
    changes: list[FieldChange]
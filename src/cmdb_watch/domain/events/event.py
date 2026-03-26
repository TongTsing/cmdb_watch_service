from dataclasses import dataclass
from typing import Any, NewType

from cmdb_watch.domain.entities.watcher import (
    WatcherId,
    WatcherRuleModel,
)
from cmdb_watch.domain.events.base import BaseEvent


InstanceID = NewType("InstanceID", str)


@dataclass(slots=True, frozen=True)
class FieldChange:
    field: str
    old_value: Any
    new_value: Any


# @dataclass(slots=True, frozen=True)
# class ChangedEvent:
#     watcher_id: WatcherId
#     model: WatcherRuleModel
#     instance_id: InstanceID
#     event_type: ChangeEventType
#     changes: list[FieldChange]


@dataclass(slots=True, frozen=True)
class WatchEvent(BaseEvent):
    watcher_id: WatcherId
    model: WatcherRuleModel
    instance_id: InstanceID


@dataclass(slots=True, frozen=True)
class CreatedEvent(WatchEvent):
    """
    创建事件包含完整的数据，因为数据是新创建的。
    """

    data: dict[str, Any]


@dataclass(slots=True, frozen=True)
class UpdatedEvent(WatchEvent):
    """
    更新事件不包含数据变更信息，因为数据已经被更新了。
    """

    changes: list[FieldChange]


@dataclass(slots=True, frozen=True)
class DeletedEvent(WatchEvent):
    """
    删除事件不包含数据变更信息，因为数据已经被删除了。
    """

    pass

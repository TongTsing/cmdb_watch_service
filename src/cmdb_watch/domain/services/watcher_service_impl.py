from cmdb_watch.domain.services.watcher_service import WatcherService
from cmdb_watch.domain.entities.watcher import Watcher, WatcherId
from cmdb_watch.domain.events.event import (
    CreatedEvent,
    DeletedEvent,
    InstanceID,
    UpdatedEvent,
)
from cmdb_watch.domain.events.base import BaseEvent


class WatcherServiceImpl(WatcherService):

    def run(self, watcher: Watcher, data: list[dict]) -> list[BaseEvent]:
        events: list[BaseEvent] = []

        for item in data:
            events.extend(self.detect_changes(watcher, item))

        return events

    def detect_changes(self, watcher: Watcher, new_data: dict) -> list[BaseEvent]:

        instance_id = InstanceID(new_data["bk_detail"]["bk_inst_id"])
        event_type = new_data["bk_event_type"]

        match event_type:
            case "update":
                event = UpdatedEvent(
                    instance_id=instance_id,
                    model=watcher.rule.model,
                    watcher_id=WatcherId(watcher.id),
                    changes=[],  # 这里你可以实现具体的字段对比逻辑，生成
                )
            case "create":
                event = CreatedEvent(
                    instance_id=instance_id,
                    model=watcher.rule.model,
                    watcher_id=WatcherId(watcher.id),
                    data={},
                )
            case "delete":
                event = DeletedEvent(
                    instance_id=instance_id,
                    model=watcher.rule.model,
                    watcher_id=WatcherId(watcher.id),
                )
            case _:
                raise ValueError(f"Unknown event type: {event_type}")
        return [event]

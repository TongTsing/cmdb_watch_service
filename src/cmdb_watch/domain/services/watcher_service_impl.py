from cmdb_watch.domain.services.watcher_service import WatcherService
from cmdb_watch.domain.entities.watcher import Watcher
from cmdb_watch.domain.events.event import (
    ChangeEventType,
    ChangedEvent,
    InstanceID,
)


class WatcherServiceImpl(WatcherService):

    def run(self, watcher: Watcher, data: list[dict]) -> list[ChangedEvent]:
        events: list[ChangedEvent] = []

        for item in data:
            events.extend(self.detect_changes(watcher, item))

        return events

    def detect_changes(self, watcher: Watcher, new_data: dict) -> list[ChangedEvent]:

        instance_id = InstanceID(new_data["bk_detail"]["bk_inst_id"])
        event_type = ChangeEventType(new_data["bk_event_type"])

        event = ChangedEvent(
            watcher_id=watcher.id,
            model=watcher.rule.model,
            instance_id=instance_id,
            event_type=event_type,
            # CMDB 没有字段 diff
            changes=[],
        )

        return [event]

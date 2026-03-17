from cmdb_watch.domain.events.event import ChangedEvent
from notification_service import NotificationService


class LocalNotificationService(NotificationService):
    def notify(self, events: list[ChangedEvent]):
        print(events)
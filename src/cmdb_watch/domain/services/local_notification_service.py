import logging

from cmdb_watch.domain.events.event import ChangedEvent
from cmdb_watch.domain.services.notification_service import NotificationService


class LocalNotificationService(NotificationService):
    def notify(self, events: list[ChangedEvent]):
        logging.info(f"LocalNotificationService received events: {events}")

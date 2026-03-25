import logging

from cmdb_watch.domain.services.email_notification_service import (
    EmailNotificationService,
)
from cmdb_watch.infrastructure.watcher_repository import WatcherRepository
from cmdb_watch.shared.event_bus import EventHandler
from cmdb_watch.domain.events.event import ChangedEvent

logging.basicConfig(level=logging.INFO)


class EmailHandler(EventHandler):
    def __init__(
        self,
        watcher_repo: WatcherRepository,
        notification_service: EmailNotificationService,
    ) -> None:
        self.watcher_repo = watcher_repo
        self.email_sender = notification_service

    def handle(self, event: ChangedEvent) -> None:
        watcher = self.watcher_repo.get_watchers_for_event(event)
        if watcher and watcher.rule.enabled:
            # 这里可以添加发送邮件的逻辑，例如使用 SMTP 库
            logging.info(
                f"Sending email to {watcher.rule.notify_emails} for event {event}"
            )
            self.email_sender.notify(event)

from cmdb_watch.domain.entities.watcher import Watcher
from cmdb_watch.domain.events.event import BaseEvent
from cmdb_watch.domain.services.notification_service import NotificationService
from cmdb_watch.domain.services.eamil_sender_service import EmailSender
from cmdb_watch.infrastructure.watcher_repository import WatcherRepository


class EmailNotificationService(NotificationService):
    def __init__(self, watcher_repo: WatcherRepository, email_sender: EmailSender):
        self.watcher_repo = watcher_repo
        self.email_sender = email_sender

    def send_notification(self, watcher: Watcher, event: BaseEvent):
        self.email_sender.send_email(
            recipient=watcher.rule.notify_emails[0],  # 简化处理，只发送给第一个邮箱
            subject=f"Watcher {watcher.id} detected an event",
            body=f"Watcher {watcher.id} detected an event of type {event.event_type} on instance {event.instance_id} of model {event.model}.",
        )

    def notify(self, event: BaseEvent):
        watcher = self.watcher_repo.get_watchers_for_event(event)
        self.send_notification(watcher, event)

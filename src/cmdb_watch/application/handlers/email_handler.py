import logging

from cmdb_watch.application.handlers.base import EventHandler
from cmdb_watch.domain.events.base import BaseEvent
from cmdb_watch.domain.events.event import CreatedEvent, UpdatedEvent, DeletedEvent

logging.basicConfig(level=logging.INFO)


class EmailHandler(EventHandler):
    def handle(self, event: BaseEvent) -> None:
        if isinstance(event, CreatedEvent):
            logging.info(f"Received CreatedEvent: {event}")
            # 处理创建事件，发送邮件通知
            # self.email_service.send_email(...)
        elif isinstance(event, UpdatedEvent):
            print(f"[EMAIL] Resource updated: {event.instance_id}")
            for change in event.changes:
                logging.info(
                    f" - {change.field}: {change.old_value} -> {change.new_value}"
                )
            # 处理更新事件，发送邮件通知
            # self.email_service.send_email(...)
        elif isinstance(event, DeletedEvent):
            logging.info(f"Received DeletedEvent: {event}")
            # 处理删除事件，发送邮件通知
            # self.email_service.send_email(...)
        else:
            logging.warning(f"Received unknown event type: {event}")

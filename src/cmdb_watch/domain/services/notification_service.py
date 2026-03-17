from abc import ABC, abstractmethod
from cmdb_watch.domain.events.event import ChangedEvent


class NotificationService(ABC):
    @abstractmethod
    def notify(self, events: list[ChangedEvent]):
        raise NotImplementedError
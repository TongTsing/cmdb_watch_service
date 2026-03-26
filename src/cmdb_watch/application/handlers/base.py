from abc import ABC, abstractmethod

from cmdb_watch.domain.events.base import BaseEvent


class EventHandler(ABC):
    @abstractmethod
    def handle(self, event: BaseEvent) -> None:
        raise NotImplementedError

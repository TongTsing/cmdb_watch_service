from abc import ABC, abstractmethod

from cmdb_watch.domain.events.event import BaseEvent
from cmdb_watch.application.handlers.base import EventHandler


class EventBus(ABC):
    @abstractmethod
    def register(self, event_type: type[BaseEvent], handler: EventHandler) -> None:
        """
        Register an event handler for a specific event type.
        """
        pass

    @abstractmethod
    def publish(self, events: list[BaseEvent]) -> None:
        """
        Publish events to all matched handlers.
        """
        pass


class SimpleEventBus(EventBus):
    def __init__(self):
        # key: event_type, value: list of handlers
        self._handlers: dict[type[BaseEvent], list[EventHandler]] = {}

    def register(self, event_type: type[BaseEvent], handler: EventHandler) -> None:
        if event_type not in self._handlers:
            self._handlers[event_type] = []

        # 防止重复注册
        if handler not in self._handlers[event_type]:
            self._handlers[event_type].append(handler)

    def publish(self, events: list[BaseEvent]) -> None:
        for event in events:
            for event_type, handlers in self._handlers.items():
                if isinstance(event, event_type):
                    for handler in handlers:
                        try:
                            handler.handle(event)
                        except Exception as e:
                            print(
                                f"[EventBus] handler error: {handler}, event: {event}, error: {e}"
                            )

from typing import Protocol
from cmdb_watch.domain.events.event import ChangedEvent


class EventHandler(Protocol):
    def handle(self, event: ChangedEvent) -> None: ...


class EventBus:
    def __init__(self):
        self._handlers: list[EventHandler] = []

    def register_handler(self, handler: EventHandler) -> None:
        """
        Register an event handler to receive events.
        """
        ...

    def publish(self, events: list[ChangedEvent]) -> None:
        """
        Publish an event to all registered handlers.
        """
        ...


class SimpleEventBus(EventBus):
    def __init__(self):
        super().__init__()

    def register_handler(self, handler: EventHandler) -> None:
        self._handlers.append(handler)

    def publish(self, events: list[ChangedEvent]) -> None:
        for handler in self._handlers:
            for event in events:
                handler.handle(event)

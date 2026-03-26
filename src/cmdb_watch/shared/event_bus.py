from typing import Protocol
from cmdb_watch.domain.events.event import ChangedEvent


class EventHandler(Protocol):
    def handle(self, event: ChangedEvent) -> None: ...


class EventBus:
    def __init__(self):
        self._handlers: dict[type[ChangedEvent], list[EventHandler]] = {}

    def register_handler(
        self, event_type: type[ChangedEvent], handler: EventHandler
    ) -> None:
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

    def register_handler(
        self, event_type: type[ChangedEvent], handler: EventHandler
    ) -> None:
        if event_type not in self._handlers:
            self._handlers[event_type] = []

        self._handlers[event_type].append(handler)

    def publish(self, events: list[ChangedEvent]) -> None:
        for event in events:
            for event_type, handlers in self._handlers.items():
                if isinstance(event, event_type):
                    for handler in handlers:
                        handler.handle(event)

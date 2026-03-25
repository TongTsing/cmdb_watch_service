from cmdb_watch.domain.events.event import ChangedEvent
from cmdb_watch.infrastructure.watcher_repository import WatcherRepository
from cmdb_watch.domain.entities.watcher import Watcher, WatcherId


class InMemoryWatcherRepository(WatcherRepository):
    def __init__(self):
        self._storage: dict[WatcherId, Watcher] = {}

    def save(self, watcher: Watcher):
        # 这里可以实现保存 Watcher 的逻辑
        self._storage[watcher.id] = watcher

    def get_by_id(self, watcher_id: WatcherId) -> Watcher:
        return self._storage[WatcherId(watcher_id)]

    def get_all(self) -> list[Watcher]:
        return list(self._storage.values())

    def delete_by_id(self, watcher_id: WatcherId):
        del self._storage[WatcherId(watcher_id)]

    def delete_all(self):
        self._storage.clear()

    def exists_by_id(self, watcher_id: WatcherId) -> bool:
        return watcher_id in self._storage

    def count(self) -> int:
        return len(self._storage)

    def clear(self):
        self._storage.clear()

    def get_watchers_for_event(self, event: ChangedEvent) -> Watcher:
        # 这里根据事件的属性来筛选相关的 Watcher
        # 例如，如果事件有一个 'type' 属性，我们可以根据这个属性来筛选 Watcher
        return self.get_by_id(event.watcher_id)

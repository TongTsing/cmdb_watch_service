from cmdb_watch.infrastructure.watcher_repository import WatcherRepository
from cmdb_watch.domain.entities.watcher import Watcher, WatcherId


class InMemoryWatcherRepository(WatcherRepository):
    def __init__(self):
        self._storage: dict[WatcherId, Watcher] = {}

    def save(self, watcher: Watcher):
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

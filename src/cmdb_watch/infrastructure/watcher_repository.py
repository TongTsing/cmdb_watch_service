from abc import ABC, abstractmethod
from cmdb_watch.domain.entities.watcher import Watcher, WatcherId


class WatcherRepository(ABC):
    @abstractmethod
    def save(self, watcher: Watcher):
        """
        保存 Watcher
        """
        raise NotImplementedError

    @abstractmethod
    def get_by_id(self, watcher_id: WatcherId) -> Watcher:
        """
        根据 ID 获取 Watcher
        """
        raise NotImplementedError

    @abstractmethod
    def get_all(self) -> list[Watcher]:
        """
        获取所有 Watcher
        """
        raise NotImplementedError

    @abstractmethod
    def get_watchers_for_event(self, event) -> Watcher:
        """
        根据事件获取相关的 Watcher
        """
        raise NotImplementedError

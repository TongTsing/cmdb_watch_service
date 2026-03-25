from abc import ABC, abstractmethod
from cmdb_watch.domain.entities.watcher import Watcher
from cmdb_watch.domain.events.event import ChangedEvent


class WatcherService(ABC):

    @abstractmethod
    def run(self, watcher: Watcher, data: list[dict]) -> list[ChangedEvent]:
        """
        执行 watcher 检查，生成变化事件
        """
        raise NotImplementedError

    @abstractmethod
    def detect_changes(self, watcher: Watcher, new_data: dict) -> list[ChangedEvent]:
        """
        对比字段生成变化事件
        """
        raise NotImplementedError

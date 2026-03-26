from abc import ABC, abstractmethod
from cmdb_watch.domain.entities.watcher import Watcher
from cmdb_watch.domain.events.event import BaseEvent


class WatcherService(ABC):

    @abstractmethod
    def run(self, watcher: Watcher, data: list[dict]) -> list[BaseEvent]:
        """
        执行 watcher 检查，生成变化事件
        """
        raise NotImplementedError

    @abstractmethod
    def detect_changes(self, watcher: Watcher, new_data: dict) -> list[BaseEvent]:
        """
        对比字段生成变化事件
        """
        raise NotImplementedError

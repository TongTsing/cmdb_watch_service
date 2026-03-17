from abc import ABC, abstractmethod
from src.cmdb_watch.domain.entities.watcher import Watcher


class WatchClient(ABC):
    @abstractmethod
    def fetch_data(self, watcher: Watcher) -> list[dict]:
        """
        拉取 CMDB 变化数据
        """
        raise NotImplementedError
    


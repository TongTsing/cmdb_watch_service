from cmdb_watch.domain.entities.watcher import Watcher
from cmdb_watch.domain.services.notification_service import NotificationService
from cmdb_watch.domain.services.watcher_service import WatcherService


from cmdb_watch.domain.entities.watcher import Watcher
from cmdb_watch.domain.services.watcher_service import WatcherService
from cmdb_watch.infrastructure.watch_client import WatchClient
from cmdb_watch.infrastructure.watcher_repository import WatcherRepository


class WatchService:
    def __init__(self, watcher_service: WatcherService, watch_client: WatchClient, notification_service: NotificationService, watcher_repo: WatcherRepository):
        self.watcher_service = watcher_service
        self.watch_client = watch_client
        self.notification_service = notification_service
        self.watcher_repo = watcher_repo

    def run(self, watcher: Watcher):
        # 1. 拉取 CMDB 变化数据
        data = self.watch_client.fetch_data(watcher)

        # 2. 调用领域服务生成变化事件
        events = self.watcher_service.run(watcher, data)

        # 3. 更新 cursor（取 data 中最大 position / id / timestamp）
        if data:
            last_position = max(item['position'] for item in data)
            watcher.update_cursor(last_position)
            self.watcher_repo.save(watcher)

        # 4. 发送通知
        if events:
            self.notification_service.notify(events)
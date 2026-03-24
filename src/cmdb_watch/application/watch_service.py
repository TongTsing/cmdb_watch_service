from cmdb_watch.domain.services.notification_service import NotificationService
from cmdb_watch.domain.services.watcher_service import WatcherService
from cmdb_watch.infrastructure.watch_client import WatchClient
from cmdb_watch.infrastructure.watcher_repository import WatcherRepository


class WatchService:

    def __init__(
        self,
        watcher_repo: WatcherRepository,
        watch_client: WatchClient,
        watcher_service: WatcherService,
        notifier: NotificationService,
    ):
        self.watcher_repo = watcher_repo
        self.client = watch_client
        self.watcher_service = watcher_service
        self.notifier = notifier

    def run(self):

        watchers = self.watcher_repo.get_all()

        for watcher in watchers:

            data = self.client.fetch_data(watcher)

            events = self.watcher_service.run(watcher, data)

            if events:
                self.notifier.notify(events)

            # 更新 cursor（你后面可以细化）
            watcher.update_cursor(data[-1]["bk_cursor"])

            self.watcher_repo.save(watcher)

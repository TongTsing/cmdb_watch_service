from src.cmdb_watch.domain.entities.watcher import WatcherRule, Watcher, Cursor, WatcherId, WatcherRuleId, WatcherRuleModel, Watcher
from src.cmdb_watch.application.watch_service import WatchService
from src.cmdb_watch.infrastructure.watch_client_impl import WatchClientImpl
from src.cmdb_watch.infrastructure.watcher_repository_impl import InMemoryWatcherRepository
from src.cmdb_watch.domain.services.watcher_service_impl import WatcherServiceImpl
from src.cmdb_watch.domain.services.local_notification_service import LocalNotificationService



def test_1():
    watch_client = WatchClientImpl("https://it-bkapi-dev.envisioncn.com/api/bk-cmdb/prod/api/v3/event/watch/resource/object_instance", "bk_iam", "44e4efd2-ef87-4456-9bbb-459c1d45b3e6")
    watcher_repo = InMemoryWatcherRepository()
    notification_service = LocalNotificationService()
    watcher_service = WatcherServiceImpl()

    watch_service = WatchService(
        watcher_service=watcher_service,
        watch_client=watch_client,
        notification_service=notification_service,
        watcher_repo=watcher_repo
    )
    # 定义 Watcher
    watcher_rule = WatcherRule(
        id=WatcherRuleId("1"),
        model=WatcherRuleModel("test_tq"),
        fields=("id",),
        interval=1,
        notify_emails=("lX7ZD@example.com",),
        enabled=True
    )
    watcher = Watcher(watcher_rule, "MQ04DTY5YjI1OWIzYmZjNDc0ODdiN2QyODA4NQ11cGRhdGUNMTc3MzY0ODgzNQ02DTU4MDA=", WatcherId("1"))  
    watch_service.run(
        watcher
    )

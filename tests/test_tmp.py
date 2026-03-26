import json
import logging

from cmdb_watch.domain.entities.watcher import (
    WatcherRule,
    Watcher,
    WatcherId,
    WatcherRuleId,
    WatcherRuleModel,
)
from cmdb_watch.application.watch_service import WatchService
from cmdb_watch.domain.events.event import CreatedEvent, UpdatedEvent
from cmdb_watch.application.handlers.email_handler import EmailHandler
from cmdb_watch.infrastructure.watch_client_impl import WatchClientImpl
from cmdb_watch.infrastructure.watcher_repository_impl import InMemoryWatcherRepository
from cmdb_watch.domain.services.watcher_service_impl import WatcherServiceImpl
from unittest.mock import patch

from cmdb_watch.shared.event_bus import SimpleEventBus


logging.basicConfig(level=logging.INFO)


def test_1():
    # watch_client = WatchClientImpl("https://it-bkapi-dev.envisioncn.com/api/bk-cmdb/prod/api/v3/event/watch/resource/object_instance", "bk_iam", "44e4efd2-ef87-4456-9bbb-459c1d45b3e6")
    with patch(
        "cmdb_watch.infrastructure.watch_client_impl.requests.post"
    ) as mock_post:
        mock_response = '{"result":true,"code":0,"message":"success","data":{"bk_watched":true,"bk_events":[{"bk_cursor":"MQ04DTY5YjI1OWIzYmZjNDc0ODdiN2QyODA4NQ11cGRhdGUNMTc3MzgwMDQ3MA0yDTU4MDA=","bk_resource":"object_instance","bk_event_type":"update","bk_detail":{"bk_inst_id":5800,"bk_inst_name":"ins1","field_1":"13"}}]}}'
        mock_response = json.loads(mock_response)
        mock_post.return_value.status_code = 200
        mock_post.return_value.json.return_value = mock_response

        watch_client = WatchClientImpl(
            "https://it-bkapi-dev.envisioncn.com/api/bk-cmdb/prod/api/v3/event/watch/resource/object_instance",
            "bk_iam",
            "44e4efd2-ef87-4456-9bbb-459c1d45b3e6",
        )
        watcher_repo = InMemoryWatcherRepository()
        watcher = Watcher(
            rule=WatcherRule(
                id=WatcherRuleId("1"),
                model=WatcherRuleModel("test_tq"),
                fields=("id",),
                interval=1,
                notify_emails=("togqing@canway.net",),
                enabled=True,
            ),
            initial_cursor="MQ04DTY5YjI1OWIzYmZjNDc0ODdiN2QyODA4NQ11cGRhdGUNMTc3MzY0ODgzNQ02DTU4MDA=",
            watcher_id=WatcherId("1"),
        )
        watcher_repo.save(watcher)
        watcher_service = WatcherServiceImpl()
        event_bus = SimpleEventBus()
        event_handler = EmailHandler()
        event_bus.register(CreatedEvent, event_handler)
        event_bus.register(UpdatedEvent, event_handler)

        watch_service = WatchService(
            watcher_service=watcher_service,
            watch_client=watch_client,
            watcher_repo=watcher_repo,
            event_bus=event_bus,
        )

        # 定义 Watcher
        watcher_rule = WatcherRule(
            id=WatcherRuleId("1"),
            model=WatcherRuleModel("test_tq"),
            fields=("id",),
            interval=1,
            notify_emails=("togqing@canway.net",),
            enabled=True,
        )
        watcher = Watcher(
            watcher_rule,
            "MQ04DTY5YjI1OWIzYmZjNDc0ODdiN2QyODA4NQ11cGRhdGUNMTc3MzY0ODgzNQ02DTU4MDA=",
            WatcherId("1"),
        )
        watch_service.run()
        logging.info("Test completed successfully.")


if __name__ == "__main__":
    test_1()

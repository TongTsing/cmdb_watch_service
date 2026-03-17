import time
import requests

from watch_client import WatchClient
from src.cmdb_watch.domain.entities.watcher import Watcher


class WatchClientImpl(WatchClient):

    def __init__(self, url: str, app_code: str, app_secret: str):
        self.url = url
        self.app_code = app_code
        self.app_secret = app_secret

    def fetch_data(self, watcher: Watcher) -> list[dict]:

        payload = {
            "bk_supplier_account": "0",
            "bk_resource": "object_instance",
            "bk_event_types": ["create", "update", "delete"],
            "bk_fields": [
                "bk_inst_id",
                "bk_inst_name",
                "field_1"
            ],
            "bk_filter": {
                "bk_sub_resource": "test_tq"
            }
        }

        if watcher.cursor.value:
            payload["bk_cursor"] = watcher.cursor.value
        else:
            payload["bk_start_from"] = int(time.time())

        headers = {
            'X-Bkapi-Authorization': f'{"bk_app_code": {self.app_code},"bk_app_secret": {self.app_secret}, "bk_username": "admin"}',
            'Content-Type': 'application/json'
        }

        resp = requests.post(
            self.url,
            headers=headers,
            json=payload,
            timeout=10
        )

        resp.raise_for_status()

        data = resp.json()

        if not data["result"]:
            raise RuntimeError(data["message"])

        watched = data["data"].get("bk_watched")

        if not watched:
            return []

        return watched

# src/cmdb_watch/domain/entities/watcher.py
from dataclasses import dataclass, field
from collections import deque
from typing import NewType, Tuple
from uuid import uuid4

# 类型定义
WatcherId = NewType("WatcherId", str)
WatcherRuleId = NewType("WatcherRuleId", str)
WatcherRuleModel = NewType("WatcherRuleModel", str)


@dataclass(frozen=True)
class WatcherRule:
    """
    Watcher 的规则部分：不可变
    """
    id: WatcherRuleId
    model: WatcherRuleModel
    fields: Tuple[str, ...]
    interval: int
    notify_emails: Tuple[str, ...]
    enabled: bool = True


class Cursor:
    """
    Cursor 管理 Watcher 的消费状态
    """
    def __init__(self, initial: str = 0, history_size: int = 10):
        self.value: str = initial
        self._history: deque[str] = deque(maxlen=history_size)

    @property
    def history(self) -> Tuple[str, ...]:
        return tuple(self._history)

    def advance(self, new_value: str):
        """
        更新 cursor，如果新的值大于当前值
        """
        if new_value > self.value:
            self.value = new_value
            self._history.append(new_value)


class Watcher:
    """
    Watcher 领域实体：
    - 包含规则和状态
    - rule: 不可变
    - cursor: 可变
    - id: 实体唯一标识
    """
    def __init__(self, rule: WatcherRule, initial_cursor: str, watcher_id: WatcherId | None = None):
        self.id: WatcherId = watcher_id or WatcherId(str(uuid4()))
        self.rule: WatcherRule = rule
        self.cursor: Cursor = Cursor(initial_cursor)

    def update_cursor(self, new_value: str):
        """
        更新消费位置
        """
        self.cursor.advance(new_value)

    @property
    def cursor_history(self) -> Tuple[str, ...]:
        return self.cursor.history

    @property
    def enabled(self) -> bool:
        return self.rule.enabled

    @property
    def model(self) -> WatcherRuleModel:
        return self.rule.model

    @property
    def fields(self) -> Tuple[str, ...]:
        return self.rule.fields

    @property
    def notify_emails(self) -> Tuple[str, ...]:
        return self.rule.notify_emails
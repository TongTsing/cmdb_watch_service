# CMDB Watch SaaS

一个基于 **事件驱动（Event-Driven）架构** 的轻量级 CMDB 变更感知系统。

> 让 CMDB 从“数据源”进化为“事件源”

---

## 🚀 项目简介

本项目用于解决 CMDB 场景中的核心问题：

* 无法实时感知资源变更
* 自动化能力弱（依赖轮询）
* 系统之间高度耦合
* 缺乏统一的变更处理机制

通过引入：

* Diff 检测
* 领域事件（Domain Event）
* 事件总线（EventBus）
* Handler 机制

实现：

```text
CMDB数据变化 → 事件 → 自动处理
```

---

## 🧠 核心设计理念

### 1. 事件驱动（Event-Driven）

系统围绕“变化”构建，而不是“数据”：

```text
数据是状态
事件是行为
```

---

### 2. 解耦（Decoupling）

通过 EventBus：

```text
生产者 → Event ← 消费者
```

而不是：

```text
A → B（直接调用）
```

---

### 3. 类型驱动（Type-based Routing）

使用事件类型本身进行路由：

```python
event_bus.register(UpdatedEvent, handler)
```

避免：

```python
if event.type == "update":
    ...
```

---

### 4. 不可变事件（Immutable Event）

```python
@dataclass(frozen=True)
```

保证：

* 安全性
* 可追溯性
* 可调试性

---

## 🏗️ 项目结构

```text
cmdb_watch/
├── domain/
│   ├── entities/
│   └── events/
│       ├── base.py
│       └── event.py
│
├── application/
│   └── watch_service.py
│
├── infrastructure/
│   └── watch_client.py
│
├── shared/
│   └── event_bus.py
│
└── handlers/
    ├── audit_handler.py
    ├── email_handler.py
    └── log_handler.py
```

---

## ⚙️ 核心模块说明

### 1. Watcher（数据监听）

负责从 CMDB 拉取数据：

```text
CMDB → WatchClient → WatchService
```

---

### 2. Diff Engine（差异检测）

对比数据变化：

```text
旧数据 vs 新数据 → FieldChange
```

---

### 3. Event（领域事件）

```python
CreatedEvent
UpdatedEvent
DeletedEvent
```

统一表达“变化”。

---

### 4. EventBus（事件总线）

负责：

* 事件分发
* 类型路由
* Handler 调度

---

### 5. Handler（事件处理）

扩展点：

* Audit（审计）
* Notification（通知）
* Logging（日志）
* Webhook（外部集成）

---

## 🔧 使用示例

### 1. 注册 Handler

```python
event_bus.register(UpdatedEvent, AuditHandler())
event_bus.register(UpdatedEvent, EmailHandler())
```

---

### 2. 发布事件

```python
events = [
    UpdatedEvent(...),
    CreatedEvent(...)
]

event_bus.publish(events)
```

---

### 3. 实现 Handler

```python
class AuditHandler:
    def handle(self, event: UpdatedEvent) -> None:
        print(f"audit log: {event}")
```

---

## ✨ 特性

* ✅ 类型安全的事件系统
* ✅ 可扩展的 Handler 机制
* ✅ 字段级变更检测（FieldChange）
* ✅ 同步事件总线（可扩展为异步）
* ✅ 解耦架构设计
* ✅ 易于演进为分布式系统

---

## 📈 演进路线

当前版本：

* 内存 EventBus（同步）

未来规划：

* [ ] AsyncEventBus（线程池/协程）
* [ ] Kafka / Redis Stream 集成
* [ ] 事件持久化（Event Store）
* [ ] 重试机制 / 死信队列（DLQ）
* [ ] 幂等处理
* [ ] 多租户支持

---

## ⚠️ 当前限制

* 同步处理（存在阻塞）
* 无事件存储（不可回放）
* 无失败重试机制
* 无分布式能力

---

## 🧩 适用场景

* CMDB 变更通知
* 运维自动化触发
* 审计日志系统
* 安全监控
* 系统集成（Webhook）

---

## 💡 一句话总结

```text
用事件连接系统，而不是用调用连接系统
```

---

## 📚 相关文章

👉 《从 CMDB 轮询到事件驱动：一个轻量级变更感知 SaaS 的设计与实现》

https://blog.tongqing.asia/detail/297/
---

## 🛠️ 开发者说明

该项目采用：

* Python 3.10+
* dataclass + typing
* 简化版 DDD 架构

适合用于：

* 事件驱动架构学习
* 后端设计能力提升
* 分布式系统演进实践

---

## 📌 License

MIT

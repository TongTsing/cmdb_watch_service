# My Backend Project

一个 **纯 Python 后端项目模板**。

设计目标：

- Clean Architecture
- Domain Driven Design (DDD)
- 框架无关
- 支持 Docker
- 支持 Pre-commit
- 适合中型项目

---

# 项目结构

src/my_backend_project

domain           领域层（核心业务规则）

application      应用层（业务用例）

infrastructure   基础设施（数据库、Redis等）

interfaces       外部接口（API、CLI、Worker）

shared           公共工具

config           配置管理

---

# 安装依赖

poetry install

---

# 启动开发环境依赖

docker-compose up -d

---

# 运行项目

make run

---

# 代码格式化

make format

---

# 代码检查

make lint

---

# 运行测试

make test

---

# 启用 git hooks

pre-commit install
# Makefile 用于统一开发命令

.PHONY: install run format lint lint-fix test test-cov clean precommit ci fix


# ==============================
# 安装依赖
# ==============================
install:
	poetry install


# ==============================
# 启动应用
# ==============================
run:
	poetry run python src/cmdb_watch/manage.py runserver


# ==============================
# 代码格式化
# ==============================
format:
	poetry run black .


# ==============================
# 代码检查
# ==============================
lint:
	poetry run ruff check .


# 自动修复 lint
lint-fix:
	poetry run ruff check . --fix


# ==============================
# 运行测试
# ==============================
test:
	poetry run pytest -s --log-cli-level=INFO


# 覆盖率
test-cov:
	poetry run pytest --cov=src --cov-report=term-missing --cov-report=html


# ==============================
# 清理缓存
# ==============================
clean:
	find . -type d -name "__pycache__" -exec rm -rf {} +
	find . -type d -name ".pytest_cache" -exec rm -rf {} +
	find . -type d -name ".mypy_cache" -exec rm -rf {} +
	find . -type d -name ".ruff_cache" -exec rm -rf {} +
	find . -type d -name ".tox" -exec rm -rf {} +
	find . -type f -name "*.pyc" -delete
	rm -rf .coverage htmlcov build dist *.egg-info


# ==============================
# pre-commit
# ==============================
precommit:
	pre-commit run --all-files


# ==============================
# 本地 CI
# ==============================
ci: clean lint test


# ==============================
# 常用修复流程
# ==============================
fix:
	make format
	make lint-fix

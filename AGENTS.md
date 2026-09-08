> 🌐 本文档由 [TheAlgorithms/Python](https://github.com/TheAlgorithms/Python) 翻译,英文原版见原项目。

# AGENTS.md

本文件为向 **TheAlgorithms/Python** 贡献的 AI 编码代理(以及它们背后的人类)提供指导。它是对 [`CONTRIBUTING.md`](CONTRIBUTING.md) 的补充——绝不会覆盖后者。请先阅读该文件。

本仓库面向教学:实现应当清晰、正确,而非追求极致优化。所有变更都要经过 CI 和 `algorithms-keeper` 机器人检查,二者都会自动拒绝不符合规范的 PR。

## 提交 Pull Request 之前

- **在 PR 描述中至少勾选一个复选框。** `algorithms-keeper` 机器人**会关闭任何"Describe your change"部分没有已勾选项(`* [x]`)的 PR**。请填写 `.github/pull_request_template.md` 自带的模板,并在提交前勾选所有适用的条目——这是自动化 PR 被关闭的最常见原因。
- **每个 PR 只包含一个算法文件。** 把不相关的改动拆分到单独的 PR 中,让评审保持聚焦。
- **不要在同一个 PR 中同时修改代码及其 doctest。** 如果你只是更新测试,请明确说明,并且不要动其他任何内容。

## 代码规范(由 CI 强制执行)

- **格式化与静态检查:** `ruff`(`uvx ruff check .` 与 `uvx ruff format .`)。在本地运行 `uvx pre-commit run --all-files`,可以提前发现 CI 会报出的所有问题。
- **类型注解:** 用[类型注解](https://docs.python.org/3/library/typing.html)标注每个函数的参数与返回值。
- **Doctest:** 每个函数至少需要一个能在 `python -m doctest -v your_file.py`(以及 `pytest`)下通过的 [doctest](https://docs.python.org/3/library/doctest.html)。
- **命名:** 文件名全部小写并使用下划线(不含空格或连字符);函数与变量遵循标准 Python 命名规范。
- **位置:** 新文件应放入已有目录中。
- **参考资料:** 新算法应附上 Wikipedia 或同类讲解的 URL。

## 在本地运行测试套件

本项目使用 [`uv`](https://docs.astral.sh/uv/) 管理——没有 `requirements.txt`。依赖记录在 `pyproject.toml`/`uv.lock` 中,`uvx` 可在一次性环境中运行工具,不会污染你的环境:

```bash
uvx pre-commit run --all-files                       # ruff、格式化、各类钩子
uvx pytest your_module/your_file.py --doctest-modules
```

(如果你更愿意使用项目锁定的环境,`uv run pytest ...` 同样可行。)

部分目录在 CI 中被有意跳过(`.github/workflows/build.yml` 中的 `--ignore` 条目),通常是因为某个重量级依赖缺少与仓库当前目标 CPython 版本匹配的 wheel。在断定某个文件没有测试覆盖之前,先查看那份清单。

## 良好的代理行为

- 保持 diff 最小化,只覆盖所声明的改动范围。
- 保留既有的风格与结构;清晰优先于炫技。
- 绝不编造 doctest 输出——真正运行它,并粘贴真实结果。
- 如果 CI 变红,阅读日志并修复根因,而不是盲目重跑。

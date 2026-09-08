> 🌐 本文档由 [TheAlgorithms/Python](https://github.com/TheAlgorithms/Python) 翻译,英文原版见原项目。

# 技能:为 TheAlgorithms/Python 创建新 pull request

依据 [`CONTRIBUTING.md`](../../../CONTRIBUTING.md) 中已写明的规则创建新的 pull request。目标是让任何人(人类或 AI)都能以相同方式创建新 PR,产出清晰、友善、经过测试、带类型注解、可合并的贡献。

## 如何运行本技能

创建新 pull request 之前,确保本地 `master` 分支已与 `upstream/master` 同步。

为 pull request 创建一个命名清晰的新分支。PR 的改动不得在 `master` 分支上直接进行或提交。

绝不手工编辑或回退 `uv.lock` 文件。如果你添加了正当的依赖,让 `uv-lock` pre-commit 钩子重新生成它——不要手动改动。手工修改过的 `uv.lock` 会导致 `algorithms-keeper` 机器人以无效为由关闭 pull request,即使是仓库维护者也无法撤销这一点。

务必在 pull request 描述("Describe your change"部分)中至少勾选一个 Markdown 复选框,否则 `algorithms-keeper` 机器人会以无效为由关闭 PR。如果你在已被关闭的 PR 上 @提及任意仓库维护者,他们可以撤销这一操作。

### 1. 贡献之前 / 这是算法吗?

- [ ] 本次改动新增、修复或文档化的是**一个算法**——不是多个,也不是在同一 PR 中同时修改代码和 doctest。
- [ ] 它是真正的算法或数据结构(见"什么是算法?"一节),而不是脚本、代码片段、现有 API 的使用教程或习题堆砌。
- [ ] 它**尚未存在于仓库中**(请搜索现有目录)。
- [ ] **没有更早的 open PR** 已经做过同样的事——如有请附上链接。
- [ ] 署名规范——无抄袭,先前来源已注明出处。

### 2. 编码风格

- [ ] 不需要 `from __future__ import annotations`,因为本仓库只使用最新版 CPython。
- [ ] 文件与目录名全部小写、使用下划线,并位于已有目录内。
- [ ] 公开函数/类带有**类型注解**。
- [ ] 公开函数带有**真正能通过的 doctest**。
- [ ] 变量与函数命名具有描述性(能用一个词说清的地方不用单个字母)。
- [ ] 对于基本只是字段集合的简单类,**考虑**用 `from typing import NamedTuple` 或 `from dataclasses import dataclass` 替代手写的 `__init__`/`__repr__`/`__eq__`。这些工具被低估了,能让简单类更短、更清晰——在真正能简化代码的地方使用,而不是到处使用。
- [ ] 代码已格式化且通过静态检查(`ruff`、`pre-commit`)。
- [ ] `DIRECTORY.md` 和 `README.md` **未经手工编辑**——`algorithms-keeper` 机器人会在合并后自动重新生成它们。

### 3. 其他提交要求

- [ ] 至少一条记录该算法的 **Wikipedia(或同等)URL**。
- [ ] Docstring 说明了函数的功能及其参数/返回值。
- [ ] 没有不必要的第三方依赖。

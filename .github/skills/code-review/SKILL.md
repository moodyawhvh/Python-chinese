> 🌐 本文档由 [TheAlgorithms/Python](https://github.com/TheAlgorithms/Python) 翻译,英文原版见原项目。

# 技能:TheAlgorithms/Python 的代码评审

依据 [`CONTRIBUTING.md`](../../../CONTRIBUTING.md) 中已写明的规则评审 pull request。目标是让任何评审者(人类或 AI)都能以相同方式执行评审,并给出清晰、友善、可操作的结论。

## 如何运行本技能

阅读 PR 的 diff,然后按顺序过一遍 `CONTRIBUTING.md` 的四个部分,并按下方固定格式输出结论。要引用你所依据的具体规则,并给出修复建议——绝不能只丢下一句"不通过"。

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
- [ ] 代码已格式化且通过静态检查(`ruff`、`pre-commit`)。

> **可选提示:** 当 PR 手写了一个基本只是字段集合的简单类(手写 `__init__` 加 `__repr__`/`__eq__`)时,值得**建议**改用 `from typing import NamedTuple` 或 `from dataclasses import dataclass` 来简化代码。这些工具被低估了,贡献者在合适之处使用会从中受益。请把它作为可选改进提出,而不是阻塞项——不要仅仅因为类是按传统写法手写的就要求修改。

#### 当 PR 未通过 `ruff check` 时

不要只报告失败——请尝试各类机械修复,并按以下顺序推荐有效的方案:

1. 运行 `ruff check --fix file_path.py`。如果能通过,推荐该方案——这些是 `ruff` 认为安全的修复。
2. 如果仍失败,运行 `ruff check --fix --unsafe-fixes file_path.py`。如果能通过**且**产生的 diff 确实安全(保持行为不变——要亲自审查,不要盲信),推荐该方案,并注明它需要 `--unsafe-fixes`。
3. 如果两者都无法通过,或不安全修复会改变行为,请描述剩余的规则违规,以及作者需要手工完成的修改。

始终原样引用 `ruff` 报告的规则代码(例如 `ruff rule UP047`、`ruff rule RUF100`),方便作者运行相应命令查看被标记的规则。同时,贴出你运行的具体命令。

### 3. 其他提交要求

- [ ] 至少一条记录该算法的 **Wikipedia(或同等)URL**。
- [ ] Docstring 说明了函数的功能及其参数/返回值。
- [ ] 没有不必要的第三方依赖。

### 4. 结论——固定输出格式

严格按以下标题输出,保证评审结果可比较、易于自动化:

```
### Is this an algorithm? — <yes/no + one-line why>
### Duplicate / prior-art check — <#NNNN | none found>
### Coding style — <pass | issues: …>
### Other requirements (doctests, type hints, descriptive names, Wikipedia URL) — <pass | issues: …>
### Verdict — <approve | request changes | close> + one-line reason
```

## 语气

评审要具体且友善。指出 `CONTRIBUTING.md` 中的确切规则并给出修复方案,而不是生硬拒绝——当前进度路径清晰时,首次贡献者和 Hacktoberfest 参与者更愿意回来继续改进 PR。

## 将发现映射到标签

当发现的问题匹配已有标签时,请点名相应标签,使评审与维护/清理工具保持一致:

- doctest 缺失/失败 → `require tests`
- 缺少类型注解 → `require type hints`
- 命名缺乏描述性 → `require descriptive names`
- CI 变红 → `tests are failing`
- 其余已可交由维护者处理 → `awaiting reviews`

> 🌐 本文档由 [TheAlgorithms/Python](https://github.com/TheAlgorithms/Python) 翻译,英文原版见原项目。

# 贡献指南

## 贡献之前

欢迎来到 [TheAlgorithms/Python](https://github.com/TheAlgorithms/Python)!在提交 pull request 之前,请务必**通读全部指南**。如果你对本贡献指南有任何疑问,欢迎[在 issue 中清楚地提出](https://github.com/TheAlgorithms/Python/issues/new),或在 [Gitter](https://gitter.im/TheAlgorithms/community) 社区提问。

## 如何贡献

### 贡献者

非常高兴你愿意为他人实现算法和数据结构!本仓库被世界各地的学习者参考和使用。成为贡献者即表示你同意并确认:

- 作品出自你之手——不允许抄袭。
  - 任何抄袭的作品都不会被合并。
- 你的 pull request 被合并后,作品将基于 [MIT 许可证](LICENSE.md)分发。
- 你提交的作品完全或基本符合我们的风格与标准。

**欢迎新的实现!** 例如:针对同一问题的新解法、图数据结构的不同表示方式、复杂度各异的算法设计等;但**不允许与已有实现完全相同的实现**。提交 pull request 之前,请先检查该解法是否已被实现过。

**改进注释**和**编写完善的测试**同样非常受欢迎。

### 贡献内容

我们感谢任何形式的贡献——从修正注释里的一个语法错误,到实现复杂的算法。如果你要贡献自己的作品,请阅读本节。

你的贡献将由我们的 [GitHub Actions 自动化测试](https://github.com/TheAlgorithms/Python/actions)验证,以节省大家的时间和精力。提交 pull request 之后,你会在提交页面底部看到 GitHub Actions 测试开始运行。如果测试失败,请点击 ___details___ 按钮查看 GitHub Actions 的输出以了解失败原因。如果仍不理解,可以在你的提交页面留言,社区成员会尽力提供帮助。

#### Issues

如果你有兴趣解决某个 [open issue](https://github.com/TheAlgorithms/Python/issues),直接提交带有修复方案的 pull request 即可。**本仓库不指派 issue**,因此请不要申请某个 issue 的"操作许可"。

**不要**为了贡献算法而创建 issue,请直接提交 pull request。

请在解决 open issue 的 pull request 描述中加上 `Fixes #{$ISSUE_NUMBER}`,帮助我们保持 issue 列表精简。例如,如果你的 pull request 修复了 issue #10,请在描述中加入:

```
Fixes #10
```

当 PR 被合并时,GitHub 会根据这个标记[自动关闭对应 issue](https://docs.github.com/en/issues/tracking-your-work-with-issues/linking-a-pull-request-to-an-issue)。

#### 什么是算法?

算法是一个或多个函数(或类),它应当:
* 接受一个或多个输入,
* 执行一些内部计算或数据操作,
* 返回一个或多个输出,
* 尽量减少副作用(例如 `print()`、`plot()`、`read()`、`write()`)。

算法的封装方式应便于读者把它放进更大的程序中。

算法应当:
* 使用直观的类名和函数名,让读者一眼明了其用途
* 遵循 Python 命名规范并使用直观的变量名,便于理解
* 能够灵活接受不同的输入值
* 为输入参数和返回值提供 Python 类型注解
* 对错误的输入值抛出 Python 异常(`ValueError` 等)
* 带有解释清晰的 docstring,并/或附上原始资料的 URL
* 包含同时覆盖合法输入与非法输入的 doctest
* 返回全部计算结果,而不是打印或绘图输出

本仓库中的算法不应当是"如何使用现有 Python 包"的示例教程,而应当通过内部计算或数据变换,把输入值转换为不同的输出值。计算过程可以使用现有 Python 包的数据类型、类或函数,但本仓库中的每个算法都应带来独特的价值。

#### Pre-commit 插件
使用 [pre-commit](https://pre-commit.com/#installation) 自动把代码格式化成我们的编码风格:

```bash
python3 -m pip install pre-commit  # 仅首次安装时需要
pre-commit install
```

搞定!之后每次提交变更时该插件都会自动运行。如果运行中发现错误,修复后重新提交即可。你甚至可以在所有文件上手动运行该插件:

```bash
pre-commit run --all-files --show-diff-on-failure
```

#### 编码风格

我们希望你的作品能被他人顺利阅读,因此请注意以下几点:

- 请使用现代化的 Python 3 编写代码。例如:`print()` 在 Python 3 中是函数,所以 `print "Hello"` *无法*运行,而 `print("Hello")` 可以。
- 请在函数、类和变量的命名上下足功夫。使用**描述性名称**能帮读者省去冗余注释。
  - 单字母变量名是*老派做法*,除非其生命周期只有寥寥几行,否则请避免。
  - 展开缩写,因为 `gcd()` 难以理解,而 `greatest_common_divisor()` 一目了然。
  - 请遵循 [Python 命名规范](https://pep8.org/#prescriptive-naming-conventions):变量名与函数名用 lower_case,常量用 UPPERCASE,类名用 CamelCase,等等。

- 鼓励在能让代码更易读的地方使用 Python [f-string](https://realpython.com/python-f-strings/#f-strings-a-new-and-improved-way-to-format-strings-in-python)。

- 提交 pull request 之前,请考虑对 Python 文件运行 [__ruff format__](https://docs.astral.sh/ruff/formatter/)。这还不是硬性要求,但它能让代码更易读,并自动满足 [PEP 8](https://peps.python.org/pep-0008/) 的许多要求。用法:

  ```bash
  python3 -m pip install ruff  # 仅首次安装时需要
  ruff format
  ```

- 所有提交必须先通过 `ruff check` 测试才会被接受,因此请尽量在提交 pull request 前在本地对 Python 文件运行该检查。

  ```bash
  python3 -m pip install ruff  # 仅首次安装时需要
  ruff check
  ```

- 原创代码提交需要带有描述作品的 docstring 或注释。

- 关于 docstring 与注释的更多说明:

  如果你编写算法时参考了 Wikipedia 条目或其他资料,请在 docstring 或注释中附上该 URL,方便读者查阅。

  以下写法被视为坏例子,可能会被要求改进:

  ```python
  x = x + 2  # increased by 2
  ```

  这种注释过于浅显。注释应当起解释作用。注释可以写在代码行的上方、行内或下方,只要在同一片代码中保持一致即可。

  我们鼓励在函数内编写 docstring,但请注意 docstring 的缩进。以下是一个好的示例:

  ```python
  def sum_ab(a, b):
      """
      Return the sum of two integers a and b.
      """
      return a + b
  ```

- 编写测试(尤其是 [__doctest__](https://docs.python.org/3/library/doctest.html))来说明并验证你的作品。我们强烈鼓励**为所有函数编写 doctest**。

  ```python
  def sum_ab(a, b):
      """
      Return the sum of two integers a and b
      >>> sum_ab(2, 2)
      4
      >>> sum_ab(-2, 3)
      1
      >>> sum_ab(4.9, 5.1)
      10.0
      """
      return a + b
  ```

  这些 doctest 会由 pytest 作为自动化测试的一部分运行,因此请在本地运行你的 doctest,确保它们能被发现并通过:

  ```bash
  python3 -m doctest -v my_submission.py
  ```

  不鼓励使用 Python 内置的 `input()` 函数:

  ```python
  input("Enter your input:")
  # Or even worse...
  input = eval(input("Enter your input: "))
  ```

  不过,如果你的代码确实使用了 `input()`,我们建议你通过添加 `.strip()` 妥善处理用户输入首尾的空白字符:

  ```python
  starting_value = int(input("Please enter a starting value: ").strip())
  ```

  鼓励为函数参数和返回值使用 [Python 类型注解](https://docs.python.org/3/library/typing.html)。我们的 CI 会运行 [ty](https://docs.astral.sh/ty/) 作为信息性检查(暂不阻塞合并),因此建议你在提交前先在本地运行一次。

  ```bash
  python3 -m pip install ty  # 仅首次安装时需要
  ty check my_file_path.py
  ```

  ```python
  def sum_ab(a: int, b: int) -> int:
      return a + b
  ```

  ty 的安装说明见[这里](https://docs.astral.sh/ty/installation/)。请使用命令 `ty check` 检查所有文件,或用 `ty check path/to/file.py` 检查特定文件。

- [__列表推导式与生成器__](https://docs.python.org/3/tutorial/datastructures.html#list-comprehensions)优先于 `lambda`、`map`、`filter`、`reduce`,但最重要的是用易读、易维护的代码展示 Python 的威力。

- 基础算法应避免导入外部库;只有复杂算法才使用外部库。
- 如果你需要的第三方模块尚未列在 `pyproject.toml` 中,请在提交时把它加入其中的 `dependencies`,`uv-lock` pre-commit 钩子会自动更新 `uv.lock` 使之匹配。

#### 其他提交要求
- 如果你要向 `project_euler/` 目录提交代码,请先阅读[专用指南](https://github.com/TheAlgorithms/Python/blob/master/project_euler/README.md),再为我们的 Project Euler 题库做贡献。
- 代码文件的扩展名应为 `.py`。Jupyter Notebook 请提交到 [TheAlgorithms/Jupyter](https://github.com/TheAlgorithms/Jupyter)。
- 文件名请严格使用 snake_case(下划线分隔),便于日后用脚本解析。
- 请尽量避免创建新目录,尽量把作品融入现有的目录结构。
- 如果可能,请遵循你所提交目录内部的标准。
- 如果修改/新增了代码,提交前请确保代码可以编译。
- 如果修改/新增了文档,请确保语言简洁、没有语法错误。
- 不要更新 README.md 或 DIRECTORY.md,它们会由我们的 GitHub Actions 流程定期自动生成。
- 建议在 [Algorithms-Explanation](https://github.com/TheAlgorithms/Algorithms-Explanation) 中添加对应的算法讲解(可选,但推荐)。
- 我们的 CI 会在每个 pull request 上运行 [__ty__](https://docs.astral.sh/ty/) 作为信息性检查(暂不阻塞合并),因此鼓励你在 `ty` 建议之处添加 [__Python 类型注解__](https://docs.python.org/3/library/typing.html)。

- 最重要的是:
  - __提交时请始终如一地遵循这些指南。__
  - 现在就来__加入__我们的 [Discord](https://discord.com/invite/c7MnfGFGa6) 和 [Gitter](https://gitter.im/TheAlgorithms/community)!
  - 祝编码愉快!

作者 [@poyea](https://github.com/poyea),2019 年 6 月。

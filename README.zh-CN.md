<div align="center">

# Python 中文文档

**TheAlgorithms/Python 中文翻译版 — 用 Python 实现的所有算法（教学用途）📚**

[![原项目](https://img.shields.io/badge/原项目-TheAlgorithms--Python-blue?style=flat-square&logo=github)](https://github.com/TheAlgorithms/Python)
[![GitHub Stars](https://img.shields.io/github/stars/TheAlgorithms/Python?style=flat-square&label=原项目Stars)](https://github.com/TheAlgorithms/Python/stargazers)
[![微信联系](https://img.shields.io/badge/微信-uaycar-brightgreen?style=flat-square&logo=wechat)](#)

</div>

---

> 本文档是 [TheAlgorithms/Python](https://github.com/TheAlgorithms/Python) 官方 README 的完整中文翻译，并附带中文导读说明。
> 完整源代码请访问原项目：https://github.com/TheAlgorithms/Python

**代部署 / 定制服务 / 技术咨询 请添加微信：uaycar**

---

## 项目简介

**The Algorithms - Python** 的目标是：*用 Python 实现所有算法 — 仅供教育* 📚

它是 GitHub 上星标数最高的开源算法集合之一，由全球开发者社区共同维护。项目内每个算法都以独立、可运行的 Python 脚本形式呈现，并配有源码注释，方便逐行理解算法原理。

> ⚠️ **重要提示（翻译自原文）**：这些实现仅用于学习目的。与 Python 标准库中的实现相比，它们可能效率更低，请自行斟酌使用。生产环境中应优先选择标准库（如 `sorted`、`heapq`）或 NumPy/SciPy 等成熟科学计算库。

## 主要特性

- **覆盖面广**：数十个算法专题、上千个实现文件，从基础排序到神经网络均有涉及
- **教学优先**：代码注重可读性与可理解性，每个文件聚焦一个算法
- **社区驱动**：任何人都可通过 Pull Request 贡献新算法或改进现有实现
- **质量管控**：持续集成（CI）自动测试全部代码，ruff 统一代码风格，启用 pre-commit 钩子
- **文档齐全**：原项目提供 `DIRECTORY.md` 目录索引与配套网站，便于按分类导航

## 算法分类一览（代表性专题）

原项目按目录组织算法，主要专题包括：

| 分类 | 内容示例 |
|:-----|:-----|
| sorts / searches | 冒泡排序、快速排序、希尔排序、二分查找等 |
| data_structures | 链表、栈、队列、堆、树、图、哈希表等 |
| dynamic_programming | 背包问题、最长公共子序列、编辑距离等 |
| graphs / greedy_methods | 最短路径、最小生成树、Dijkstra、Kruskal 等 |
| maths / linear_algebra | 素数、矩阵运算、数值积分、欧拉方法等 |
| machine_learning / neural_network | 感知机、KNN、朴素贝叶斯、随机森林等 |
| ciphers / hashes | 凯撒密码、维吉尼亚密码、RSA、哈希函数等 |
| computer_vision / digital_image_processing | 图像滤波、边缘检测、卷积等 |
| 其他 | 区块链、量化金融、分形、模糊逻辑、遗传算法、量子计算等 |

完整列表请查阅原项目的 [DIRECTORY.md](https://github.com/TheAlgorithms/Python/blob/master/DIRECTORY.md)。

## 快速开始

1. 安装 Git 与 Python 3（建议 3.9 及以上）。

2. 克隆原项目仓库：

```bash
git clone https://github.com/TheAlgorithms/Python.git
cd Python
```

3. 挑选任意感兴趣的算法直接运行，例如梯度下降：

```bash
python machine_learning/gradient_descent.py
```

4. 部分实现依赖第三方库，按需安装即可，例如：

```bash
pip install numpy
pip install scipy
pip install Pillow
```

5. 通过 [DIRECTORY.md](https://github.com/TheAlgorithms/Python/blob/master/DIRECTORY.md) 索引按分类浏览全部算法。

6. 建议配合阅读源码注释学习，运行结果与教材中的算法步骤一一对应。

## 参与贡献

原项目欢迎任何人贡献代码。开始之前，请先阅读其英文版[贡献指南（CONTRIBUTING.md）](https://github.com/TheAlgorithms/Python/blob/master/CONTRIBUTING.md)，注意代码风格（ruff）与测试要求。

## 社区频道

原项目在 [Discord](https://the-algorithms.com/discord) 上设有社区频道，是提问和获取帮助的好地方，欢迎加入！

## 相关项目

- [TheAlgorithms/Python](https://github.com/TheAlgorithms/Python) — 本仓库翻译的原始项目
- [The Algorithms 官网](https://the-algorithms.com/) — 支持在线浏览与搜索全部算法
- TheAlgorithms 组织下还有 C-Plus-Plus、Java、C、JavaScript 等语言的姊妹仓库

---

## 版权声明

本项目为 [TheAlgorithms/Python](https://github.com/TheAlgorithms/Python) 的中文翻译版本，仅作学习交流之用。所有算法代码的版权归原项目作者所有，遵循原项目的原始许可证（MIT License）。

**代部署 / 定制服务 / 技术咨询 请添加微信：uaycar**

**如果觉得有用，请给原项目点个 Star！** ⭐

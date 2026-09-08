> 🌐 本文档由 [TheAlgorithms/Python](https://github.com/TheAlgorithms/Python) 翻译,英文原版见原项目。

# 正态分布快速排序(Normal Distribution QuickSort)

一种快速排序算法:基准元素在数组首、尾元素之间随机选取,且数组元素取自标准正态分布。

## 数组元素

数组元素取自标准正态分布,均值 = 0,标准差 = 1。

### 代码

```python

>>> import numpy as np
>>> from tempfile import TemporaryFile
>>> outfile = TemporaryFile()
>>> p = 100 # 待排序的元素个数为 100
>>> mu, sigma = 0, 1 # 均值和标准差
>>> X = np.random.normal(mu, sigma, p)
>>> np.save(outfile, X)
>>> 'The array is'
>>> X

```

------

#### 数组元素的分布

```python
>>> mu, sigma = 0, 1 # 均值和标准差
>>> s = np.random.normal(mu, sigma, p)
>>> count, bins, ignored = plt.hist(s, 30, normed=True)
>>> plt.plot(bins , 1/(sigma * np.sqrt(2 * np.pi)) *np.exp( - (bins - mu)**2 / (2 * sigma**2) ),linewidth=2, color='r')
>>> plt.show()
```

------
![normal distribution large](https://upload.wikimedia.org/wikipedia/commons/thumb/2/25/The_Normal_Distribution.svg/1280px-The_Normal_Distribution.svg.png)

------

## 比较次数的对比

我们可以绘制函数曲线,比较正态分布快速排序与普通快速排序的"比较次数":

```python
>>> import matplotlib.pyplot as plt

    # 正态分布快速排序为红色
>>> plt.plot([1,2,4,16,32,64,128,256,512,1024,2048],[1,1,6,15,43,136,340,800,2156,6821,16325],linewidth=2, color='r')

    # 普通快速排序为绿色
>>> plt.plot([1,2,4,16,32,64,128,256,512,1024,2048],[1,1,4,16,67,122,362,949,2131,5086,12866],linewidth=2, color='g')

>>> plt.show()
```

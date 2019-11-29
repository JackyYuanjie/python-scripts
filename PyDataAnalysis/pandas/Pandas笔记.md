### pandas笔记

#### 数据结构
| 维数 | 名称      | 描述                                                  |
| ---- | --------- | ----------------------------------------------------- |
| 1    | Series    | 有标签的一维数组,是scalars的集合,也是DataFrame的元素. |
| 2    | DataFrame | 二维标签,尺寸可变的表格结构                           |

Pandas和NumPy之间的区别: 
- DataFrame.to_numpy()会给出一个比较底层的NumPy对象.
- NumPy的每一个array对象只有一种数据类型,但是Pandas的每一列的数据类型是相同的.



### 基础学习

- 导入模块:`import pandas as pd `
- 读取数据:`df = pd.read_excel()`

- 查看头部数据: `df.head()`
- 查看尾部数据: `df.tail(2)`
- 查看行数:`df.shape[0]` 或者`len(df)`
- 查看列数:`df.shape[1]`
- 查看索引: `df.index`
- 查看列名称:`df.columns`
- 查看数据的快速统计摘要:`df.describe()`
- `df.to_numpy()`的输出不包含行索引和列索引.
- 
### pandas笔记

#### 数据结构
| 维数 | 名称      | 描述                                                  |
| ---- | --------- | ----------------------------------------------------- |
| 1    | Series    | 有标签的一维数组,是scalars的集合,也是DataFrame的元素. |
| 2    | DataFrame | 二维标签,尺寸可变的表格结构                           |

Pandas和NumPy之间的区别: 
- DataFrame.to_numpy()会给出一个比较底层的NumPy对象.
- NumPy的每一个array对象只有一种数据类型,但是Pandas的每一列的数据类型是相同的.
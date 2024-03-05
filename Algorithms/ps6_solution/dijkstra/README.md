### 最短路问题，实现dijkstra算法

### 文件目录：
  * implemented_dijkstra.py - 主程序
  * dijkstra_test.py - 用于评分的测试器
  * nhpn.py - 从NHPN文件解析数据的加载器
  * priority_queue.py - 基于堆的优先队列
  * data/nhpn.lnk - 来自NHPN数据库的链路数据
  * data/nhpn.nod - 来自NHPN数据库的节点数据
  * data/{datadict, format}.txt - 数据格式描述
  * tests/* - 测试样例

### 使用方法
    python implemented_dijkstra.py < tests/{case}.in > out
    diff out tests/{case}.gold
    python dijkstra_test.py

### 实现细节
    关键在于和题目给出的数据对象进行处理方法的对齐

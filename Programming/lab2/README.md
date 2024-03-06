### 社交路径计算项目，要求通过构建社交网络来判断对象之间的最短社会联系距离

### 文件目录：
  * lab.py - 基于题目提供的接口、对各个方法的公式说明，实例化方法
  * test.py - 测试主程序
  * resources/* - 关系文件描述

### 使用方法:
  * python test.py (option)[e.g. TestBaconNumber.test_05]
  

### 实现细节：
  * 实例化多个接口
  * get_actors_with_bacon_number() - 返回所有与Bacon节点最短距离为n的演员序列。采用BFS，遍历对应深度的所有非重复叶子结点。
  * get_bacon_path() - 返回某个演员到Bacon节点的最短关系路径。采用BFS，维护队列存储搜索途中的路径，直到匹配目标节点。
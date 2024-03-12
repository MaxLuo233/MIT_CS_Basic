### 图建模问题，面向对象编程
---
### 文件目录：
  * lab.py - 基于题目提供的接口、对各个方法的公式说明，实例化方法
  * test.py - 测试主程序
  * graph.py - 图抽象类文件
  * resource/* - 输入文件

### 使用方法:
  * python test.py - 测试全部样例
  * python test.py (option)[e.g. TestQueryMedium.test_01]
  

### 实现细节：
  * 实例化多个接口
  * SimpleGraph类 - 实例化Graph抽象类，支持增删查改图标签的基础操作
  * CompactGraph类 - 实例化Graph抽象类，针对大部分节点有相同的邻居节点集合的图做存储空间上的压缩
  * GraphFactory类 - 接受Graph类作为输入，支持对Graph类批量增删数据
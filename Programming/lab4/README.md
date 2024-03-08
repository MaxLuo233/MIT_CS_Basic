### 密铺问题，给定一个含有禁区的二维图和密铺的图形形状，能否在最大空闲位的限制要求下进行密铺

### 文件目录：
  * lab.py - 基于题目提供的接口、对各个方法的公式说明，实例化方法
  * test.py - 测试主程序
  * resources/cases/* - 测试文件，包含图大小和禁区坐标

### 使用方法:
  * python test.py - 测试全部样例
  * python test.py (option)[e.g. TestPacking.test_10]
  

### 实现细节：
  * 实例化pack(), 主方法
  * pack(tent_size, missing_squares, bag_list, max_vacancy) - 图大小、禁区坐标、密铺图形形状、最大空闲坐标数作为4个参数输入
  * pack是递归方法，遍历所有密铺形状，如果形状可以放下则改变missing_squares，进行重复调用（深度优先搜索）
  * 由于有最大空闲坐标数作为限制，对于深度优先搜索出的方案还要进一步密铺,max_vacancy减一后继续迭代
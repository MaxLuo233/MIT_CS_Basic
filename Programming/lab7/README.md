### lab6查询方式升级

### 文件目录：
  * lab.py - 基于题目提供的接口、对各个方法的公式说明，实例化方法
  * test.py - 测试主程序
  * test_inputs/* - 测试文件

### 使用方法:
  * python test.py - 测试全部样例
  * python test.py (option)[e.g. Test_4_QueryCliques.test_01]
  

### 实现细节：
  * 实例化多个接口
  * FastGraph类 - 实例化Graph抽象类，优化query方法，对于clique和star的pattern查询进行特殊方法处理，快速查询优化结构
  * GraphFactory类 - 接受Graph类作为输入，支持对Graph类批量增删数据
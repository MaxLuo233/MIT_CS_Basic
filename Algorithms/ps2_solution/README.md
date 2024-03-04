### 仿真电路项目，要求是通过替换原circuit.py中用于仿真电路的数据结构，提高测试样例的仿真速度，尤其是5devadas13样例的仿真速度

### 文件目录：
  *circuit.py - 主程序，包含电路仿真器类，采用堆结构优先队列
  *tests/* - 测试样例，来自官网

### 使用方法:
  python circuit.py < tests/{case}.in > out
  diff out tests/{case}.gold #1-4要求无差错, 5要求提升时间

### 改进方式：
  python -m cProfile -s time circuit.py < tests/5devadas13.in 找到最时间开销最大的函数方法。
  开销主要在Simulation类建立的优先队列中的min()方法。line340, 保持优先队列思想，改用堆结构，min()方法复杂度O(n)-->O(1)

### 结果
  5devadas13样例仿真时间: 16629d16384 --> 16385
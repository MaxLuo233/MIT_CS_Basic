仿真电路项目，目的是通过替换原circuit.py中用于仿真电路的数据结构，提高测试样例的仿真速度，尤其是5devadas13样例的仿真速度

文件目录：
  *circuit.py - 主程序，包含电路仿真器类，采用堆结构优先队列
  *tests/* - 测试样例，来自官网

使用方法
  python circuit.py < tests/{case}.in > out
  diff out tests/{case}.gold #要求无差错
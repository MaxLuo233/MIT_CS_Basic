### 仿真电路项目升级，检查数字电路图的布线是否缠绕，要求改进circuit2.py中sweep-line算法，使得校验电线布控的时间开销显著降低。

### 文件目录：
  *modified_circuit2.py - 主程序，包含修改过的CrossVerifier类，RangeIndex类通过线路端点坐标检验判断布线是否交差，运用sweep-line算法消除缠线
  *tests/* - 测试样例，来自官网
  *circuit2/* - 题目源文件，包含没修改过的circuit2.py

### 使用方法:
  python modified_circuit2.py < tests/{case}.in > out
  diff out tests/{case}.gold #返回交叉对，要求无差错

### 改进方式：
  python -m cProfile -s time circuit2/circuit2.py < circuit2/tests/10grid_s.in 找到最时间开销最大的函数方法wire.intersects()。

  wire.intersects()调用次数过多，是主要的时间开销来源。
  原circuit2.py采用的横向扫描算法，通过维护一个存储横线坐标的RangeIndex对象，扫描到的竖线与RangeIndex对象里的所有横线坐标会冲突（缠绕），冲突的横竖线会冲突。
  
  改进RangeIndex对象，在减少维护对象所需要的增删操作的同时，减少wire.intersects()方法调用次数。

  采用AVL结构实例化RangeIndex对象。开始扫描到的所有横线左端点坐标、key(纵坐标)插入AVL树；扫描到右端点时，删除结点。扫描到竖线时，使用竖线的横坐标对AVL树做自上而下的比较搜索，依次记录冲突对。由于AVL树不会退化成链表结构，时间开销从O(n)下降到O(logn)。


### 结果
  改用AVL实现RangeIndex对象后：wire.intersects()调用次数：187590314 --> 291134；所有测试均可在60s内完成
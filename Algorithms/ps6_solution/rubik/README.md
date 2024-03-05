### 2阶魔方问题，目的是使用BFS找到复原魔方的方法

### 文件说明
  * rubik.py - 魔方的抽象
  * final_solver.py - 主程序，使用头尾BFS
  * test_solver.py - 测试文件

### 使用方法
     python test_solver.py

### 实现方法
  * 使用双向BFS，从起点和终点同时往中间搜索。
  * 在实现细节上, final_solver维护了一个双向队列，同时记录两条搜索路径的遍历状态，每次搜索会与两个状态集进行比较。

### 实现结果
    1s内完成所有测试

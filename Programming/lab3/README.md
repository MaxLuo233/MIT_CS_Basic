### 高维扫雷游戏设计

### 文件目录：
  * lab.py - 基于题目提供的接口、对各个方法的公式说明，实例化方法
  * test.py - 测试主程序
  * test_inputs/* - 测试文件，包含4个项目属性，项目设计需要维护这5个状态：
    * dimension 扫雷维度
    * board 雷区布局坐标
    * mask 当前扫雷进度
    * state 游戏状态


### 使用方法:
  * python test.py - 测试全部样例
  * python test.py (option)[e.g. TestIntegration.test_integration1] - 测试单个样例

### 实现细节：
  * 实例化多个接口
  * get_coords() - 返回单位属性
  * set_coords() - 设置单位属性，取消掉mask; 由于输入是坐标列表，该方法采用迭代处理列表
  * make_board(dimensions, elem) - 根据维度和雷区分布初始化游戏版面
  * is_in_bounds(coords) - 判断是否触雷
  * neighbors(coords) - 返回周围雷区状态
  * is_victory() - 胜利条件判断


 
### 塔防游戏开发，面向对象变成

### 文件目录：
  * lab.py - 基于题目提供的接口、对各个方法的公式说明，实例化方法
  * test.py - 测试主程序
  * resources/maps/* - 地图初始化数据
  * cases/* - 游戏参数设置

### 使用方法:
  * python test.py - 测试全部样例
  * python test.py (option)[e.g. Test_2_AnimalMovement.test_01]
  

### 实现细节：
  * 实例化多个接口
  * 四个类：
    > Games类，加载地图数据和游戏初始化设置，设置timestep()方法，定义游戏规则，按照规则更新对象状态 
    > Animals类，定义动物基本属性，正常状态更新方法，遭遇事件更新方法
    > Food类，定义塔防所用食物基本属性
    > Keeper类，定义塔防单位基本属性，抛掷食物的方法
### 图像处理，要求实例化图像处理的若干基本方法

### 文件目录：
  * lab.py - 基于题目提供的接口、对各个方法的公式说明，实例化方法
  * test_images/* - 测试样例，来自官网
  * test_results/* - 处理后的图片

### 使用方法:
  * python test.py [TestImage, TestInverted.test_inverted_images, TestFilters.test_blurred, TestFilters.test_sharpened, TestFilters.test_edges]

### 实现细节：
  * 实例化多个接口
  * load(), save(), show() - 加载、储存、显示图片
  * inverted() - 像素补码，255-c
  * blur() - 虚化
  * sharpened() - 锐化
  * edges() - 轮廓化

### 图像处理问题，找到分割线

### 文件目录：
  * final_resizeable_image.py - 主程序

### 使用方法:
  python test_resizeable_image.py

### 实现方式：
  使用动态规划，递推式为： dp[i,j] = min(dp[i,j-1],dp[i-1,j-1],dp[i+1,j-1]) + energy(i,j), (i,j)为像素坐标

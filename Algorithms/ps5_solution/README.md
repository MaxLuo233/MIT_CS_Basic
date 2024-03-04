### 解决某芯片的RSA计算效率问题，关键在于提高乘法和除法的效率，目的在于以空间换时间处理大数计算问题。

### 文件目录：
  *rsa/* 主文件
  *rsa/modified_big_num.py 主程序

### 使用方法:
  python modified_big_num.py < tests/{case}.in > out
  diff out tests/{case}.gold #返回结果，要求无差错

### 改进方式：
  找到最耗时的方法__mul__

### 结果
  
### 解决某芯片的RSA计算效率问题，关键在于提高乘法和除法的效率，目的在于以空间换时间处理大数计算问题。

### 文件目录：
  * rsa/* 主文件
  * rsa/modified_big_num.py 作业程序，修改大数乘法和除法逻辑
  * rsa/big_num_test.py 提供sanity test
  * rsa/rsa.py 主程序
  * rsa/tests 测试样例

### 使用方法:
  python rsa.py < tests/{case}.in > out
  diff out tests/{case}.gold  # 返回结果，要求无差错
  python rsa_test.py  # 所有测试样例

### 实现方式：
  RSA计算的主要开销在乘法（幂运算）和除法（模运算），为此总设计采取用空间换取时间的方法计算大数乘除法。在乘除法算法方面，选取Karasbute乘法和Newton除法进行运算，较常规运算而言复杂度从O(n^2)下降到O(n^log2(3))，n是字节数；然而RSA在调用这两个算法时常数因子较大，对于较小规模的n而言增加了负担，因此进一步改进为当n小于8时，RSA使用直接乘除法进行运算。
  【覆写__mul__方法：slow_mul()--fast_mul(); 覆写__divmod__方法：slow_divmod()--fast_divmod()】

### 结果
  __mul__，__divmod__ 方法平均运算时间下降50%以上
  
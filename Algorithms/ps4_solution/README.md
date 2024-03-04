### DNA序列相似度问题，目的是通过Hash方法来评估超长序列的相似度。
#

### 文件目录：
  *final_dnaseq.py - 实例化源文件dnaseq.py中的接口
  *dist/data* - 测试样例，来自官网
  *dnaseqlib.py* - 题目源文件，包含依赖，其中规定了Hash方法

### 使用方法:
  python final_dnaseq.py

### 实现方式与分析：
  实例化三个接口: Multidict, getExactSubmatch, intervalSubsequenceHashes。
  Multidict是一键多值字典，存储一个hash值和其对应的序列片段; 
  getExactSubmatch对切分后的片段进行匹配，对序列a进行k长度切分，对子序列计算hash值，存入Multidict一键多值字典，对b进行k长度切分并计算子序列hash值，通过hash值在字典中找到相同hash值的a的子序列片段集合，进行匹配。全量匹配时间由O(n^2)缩短至O(n*C)，C为该方法hash字典的平均长度。
  intervalSubsequenceHashes方法：新增参数m, 对a序列进行切分时只在m个子序列里计算一次hash，减少了计算hash表的时间和hash表的尺寸，但匹配结果相对于原方法而言遗失度不到10%，且k值越大遗失度越小，这说明对该hash方法能将大多数序列映射为相同的hash值，少计算hash并不会显著降低不同hash值的个数。

### 分布式文件下载器
---

### 文件目录：
  * lab.py - 基于题目提供的接口、对各个方法的公式说明，实例化方法
  * test.py - 测试主程序
  * http009.py - 基于socket类和http.client类的wrapper，返回http_response对象作为处理输入处理
  * test_files/test_file_sequence.input - 测试输入样例

### 使用方法:
  * python test.py - 测试全部样例
  * python test.py (option)[e.g. Test5_Caching.test_catsaremeanttobehappy]
  

### 实现细节：
  * 实例化多个接口
  * download_files()方法 - 根据http_response对象状态码进行结果处理，注意在重定向处迭代使用
  * manifest()方法 - 定义了缓存机制。文件源被分割成了数个URL组成的片段，由于URL会重复出现，将出现过的URL及其对应的文件下载内容置于缓存中
  * file_from_bytes()方法 - 根据状态码，将最终下载到的比特流对象转化为文字
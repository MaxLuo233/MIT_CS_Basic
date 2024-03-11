### 前缀树问题，要求构建支持多项操作的前缀树

### 文件目录：
  * lab.py - 基于题目提供的接口、对各个方法的公式说明，实例化方法
  * test.py - 测试主程序
  * 

### 使用方法:
  * python test.py - 测试全部样例
  * python test.py (option)[e.g. Test_3_Corpora.test_01_word_trie]
  

### 实现细节：
  * 实例化多个接口
  * Trie(key, value).set() - 迭代生成前缀树结构，如果是叶子结点则赋值，如果不是则children属性值为一个新Trie()
  * make_word_trie() - 没有单词就是设置频率为1，有则频率加1
  * make_phrase_trie() - 方法同make_work_trie()，改为统计短语的频率
  * autocomplete() - 给定前缀，找到前缀key对应节点的子树的所有叶子结点中频率最高的节点，返回到该节点的key
  * autocorrect() - 给定前缀，找到和前缀相似的节点中对应频率最大节点
  * word_filter() - 通配符匹配，采用迭代方式进行搜索
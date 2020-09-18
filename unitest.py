import unittest
import algorithm  # 引用一下计算程序，不然代码属实太长
import warnings
from BeautifulReport import BeautifulReport

class TestForAllTextTfIdf(unittest.TestCase):
    @classmethod
    def setUp(self):
        print("开始单元测试……")
    @classmethod
    def tearDown(self):
        print("已结束测试")

    def setUpClass():
        warnings.simplefilter('ignore', ResourceWarning)

    def test_rep_tfidf_TextSameError(self):
        print("正在载入")

    def test_add(self):
        print("正在载入orig_add.txt")
        mini = algorithm.CosineSimilarity('F:/sim_0.8/orig.txt', 'F:/sim_0.8/orig_0.8_add.txt')
        print('相似度: %.2f%%' % (mini.main() * 100))

    def test_del(self):
        print("正在载入orig_del.txt")
        mini = algorithm.CosineSimilarity('F:/sim_0.8/orig.txt', 'F:/sim_0.8/orig_0.8_del.txt')
        print('相似度: %.2f%%' % (mini.main() * 100))

    def test_dis_1(self):
        print("正在载入orig_dis_1.txt")
        mini=algorithm.CosineSimilarity('F:/sim_0.8/orig.txt', 'F:/sim_0.8/orig_0.8_dis_1.txt')
        print('相似度: %.2f%%' % (mini.main() * 100))


    def test_dis_3(self):
        print("正在载入orig_dis_3.txt")
        mini = algorithm.CosineSimilarity('F:/sim_0.8/orig.txt', 'F:/sim_0.8/orig_0.8_dis_3.txt')
        print('相似度: %.2f%%' % (mini.main() * 100))

    def test_dis_7(self):
        print("正在载入orig_dis_7.txt")
        mini = algorithm.CosineSimilarity('F:/sim_0.8/orig.txt', 'F:/sim_0.8/orig_0.8_dis_7.txt')
        print('相似度: %.2f%%' % (mini.main() * 100))

    def test_dis_10(self):
        print("正在载入orig_dis_10.txt")
        mini = algorithm.CosineSimilarity('F:/sim_0.8/orig.txt', 'F:/sim_0.8/orig_0.8_dis_10.txt')
        print('相似度: %.2f%%' % (mini.main() * 100))

    def test_dis_15(self):
        print("正在载入orig_dis_15.txt")
        mini = algorithm.CosineSimilarity('F:/sim_0.8/orig.txt', 'F:/sim_0.8/orig_0.8_dis_15.txt')
        print('相似度: %.2f%%' % (mini.main() * 100))


    def test_mix(self):
        print("正在载入orig_mix.txt")
        mini = algorithm.CosineSimilarity('F:/sim_0.8/orig.txt', 'F:/sim_0.8/orig_0.8_mix.txt')
        print('相似度: %.2f%%' % (mini.main() * 100))

    def test_rep(self):
        print("正在载入orig_rep.txt")
        mini=algorithm.CosineSimilarity('F:/sim_0.8/orig.txt', 'F:/sim_0.8/orig_0.8_rep.txt')
        print('相似度: %.2f%%' % (mini.main() * 100))


if __name__ == '__main__':
    #unittest.main()
    suite = unittest.TestSuite()
    suite.addTest(Testcase('test_add'))
    suite.addTest(Testcase('test_del'))
    suite.addTest(Testcase('test_dis_1'))
    suite.addTest(Testcase('test_dis_3'))
    suite.addTest(Testcase('test_dis_7'))
    suite.addTest(Testcase('test_dis_10'))
    suite.addTest(Testcase('test_dis_15'))
    suite.addTest(Testcase('test_mix'))
    suite.addTest(Testcase('test_rep'))
    runner = BeautifulReport(suite)
    runner.report(
        description='论文查重测试报告',  # => 报告描述
        filename='nlp_TFIDF.html',  # => 生成的报告文件名
        log_path='.'  # => 报告路径
    )

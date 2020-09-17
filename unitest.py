
import unittest
import algorithm
import warnings


class MyTestCase(unittest.TestCase):

    def setUpClass():
        warnings.simplefilter('ignore', ResourceWarning)

    def test_orig_add(self):
        print("正在载入orig_add.txt")
        mini=algorithm.CosineSimilarity('F:/sim_0.8/orig.txt', 'F:/sim_0.8/orig_0.8_add.txt')
        print('相似度: %.2f%%' % (mini.main()*100))

    def test_orig_del(self):
        print("正在载入orig_del.txt")
        mini=algorithm.CosineSimilarity('F:/sim_0.8/orig.txt', 'F:/sim_0.8/orig_0.8_del.txt')
        print('相似度: %.2f%%' % (mini.main() * 100))

    def test_orig_dis_1(self):
        print("正在载入orig_dis_1.txt")
        mini=algorithm.CosineSimilarity('F:/sim_0.8/orig.txt', 'F:/sim_0.8/orig_0.8_dis_1.txt')
        print('相似度: %.2f%%' % (mini.main() * 100))

    def test_orig_dis_3(self):
        print("正在载入orig_dis_3.txt")
        mini=algorithm.CosineSimilarity('F:/sim_0.8/orig.txt', 'F:/sim_0.8/orig_0.8_dis_3.txt')
        print('相似度: %.2f%%' % (mini.main() * 100))
    def test_orig_dis_7(self):
        print("正在载入orig_dis_7.txt")
        mini=algorithm.CosineSimilarity('F:/sim_0.8/orig.txt', 'F:/sim_0.8/orig_0.8_dis_7.txt')
        print('相似度: %.2f%%' % (mini.main() * 100))

    def test_orig_dis_10(self):
        print("正在载入orig_dis_10.txt")
        mini=algorithm.CosineSimilarity('F:/sim_0.8/orig.txt', 'F:/sim_0.8/orig_0.8_dis_10.txt')
        print('相似度: %.2f%%' % (mini.main() * 100))

    def test_orig_dis_15(self):
        print("正在载入orig_dis_15.txt")
        mini=algorithm.CosineSimilarity('F:/sim_0.8/orig.txt', 'F:/sim_0.8/orig_0.8_dis_15.txt')
        print('相似度: %.2f%%' % (mini.main() * 100))

    def test_orig_dis_mix(self):
        print("正在载入orig_dis_mix.txt")
        mini=algorithm.CosineSimilarity('F:/sim_0.8/orig.txt', 'F:/sim_0.8/orig_0.8_mix.txt')
        print('相似度: %.2f%%' % (mini.main() * 100))


    def test_orig_rep(self):
        print("正在载入orig_dis_rep.txt")
        mini=algorithm.CosineSimilarity('F:/sim_0.8/orig.txt', 'F:/sim_0.8/orig_0.8_rep.txt')
        print('相似度: %.2f%%' % (mini.main() * 100))


if __name__ == '__main__':
    #unittest.main()
    suite = unittest.TestSuite()
    suite.addTest(MyTestCase('test_orig_add'))
    suite.addTest(MyTestCase('test_orig_del'))
    suite.addTest(MyTestCase('test_orig_dis_1'))
    suite.addTest(MyTestCase('test_orig_dis_3'))
    suite.addTest(MyTestCase('test_orig_dis_7'))
    suite.addTest(MyTestCase('test_orig_dis_10'))
    suite.addTest(MyTestCase('test_orig_dis_15'))
    suite.addTest(MyTestCase('test_orig_mix'))
    suite.addTest(MyTestCase('test_orig_rep'))


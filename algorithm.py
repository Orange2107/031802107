# coding:utf-8
# 正则包
import re
# 自然语言处理包
import jieba
import jieba.analyse
import io
import sys
# 机器学习包
from sklearn.metrics.pairwise import cosine_similarity  # 计算多个量的余弦值


class CosineSimilarity(object):
    """
    余弦相似度
    """
    def __init__(self, orig_position, exam_position):
        with open(orig_position, encoding='UTF-8') as x, open(exam_position, encoding='UTF-8') as y:
            content_x = x.read()  # 从文件指针所在的位置，读到文件结尾
            content_y = y.read()
        self.s1 = content_x
        self.s2 = content_y

    @staticmethod
    def extract_keyword(content):  # 提取关键词
        # 切割
        seg = [i for i in jieba.cut(content, cut_all=True) if i != '']
        # 提取关键词
        keywords = jieba.analyse.extract_tags("|".join(seg), topK=200, withWeight=False)
        return keywords

    @staticmethod
    def one_hot(word_dict, keywords):  # oneHot编码
        # cut_code = [word_dict[word] for word in keywords]
        cut_code = [0] * len(word_dict)
        for word in keywords:
            cut_code[word_dict[word]] += 1
        return cut_code

    def main(self):
        # 去除停用词
        jieba.analyse.set_stop_words('F:/sim_0.8/stopwords.txt')

        # 提取关键词
        keywords1 = self.extract_keyword(self.s1)
        keywords2 = self.extract_keyword(self.s2)
        # 词的并集
        union = set(keywords1).union(set(keywords2))
        # 编码
        word_dict = {}
        i = 0
        for word in union:
            word_dict[word] = i
            i += 1
        # oneHot编码
        s1_cut_code = self.one_hot(word_dict, keywords1)
        s2_cut_code = self.one_hot(word_dict, keywords2)
        # 余弦相似度计算
        sample = [s1_cut_code, s2_cut_code]  # 数组中存放数组
        # 除零处理
        try:
            sim = cosine_similarity(sample)  # 求出余弦的二维数组
            return sim[1][0]
        except Exception as e:
            print(e)  # 打印出错误明细
            return 0.0


# 测试

# def  begin(orig_position,exam_position):
if __name__ == '__main__':
    similarity = CosineSimilarity(sys.argv[1], sys.argv[2])  # 对类进行赋值
    similarity = similarity.main()
    print('相似度: %.2f%%' % (similarity*100))    #输出两位小数
    print('————————————————————————')
    #z = open(r'F:\pythonProject3\output.txt', 'a', encoding='UTF-8')
    #result = str('%.2f%%\n' % (similarity * 100))
    #z.write(result)
    #z.close()

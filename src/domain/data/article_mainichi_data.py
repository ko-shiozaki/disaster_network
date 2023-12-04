
from src.domain.article.article_mainichi import ArticleMainichi

class ArticleMainichiData:
    def __init__(self):
        self.id2article_dic = {}

    def make_article(self, id, sentence_lst,pagetype):
        new_article_asahi = ArticleMainichi.initialise_from_sentence_lst(id, sentence_lst, pagetype)
        self.id2article_dic[id] = new_article_asahi

    def data2csv(self):
        # future:csvへの出力処理を書く
        print(1)

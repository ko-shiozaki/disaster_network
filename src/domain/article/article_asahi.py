import re

class ArticleAsahi:
    # note:新聞記事のクラス（一文ごとではない）
    def __init__(self,
                 id,
                 date,
                 papertype,
                 papername,
                 pagename,
                 pagetype,
                 genre,
                 wordcount,
                 title,
                 body_lst):
        self.id = id#記事ごとの固有id
        self.date = date#掲載年月日
        self.papertype = papertype#刊種
        self.papername = papername#刊誌
        self.pagename = pagename#面名
        self.pagetype = pagetype#本紙・地域面
        self.genre = genre#記事分類
        self.wordcount = wordcount#文字数
        self.title = title#見出し
        self.body_lst = body_lst#本文

    @staticmethod
    def initialise_from_sentence_lst(id, sentence_lst):
        # note:Articleクラスを作成

        #1文字以下のsentenceを削除する
        sentence_lst = [sentence for sentence in sentence_lst if len(sentence)>1]

        #記事の最初のラベル
        label_pattern = r'"([^"]*)","([^"]*)","([^"]*)","([^"]*)","([^"]*)","([^"]*)","([^"]*)","([^"]*)","([^"]*)'
        label = sentence_lst[0]
        label_match = re.match(label_pattern, label)
        # todo:全部のラベルパターンに対応させる
        if label_match:
            label_lst = label_match.groups()
            date = label_lst[0]
            papertype = label_lst[1]
            papername = label_lst[2]
            pagename = label_lst[3]
            pagetype = label_lst[4]
            genre = label_lst[5]
            wordcount = label_lst[6]
            title = label_lst[7]
            body_lst = [label_lst[8]] + sentence_lst[1:]
        else:
            label_pattern_nobody = r'"([^"]*)","([^"]*)","([^"]*)","([^"]*)","([^"]*)","([^"]*)","([^"]*)","([^"]*)'
            label_match = re.match(label_pattern_nobody, label)
            label_lst = label_match.groups()
            date = label_lst[0]
            papertype = label_lst[1]
            papername = label_lst[2]
            pagename = label_lst[3]
            pagetype = label_lst[4]
            genre = label_lst[5]
            wordcount = label_lst[6]
            title = label_lst[7]
            body_lst = sentence_lst[1:]

        new_article = ArticleAsahi(
            id = id,
            date = date,
            papertype = papertype,
            papername = papername,
            pagename = pagename,
            pagetype = pagetype,
            genre = genre,
            wordcount = wordcount,
            title = title,
            body_lst = body_lst
        )

        return new_article


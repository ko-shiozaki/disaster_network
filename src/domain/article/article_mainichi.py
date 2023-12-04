import re
import unicodedata

from src.utility.utility import Utility

class ArticleMainichi:
    # note:新聞記事のクラス（一文ごとではない）
    def __init__(self,
                 id,
                 date,
                 papertype,
                 # papername,
                 pagename,
                 pagetype,
                 # genre,
                 wordcount,
                 title,
                 body_lst):
        self.id = id  # 記事ごとの固有id
        self.date = date  # 掲載年月日
        self.papertype = papertype  # 刊種
        self.papername = "毎日新聞"  # 刊誌
        self.pagename = pagename  # 面名
        self.pagetype = pagetype  # 本紙・地域面
        self.genre = None # 記事分類
        self.wordcount = wordcount  # 文字数
        self.title = title  # 見出し
        self.body_lst = body_lst  # 本文

    @staticmethod
    def initialise_from_sentence_lst(id, sentence_lst,pagetype):
        # note:Articleクラスを作

        papertype = None

        # 記事の最初のラベル
        property_pattern = r'＼Ｓ１＼'
        body_pattern = r'＼Ｔ２＼'
        title_pattern = r'＼Ｔ１＼'
        # date_pattern = r'＼Ｃ０([^＼]+)'
        body_lst = []
        for sentence in sentence_lst:
            # date_match = re.match(date_pattern, sentence)
            property_match = re.match(property_pattern, sentence)
            body_match = re.match(body_pattern, sentence)
            title_match = re.match(title_pattern, sentence)

            if body_match:
                sentence_replaced = sentence.replace("＼Ｔ２＼　", "")
                body_lst += [sentence.strip() for sentence in sentence_replaced.split('。') if sentence.strip()]
            elif property_match:
                sentence_replaced = sentence.replace("＼Ｓ１＼　　　　", "")
                if pagetype == "地域面":
                    title_detailed_pattern = r'’([０-９]+)．([０-９]+)．([０-９]+)　地方版　([０-９]+)頁[^\d]+全([０-９]+)'
                    title_detailed_match = re.match(title_detailed_pattern, sentence_replaced)
                    if title_detailed_match:
                        year, month, day, pagename, wordcount = title_detailed_match.groups()
                        year_complemented = Utility.complement_year(year)
                        date = unicodedata.normalize("NFKD", str(year_complemented) + str(int(month)) + str(int(day)))
                        pagename = int(pagename)
                        wordcount = int(wordcount)
                else:
                    title_detailed_pattern = r'’([０-９]+)．([０-９]+)．([０-９]+)　([朝夕]刊).*　([０-９]+)頁[^\d]+全([０-９]+)'
                    title_detailed_match = re.match(title_detailed_pattern, sentence_replaced)
                    if title_detailed_match:
                        year, month, day, papertype, pagename, wordcount = title_detailed_match.groups()
                        year_complemented = Utility.complement_year(year)
                        date = unicodedata.normalize("NFKD", str(year_complemented) + str(int(month)) + str(int(day)))
                        pagename = int(pagename)
                        wordcount = int(wordcount)
            elif title_match:
                sentence_replaced = sentence.replace("＼Ｔ１＼", "")
                title = sentence_replaced
            else:
                continue

        new_article = ArticleMainichi(
            id=id,
            date=date,
            papertype=papertype,
            # papername=papername,
            pagename=pagename,
            pagetype=pagetype,
            # genre=genre,
            wordcount=wordcount,
            title=title,
            body_lst=body_lst
        )

        return new_article
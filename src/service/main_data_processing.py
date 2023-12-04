import os
import re
import glob

from src.domain.data.article_asahi_data import ArticleAsahiData
from src.domain.data.article_mainichi_data import ArticleMainichiData

class DataProcessing:
    @staticmethod
    def make_article_data_asahi(file):
        # note:朝日新聞でArticleクラスを作成する

        # txtファイルの読み込み
        with open(file, 'r', encoding='sjis') as txt_file:
            text_content = txt_file.read()

        new_article_asahi_data = ArticleAsahiData()
        # 読点か改行ごとにわける
        top_pattern = r'"(\d{8})","([朝夕]刊)"'
        sentence_lst = []
        id = 0
        first_flag = False
        for sentence in re.split(r'\n|。', text_content)[1:]:#一行目は除く
            # タイトルパターンに一致する
            if re.match(top_pattern, sentence):
                #１つ目のタイトルラベルは飛ばす
                if first_flag:
                    new_article_asahi_data.make_article(id, sentence_lst)
                    id += 1
                    sentence_lst = []
                    sentence_lst.append(sentence.strip())
                else:
                    sentence_lst.append(sentence.strip())
                    first_flag = True
            else:
                sentence_lst.append(sentence.strip())
        print(1)

    @staticmethod
    def read_file(file):
        try:
            with open(file, 'r', encoding='sjis') as f:
                for line in f:
                    yield line
        except UnicodeDecodeError:
            print("例外")


    @staticmethod
    def make_article_data_mainichi(file):
        # txtファイルの読み込み
        generator = DataProcessing.read_file(file)
        # with open(file, 'r', encoding='sjis') as txt_file:
        #     text_content = txt_file.read()

        new_article_mainichi_data = ArticleMainichiData()

        # 朝刊か否かはファイル名から判断
        if "lo" in file:
            pagetype = "地域面"
        else:
            pagetype = "本誌"

        id = 0
        first_flag = False
        top_pattern = r'＼ＩＤ＼([^＼]+)'
        sentence_lst = []
        for sentence in generator:
            sentence = sentence.strip()
            # タイトルパターンに一致する
            if re.match(top_pattern, sentence):
                # １つ目のタイトルラベルは飛ばす
                if first_flag:
                    # 著作権関係で非表示の場合はスキップする
                    if len([sentence for sentence in sentence_lst if "現在著作権交渉中の為" in  sentence])>0:
                        sentence_lst = []
                        continue
                    else:
                        new_article_mainichi_data.make_article(id, sentence_lst, pagetype)
                        id += 1
                        sentence_lst = []
                        sentence_lst = []
                else:
                    sentence_lst.append(sentence.strip())
                    first_flag = True
            else:
                sentence_lst.append(sentence.strip())
        print(1)

    @staticmethod
    def make_article_data_yomiuri():
        # todo:書く
        print(1)

    @staticmethod
    def get_filelist():
        # note:新聞名とファイルパスを取得する
        filelist_asahi = glob.glob("input/asahi/all/*.txt")
        filelist_mainichi = glob.glob("input/mainichi/all/*.txt")
        return filelist_asahi, filelist_mainichi

    @ staticmethod
    def main():
        # ファイル名一覧を取得
        # todo:ファイル名一覧を取得する処理を書く
        filelist_asahi, filelist_mainichi = DataProcessing.get_filelist()

        # Articleクラスの作成
        # 朝日新聞
        # for file in filelist_asahi:
        #     DataProcessing.make_article_data_asahi(file)
        # 毎日新聞
        for file in filelist_mainichi[7:]:
            DataProcessing.make_article_data_mainichi(file)
        # future:読売新聞

        #　出力
        # todo:出力処理を書く


if __name__ == "__main__":
    DataProcessing.main()

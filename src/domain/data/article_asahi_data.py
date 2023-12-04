import CaboCha
import csv
import os
import MeCab
import re
import sys
import sqlite3

from src.domain.article.article_asahi import ArticleAsahi

class ArticleAsahiData:
    def __init__(self):
        self.id2article_dic = {}

    def make_article(self, id, sentence_lst):
        new_article_asahi = ArticleAsahi.initialise_from_sentence_lst(id, sentence_lst)
        self.id2article_dic[id] = new_article_asahi

    def data2csv(self):
        # future:csvへの出力処理を書く
        print(1)
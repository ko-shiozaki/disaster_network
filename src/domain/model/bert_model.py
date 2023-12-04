import abc

from src.domain.sentence.sentence import Sentence
from src.domain.model.abstract_model import AbstractModel

class BertModel(AbstractModel):
    def extract_causal(self, sentence):
        # note:因果を抽出する
        pass

    def classify_causal(self, sentence):
        # note:因果関係があるか判定する
        pass

    def extract_ner(selfself, sentence):
        # note:重要用語の抽出
        pass
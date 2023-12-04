from transformers import AutoTokenizer
tokenizer = AutoTokenizer.from_pretrained("nlp-waseda/roberta-base-japanese")

from src.domain.model.abstract_model import AbstractModel

class RobertaModel(AbstractModel)
    def classify_causal(self, sentence):
        # note:因果関係があるか判定する
        return 1


    def extract_causal(self, sentence):
        # note:因果を抽出する
        pass

    def extract_ner(selfself, sentence):
        # note:重要用語の抽出
        pass
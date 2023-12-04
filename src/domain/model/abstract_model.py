
import abc

class AbstractModel:

    @abc.abstractmethod
    def classify_causal(self, sentence):
        # note:因果関係があるか判定する
        return 1

    @abc.abstractmethod
    def extract_causal(self, sentence):
        # note:因果を抽出する
        pass

    @abc.abstractmethod
    def extract_ner(selfself, sentence):
        # note:重要用語の抽出
        pass
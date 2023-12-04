

class ModelData:
    def __init__(self):
        # todo:機能でモデルをくくるか種類（bert系とかgpt系とか？）でくくるか？

        self.extract_causal_lst = []#因果関係判定系のモデル
        self.extract_ner = []#固有表現抽出系のモデル


    def initialise(self):
        # future:パターンクラスみたいなのを作ってそこからモデルを量産してここに入れるゾイ、パターンクラスに入れればいい気もするゾイ

        # self.extract_causal_lst.append()
        # self.extract_ner.append()
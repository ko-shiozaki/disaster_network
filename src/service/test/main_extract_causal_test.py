import pandas as pd
from sklearn.metrics import accuracy_score
from transformers import AutoTokenizer
tokenizer = AutoTokenizer.from_pretrained("nlp-waseda/roberta-base-japanese")
import torch
from transformers import AutoModelForSequenceClassification

from src.domain.model.bert_model import BertModel

class ExtractCausalTest:
    @staticmethod
    def preprocess_function(data):
        # note:文をトークンに変換
        texts = [q.strip() for q in data["text"]]
        inputs = tokenizer(
            texts,
            max_length=450,
            truncation=True,
            padding=True,
        )

        inputs['labels'] = torch.tensor(data['label'])

        return inputs

    @staticmethod
    def classiffier():
        num_labels = 2
        device = "cuda:0" if torch.cuda.is_available() else "cpu"
        model = AutoModelForSequenceClassification.from_pretrained("nlp-waseda/roberta-base-japanese",num_labels=num_labels).to(device)


    @staticmethod
    def main():
        # 坂平先生のアノテーションデータを引っ張ってくる
        filepath = "./input/annotation/阪神淡路大震災1カ月から6カ月_日付_for_KKE_AnnotationSample.xlsx"
        df = pd.read_excel(filepath, sheet_name="keiki", encoding="sjis")
        sentence_lst = list(df["入力データ"])
        label_lst = list(df["Y"])
        answer_lst = []

        classifier = BertModel()

        for sentence in sentence_lst:
            answer = classifier.extract(sentence)
            answer_lst.append(answer)

        print(accuracy_score(label_lst, answer_lst))

if __name__ == "__main__":
    ExtractCausalTest.main()
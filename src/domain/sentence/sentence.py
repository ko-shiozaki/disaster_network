

class Sentence:
    def __init__(self,
                 body):
        self.body = body

        self.whether_casual = None
        self.cause = None
        self.effect = None

    def judge_case(self):
        # note:因果関係があるか判定する（重要）
        if True:
            # todo:因果関係があるか判定するコード（別の判定クラスを作るのが良さそう）
            self.whether_casual = True
        else:
            self.whether_casual = False

    def make_from_text_test(self, text):
        new_sentence = Sentence(text)
        return new_sentence

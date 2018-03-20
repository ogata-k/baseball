# -*- coding: utf-8 -*-


class Field:
    def __init__(self, field_nums):
        """
        field_nums:(行数, 列数)
        """
        self.H = field_nums[0]
        self.W = field_nums[1]
        self.FIELD = [[self.W*i + j for j in range(self.W)] for i in range(self.H)]

    def print_field(self):
        """
        field描画用
        """
        for f in self.FIELD:
            print(" ".join([str(i) for i in f]))
        print()

    def specify_num(self, num):
        """
        範囲内にあるならfieldのインデックスのリスト
        範囲内にないなら空のリスト
        """

        if num >= self.H*self.W or num < 0:
            return []
        return [num // self.W, num % self.W]


PLAYERSTATUS = {0: "攻撃", 1: "防御"}
RANGEMSG = {0: "その番号で打ちます。", 1: "その番号に投げます。"}
OUTRANGEMSG = {0: "見送ります。", 1: "牽制球です。"}


class Player:
    """
    ゲーム内のプレイヤーの挙動
    """

    def __init__(self, name, field, pstatus):
        """
        name：プレイヤーの名前
        field：番号指定用フィールド
        pstatus:プレイヤーの状態 0 or 1
        """
        self.FIELD = field
        self.index = []

        self.name = name
        self.status = pstatus
        self.point = 0

    def print_player(self, numbers, names):
        """
        プレーヤーへのメッセージを表示
        """
        self.print_message()
        print("前回の入力値は{1[0]}は{0[0]}、{1[1]}は{0[1]}です。".format(numbers, names))
        self.FIELD.print_field()

    def print_message(self):
        print("{0}さんの番で{1}側{2}点です。"
              .format(self.name, PLAYERSTATUS[self.status], self.point))
        print("範囲内なら{0}範囲外なら{1}\n".format(RANGEMSG[self.status], OUTRANGEMSG[self.status]))

    def change_status(self):
        self.status = (self.status + 1) % 2

    def input_index(self):
        """
        プレイヤーに入力をさせる
        """
        self.index = self.FIELD.specify_num(get_int())

    def get_index(self):
        return self.index[:]

    def get_number(self):
        """
        Playerクラス内のindexから入力数を取得する関数
        """
        num = 3*self.index[0]+self.index[1] if self.index[:] else self.FIELD.H*self.FIELD.W
        return num


def get_int():
    """
    入力用の関数で整数を入手用
    """
    num = None
    while num is None:
        try:
            num = int(input("番号を指定してください："))
        except ValueError as ve:
            print("番号が不正です。再入力をお願いします。")

    return num

# -*- coding: utf-8 -*-


class Game:
    def __init__(self, STATUS, GAME_STATUS, init_game_counts, turn_name):
        """
        STATUS: 審判が攻守交替するときに必要な各回のデータ
        GAME_STATUS: 審判が判断するときに必要な基準データ
        init_game_counts: 初期のゲームカウント [開始番号, 名前指定用番号]
        # 名前指定番号は現仕様上01のどちらか
        turn_name: 名前指定番号に対応する名前で
        # 上の注意と同じく2つまで
        """
        # [ストライク, ボール, アウト、得点]
        self.STATUS = {0: "S", 1: "B", 2: "O", 3: "得点"}
        self.GAME_STATUS = (3, 4, 3)  # (S, B, O)の最大表示範囲
        self.game_status = []
        self.init_game_status()
        self.game_counts = init_game_counts
        self.FLIP_NAME = {i: name for i, name in enumerate(turn_name)}

    def judge(self, players):
        """
        審判
        それぞれGAME_STATUSのリスト番号に対応
        """
        p1_index, p2_index = [p.get_index() for p in players]
        if not p1_index and not p2_index:
            print("ボール！", end="")
            i = 1
        elif p1_index == p2_index:
            print("ヒット！", end="")
            i = 3
        else:
            print("ストライク！", end="")
            i = 0

        return i

    def update_game_status(self, players):
        """
        ゲームカウントの更新
        players: プレイヤーのリスト（サイズは２）
        """
        i = self.judge(players)
        s = ""

        if i==3:  # ヒット
            players[self.game_counts[1]].point += 1
            s = "攻撃側の得点です。"
            self.game_status[0:2] = [0, 0]
        else:
            self.game_status[i] += 1

            if self.game_status[0] == 3:  # スリーストライク
                s = "スリーストライクによりアウト。"
                self.game_status[0:2] = [0, 0]
                self.game_status[2] += 1
            elif self.game_status[1] == 4:  # フォアボール
                self.game_status[0:2] = [0, 0]
                players[self.game_counts[1]].point += 1
                s = "フォアボールにより攻撃側の得点です。"
        print(s)


    def update_game(self, players):
        """
        ゲーム状況の更新
        """
        if self.check_game_change():
            self.game_change(players)
            print("攻守交替")

    def game_change(self, players):
        """
        ゲームの攻守交替
        """
        game_count, flip = self.game_counts[:]
        self.game_counts[:] = [game_count + flip, (flip + 1) % 2]
        for p in players:
            p.change_status()
        self.init_game_status()

    def init_game_status(self):
        """
        ゲームカウントの初期化
        """
        self.game_status[:] = [0 for i in range(len(self.GAME_STATUS))]

    def check_game_change(self):
        """
        攻守交替するかのチェック
        """
        if self.game_status[2] == 3:
            return True
        return False

    def print_game_info(self, count):
        print("このゲームは野球を簡単にした二人対戦用のゲームです。")
        print("野球とは違い塁という概念はなく、打てば得点になります。")
        print("プレイヤー二人は攻撃側と防御側に分かれます。")
        print("攻撃側はいわゆるバッターで防御側はいわゆるピッチャーとなります。")
        print("まず各プレイヤーは番号を指定します。その後その番号における動作が行われます。")
        print("攻撃側防御側の交代条件は野球と同じで、第"+str(count)+"ゲームまで行われます。")
        print("そして勝利条件は得点が多いことです。")
        print("ルール説明はこれで終わりです。さぁ、ゲームを始めましょう。")
        print()
        input("続けるにはEnterキーを押してください...")

    def input_names(self):
        names = []
        status = ["攻撃側", "防御側"]
        print("文字化けする可能性があるので名前の入力は半角英数字でお願いします。")
        for i in range(2):
            name = input(status[i]+"の名前を入力してください:")
            names.append(name)
        print()
        return names

    def print_game_start(self):
        """
        ゲーム状況の描画
        """
        print("%d回 %s\n" % (self.game_counts[0], self.FLIP_NAME[self.game_counts[1]]))
        self.print_game_status()

    def print_game_status(self):
        """
        ゲームカウントを描画する
        """
        for i in range(3):
            s = self.STATUS[i] + "："
            s += "◎" * self.game_status[i] +"〇" * (self.GAME_STATUS[i]-self.game_status[i])
            print(s)
        print()

    def print_result(self, players):
        for p in players:
            print("{0}さん:{1:2}点".format(p.name, p.point))
        self.print_winner(players)

    def print_winner(self, players):
        s = ""
        if players[0].point == players[1].point:
            s = "同点です。"
        else:
            sort = sorted(players, key=lambda p: -p.point)
            sort = [p.name for p in sort]
            s = "{0}さんの勝利で{1}さんの敗北です。".format(*sort)
        print(s)

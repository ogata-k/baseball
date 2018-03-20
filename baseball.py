# -*- coding: utf-8 -*-
"""
Created on Sat May 27 18:12:00 2017

@author: Owner
"""

import os
import game_property as gp
import player

# ヒットやフォアボールの処理や得点の処理を追加
# 攻守交替の作成

FIELD_NUMS = (3, 3)  # (行数, 列数)

STATUS = [("S", 0), ("B", 1), ("O", 2)]  # [ストライク, ボール, アウト]
GAME_STATUS = (3, 4, 3)  # (S, B, O)の最大表示範囲

END = 4
game_counts = [1, 0]  # 1回目のturn_name
turn_name = ["表", "裏"]

g = gp.Game(STATUS, GAME_STATUS, game_counts, turn_name)
f = player.Field(FIELD_NUMS)
player_names = g.input_names()

players = [player.Player(player_names[i], f, game_counts[1]+i) for i in range(2)]
numbers = ["未入力","未入力"]

g.print_game_info(END)
while g.game_counts[0] <= END:
    for p in players:
        os.system("cls")

        g.print_game_start()
        p.print_player(numbers, player_names)
        p.input_index()
    numbers = [p.get_number() for p in players]
    os.system("cls")

    g.update_game_status(players)  # ゲーム情報の更新

    g.print_game_status()

    g.update_game(players)  # ゲームの更新

    input("続けるにはEnterキーを押してください...")

os.system("cls")
g.print_result(players)
input("Enterキーを押すと終了します。")


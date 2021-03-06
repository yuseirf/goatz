#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from pywebio.input import radio
from pywebio.output import put_text, popup

from game_app.models.tiebreak import SevenPointsTieBreak


class SixGames(object):
    def __init__(self, player1_name="Aさん", player2_name="Bさん"):
        self.player1_name = player1_name
        self.player2_name = player2_name
        self.win_player1 = "Game set and match won by " + self.player1_name + "."
        self.win_player2 = "Game set and match won by " + self.player2_name + "."

    def which_player_get_point(self, player1_count, player2_count):
        which_point = "1か2で入力して下さい："
        get_point = radio(which_point, options=[1, 2])
        if get_point == 1:
            player1_count += 1
        elif get_point == 2:
            player2_count += 1
        return player1_count, player2_count

    def to_player1_point_and_game(self, player1_count, player1_game_count):
        players_count = {1: "0", 2: "15", 3: "30", 4: "40", 5: "game"}
        player1_points = "0"
        if player1_count != 0 and player1_count % 5 == 0:
            player1_points = players_count[5]
            player1_game_count += 1
        elif player1_count != 0 and player1_count % 4 == 0:
            player1_points = players_count[4]
        elif player1_count != 0 and player1_count % 3 == 0:
            player1_points = players_count[3]
        elif player1_count != 0 and player1_count % 2 == 0:
            player1_points = players_count[2]
        elif player1_count != 0 and player1_count % 1 == 0:
            player1_points = players_count[1]
        return player1_points, player1_game_count

    def to_player2_point_and_game(self, player2_count, player2_game_count):
        players_count = {1: "0", 2: "15", 3: "30", 4: "40", 5: "game"}
        player2_points = "0"
        if player2_count != 0 and player2_count % 5 == 0:
            player2_points = players_count[5]
            player2_game_count += 1
        elif player2_count != 0 and player2_count % 4 == 0:
            player2_points = players_count[4]
        elif player2_count != 0 and player2_count % 3 == 0:
            player2_points = players_count[3]
        elif player2_count != 0 and player2_count % 2 == 0:
            player2_points = players_count[2]
        elif player2_count != 0 and player2_count % 1 == 0:
            player2_points = players_count[1]
        return player2_points, player2_game_count

    def forty_all_result(self, player1_count, player1_game_count, player2_count, player2_game_count):
        players_count = {1: "0", 2: "15", 3: "30", 4: "40", 5: "game"}
        player1_points = "0"
        player2_points = "0"
        two_players_are_fourty_all = self.player1_name + ": " + "40\n" + self.player2_name + ": " + "40"
        popup(two_players_are_fourty_all, size='large')

        while True:
            player1_count, player2_count = self.which_player_get_point(player1_count, player2_count)
            dif = abs(player1_count - player2_count)
            if dif == 2 and player1_count > player2_count:
                player1_points = players_count[5]
                player2_points = players_count[4]
                player1_game_count += 1
                player1_get_game = self.player1_name + ": " + player1_points + "\n" + self.player2_name + ": " + player2_points + "\n" + self.win_player1
                put_text(player1_get_game)
                result_of_forty_all = "finish"
                return player1_game_count, player2_game_count, result_of_forty_all
            elif dif == 2 and player1_count < player2_count:
                player1_points = players_count[4]
                player2_points = players_count[5]
                player2_game_count += 1
                player2_get_game = self.player1_name + ": " + player1_points + "\n" + self.player2_name + ": " + player2_points + "\n" + self.win_player2
                put_text(player2_get_game)
                result_of_forty_all = "finish"
                return player1_game_count, player2_game_count, result_of_forty_all
            elif player1_count == player2_count:
                player1_points = players_count[4]
                player2_points = players_count[4]
            elif player1_count > player2_count:
                player1_points = "Ad"
                player2_points = players_count[4]
            elif player1_count < player2_count:
                player1_points = players_count[4]
                player2_points = "Ad"

            result_of_points = self.player1_name + ": " + player1_points + "\n" + self.player2_name + ": " + player2_points
            popup(result_of_points, size='large')

    def players_game_result(self, player1_game_count=0, player2_game_count=0):
        player1_count = 1
        player2_count = 1
        which_player_get_point_is = "1:" + self.player1_name + "がポイントを取った\n" + "2:" + self.player2_name + "がポイントを取った"
        if player1_game_count == 0 and player2_game_count == 0:
            put_text(which_player_get_point_is)
        while True:
            # どちらのプレイヤーがポイントを取得したかを入力
            player1_count, player2_count = self.which_player_get_point(player1_count, player2_count)

            # 40-40になった場合のゲームカウントを返す
            forty_all_result = "still"
            if player1_count % 4 == 0 and player2_count % 4 == 0:
                player1_game_count, player2_game_count, forty_all_result = self.forty_all_result(player1_count,
                                                                                                 player1_game_count,
                                                                                                 player2_count,
                                                                                                 player2_game_count)
            if forty_all_result == "finish":
                return player1_game_count, player2_game_count

            # 入力に応じたプレイヤーのポイントとゲームを取得する
            player1_points, player1_game_count = self.to_player1_point_and_game(player1_count, player1_game_count)
            player2_points, player2_game_count = self.to_player2_point_and_game(player2_count, player2_game_count)

            # プレイヤーのゲームカウントを返す
            if player1_count >= 5:
                player1_get_game = self.player1_name + ": " + player1_points + "\n" + self.player2_name + ": " + player2_points + "\ngame " + self.player1_name
                popup(player1_get_game, size='large')
                return player1_game_count, player2_game_count
            elif player2_count >= 5:
                player2_get_game = self.player1_name + ": " + player1_points + "\n" + self.player2_name + ": " + player2_points + "\ngame " + self.player2_name
                popup(player2_get_game, size='large')
                return player1_game_count, player2_game_count

            # プレイヤー1と2の現在のポイント状況を出力する
            result_of_points = self.player1_name + ": " + player1_points + "\n" + self.player2_name + ": " + player2_points
            popup(result_of_points, size='large')

    def five_games_all_and_tiebreak_result(self, player1_game_count, player2_game_count, result_of_tiebreak):
        tiebreak = SevenPointsTieBreak(self.player1_name, self.player2_name)
        player1_tiebreak_point = 0
        player2_tiebreak_point = 0

        while True:
            if player1_game_count == 6 and player2_game_count == 6:
                start_tiebreak_match = "\n6 game all, Tie-Break\n"
                popup(start_tiebreak_match, size='large')
                player1_tiebreak_point, player2_tiebreak_point = tiebreak.run_seven_points_tie_break()
                result_of_tiebreak = "finish"
                return player1_game_count, player2_game_count, player1_tiebreak_point, player2_tiebreak_point, result_of_tiebreak
            # タイブレークに突入しなくてもタイブレークポイントを0で返す。
            elif player1_game_count == 7:
                result_of_set_match = "【Games】\n" + self.player1_name + ": " + str(player1_game_count) + "\n" + \
                                      self.player2_name + ": " + str(player2_game_count) + "\n" + self.win_player1
                put_text(result_of_set_match)
                return player1_game_count, player2_game_count, player1_tiebreak_point, player2_tiebreak_point, result_of_tiebreak
            elif player2_game_count == 7:
                result_of_set_match = "【Games】\n" + self.player1_name + ": " + str(player1_game_count) + "\n" + \
                                      self.player2_name + ": " + str(player2_game_count) + "\n" + self.win_player2
                put_text(result_of_set_match)
                return player1_game_count, player2_game_count, player1_tiebreak_point, player2_tiebreak_point, result_of_tiebreak

            result_of_set_match = "【Games】\n" + self.player1_name + ": " + str(player1_game_count) + "\n" \
                                  + self.player2_name + ": " + str(player2_game_count)
            popup(result_of_set_match, size='large')
            player1_game_count, player2_game_count = self.players_game_result(player1_game_count, player2_game_count)

    def which_player_won_tiebreak_match_is_output(self, player1_tiebreak_point, player2_tiebreak_point):
        if player1_tiebreak_point > player2_tiebreak_point:
            player1_win_tiebreak_match = "【Tie-break】\n" + self.player1_name + ": 7" + "\n" + self.player2_name +\
                                         ": 6(" + str(player2_tiebreak_point) + ")\n" + self.win_player1
            put_text(player1_win_tiebreak_match)
        elif player1_tiebreak_point < player2_tiebreak_point:
            player2_win_tiebreak_match = "【Tie-break】\n" + self.player1_name + ": 6(" + str(player1_tiebreak_point) + \
                                         ")\n" + self.player2_name + ": 7\n" + self.win_player2
            put_text(player2_win_tiebreak_match)

    def run_six_games_match(self):
        player1_game_count = 0
        player2_game_count = 0
        player1_tiebreak_point = 0
        player2_tiebreak_point = 0

        while True:
            result_of_tiebreak = "still"
            if (player1_game_count != 0 and player1_game_count % 5 == 0) and (
                    player2_game_count != 0 and player2_game_count % 5 == 0):
                player1_game_count, player2_game_count, \
                player1_tiebreak_point, player2_tiebreak_point, \
                result_of_tiebreak = self.five_games_all_and_tiebreak_result(player1_game_count,
                                                                             player2_game_count,
                                                                             result_of_tiebreak)

            if result_of_tiebreak == "finish":
                # タイブレーク結果を出力
                self.which_player_won_tiebreak_match_is_output(player1_tiebreak_point, player2_tiebreak_point)
                break
            elif player1_game_count == 7 or player2_game_count == 7:
                break

            if player1_game_count != 0 and player1_game_count % 6 == 0:
                player1_win_set_match = self.player1_name + ": " + str(player1_game_count) + "\n" \
                                        + self.player2_name + ": " + str(player2_game_count) + "\n" + self.win_player1
                put_text(player1_win_set_match)
                break
            elif player2_game_count != 0 and player2_game_count % 6 == 0:
                player2_win_set_match = self.player1_name + ": " + str(player1_game_count) + "\n" \
                                        + self.player2_name + ": " + str(player2_game_count) + "\n" + self.win_player2
                put_text(player2_win_set_match)
                break

            result_of_set_match = "【Games】\n" + self.player1_name + ": " + str(player1_game_count) + "\n" \
                                  + self.player2_name + ": " + str(player2_game_count)
            popup(result_of_set_match, size='large')
            player1_game_count, player2_game_count = self.players_game_result(player1_game_count, player2_game_count)
        return player1_game_count, player2_game_count, player1_tiebreak_point, player2_tiebreak_point
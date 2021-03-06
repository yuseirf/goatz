#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from pywebio.input import radio
from pywebio.output import put_text, popup


class SevenPointsTieBreak(object):
    def __init__(self, player1_name="Aさん", player2_name="Bさん"):
        self.player1_name = player1_name
        self.player2_name = player2_name
        self.win_player1 = "Game set and match won by " + self.player1_name + "."
        self.win_player2 = "Game set and match won by " + self.player2_name + "."

    def which_player_point_acquired_is(self, count_player1=0, count_player2=0):
        which_point = "1か2で入力して下さい："
        get_point = radio(which_point, options=[1, 2])
        if get_point == 1:
            count_player1 += 1
        elif get_point == 2:
            count_player2 += 1
        return count_player1, count_player2

    def run_seven_points_tie_break(self):
        count_player1 = 0
        count_player2 = 0
        which_player_get_point_is = "1:" + self.player1_name + "がポイントを取った\n" + "2:" + self.player2_name + "がポイントを取った"
        put_text(which_player_get_point_is)
        while True:
            count_player1, count_player2 = self.which_player_point_acquired_is(count_player1, count_player2)
            point_of_two_players = "【Tie-break】\n" + self.player1_name + ": " + str(count_player1) \
                                   + "\n" + self.player2_name + ": " + str(count_player2)
            popup(point_of_two_players, size='large')

            dif = abs(count_player1 - count_player2)
            if dif == 2 and (count_player1 >= 8 or count_player2 >= 8):
                player1_tiebreak_point = count_player1
                player2_tiebreak_point = count_player2
                return player1_tiebreak_point, player2_tiebreak_point
            elif (count_player1 == 7 or count_player2 == 7) and (count_player1 < 6 or count_player2 < 6):
                player1_tiebreak_point = count_player1
                player2_tiebreak_point = count_player2
                return player1_tiebreak_point, player2_tiebreak_point

    def seven_points_tie_break_result(self):
        player1_tiebreak_point, player2_tiebreak_point = self.run_seven_points_tie_break()

        if player1_tiebreak_point > player2_tiebreak_point:
            player1_win_tiebreak_match = "【Tie-break】\n" + self.player1_name + ": " + str(player1_tiebreak_point) \
                                         + "\n" + self.player2_name + ": " + str(player2_tiebreak_point) + "\n" \
                                         + self.win_player1
            put_text(player1_win_tiebreak_match)
        elif player1_tiebreak_point < player2_tiebreak_point:
            player2_win_tiebreak_match = "【Tie-break】\n" + self.player1_name + ": " + str(player1_tiebreak_point) \
                                         + "\n" + self.player2_name + ": " + str(player2_tiebreak_point) + "\n" \
                                         + self.win_player2
            put_text(player2_win_tiebreak_match)


class TenPointsTieBreak(SevenPointsTieBreak):
    def __init__(self, player1_name="Aさん", player2_name="Bさん"):
        super().__init__(player1_name, player2_name)
        self.win_player1 = "Game set and match won by " + self.player1_name + "."
        self.win_player2 = "Game set and match won by " + self.player2_name + "."

    def run_ten_points_tie_break(self):
        count_player1 = 0
        count_player2 = 0
        while True:
            count_player1, count_player2 = self.which_player_point_acquired_is(count_player1, count_player2)
            point_of_two_players = "【Tie-break】\n" + self.player1_name + ": " + str(count_player1) \
                                   + "\n" + self.player2_name + ": " + str(count_player2)
            popup(point_of_two_players, size='large')

            dif = abs(count_player1 - count_player2)
            if dif == 2 and (count_player1 >= 11 or count_player2 >= 11):
                player1_tiebreak_point = count_player1
                player2_tiebreak_point = count_player2
                return player1_tiebreak_point, player2_tiebreak_point
            elif (count_player1 == 10 or count_player2 == 10) and (count_player1 < 9 or count_player2 < 9):
                player1_tiebreak_point = count_player1
                player2_tiebreak_point = count_player2
                return player1_tiebreak_point, player2_tiebreak_point

    def ten_points_tie_break_result(self):
        player1_tiebreak_point, player2_tiebreak_point = self.run_ten_points_tie_break()

        if player1_tiebreak_point > player2_tiebreak_point:
            player1_win_tiebreak_match = "【Tie-break】\n" + self.player1_name + ": " + str(player1_tiebreak_point) \
                                         + "\n" + self.player2_name + ": " + str(player2_tiebreak_point) + "\n" \
                                         + self.win_player1
            put_text(player1_win_tiebreak_match)
        elif player1_tiebreak_point < player2_tiebreak_point:
            player2_win_tiebreak_match = "【Tie-break】\n" + self.player1_name + ": " + str(player1_tiebreak_point) \
                                         + "\n" + self.player2_name + ": " + str(player2_tiebreak_point) + "\n" \
                                         + self.win_player2
            put_text(player2_win_tiebreak_match)

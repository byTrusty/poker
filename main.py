import unittest

cards = ('S2','S3','S4','S5','S6','S7','S8','S9','S10','SJ','SQ','SK','SA')

def check_straight(card1, card2, card3):
    card_values = [int(card[1:]) for card in [card1, card2, card3]]
    card_values.sort()
    if card_values == [2, 3, 4] or card_values == [3, 4, 5] or card_values == [4, 5, 6] or card_values == [5, 6, 7] or card_values == [6, 7, 8] or card_values == [7, 8, 9] or card_values == [8, 9, 10] or card_values == [9, 10, 11] or card_values == [10, 11, 12] or card_values == [11, 12, 13] or card_values == [12, 13, 14]:
        return max(card_values)
    else:
        return 0

def check_3ofa_kind(card1, card2, card3):
    card_values = [int(card[1:]) for card in [card1, card2, card3]]
    if card_values.count(card_values[0]) == 3:
        return card_values[0]
    else:
        return 0

def check_royal_flush(card1, card2, card3):
    if check_straight(card1, card2, card3) == 14:
        return 14
    else:
        return 0

def play_cards(left1, left2, left3, right1, right2, right3):
    left_cards = [left1, left2, left3]
    right_cards = [right1, right2, right3]

    left_cards.sort(key=lambda x: int(x[1:]))
    right_cards.sort(key=lambda x: int(x[1:]))

    left_straight = check_straight(*left_cards)
    right_straight = check_straight(*right_cards)

    left_3ofakind = check_3ofa_kind(*left_cards)
    right_3ofakind = check_3ofa_kind(*right_cards)

    left_royal_flush = check_royal_flush(*left_cards)
    right_royal_flush = check_royal_flush(*right_cards)

    if left_royal_flush > right_royal_flush:
        return -1
    elif right_royal_flush > left_royal_flush:
        return 1
    elif left_3ofakind > right_3ofakind:
        return -1
    elif right_3ofakind > left_3ofakind:
        return 1
    elif left_straight > right_straight:
        return -1
    elif right_straight > left_straight:
        return 1
    else:
        return 0


class TestPokerFunctions(unittest.TestCase):

    def test_check_straight(self):
        self.assertEqual(check_straight('S5', 'S6', 'S7'), 7)
        self.assertEqual(check_straight('S6', 'S5', 'S7'), 7)
        self.assertEqual(check_straight('S3', 'SQ', 'SK'), 0)
        self.assertEqual(check_straight('S2', 'S3', 'S4'), 4)
        self.assertEqual(check_straight('S10', 'SJ', 'SQ'), 0)
        self.assertEqual(check_straight('SA', 'SK', 'SJ'), 14)

    def test_check_3ofa_kind(self):
        self.assertEqual(check_3ofa_kind('S9', 'S9', 'S9'), 9)
        self.assertEqual(check_3ofa_kind('S2', 'S4', 'S2'), 0)
        self.assertEqual(check_3ofa_kind('S7', 'S7', 'SK'), 0)
        self.assertEqual(check_3ofa_kind('SJ', 'SJ', 'SJ'), 11)
        self.assertEqual(check_3ofa_kind('SA', 'SK', 'SJ'), 0)

    def test_check_royal_flush(self):
        self.assertEqual(check_royal_flush('S10', 'SJ', 'SQ'), 0)
        self.assertEqual(check_royal_flush('SA', 'SK', 'SQ'), 0)
        self.assertEqual(check_royal_flush('SA', 'SK', 'SJ'), 0)
        self.assertEqual(check_royal_flush('SA', 'SK', 'SJ', 'SQ', 'S10', 'S9'), 14)
        self.assertEqual(check_royal_flush('SA', 'SK', 'SJ', 'SQ', 'S10', 'C9'), 0)

    def test_play_cards(self):
        self.assertEqual(play_cards('S5', 'S6', 'S7', 'S8', 'S9', 'S10'), -1)
        self.assertEqual(play_cards('SA', 'SK', 'SJ', 'SQ', 'S10', 'S9'), 1)
        self.assertEqual(play_cards('S5', 'S6', 'S7', 'S7', 'S7', 'S10'), 1)
        self.assertEqual(play_cards('S5', 'S6', 'S7', 'S7', 'S7', 'S10'), 1)
        self.assertEqual(play_cards('SA', 'SK', 'SJ', 'SQ', 'S10', 'C9'), 0)


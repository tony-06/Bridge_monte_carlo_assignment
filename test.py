import unittest

import card_funcs


# noinspection SpellCheckingInspection
class MyTestCase(unittest.TestCase):
    def test_void(self):
        void_hand = card_funcs.pydealer.stack.Stack()
        for i in range(13):
            void_hand.add(card_funcs.pydealer.Card("2", "spades"))
        void_test_score = card_funcs.get_score(void_hand)
        self.assertEqual(void_test_score, 15)  # a hand with all 2 of spades should return 15 points for 3 voids

    def test_singleton(self):
        singleton_hand = card_funcs.pydealer.stack.Stack()
        for j in range(12):
            singleton_hand.add(card_funcs.pydealer.Card("2", "spades"))
        singleton_hand.add(card_funcs.pydealer.Card("2", "hearts"))
        singleton_test_score = card_funcs.get_score(singleton_hand)
        self.assertEqual(singleton_test_score, 12)  # 2 voids and one singleton is 12 points

    def test_doubleton(self):
        doubleton_hand = card_funcs.pydealer.stack.Stack()
        for k in range(11):
            doubleton_hand.add(card_funcs.pydealer.Card("2", "spades"))
        doubleton_hand.add(card_funcs.pydealer.Card("2", "hearts"))
        doubleton_hand.add(card_funcs.pydealer.Card("2", "hearts"))
        doubleton_test_score = card_funcs.get_score(doubleton_hand)
        self.assertEqual(doubleton_test_score, 11)  # 2 voids and one doubleton is 11 points


if __name__ == '__main__':
    unittest.main()

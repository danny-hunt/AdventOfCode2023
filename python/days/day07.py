from dataclasses import dataclass
from utils.timing import timer
from utils.parsing import input_data
from functools import lru_cache, cmp_to_key
from collections import Counter


@dataclass
class Hand:
    cards: str
    bid: int


@lru_cache(maxsize=None)
def compare_cards(card_1: str, card_2: str, part: int) -> int:
    if part == 1:
        sorted_cards = ['2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', "A"]
    elif part == 2:
        sorted_cards = ['J', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'Q', 'K', "A"]
    card_1_val = sorted_cards.index(card_1)
    card_2_val = sorted_cards.index(card_2)
    if card_1_val > card_2_val:
        return 1
    elif card_2_val > card_1_val:
        return -1
    else:
        # Shouldn't be hit
        return 0


def compare_hand_labels(hand_1: Hand, hand_2: Hand, part: int) -> int:
    for card_1, card_2 in zip(hand_1.cards, hand_2.cards):
        result = compare_cards(card_1, card_2, part)
        if result != 0:
            return result
    raise Exception("Tie shouldn't be possible")


def compare_hand_types(hand_1: Hand, hand_2: Hand, part: int) -> int:
    hand_1_cards = Counter(hand_1.cards)
    hand_2_cards = Counter(hand_2.cards)
    if part == 2:
        hand_1_jacks = hand_1_cards.pop('J') if 'J' in hand_1_cards else 0
        hand_2_jacks = hand_2_cards.pop('J') if 'J' in hand_2_cards else 0
    hand_1_card_counts = sorted(hand_1_cards.values(), reverse=True) or [0]
    hand_2_card_counts = sorted(hand_2_cards.values(), reverse=True) or [0]
    if part == 2:
        hand_1_card_counts[0] += hand_1_jacks
        hand_2_card_counts[0] += hand_2_jacks
    for count_1, count_2 in zip(hand_1_card_counts, hand_2_card_counts):
        if count_1 > count_2:
            return 1
        elif count_2 > count_1:
            return -1
    return compare_hand_labels(hand_1, hand_2, part)


def parser(input: str) -> Hand:
    cards, bid = input.split()
    return Hand(cards, int(bid))


@lru_cache(maxsize=None)
@timer(7)
def part_one():
    input = input_data(7, parser)
    input.sort(key=cmp_to_key(lambda x, y: compare_hand_types(x,y,1)))
    total = 0
    for i, hand in enumerate(input):
        # if hand.bid // 30 == 0:
        # print(hand.cards)
        total += hand.bid * (i + 1)
    return total
    

@timer(7)
def part_two():
    input = input_data(7, parser)
    input.sort(key=cmp_to_key(lambda x, y: compare_hand_types(x,y,2)))
    total = 0
    for i, hand in enumerate(input):
        # if hand.bid // 30 == 0:
        # print(hand.cards)
        total += hand.bid * (i + 1)
    return total

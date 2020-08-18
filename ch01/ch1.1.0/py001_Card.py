import collections
from random import choice

Card = collections.namedtuple('Card', ['rank', 'suit'])


class FrenchDeck:
    ranks = [str(n) for n in range(2, 11)] + list('JQKA')
    suits = 'spades diamonds clubs hearts'.split()

    def __init__(self):
        # 两个for的时候，注意顺序
        self._cards = [Card(rank, suit) for suit in self.suits
                       for rank in self.ranks]

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, position):
        return self._cards[position]


if __name__ == '__main__':
    deck = FrenchDeck()
    print(len(deck))

    print(deck[0])
    print(deck[1])

    print(choice(deck))
    print(choice(deck))
    print(choice(deck))

    # 因为__getitem__方法把[]交给了列表，所以，支持切片
    print(deck[:3])
    print(deck[12::13])

    # 只要实现了__getitem__方法，就是可迭代的了
    for card in deck:
        print(card)

    print('=' * 30)
    # 反向迭代也可以
    for card in reversed(deck):
        print(card)

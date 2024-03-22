# 시간 초과
# 해답: https://tolerblanc.github.io/programmers/programmers-nplueone-cardgame/

from collections import deque

def solution(coin, cards):
    answer = 1
    
    N = len(cards)
    hand = cards[:N // 3]
    deck = deque(cards[N // 3:])
    pending = set()
    
    def check(deck1, deck2):
        for card in deck1:
            if N + 1 - card in deck2:
                deck1.remove(card)
                deck2.remove(N + 1 - card)
                return True
        return False
    
    while deck:
        pending.add(deck.popleft())
        pending.add(deck.popleft())
        
        if check(hand, hand):
            pass
        elif coin > 0 and check(hand, pending):
            coin -= 1
        elif coin > 1 and check(pending, pending):
            coin -= 2
        else:
            break
        
        answer += 1
    
    return answer
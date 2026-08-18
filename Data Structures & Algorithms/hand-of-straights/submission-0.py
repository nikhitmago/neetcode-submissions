from collections import Counter

class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        '''
        [1,2,2,3,3,4,4,5], group_size = 4

        counter = {
            1:0,
            2:1,
            3:1,
            4:1,
            5:1,
        }


        '''

        hand.sort()
        counter = Counter(hand)
        
        for card in hand:
            if counter[card]:
                for i in range(card, card + groupSize):
                    if counter.get(i, 0) == 0:
                        return False
                    counter[i] -= 1
        return True
class Solution:
    def recoverOrder(self, order: List[int], friends: List[int]) -> List[int]:

        OrderAray = []
        for I in range(len(order)):
            print("Outer")
            for J in range(len(friends)):
                if order[I] == friends[J]:
                    OrderAray.append(order[I])
        return OrderAray

        

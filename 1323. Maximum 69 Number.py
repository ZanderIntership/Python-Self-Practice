class Solution:
    def maximum69Number (self, num: int) -> int:
        DummyNum = str(num)
        BrandNewString = DummyNum
        found = False
        for i in range(0,len(DummyNum)):
            if DummyNum[i] == "6" and found == False:
                BrandNewString = DummyNum[:i] + '9' + DummyNum[i + 1:]
                found = True
                break

        num = int(BrandNewString)
        return num

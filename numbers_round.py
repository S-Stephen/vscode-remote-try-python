import itertools

class NumbersRound:
    numbers = [] # six numbers
    target = -1

    def __init__(self, numbers, target):
        self.numbers = numbers
        self.target = target
        
    def numberPerms(self):
        return list(itertools.permutations(self.numbers))

    def _add(self,total,value):
        return total+value

    def _subtractFromTotal(self,total,value):
        return total-value
    
    def _subtractTotalFrom(self,total,value):
        return value-total

    def _divideNRByValue(self,numbersRound,value):
        """
        Divide those that produce whole numbers
        """
        return self._filterNonzeros([x/value if x%value ==0 else 0 for x in numbersRound._totals()])

    def _divideValueByNR(self,numbersRound,value):
        """
        Divide those that produce whole numbers
        """
        return self._filterNonzeros([value/x if x%value ==0 else 0  for x in numbersRound._totals()])

    def _multiplyNR(self,numbersRound,value):
        return [x*value for x in numbersRound._totals()]

    def _filterNonzeros(self,mylist):
        return filter(lambda value: value!=0, mylist)

    def _operators(self):
        """
        The signitures for these functions should be the same
        (so that we can loop through them)
        """
        return [
            self._divideValueByNR,
            self._divideNRByValue,
            self._add,
            self._subtractFromTotal,
            self._subtractTotalFrom,
            self._multiplyNR
        ]

    def _totals(self,numbersRound):
        """
        returns a list of all the possible values 
        """
        ## foreach of the values apply each operator to it and the remaining numbersRound



        self._operators()

if __name__ == '__main__':
    # new numbers round
    numbersRound = NumbersRound([1,2,8,10,25,50],180)
    #print(myArr)
    print(numbersRound.numberPerms())
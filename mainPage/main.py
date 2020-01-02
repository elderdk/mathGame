from random import randrange

class newNumber:
    """
    newSet = newNumber([100, 100], ['+', '-'])
    """

    def __init__(self, arr, allowedOperators, negativeAnswerAllowed = False, canExceedTen = True):
        if arr == [] or len(arr[0]) == 0:
            self.arr = [[1, 10], [1, 10]]
        else:
            splitNums = arr[0].split(';')
            returnArr = [];
            for i in splitNums:
                n = i.replace('(', '').replace(')', '').split(',')
                returnArr.append(n)
            self.arr = returnArr
        if allowedOperators == []:
            self.allowedOperators = ['+']
        else:
            self.allowedOperators = allowedOperators;

        self.negativeAnswerAllowed = negativeAnswerAllowed;
        self.canExceedTen = canExceedTen;

    def getOp(self):
        op = self.allowedOperators
        return op[randrange(len(op))]

    def nums(self):
        nums = self.arr
        returnArr = [];
        for i in nums:
            returnArr.append(randrange(int(i[0]), int(i[1])))
        return returnArr

    def equation(self):
        nums = self.nums()
        equation = ''
        count = 1;
        for i in nums:
            
            if count == len(nums):
                equation = equation + str(i)
            else:
                equation = equation + str(i) + ' ' + self.getOp() + ' '
            count += 1
            
        return equation
    
    def is_valid(self, answer):
        if self.negativeAnswerAllowed == False and answer < 0:
            return False
        if self.canExceedTen == False and answer > 10:
            return False
        return True

    def finalEquation(self):
        while True:
            equation = self.equation()
            answer = eval(equation)
            if self.is_valid(answer):
                eq = equation.split(' ')
                eq.append(str(answer))
                if len(eq) > 2:
                    return eq
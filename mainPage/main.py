import random

class newNumber:
    """
    newSet = newNumber([100, 100], ['+', '-'])
    """

    def __init__(self, arr, allowedOperators, negativeAnswerAllowed = False):
        
        # get the numbers
        splitNums = arr[0].split(';')
        returnArr = [];
        for i in splitNums:
            n = i.replace('(', '').replace(')', '').split(',')
            returnArr.append(n)
        self.arr = returnArr

        if allowedOperators == []:
            self.allowedOperators = ['+']
        else:
            self.allowedOperators = []
            l = allowedOperators
            for i in l[0]:
                self.allowedOperators.append(i)

        self.negativeAnswerAllowed = negativeAnswerAllowed;

    def getOp(self):
        op = self.allowedOperators
        return op[random.randrange(len(op))]

    def nums(self):
        nums = self.arr
        returnArr = [];
        for i in nums:
            returnArr.append(random.randrange(int(i[0]), int(i[1])))
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
    
    def is_valid(self, answer, is_bonus, is_skull):
        if self.negativeAnswerAllowed == False and answer < 0:
                return False
        if is_bonus and is_skull:
                return False
        return True

    def is_bonus(self):
        if random.random() < 0.08:  #Current bonus pop-up rate is 8%
            return True
        else:
            return False

    def is_skull(self):
        if random.random() < 0.04:  #Current bonus pop-up rate is 8%
            return True
        else:
            return False

    def finalEquation(self):
        eq = {}
        while True:
            equation = self.equation()
            answer = eval(equation)
            is_bonus = self.is_bonus()
            is_skull = self.is_skull()
            if self.is_valid(answer, is_bonus, is_skull):
                eq = {  
                        'equation': equation.split(' '), 
                        'answer': answer, 
                        'is_bonus': is_bonus, 
                        'is_skull': is_skull
                    }
                return eq
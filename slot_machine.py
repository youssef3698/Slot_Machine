import random
 
class SlotMachine:
    def __init__(self):
        self.wheel_1 = ['A','A','A','A','B','B','B','C','C','D']
        self.wheel_2 = ['A','A','A','A','B','B','B','C','C','D']
        self.wheel_3 = ['A','A','A','A','B','B','B','C','C','D']

    def roll(self):
        self.row_1 = [self.wheel_1.pop(random.randrange(len(self.wheel_1))), self.wheel_2.pop(random.randrange(len(self.wheel_2))), self.wheel_3.pop(random.randrange(len(self.wheel_3)))]
        self.row_2 = [self.wheel_1.pop(random.randrange(len(self.wheel_1))), self.wheel_2.pop(random.randrange(len(self.wheel_2))), self.wheel_3.pop(random.randrange(len(self.wheel_3)))]
        self.row_3 = [self.wheel_1.pop(random.randrange(len(self.wheel_1))), self.wheel_2.pop(random.randrange(len(self.wheel_2))), self.wheel_3.pop(random.randrange(len(self.wheel_3)))]
        print(self.row_1[0] + " | " + self.row_1[1] + " | " + self.row_1[2])
        print(self.row_2[0] + " | " + self.row_2[1] + " | " + self.row_2[2])
        print(self.row_3[0] + " | " + self.row_3[1] + " | " + self.row_3[2])

    def check_wins(self, lines, mult_2, mult_3, bet):
        duplicates_1 = len(self.row_1) - len(set(self.row_1)) + 1
        duplicates_2 = len(self.row_2) - len(set(self.row_2)) + 1
        duplicates_3 = len(self.row_3) - len(set(self.row_3)) + 1
        
        if duplicates_1 == 1:
            result_1 = 0
        elif duplicates_1 == 2:
            result_1 = mult_2 * bet
        else:
            result_1 = mult_3 * bet
        
        if duplicates_2 == 1:
            result_2 = 0
        elif duplicates_2 == 2:
            result_2 = mult_2 * bet
        else:
            result_2 = mult_3 * bet
        
        if duplicates_3 == 1:
            result_3 = 0
        elif duplicates_3 == 2:
            result_3 = mult_2 * bet
        else:
            result_3 = mult_3 * bet
            
        if lines == 1:
            total = result_1
        elif lines == 2:
            total = result_1 + result_2
        else:
            total = result_1 + result_2 + result_3
            
        return total
        
        
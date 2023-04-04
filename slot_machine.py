import random

MULT_2 = 1.2
MULT_3 = 1.5
MULT_A = 1.0
MULT_B = 1.5
MULT_C = 2.0
MULT_D = 3.0

class SlotMachine():
    def __init__(self):
        self.wheel_1 = ['A','A','A','A','B','B','B','C','C','D']
        self.wheel_2 = ['A','A','A','A','B','B','B','C','C','D']
        self.wheel_3 = ['A','A','A','A','B','B','B','C','C','D']
        
    def roll(self):
        self.row_1 = [self.wheel_1.pop(random.randrange(len(self.wheel_1))), self.wheel_2.pop(random.randrange(len(self.wheel_2))), self.wheel_3.pop(random.randrange(len(self.wheel_3)))]
        self.row_2 = [self.wheel_1.pop(random.randrange(len(self.wheel_1))), self.wheel_2.pop(random.randrange(len(self.wheel_2))), self.wheel_3.pop(random.randrange(len(self.wheel_3)))]
        self.row_3 = [self.wheel_1.pop(random.randrange(len(self.wheel_1))), self.wheel_2.pop(random.randrange(len(self.wheel_2))), self.wheel_3.pop(random.randrange(len(self.wheel_3)))]
        
        print(self.row_1[0], ' | ',self.row_1[1], ' | ',self.row_1[2])
        print(self.row_2[0], ' | ',self.row_2[1], ' | ',self.row_2[2])
        print(self.row_3[0], ' | ',self.row_3[1], ' | ',self.row_3[2])
        
    def count_items(self):
        dict_1 = {i:self.row_1.count(i) for i in self.row_1}
        dict_2 = {i:self.row_2.count(i) for i in self.row_2}
        dict_3 = {i:self.row_3.count(i) for i in self.row_3}
        
        for k,v in dict_1.items():
            if v == max(dict_1.values()):
                symbol_1 = k
                dup_1 = v
        
        for k,v in dict_2.items():
            if v == max(dict_2.values()):
                symbol_2 = k
                dup_2 = v
                
        for k,v in dict_3.items():
            if v == max(dict_3.values()):
                symbol_3 = k
                dup_3 = v
        
        
        return [symbol_1, dup_1], [symbol_2, dup_2], [symbol_3, dup_3]
    
    def check_wins(self, lines, bet):
        mult = 0
        
        for i in range(lines):
            mult += self.get_mult(self.count_items()[i])
            
        wins = mult * bet
            
        return wins
            
    def get_mult(self, li):
        if li[0] == "A":
            m_s = MULT_A
        elif li[0] == "B":
            m_s = MULT_B
        elif li[0] == "C":
            m_s = MULT_C
        elif li[0] == "D":
            m_s = MULT_D 
        else:
            print("Wrong symbol was printed")
        
        if li[1] == 1:
            m_d = 0
        elif li[1] == 2:
            m_d = MULT_2
        elif li[1] == 3:
            m_d = MULT_3
        else:
            print("The symbol count is wrong")
            
        if m_d == 0:
            m_t = 1
        else:
            m_t = m_s * m_d
            
        return m_t

players = [['amy',100],['david',100],['heraldo',50],['aakansha',75],['aleska',150]]


from functools import cmp_to_key
class Player:
    def __init__(self, name, score):
        self.name = name
        self.score = score        
        
    def comparator(a, b):
        if a.score<b.score:
            return 1
        if a.score>b.score:
            return -1
        if a.score==b.score:
            return 0
        if a.name<b.name:
            return -1
        return 1





import math
data = [['A1', 28], ['A2', 32], ['A3', 1], ['A4', 0],
        ['A5', 10], ['A6', 22], ['A7', 30], ['A8', 19],
		['B1', 145], ['B2', 27], ['B3', 36], ['B4', 25],
		['B5', 9], ['B6', 38], ['B7', 21], ['B8', 12],
		['C1', 122], ['C2', 87], ['C3', 36], ['C4', 3],
		['D1', 0], ['D2', 5], ['D3', 55], ['D4', 62],
		['D5', 98], ['D6', 32]]

def average():
    sum = 0
    for i in range(len(data)):
        sum = sum + int(data[i][1])
    
    return math.ceil(sum/len(data)) 

def C_elements():
    for i in range(len(data)):
        for x in range(1,5):
            if data[i][0] == 'C'+str(x):
                print(data[i][1])
        
        
C_elements()
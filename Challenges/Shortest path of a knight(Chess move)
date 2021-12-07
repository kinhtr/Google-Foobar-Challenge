#The challenge is to write a function to calculate the shortest moves 
#that a piece of knight need to travel from any starting positions to any destinations in a 8x8 chess board
def constraint(position, move):
    c1 = [0,8,16,24,32,40,48,56]
    c2 = [1,9,17,25,33,41,49,57]
    c7 = [6,14,22,30,38,46,54,62]
    c8 = [7,15,23,31,39,47,55,63]
    
    if position in c1 and move in [6,15,-10,-17]:
        return False
    elif position in c2 and move in [6,-10]:
        return False
    elif position in c7 and move in [10,-6]:
        return False
    elif position in c8 and move in [10,17,-6,-15]:
        return False
    return True

def solution(src, dest):
    l = [6,-10,10,-6,17,-17,15,-15]
    count = 0
    positions = []
    tmp = []
    tmp.append(src)
    arrived = False
    while not arrived and src != dest:
        count += 1
        positions = tmp
        tmp = []
        for p in positions:
            for i in l:
                if p + i in range(1,64) and constraint(p,i):
                    if p + i == dest:
                        arrived = True   
                        break
                    else:
                        tmp.append(p+i)
            if arrived:
                break
    return count

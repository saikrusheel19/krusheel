import re
pos = [10,10]
init_direct = 'N'
flag = True
a = []

def turn_left():
    if init_direct == 'N':
        return 'W'
    elif init_direct == 'W':
        return 'S'
    elif init_direct == 'S':
        return 'E'
    elif init_direct == 'E':
        return 'N'
        
def turn_right():
    if init_direct == 'N':
        return 'E'
    elif init_direct == 'W':
        return 'N'
    elif init_direct == 'S':
        return 'W'
    elif init_direct == 'E':
        return 'S'
        
def move_pos(pos):
    if init_direct == 'N':
        pos[1] = pos[1] + 1
        return pos
    elif init_direct == 'E':
        pos[0] = pos[0] + 1
        return pos
    elif init_direct == 'W':
        pos[0] = pos[0] - 1
        return pos
    elif init_direct == 'S':
        pos[1] = pos[1] - 1
        return pos
    
def bound_check():
    if pos[0] not in range(0,21) or pos[1] not in range(0,21):
        print("Game Over")
        flag = False
        return flag
        
def input_valid():  
    var = re.compile('[^LMR]')
    match  = re.finditer(var,n)
    for mat in match:
        a.append(mat)
        return len(a)
n = input("Enter the direction:").upper()
input_valid()
if len(a) == 0:
    for elem in n:
        if elem == 'L':
            init_direct = turn_left()
            print("L:",init_direct)
        elif elem == 'R':
            init_direct = turn_right()
            print("R:",init_direct)
        elif elem == 'M':
            pos = move_pos(pos)
            print("posi:",pos)
        if bound_check() == False:
            break
    if flag == True:
        print('\n',init_direct)
        print(' '.join(str(elem) for elem in pos), end = "")
else:
    print("Invalid input")

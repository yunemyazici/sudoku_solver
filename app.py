import timeit
possible_values = {}



groups = [[1,1], [4,1], [7,1], [1,4], [4,4], [7,4], [1,7], [4,7], [7,7]]


#returns the location of the center of the group
def find_the_group(index):
    if index in [0,1,2,9,10,11,18,19,20]:
        return [1,1]
    elif index in [3,4,5,12,13,14,21,22,23]:
        return [1,4]
    elif index in [6,7,8,15,16,17,24,25,26]:
        return [1,7]
    elif index in [27,28,29,36,37,38,45,46,47]:
        return [4,1]
    elif index in [30,31,32,39,40,41,48,49,50]:
        return [4,4]
    elif index in [33,34,35,42,43,44,51,52,53]:
        return [4,7]
    elif index in [54,55,56,63,64,65,72,73,74]:
        return [7,1]
    elif index in [57,58,59,66,67,68,75,76,77]:
        return [7,4]
    elif index in [60,61,62,69,70,71,78,79,80]:
        return [7,7]                   



#assigning possible values to each empty cell
def assign_values():    
    for i in range(81):
        row = i // 9
        col = i % 9
        if game[row][col] == None:
            possible_values[i] = calculate_values(i)


#calculating that possible values
def calculate_values(number):
    horizontal_values = []
    possible_horizontal_values = []
    vertical_values = []
    possible_vertical_values = []
    group_values = []
    possible_group_values = []
    return_values = []
    row = number // 9
    col = number % 9
    group = find_the_group(number)
    for index in range(9):
        if game[row][index] != None:
            horizontal_values.append(game[row][index])
        if game[index][col] != None:
            vertical_values.append(game[index][col])
    for r in range(group[0]-1,(group[0]+1)+1):#bazı yerlerde burada sorun çıkıyor
        for c in range(group[1]-1, (group[1]+1)+1):
            if game[r][c] != None:
                group_values.append(game[r][c])

    for i in range(1,10):
        if i not in horizontal_values:
            possible_horizontal_values.append(i)
        if i not in vertical_values:
            possible_vertical_values.append(i)
        if i not in group_values:
            possible_group_values.append(i)

    for i in min(possible_vertical_values,possible_horizontal_values,possible_group_values):
        if i in possible_vertical_values and i in possible_horizontal_values and i in possible_group_values:
            return_values.append(i)

    return return_values         

#solving the sudoku
def check_if_one_in_group(group):
    values_in_the_group = {} #possible values of each empty cell
    changed = "no"
    for r in range(group[0]-1,(group[0]+1)+1):
        for c in range(group[1]-1, (group[1]+1)+1):
            if game[r][c] == None:
                index = r*9 + c
                values_in_the_group[index] = possible_values[index]
    for i in values_in_the_group:
        for j in values_in_the_group[i]:
            value = 0
            for k in values_in_the_group:
                for l in values_in_the_group[k]:
                    if l == j:
                        value += 1
            row = i // 9
            col = i % 9
            if value == 1:
                game[row][col] = j 
                changed = "yes"
                continue
    return changed



#game board
game = [[1,3,None,6,8,5,None,None,None],
        [None,None,None,None,None,None,None,None,2],
        [None,6,None,None,1,9,None,3,8],
        [None,None,1,None,None,None,None,4,None],
        [None,5,None,4,None,3,None,None,None],
        [3,None,None,8,None,None,None,None,6],
        [4,2,7,5,6,None,9,None,None],
        [None,None,5,None,None,2,None,8,None],
        [None,8,None,None,None,7,None,None,None]]





#main function
def sudoku_solver():
    start = timeit.default_timer()
    gameRunning = True
    while gameRunning:
        count = 0
        assign_values()
        for group in groups:
            control = check_if_one_in_group(group)
            if control == "yes":
                break
        for i in range(len(game)):
            for j in range(9):
                if game[i][j] == None:
                    count += 1
        for g in game:
            print(g)            
        if count == 0:
            gameRunning = False

    for g in game:
        print(g)


    stop = timeit.default_timer()

    print('Time: ', stop - start)


if __name__ == "__main__":
    sudoku_solver()


    #the algorithm is not efficient at all. as i have seen, it takes too much time to solve the harder sudokus than easy ones.  and i have not seen whether the program
#is able to solve the harder sudokus. even if it is able to solve them, it doesn't matter.

#i have to make this algortihm much more efficient

import random

def plantMine():
    for i in range(10):
        mRow = random.randint(0,9)
        mColl = random.randint(0,9)
        while mines[mRow][mColl] == "X":
            mRow = random.randint(0,9)
            mColl = random.randint(0,9)
        mines[mRow][mColl] = "X"
    for j in range(10):
        for y in range(10):
            if mines[j][y] != "X":
                count = 0
                for p in range(-1,2):
                    for l in range(-1,2):
                        if (j+p >= 0 and j+p < 10) and (y+l >= 0 and y+l < 10):
                            try:
                                if mines[j+p][y+l] == "X":
                                    count += 1
                            except:
                                continue
                mines[j][y] = str(count)




def printBoard(board):
    print('  ********************')
    print('  A B C D E F G H I J')
    row_num=0
    for row in board:
        print("%d|%s|" % (row_num, "|".join(row)))
        row_num +=1

def adj(r, c):
    if pBoard[r][c] == " " and mines[r][c] != "X":
        pBoard[r][c] = mines[r][c]
        if mines[r][c] == "0":
            for i in range(-1, 2):
                for j in range(-1, 2):
                    if i == 0 and j == 0:
                        continue
                    try:
                        if pBoard[r + i][c + j] == " ":
                            adj(r + i, c + j)
                    except IndexError:
                        continue

def isWon():
    spaceCount = 0
    for i in range(10):
        for j in range(10):
            if pBoard[i][j] == " ":
                spaceCount += 1
            if spaceCount > 10:
                return False
    return True
                
        
def main():
    global nums
    nums = {"A":0,"B":1,"C":2,"D":3,"E":4,"F":5,"G":6,"H":7,"I":8,"J":9}
    mineHit = False
    global pBoard
    pBoard=[[' ']*10 for x in range(10)]
    global mines
    mines = [['0']*10 for x in range(10)]
    plantMine()
    printBoard(mines)
    while not mineHit:
        printBoard(pBoard)
        r = input("Enter a row(0-9): ")
        while r not in ['0','1','2','3','4','5','6','7','8','9']:
            r=input("Please enter a number 1-9: ")
        c = input("Enter a column(A-J): ").upper()
        while c not in nums:
            c=input("Please enter a letter A-J: ").upper()
        #guessed = True
        #while guessed: #implemet later prints you alr know a ton of times(needs to ask r, c again instead)
            #if pBoard[int(r)][nums[c]] != " ":
                #print("You already know this spot")
            #else:
                #guessed = False
        if mines[int(r)][nums[c]] == "X":
            print("Boom! You hit a mine")
            print("You lose")
            mineHit = True
        else:
            adj(int(r),nums[c])
        if isWon():
            print("Congratulations, you won!")
            mineHit = True
    printBoard(mines)


if __name__ == "__main__":
    main()
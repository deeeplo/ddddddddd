import random

def plantMine(board):
    for i in range(10):
        mRow = random.randint(0,9)
        mColl = random.randint(0,9)
        while board[mRow][mColl] == "X":
            mRow = random.randint(0,9)
            mColl = random.randint(0,9)
        board[mRow][mColl] = "X"
    for j in range(10):
        for y in range(10):
            if mines[j][y] != "X":
                for p in range(-1,2):
                    for l in range(-1,2):
                        m = 0
                        try:
                            if mines[j+p][y+l] == "X":
                                m = int((mines[j][y]))
                                print(m)
                                m +=1
                                mines[j][y] = str(m)
                        except:
                            continue




def printBoard(board):
    print('  ********************')
    print('  A B C D E F G H I J')
    row_num=0
    for row in board:
        print("%d|%s|" % (row_num, "|".join(row)))
        row_num +=1

def adj(r, c):
    pass#implement this

def main():
    global nums
    nums = {"A":0,"B":1,"C":2,"D":3,"E":4,"F":5,"G":6,"H":7,"I":8,"J":9}
    #8x8 blank 2d array
    mineHit = False
    global pBoard
    pBoard=[[' ']*10 for x in range(10)]
    global mines
    mines = [['0']*10 for x in range(10)]
    plantMine(mines)
    printBoard(mines)
    while not mineHit:
        printBoard(pBoard)
        r = input("Enter a row(1-9): ")
        while r not in ['0','1','2','3','4','5','6','7','8','9']:
            r=input("Please enter a number 1-9: ")
        c = input("Enter a column(A-J): ").upper()
        while c not in nums:
            c=input("Please enter a letter A-J: ").upper()
        if pBoard[int(r)][nums[c]] != " ":
            print("You already guessed this square")
        elif mines[int(r)][nums[c]] == "X":
            print("Boom! You hit a mine")
            print("You lose")
            mineHit = True
        else:
            adj(int(r),nums[c])

if __name__ == "__main__":
    main()
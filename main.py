def display(L):
    print(" {} || {} || {}".format(L[0],L[1],L[2]))
    print("------------")
    print(" {} || {} || {}".format(L[3],L[4],L[5]))
    print("------------")
    print(" {} || {} || {}".format(L[6],L[7],L[8]))
def ChkO(L,position):
    L[position-1] = 'O'
def ChkX(L,position):
    L[position-1] = 'X'
def Play():
    print("enter")
    player1 = int(input("Enter your choice: 'O' or 'X' 1 or 2?"))
    if player1 == 1:
        player1 = 'O'
        player2 = 'X'
    else:
        player1 = 'X'
        player2 = 'O'
    L = [1,2,3,4,5,6,7,8,9]
    i = True
    for p in range(9):
        print('-'*60)
        display(L)
        print('-'*60)
        if L[0] == L[1] == L[2] or L[0] == L[4] == L[8] or L[0] == L[3] == L[6] or L[1] == L[4] == L[7] or L[2] == L[4] == L[6] or L[2] == L[5] == L[8] or L[3] == L[4] == L[5] or L[6] == L[7] == L[8]:
            if not i:
                print("Winner is Player 1.. Congratulations")
            else:
                print("Winner is Player 2.. Congratulations")
            break
        if p == 9:
            print("Draw break")
            break
        if i:
            print("Player 1")
            position = int(input("Enter position: "))
            if player1 == 'X':
                ChkX(L,position)
            else:
                ChkO(L,position)
            i = False
        else:
            print("Player 2")
            position = int(input("Enter position: "))
            if player2 == 'X':
                ChkX(L,position)
            else:
                ChkO(L,position)
            i = True
    else:
        print("Match Drawn!!")
k = 0
while True:
    if k == 0:
        print("Dou you want to start the game? ")
        ans = input()
        if ans == "yes":
            k = 1
            Play()
        else:
            break
    else:
        print("Do you want to play again: ")
        ans = input()
        if ans == "yes":
            Play()
        else:
            print("Thankyou!")
            break

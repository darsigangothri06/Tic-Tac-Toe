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
player1 = int(input("Enter your choice: 'O' or 'X' 1 or 2?"))
if player1 == 1:
    player1 = 'O'
    player2 = 'X'
else:
    player1 = 'X'
    player2 = 'O'
L = [1,2,3,4,5,6,7,8,9]
i = True
j = 0
while True:
    j += 1
    print('-'*60)
    display(L)
    print('-'*60)
    if L[0] == L[1] == L[2] or L[0] == L[4] == L[8] or L[0] == L[3] == L[6] or L[1] == L[4] == L[7] or L[2] == L[4] == L[6] or L[2] == L[5] == L[8] or L[3] == L[4] == L[5] or L[6] == L[7] == L[8]:
        print("Done winner")
        break
    if j == 9:
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

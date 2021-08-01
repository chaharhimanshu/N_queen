from random import choice


#METHOD FOR PRINTING THE BOARD
def printBoard(result, param):
    # If the results list is empty (eg hc can return an empty list)
    if not result:
        print([None])
    # If you get results and --all = 0
    if param == 0 and result:
        r = choice(result)
        # print r
        board = []
        for col in r:
            line = ['.'] * len(r)
            line[col] = 'Q'
            board.append(str().join(line))

        charlist = map(list, board)
        for line in charlist:
            print (" ".join(line))
    # If you get results and --all = 1
    else:
        # print result
        board = []
        for r in result:
            for c in r:
                line = ['.'] * len(r)
                line[c] = 'Q'
                board.append(str().join(line))

        charlist = map(list, board)
        for i in range(0, len(charlist)):
            if i % len(charlist[i]) == 0:
                print ("\n")

            print(" ".join(charlist[i]))
    print ("\n")

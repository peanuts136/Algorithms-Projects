from pam120script import parseTable, pam120Score


def smithWaterman(x,y,gapPenalty, scoreFunction):
    m= len(x)
    n= len(y)
    x=x.upper()
    y=y.upper()
    dp = [[0]*(n+1) for _ in range(m+1)]
    tracebackTable = [[None]*(n+1) for _ in range(m+1)]

    maxScoreEncountered = 0
    maxScorePosition = (0,0)

    dp[0][0] = 0 #the first row and column should be all init to 0
    for i in range(1,m+1):
        dp[i][0] = 0
    for j in range(1, n+1):
        dp[0][j] = 0
    

    for i in range(1,m+1):
        for j in range(1,n+1):
            diagonalScore = dp[i-1][j-1] + scoreFunction(x[i-1],y[j-1]) #-1 to account for array indexing
            upScore = dp[i-1][j] - gapPenalty
            leftScore = dp[i][j-1] - gapPenalty
            

            #Defaults to no movement 
            bestScore = 0
            bestDirection = None

            if diagonalScore > bestScore:
                bestScore = diagonalScore
                bestDirection = "diag"
            
            if upScore > bestScore:
                bestScore = upScore
                bestDirection = "up"
            
            if leftScore > bestScore:
                bestScore = leftScore
                bestDirection = "left"
            dp[i][j] = bestScore
            tracebackTable[i][j] = bestDirection

            #Checks if this score is the current maximum
            if bestScore > maxScoreEncountered:
                maxScoreEncountered = bestScore
                maxScorePosition = (i,j)
    
    alignedX = []
    alignedY = []     
    i, j = maxScorePosition

    while i > 0 and j > 0 and dp[i][j] != 0:
        direction = tracebackTable[i][j]
        if direction == "diag":
            alignedX.append(x[i-1])
            alignedY.append(y[j-1])
            i-=1
            j-=1
        elif direction == "up":
            alignedX.append(x[i-1])
            alignedY.append('-')
            i-=1
        elif direction == "left":
            alignedX.append('-')
            alignedY.append(y[j-1])
            j-=1
        else:
            #direction is None 
            break
    alignedX.reverse()
    alignedY.reverse()

    return ''.join(alignedX).lower(), ''.join(alignedY).lower(), maxScoreEncountered

if __name__ =="__main__":
    table = """
    3  0 -3  0  0 -4  1 -3 -1 -2 -3 -2 -1  1 -1 -3  1  1  0 -7 -1 -4 -1 -8
    0  4 -6  4  3 -5  0  1 -3  0 -4 -4  3 -2  0 -2  0  0 -3 -6 -1 -3  2 -8
    -3 -6  9 -7 -7 -6 -4 -4 -3 -7 -7 -6 -5 -4 -7 -4  0 -3 -3 -8 -4 -1 -7 -8
    0  4 -7  5  3 -7  0  0 -3 -1 -5 -4  2 -3  1 -3  0 -1 -3 -8 -2 -5  3 -8
    0  3 -7  3  5 -7 -1 -1 -3 -1 -4 -3  1 -2  2 -3 -1 -2 -3 -8 -1 -5  4 -8
    -4 -5 -6 -7 -7  8 -5 -3  0 -7  0 -1 -4 -5 -6 -5 -3 -4 -3 -1 -3  4 -6 -8
    1  0 -4  0 -1 -5  5 -4 -4 -3 -5 -4  0 -2 -3 -4  1 -1 -2 -8 -2 -6 -2 -8
    -3  1 -4  0 -1 -3 -4  7 -4 -2 -3 -4  2 -1  3  1 -2 -3 -3 -3 -2 -1  1 -8
    -1 -3 -3 -3 -3  0 -4 -4  6 -3  1  1 -2 -3 -3 -2 -2  0  3 -6 -1 -2 -3 -8
    -2  0 -7 -1 -1 -7 -3 -2 -3  5 -4  0  1 -2  0  2 -1 -1 -4 -5 -2 -5 -1 -8
    -3 -4 -7 -5 -4  0 -5 -3  1 -4  5  3 -4 -3 -2 -4 -4 -3  1 -3 -2 -2 -3 -8
    -2 -4 -6 -4 -3 -1 -4 -4  1  0  3  8 -3 -3 -1 -1 -2 -1  1 -6 -2 -4 -2 -8
    -1  3 -5  2  1 -4  0  2 -2  1 -4 -3  4 -2  0 -1  1  0 -3 -4 -1 -2  0 -8
    1 -2 -4 -3 -2 -5 -2 -1 -3 -2 -3 -3 -2  6  0 -1  1 -1 -2 -7 -2 -6 -1 -8
    -1  0 -7  1  2 -6 -3  3 -3  0 -2 -1  0  0  6  1 -2 -2 -3 -6 -1 -5  4 -8
    -3 -2 -4 -3 -3 -5 -4  1 -2  2 -4 -1 -1 -1  1  6 -1 -2 -3  1 -2 -5 -1 -8
    1  0  0  0 -1 -3  1 -2 -2 -1 -4 -2  1  1 -2 -1  3  2 -2 -2 -1 -3 -1 -8
    1  0 -3 -1 -2 -4 -1 -3  0 -1 -3 -1  0 -1 -2 -2  2  4  0 -6 -1 -3 -2 -8
    0 -3 -3 -3 -3 -3 -2 -3  3 -4  1  1 -3 -2 -3 -3 -2  0  5 -8 -1 -3 -3 -8
    -7 -6 -8 -8 -8 -1 -8 -3 -6 -5 -3 -6 -4 -7 -6  1 -2 -6 -8 12 -5 -2 -7 -8
    -1 -1 -4 -2 -1 -3 -2 -2 -1 -2 -2 -2 -1 -2 -1 -2 -1 -1 -1 -5 -2 -3 -1 -8
    -4 -3 -1 -5 -5  4 -6 -1 -2 -5 -2 -4 -2 -6 -5 -5 -3 -3 -3 -2 -3  8 -5 -8
    -1  2 -7  3  4 -6 -2  1 -3 -1 -3 -2  0 -1  4 -1 -1 -2 -3 -7 -1 -5  4 -8
    -8 -8 -8 -8 -8 -8 -8 -8 -8 -8 -8 -8 -8 -8 -8 -8 -8 -8 -8 -8 -8 -8 -8  1
    """

    labels = ["A","B","C","D","E","F","G","H","I","K","L","M","N","P","Q","R","S","T","V","W","X","Y","Z","*"]

    scoring_matrix = parseTable(labels, table)
    inputFile = "C:\\Users\heton\\3500 HonorsProjects\\Project2\\input.txt"
    
    with open(inputFile, "r") as file:

        inputLines = file.read().strip().split('\n')
        if len(inputLines) < 2:
            print("Not enough sequences")
            exit(1)
        if len(inputLines) > 2:
            print("Too many sequences")
            exit(1)
        sequenceX=inputLines[0].strip() #removes whitespace
        sequenceY=inputLines[1].strip()

        gapPenalty = 5
    
    
    alignedX, alignedY, score = smithWaterman(sequenceX,sequenceY,gapPenalty,pam120Score)
    outputFile = "output.txt"
    with open(outputFile, "w") as file:
        file.write("Alignment sequence: \n")
        file.write(alignedX + "\n")
        file.write(alignedY + "\n")
        file.write("Score: " + str(score) + "\n")

    print("Alignment successful")

        
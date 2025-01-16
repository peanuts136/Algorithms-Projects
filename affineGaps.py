from pam120script import parseTable, pam120Score

def affineGlobalAlignment(x,y,scoreFunction, A,B):
    #The formula is A+B*(L-1)
    #A=Gap opening cost
    #B is gap extension cost
    #L = length of gap
    m = len(x)
    n = len(y)
    x=x.upper()
    y=y.upper()

    #Makes sure A and B are positive
    if A < 0:
        A =  -A
    if B < 0:
        B = -B
    
    M = [[float('-inf')] * (n+1) for _ in range(m+1)] #For standard no gap
    X = [[float('-inf')] * (n+1) for _ in range(m+1)] #For when at position i in X, there is gap in y
    Y = [[float('-inf')] * (n+1) for _ in range(m+1)] #For when at position j in Y, there is gap in X

    traceBackM = [[float('-inf')] * (n+1) for _ in range(m+1)]
    traceBackX = [[float('-inf')] * (n+1) for _ in range(m+1)]
    traceBackY = [[float('-inf')] * (n+1) for _ in range(m+1)]

    #initialization

    M[0][0] = 0
    for i in range(1, m):
        #A + B*L
        X[i][0] = -(A +(i-1)*B) 
        traceBackX[i][0] = "X"
    for j in range(1,n):
        Y[0][j] = -(A+(j-1)*B)
        traceBackY[0][j] = "Y"
    
    #Recurrence formulas
    #M[i][j] = max(
    #           M[i-1][j-1] + score,
    #           X[i-1][j-1] + score,
    #           Y[i-1][j-1] + score,
    #X[i][j] = max(
    #           M[i-1][j] - (A+B),
    #           X[i-1][j] - B
    #Y[i][j] = max(
    #           M[i][j-1] - (A+B),
    #           Y[i-1][j] - B
    for i in range(1,m+1):
        for j in range(1,n+1):
            score = scoreFunction(x[i-1],y[j-1])

            MCandidates = [(M[i-1][j-1]+score, "M"), 
                           (X[i-1][j-1]+score, "X"), 
                           (Y[i-1][j-1]+score, "Y")]
            M[i][j], traceBackM[i][j] = max(MCandidates, key=lambda c: c[0])

            XCandidates = [(M[i-1][j] - (A+B), "M"),
                           (X[i-1][j] - B, "X")]
            X[i][j], traceBackX[i][j] = max(XCandidates, key=lambda c: c[0])
            YCandidates = [(M[i][j-1] - (A+B), "M"),
                           (Y[i][j-1] - B, "Y")]
            Y[i][j], traceBackY[i][j] = max(YCandidates, key=lambda c: c[0])
    
    #Need to find the best score and which matrix contains that best score
    finalMaxScores = [(M[m][n], "M"),
                     (X[m][n], "X"),
                      (Y[m][n], "Y") ]
    bestScore, bestFinalMatrix = max(finalMaxScores, key=lambda c: c[0]) 

    alignedX=[]
    alignedY=[]

    i,j = m,n
    currentMatrix = bestFinalMatrix

    while i>0 or j>0:
    
        if currentMatrix == "M":
            currentMatrix = traceBackM[i][j]
            alignedX.append(x[i-1])
            alignedY.append(y[j-1])

            i-=1
            j-=1

        elif currentMatrix =="X":
            currentMatrix = traceBackX[i][j]
            alignedX.append(x[i-1])
            alignedY.append("-")
            i-=1

        elif currentMatrix == "Y":
            currentMatrix = traceBackY[i][j]
            alignedX.append("-")
            alignedY.append(y[j-1])
            j-=1
        else:
            break

    alignedX.reverse()
    alignedY.reverse()

    return ''.join(alignedX).lower(), ''.join(alignedY).lower(), bestScore



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

    
    A= 2
    B = 2
    
    alignedX, alignedY, score = affineGlobalAlignment(sequenceX,sequenceY,pam120Score,A,B)
    outputFile = "output.txt"
    with open(outputFile, "w") as file:
        file.write("Affline Gap -> Inputted sequences: \n")
        file.write(sequenceX + "\n")
        file.write(sequenceY + "\n")
        file.write("Alignment sequence: \n")
        file.write(alignedX + "\n")
        file.write(alignedY + "\n")
        file.write("Score: " + str(score) + "\n")

    print("Alignment successful")


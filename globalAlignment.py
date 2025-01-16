import string
import sys
from pam120script import parseTable

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

def pam120Score(a,b):
    return scoring_matrix[a][b]
def globalAlignment(x,y,gapPenalty, scoreFunction):
    m = len(x)
    n = len(y)
    x=x.upper()
    y=y.upper()
    dp = [[0]*(n+1) for _ in range(m+1)] #Set up the DP table
    traceBackTable = [[None]*(n+1) for _ in range(m+1)] #Stores the decisions made

    #Recursive relationship
    #T(i,j) = max{
    #             T(i-1,j) - d gap in y
    #             T(i,j-1) - d gap in x
    #             T(i-1,j-1) + s(x[i],y[j])
    #              }
    #Initialization for the first row and first column
    dp[0][0] = 0
    for i in range(1,m+1):
        dp[i][0] = dp[i-1][0] - gapPenalty
        traceBackTable[i][0] = "up"
    for j in range(1, n+1):
        dp[0][j] = dp[0][j-1] - gapPenalty
        traceBackTable[0][j] = "left"
    
    for i in range(1, m+1):
        for j in range(1, n+1):
            diagonalScore = dp[i-1][j-1] + scoreFunction(x[i-1],y[j-1]) #-1 because need to account for the x,y character starts at index 0
            upScore = dp[i-1][j] - gapPenalty
            leftScore = dp[i][j-1] - gapPenalty
            
            bestCurrentScore = diagonalScore #defaults to diagonal
            bestCurrentDirection = "diag" #defaults to diag

            if upScore > bestCurrentScore:
                bestCurrentScore = upScore
                bestCurrentDirection = "up"
            if leftScore > bestCurrentScore:
                bestCurrentScore = leftScore
                bestCurrentDirection = "left"
            dp[i][j] =bestCurrentScore
            traceBackTable[i][j] = bestCurrentDirection
    alignedX = []
    alignedY = []
    i,j = m,n #initialize i, j as the lengths the strings

    while i>0 or j>0:
        direction = traceBackTable[i][j]
        if direction =="diag":
            alignedX.append(x[i-1])
            alignedY.append(y[j-1])
            i-=1
            j-=1
        elif direction =="up":
            alignedX.append(x[i-1])
            alignedY.append("-")
            i-=1
        elif direction =="left":
            alignedX.append("-")
            alignedY.append(y[j-1])
            j-=1
        else:
            break
    alignedX.reverse()
    alignedY.reverse()

    return ''.join(alignedX).lower(), ''.join(alignedY).lower(), dp[m][n]



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
    
    
    alignedX, alignedY, score = globalAlignment(sequenceX,sequenceY,gapPenalty,pam120Score)
    outputFile = "output.txt"
    with open(outputFile, "w") as file:
        file.write("Alignment sequence: \n")
        file.write(alignedX + "\n")
        file.write(alignedY + "\n")
        file.write("Score: " + str(score) + "\n")

    print("Alignment successful")



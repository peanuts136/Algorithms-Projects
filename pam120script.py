def parseTable(labels, tableStr):
    lines = tableStr.strip().split("\n")
    # Split each line into its elements (scores)
    elements = [line.strip().split() for line in lines]

    # Initialize the scoring dictionary
    scoring_dict = {}

    # Assume that each line in 'elements' corresponds to a row in 'labels'
    # and that each column corresponds to a column in 'labels'
    # Make sure the dimensions match (each line should have as many scores as labels)
    for i, row_label in enumerate(labels):
        scoring_dict[row_label] = {}  # Create a dictionary for this row
        for j, col_label in enumerate(labels):
            score_str = elements[i][j]
            scoring_dict[row_label][col_label] = int(score_str)

    return scoring_dict

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

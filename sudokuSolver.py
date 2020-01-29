import copy
# isNumInRow FUNCTION ###################################################################
#
# DESCR: This function takes an integer number between 1 to 9 inclusive
# and an array table of the solved Sudoku piece so far. It checks if that number
# is found in that particular row of the Sudoku piece. The function returns True 
# if that's the case, and False if it is not.
#
# INPUTS:
# numberToCheck: One integer number between 1 to 9 inclusive.
# rowToCheck: One integer number between 0 and 8 inclusive.
# sudokuGrid: An array table of the solved Sudoku piece so far.
#
# OUTPUTS:
# Returns True if numberToCheck has been found in the row.
# Returns False if numberToCheck has been found in the row.

def isNumInRow(numberToCheck, rowToCheck, sudokuGrid):
    for column in range(9):
        if len(sudokuGrid[rowToCheck][column]) != 0:
            if (numberToCheck == sudokuGrid[rowToCheck][column][0]):
                return True
    return False

################################################################################

def isNumInRowPossibility(numberToCheck, rowToCheck, sudokuGridPoss):
    for column in range(9):
        if len(sudokuGridPoss[rowToCheck][column]) != 0:
            for i in range(len(sudokuGridPoss[rowToCheck][column])):
                if (numberToCheck == sudokuGridPoss[rowToCheck][column][i]):
                    return True
        else: 
            return False



def isNumInCol(numberToCheck, columnToCheck, sudokuGrid):
    for row in range(9):
        if len(sudokuGrid[row][columnToCheck]) != 0: 
            if (numberToCheck == sudokuGrid[row][columnToCheck][0]): #Computer doesn't recognize 9, it sees [9] which is not equal to 9.
                return True
    return False


def isNumInColPossibility(numberToCheck, columnToCheck, sudokuGridPoss):
    for row in range(9):
        if len(sudokuGridPoss[row][columnToCheck]) != 0: 
            for i in range(len(sudokuGridPoss[row][columnToCheck])):
                if (numberToCheck == sudokuGridPoss[row][columnToCheck][i]):
                    return True
        else: 
            return False







def isNumInBox(numberToCheck, topBoundInclu, bottomBoundExclu, leftBoundInclu, rightBoundExclu, sudokuGrid):
    for row in range(topBoundInclu, bottomBoundExclu):
        for column in range(leftBoundInclu, rightBoundExclu):
            if len(sudokuGrid[row][column]) != 0:
                if numberToCheck == sudokuGrid[row][column][0]:
                    return True
    return False
    

def isNumInBoxPossibility(numberToCheck, topBoundInclu, bottomBoundExclu, leftBoundInclu, rightBoundExclu, sudokuGridPoss):
    for row in range(topBoundInclu, bottomBoundExclu):
        for column in range(leftBoundInclu, rightBoundExclu):
            if len(sudokuGridPoss[row][column]) != 0:
                for i in range(len(sudokuGridPoss[row][column])):
                    if numberToCheck == sudokuGridPoss[row][column][i]:
                        return True
            else:
                return False





def isWholeBoxSolved(topBoundInclu, bottomBoundExclu, leftBoundInclu, rightBoundExclu, sudokuGrid):
    filledCount = 0
    for row in range(topBoundInclu, bottomBoundExclu):
        for column in range(leftBoundInclu, rightBoundExclu):
            if len(sudokuGrid[row][column]) == 1:
                filledCount += 1 

    if filledCount == 9:
        return True
    else:
        return False

def processingABox(topBoundInclu, bottomBoundExclu, leftBoundInclu, rightBoundExclu, sudokuGridAct, sudokuGridPoss):
    for row in range(topBoundInclu,bottomBoundExclu):
                for column in range(leftBoundInclu,rightBoundExclu):
                    if len(sudokuGridAct[row][column]) != 1: #If there is no element in the square...
                        for testNumber in range(1,10):
                            hasBeenFound = isNumInRow(testNumber, row, sudokuGridAct)
                            if hasBeenFound == False:
                                hasBeenFound = isNumInCol(testNumber, column, sudokuGridAct)
                                if hasBeenFound == False:
                                    hasBeenFound == isNumInBox(testNumber, leftBoundInclu, rightBoundExclu, topBoundInclu, bottomBoundExclu, sudokuGridAct)
                                    if hasBeenFound == False:
                                        sudokuGridPoss[row][column].append(testNumber)
                                            
                        if len(sudokuGridPoss[row][column]) == 1:
                            sudokuGridAct[row][column] = sudokuGridPoss[row][column]
                        #sudokuGridPoss[row][column].clear()
                        
    return [sudokuGridAct, sudokuGridPoss]


def narrowingPossibilitiesByBox(topInclu, bottomExclu, leftInclu, rightExclu, sudokuGridAct, sudokuGridPoss):
    for row in range(topInclu, bottomExclu):
        for column in range(leftInclu, rightExclu):
            if len(sudokuGridPoss[row][column]) > 1:
                i = 0
                while i < (len(sudokuGridPoss[row][column]) ):
                    testNumber = sudokuGridPoss[row][column][i]
                    hasBeenFound = isNumInRowPossibility(testNumber, row, sudokuGridPoss)
                    if hasBeenFound == False:
                        hasBeenFound = isNumInColPossibility(testNumber, column, sudokuGridPoss)
                        if hasBeenFound == False:
                            hasBeenFound = isNumInBoxPossibility(testNumber, topInclu, bottomExclu, leftInclu, rightExclu, sudokuGridPoss)
                            if hasBeenFound == False:
                                sudokuGridPoss[row][column].clear()
                                sudokuGridPoss[row][column].append(testNumber) #Check this line
                                sudokuGridAct[row][column].append(testNumber)
                                
                                #Now delete that option in the possibilities, row, column, and box:

                                #Row
                                for k in range(9):
                                    for m in range(len(sudokuGridPoss[k][column])):
                                        if sudokuGridPoss[k][column][m] == testNumber:
                                            #sudokuGridPoss[k][column].pop(m)
                                            sudokuGridPoss[k][column][m] = 0

                                #Column
                                for k in range(9):
                                    for m in range(len(sudokuGridPoss[row][k])):
                                        if sudokuGridPoss[row][k][m] == testNumber:
                                            #sudokuGridPoss[row][k].pop(m)
                                            sudokuGridPoss[row][k][m] = 0
                                #Box
                                for k in range(topInclu, bottomExclu):
                                    for m in range(leftInclu, rightExclu):
                                        for f in range(len(sudokuGridPoss[k][m])):
                                            if sudokuGridPoss[k][m][f] == testNumber:
                                                #sudokuGridPoss[k][m].pop(f)
                                                sudokuGridPoss[k][m][f] = 0
                                #Iterate
                                i += 1
                            else: 
                                i += 1
                        else:
                            i += 1
                    else:
                        i += 1
                            
    return [sudokuGridAct, sudokuGridPoss]

# ACTUAL PROGRAM
def main():

    sudokuPiece = [] # Actual Sudoku grid to fill in.
    sudokuPoss = [] # A sudoku grid containing all the possibilities for each square.

    # This makes the actual sudoku grid.

    for row in range(9):
        sudokuPiece.append([])
        for column in range(9):
            sudokuPiece[row].append([])

    sudokuPiece =  #Input a 2x2 array here of your puzzle.

    #This makes the sudoku possibilities grid.

    for row in range(9):
        sudokuPoss.append([])
        for column in range(9):
            sudokuPoss[row].append([])


    # This sets all the Filled Boxes to FALSE

    filledBoxA = False
    filledBoxB = False
    filledBoxC = False
    filledBoxD = False
    filledBoxE = False
    filledBoxF = False
    filledBoxG = False
    filledBoxH = False
    filledBoxI = False

    # INPUT
    print("Please enter the numbers found in your sudoku puzzle." )
    #print("Are there any squares left that have numbers not entered into the program yet? (Y/N): ")
    #anySquaresLeft = input()

    #while anySquaresLeft == "Y":
        #print("What is the number in the square? ")
        #number = int(input())
        #print("What is the row number of that square? ")
        #rowNum = int(input())
        #print("What is the column number of that square? ")
        #columnNum = int(input())
        #sudokuPiece[rowNum-1][columnNum-1] = number
        #print("Are there any squares left that have numbers not entered into the program yet? (Y/N): ")
        #anySquaresLeft = input()

   
    print("Thank you! Analyzing...")

    didSudokuPieceChange = True

    while (didSudokuPieceChange) == True:
            temp = copy.deepcopy(sudokuPoss) #Works now, but understand why.
            #Reset the sudokuPoss to blank
            sudokuPoss = []
            for row in range(9):
                sudokuPoss.append([])
                for column in range(9):
                    sudokuPoss[row].append([])


            #Go through Box A 
            theSudokuGrids = processingABox(0,3,0,3,sudokuPiece,sudokuPoss)
            sudokuPiece = theSudokuGrids[0]
            sudokuPoss = theSudokuGrids[1]
            filledBoxA = isWholeBoxSolved(0,3,0,3,sudokuPiece)
            
            #Go through Box B
            theSudokuGrids = processingABox(0,3,3,6,sudokuPiece,sudokuPoss)
            sudokuPiece = theSudokuGrids[0]
            sudokuPoss = theSudokuGrids[1]
            filledBoxB = isWholeBoxSolved(0,3,3,6,sudokuPiece)

            #Go through Box C
            theSudokuGrids = processingABox(0,3,6,9,sudokuPiece,sudokuPoss)
            sudokuPiece = theSudokuGrids[0]
            sudokuPoss = theSudokuGrids[1]
            filledBoxC = isWholeBoxSolved(0,3,6,9,sudokuPiece)

            #Go through Box D
            theSudokuGrids = processingABox(3,6,0,3,sudokuPiece,sudokuPoss)
            sudokuPiece = theSudokuGrids[0]
            sudokuPoss = theSudokuGrids[1]
            filledBoxD = isWholeBoxSolved(3,6,0,3,sudokuPiece)
            
            #Go through Box E
            theSudokuGrids = processingABox(3,6,3,6,sudokuPiece,sudokuPoss)
            sudokuPiece = theSudokuGrids[0]
            sudokuPoss = theSudokuGrids[1]
            filledBoxE = isWholeBoxSolved(3,6,3,6,sudokuPiece)

            #Go through Box F
            theSudokuGrids = processingABox(3,6,6,9,sudokuPiece,sudokuPoss)
            sudokuPiece = theSudokuGrids[0]
            sudokuPoss = theSudokuGrids[1]
            filledBoxF = isWholeBoxSolved(3,6,6,9,sudokuPiece)

            #Go through Box G
            theSudokuGrids = processingABox(6,9,0,3,sudokuPiece,sudokuPoss)
            sudokuPiece = theSudokuGrids[0]
            sudokuPoss = theSudokuGrids[1]
            filledBoxG = isWholeBoxSolved(6,9,0,3,sudokuPiece)

             #Go through Box H
            theSudokuGrids = processingABox(6,9,3,6,sudokuPiece,sudokuPoss)
            sudokuPiece = theSudokuGrids[0]
            sudokuPoss = theSudokuGrids[1]
            filledBoxH = isWholeBoxSolved(6,9,3,6,sudokuPiece)

             #Go through Box I
            theSudokuGrids = processingABox(6,9,6,9,sudokuPiece,sudokuPoss)
            sudokuPiece = theSudokuGrids[0]
            sudokuPoss = theSudokuGrids[1]
            filledBoxI = isWholeBoxSolved(6,9,6,9,sudokuPiece)

            if sudokuPoss != temp:
                didSudokuPieceChange = True
            else:
                didSudokuPieceChange = False

    


    while (filledBoxA and filledBoxB and filledBoxC \
        and filledBoxD and filledBoxE and filledBoxF \
        and filledBoxG and filledBoxH and  filledBoxI) == False:

            #Go through Box A 
            theSudokuGrids = narrowingPossibilitiesByBox(0,3,0,3,sudokuPiece,sudokuPoss)
            sudokuPiece = theSudokuGrids[0]
            sudokuPoss = theSudokuGrids[1]

            filledBoxA = isWholeBoxSolved(0,3,0,3,sudokuPiece)
            
            #Go through Box B
            theSudokuGrids = narrowingPossibilitiesByBox(0,3,3,6,sudokuPiece,sudokuPoss)
            sudokuPiece = theSudokuGrids[0]
            sudokuPoss = theSudokuGrids[1]
            filledBoxB = isWholeBoxSolved(0,3,3,6,sudokuPiece)

            #Go through Box C
            theSudokuGrids = narrowingPossibilitiesByBox(0,3,6,9,sudokuPiece,sudokuPoss)
            sudokuPiece = theSudokuGrids[0]
            sudokuPoss = theSudokuGrids[1]
            filledBoxC = isWholeBoxSolved(0,3,6,9,sudokuPiece)

            #Go through Box D
            theSudokuGrids = narrowingPossibilitiesByBox(3,6,0,3,sudokuPiece,sudokuPoss)
            sudokuPiece = theSudokuGrids[0]
            sudokuPoss = theSudokuGrids[1]
            filledBoxD = isWholeBoxSolved(3,6,0,3,sudokuPiece)
            
            #Go through Box E
            theSudokuGrids = narrowingPossibilitiesByBox(3,6,3,6,sudokuPiece,sudokuPoss)
            sudokuPiece = theSudokuGrids[0]
            sudokuPoss = theSudokuGrids[1]
            filledBoxE = isWholeBoxSolved(3,6,3,6,sudokuPiece)

            #Go through Box F
            theSudokuGrids = narrowingPossibilitiesByBox(3,6,6,9,sudokuPiece,sudokuPoss)
            sudokuPiece = theSudokuGrids[0]
            sudokuPoss = theSudokuGrids[1]
            filledBoxF = isWholeBoxSolved(3,6,6,9,sudokuPiece)

            #Go through Box G
            theSudokuGrids = narrowingPossibilitiesByBox(6,9,0,3,sudokuPiece,sudokuPoss)
            sudokuPiece = theSudokuGrids[0]
            sudokuPoss = theSudokuGrids[1]
            filledBoxG = isWholeBoxSolved(6,9,0,3,sudokuPiece)

             #Go through Box H
            theSudokuGrids = narrowingPossibilitiesByBox(6,9,3,6,sudokuPiece,sudokuPoss)
            sudokuPiece = theSudokuGrids[0]
            sudokuPoss = theSudokuGrids[1]
            filledBoxH = isWholeBoxSolved(6,9,3,6,sudokuPiece)

             #Go through Box I
            theSudokuGrids = narrowingPossibilitiesByBox(6,9,6,9,sudokuPiece,sudokuPoss)
            sudokuPiece = theSudokuGrids[0]
            sudokuPoss = theSudokuGrids[1]
            filledBoxI = isWholeBoxSolved(6,9,6,9,sudokuPiece)
    
    #OUTPUT
    print(sudokuPiece)


main()




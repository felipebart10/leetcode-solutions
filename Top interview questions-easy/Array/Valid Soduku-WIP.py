def isValidSudoku(matrix):
    linhaAtual = 0
    colunaAtual = 0

    while linhaAtual < 9:
        while colunaAtual < 9:
            i = 0
            j = 0
            temp = []
            elementoTestado = matrix[linhaAtual][colunaAtual]
            if elementoTestado != ".":
                temp.append(elementoTestado)
                while i < 9:
                    while j < 9:
                        if matrix[i][j] == elementoTestado:
                            temp.append(elementoTestado)
                        j += 1
                        
                        
                


                
                

    

    


sudoku = [
    [".", "3", ".", ".", "7", ".", ".", ".", "."],
    ["6", ".", ".", "1", "9", "5", ".", ".", "."],
    [".", "9", "8", ".", ".", ".", ".", "6", "."],
    ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
    ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
    ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
    [".", "6", ".", ".", ".", ".", "2", "8", "."],
    [".", ".", ".", "4", "1", "9", "8", ".", "5"],
    [".", ".", ".", ".", "8", ".", ".", "7", "9"],
]

print(isValidSudoku(sudoku))

def isValidSudoku(matriz):
    for linhas in matriz:
        for elemento in linhas:
            if linhas.count(elemento) > 1:
                return False
    
    
        



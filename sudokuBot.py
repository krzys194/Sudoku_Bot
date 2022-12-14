import time
import pyautogui
from threading import local
from numpy import number

M = 9
def puzzle(a):
    for i in range(M):
        for j in range(M):
            print(a[i][j],end = " ")
        print()
def solve(grid, row, col, num):
    for x in range(9):
        if grid[row][x] == num:
            return False
            
    for x in range(9):
        if grid[x][col] == num:
            return False


    startRow = row - row % 3
    startCol = col - col % 3
    for i in range(3):
        for j in range(3):
            if grid[i + startRow][j + startCol] == num:
                return False
    return True

def Suduko(grid, row, col):

    if (row == M - 1 and col == M):
        return True
    if col == M:
        row += 1
        col = 0
    if grid[row][col] > 0:
        return Suduko(grid, row, col + 1)
    for num in range(1, M + 1, 1): 
    
        if solve(grid, row, col, num):
        
            grid[row][col] = num
            if Suduko(grid, row, col + 1):
                return True
        grid[row][col] = 0
    return False
        

def find_plansza():
    plansza = pyautogui.locateOnScreen("sp1.png", confidence=0.7)
    
    tab = [[0,0,0,0,0,0,0,0,0], 
            [0,0,0,0,0,0,0,0,0], 
            [0,0,0,0,0,0,0,0,0], 
            [0,0,0,0,0,0,0,0,0], 
            [0,0,0,0,0,0,0,0,0], 
            [0,0,0,0,0,0,0,0,0], 
            [0,0,0,0,0,0,0,0,0], 
            [0,0,0,0,0,0,0,0,0], 
            [0,0,0,0,0,0,0,0,0]]
  
    if not plansza:
        print("Nie widzę planszy!")
        return
    
    print ("Widze plansze")
    print(plansza)
    borderFromLeftX, borderFromTopY, plansza_x, plansza_y = plansza
    # screenShot = pyautogui.screenshot(region = (borderFromLeftX, borderFromTopY, plansza_x, plansza_y))
    # screenShot.save("zdjeciePlanszy.png")
    
    borderFromLeftXConst = borderFromLeftX
    borderFromTopYConst = borderFromTopY
    widthBox1 = int((plansza_x/9))
    widthBox = int((plansza_x/9)-13)
    print(widthBox, plansza_x)
    hightBox1 = int((plansza_y/9))
    hightBox = int((plansza_y/9)-15)
    print(hightBox, plansza_y)
    
    for row in range(0,9):
        borderFromTopY = borderFromTopYConst + ((hightBox1) * row) + 2*row
        
        for column in range(0,9):
            precision = 0.88
            number1 = pyautogui.locateOnScreen("1.png", confidence=precision, region = (borderFromLeftX, borderFromTopY, widthBox, hightBox))
            number2 = pyautogui.locateOnScreen("2.png", confidence=precision, region = (borderFromLeftX, borderFromTopY, widthBox, hightBox))
            number3 = pyautogui.locateOnScreen("3.png", confidence=precision, region = (borderFromLeftX, borderFromTopY, widthBox, hightBox))
            number4 = pyautogui.locateOnScreen("4.png", confidence=precision, region = (borderFromLeftX, borderFromTopY, widthBox, hightBox))
            number5 = pyautogui.locateOnScreen("5.png", confidence=precision, region = (borderFromLeftX, borderFromTopY, widthBox, hightBox))
            number6 = pyautogui.locateOnScreen("6.png", confidence=precision, region = (borderFromLeftX, borderFromTopY, widthBox, hightBox))
            number7 = pyautogui.locateOnScreen("7.png", confidence=precision, region = (borderFromLeftX, borderFromTopY, widthBox, hightBox))
            number8 = pyautogui.locateOnScreen("8.png", confidence=precision, region = (borderFromLeftX, borderFromTopY, widthBox, hightBox))
            number9 = pyautogui.locateOnScreen("9.png", confidence=precision, region = (borderFromLeftX, borderFromTopY, widthBox, hightBox))
            borderFromLeftX = borderFromLeftXConst + ((widthBox1) * column) + 2*column 

            if number1:
                tab[row][column-1] = 1
            elif number2:
                tab[row][column-1] = 2
            elif number3:
                tab[row][column-1] = 3
            elif number4:
                tab[row][column-1] = 4
            elif number5:
                tab[row][column-1] = 5
            elif number6:
                tab[row][column-1] = 6
            elif number7:
                tab[row][column-1] = 7 
            elif number8:
                tab[row][column-1] = 8
            elif number9:
                tab[row][column-1] = 9
            else:
                tab[row][column-1] = 0

    print("Pobrana tabela: \n", tab)
    grid = tab
    print(grid)
    if (Suduko(grid, 0, 0)):
        puzzle(grid)
    else:
        print("Solution does not exist:(")

    print("", tab)
    print("Rozwiazana tabela: |n", grid)
    
    for row in range(0,9):
        borderFromTopY = borderFromTopYConst + ((hightBox1) * row) + 2*row
        
        for column in range(0,9):                   
            print("Rząd nr: ", row+1, "Kolumna nr: ", column+1)
            borderFromLeftX = borderFromLeftXConst + ((widthBox1) * column) + 2*column
            a = str(tab[row][column])
            print(type(a))
            pyautogui.moveTo(borderFromLeftX+20, borderFromTopY+22)
            pyautogui.click()
            pyautogui.write(a)
    time.sleep(5)
    pyautogui.press('enter')
    
       
while(True):
    find_plansza()
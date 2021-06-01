from queue import Queue
from BFS_Sudoku import BFS_solve
import copy
import time
from tkinter import *
from tkinter.font import BOLD
from typing import Sized
import random
from tkinter import messagebox

entries = []

def initialize(top,arr):
    E = entries[0]
    m=1
    for i in range(9):
        for j in range(9):
            if(not E.get()):
                arr[i][j] = 0
            else:
                arr[i][j] = int(E.get())
            if(m<=80):
                E = entries[m]
                m+=1

# def easy(top,arr):
#     E = entries[0]
#     m=1
#     for i in range(9):
#         for j in range(9):
#             if(((i*j) % random.randrange(1,8) == 0) and i % random.randrange(1,8) == 0 and j % random.randrange(1,8) == 0):
#                     arr[i][j] = random.randrange(1,9)
#             else:
#                     arr[i][j] = 0
#             if(m<=80):
#                 E = entries[m]
#                 m+=1
#     print_maze(arr)

# def medium(top,arr):
#     E = entries[0]
#     m=1
#     for i in range(9):
#         for j in range(9):
#             if((i*j) % random.randrange(1,8) == 1):
#                 arr[i][j] = random.randrange(1,9)
#             else:
#                 arr[i][j] = 0
#             if(m<=80):
#                 E = entries[m]
#                 m+=1
#     for row in arr:
#         print (row)
#     print_maze(arr)


def hard(top,arr):
    x = random.randrange(1,6)
    if(x==1):
        arr = [[0,3,0,0,0,1,5,0,0], 
        [0,0,0,5,0,0,0,8,4],
        [0,0,5,0,0,7,0,6,0],
        [0,0,0,0,0,0,0,0,0],
        [0,8,0,2,0,0,0,7,0],
        [0,0,0,8,5,0,0,0,9],
        [0,0,3,0,9,4,0,0,7],
        [0,0,4,0,0,0,0,0,8],
        [5,0,6,0,1,0,0,0,0]]
    elif(x==2):
        arr = [[0,0,7,2,8,0,0,0,0], # easy
            [0,0,0,0,0,0,5,0,6],
            [4,1,3,0,0,6,0,8,0],
            [7,2,0,3,9,0,0,0,0],
            [3,4,0,0,0,0,8,1,0],
            [6,8,0,1,0,7,0,0,2],
            [0,0,0,6,7,4,0,2,3],
            [0,0,0,0,0,5,7,0,0],
            [1,0,6,0,2,3,0,4,0]]
    elif(x==3):
        arr = [[0,0,0,8,4,0,6,5,0], # given
            [0,8,0,0,0,0,0,0,9],
            [0,0,0,0,0,5,2,0,1],
            [0,3,4,0,7,0,5,0,6],
            [0,6,0,2,5,1,0,3,0],
            [5,0,9,0,6,0,7,2,0],
            [1,0,8,5,0,0,0,0,0],
            [6,0,0,0,0,0,0,4,0],
            [0,5,2,0,8,6,0,0,0]]
    elif(x==4):
        arr = [[0,3,9,0,0,0,1,2,0], #given
            [0,0,0,9,0,7,0,0,0],
            [8,0,0,4,0,1,0,0,6],
            [0,4,2,0,0,0,7,9,0],
            [0,0,0,0,0,0,0,0,0],
            [0,9,1,0,0,0,5,4,0],
            [5,0,0,1,0,9,0,0,3],
            [0,0,0,8,0,5,0,0,0],
            [0,1,4,0,0,0,8,7,0]]
    elif(x==5):
        arr = [[0,0,0,0,5,0,9,7,6], # medium
            [8,0,5,1,9,0,0,3,0],
            [3,7,0,0,4,0,0,8,0],
            [0,8,0,0,0,0,0,0,9],
            [0,2,0,0,0,0,4,0,7],
            [0,9,0,0,2,6,0,1,5],
            [0,0,0,0,8,1,6,0,0],
            [9,0,0,3,0,0,0,0,0],
            [2,0,0,4,0,9,0,0,0]]
    elif(x==6):
        grid = [[0,3,0,0,0,1,5,0,0], # very hard
            [0,0,0,5,0,0,0,8,4],
            [0,0,5,0,0,7,0,6,0],
            [0,0,0,0,0,0,0,0,0],
            [0,8,0,2,0,0,0,7,0],
            [0,0,0,8,5,0,0,0,9],
            [0,0,3,0,9,4,0,0,7],
            [0,0,4,0,0,0,0,0,8],
            [5,0,6,0,1,0,0,0,0]]
        
    E = entries[0]
    m=0
    for i in range(9):
        for j in range(9):
            # if((i*j) % random.randrange(1,8) == 3):
            #     arr[i][j] = random.randrange(1,9)
            # else:
            #     arr[i][j] = 0
            if(m<=80):
                E = entries[m]
                m+=1
    for row in arr:
        print (row)
    print_maze(arr)


def print_maze(arr):
    clean_Mess()
    E = entries[0]
    m=1
    for i in range(9):
        for j in range(9):
            if(arr[i][j] != 0):
                E.insert(1,arr[i][j])
            if(m<=80):
                E = entries[m]
                m+=1
            
        
def find_empty_location(arr,l):
    for row in range(9):
        for col in range(9):
            if(arr[row][col]==0):
                l[0]=row
                l[1]=col
                return True
    return False
def used_in_row(arr,row,num):
    for i in range(9):
        if(arr[row][i] == num):
            return True
    return False
def used_in_col(arr,col,num):
    for i in range(9):
        if(arr[i][col] == num):
            return True
    return False
def used_in_box(arr,row,col,num):
    for i in range(3):
        for j in range(3):
            if(arr[i+row][j+col] == num):
                return True
    return False
def check_location_is_safe(arr,row,col,num):
    return not used_in_row(arr,row,num) and not used_in_col(arr,col,num) and not used_in_box(arr,row - row%3,col - col%3,num)

def solve_sudoku(arr):
    l=[0,0]
    if(not find_empty_location(arr,l)):
        return True
    row=l[0]
    col=l[1]
    for num in range(1,10):
        if(check_location_is_safe(arr,row,col,num)):
            arr[row][col]=num
            if(solve_sudoku(arr)):
                return True
            arr[row][col] = 0
    return False


def createGUI(maze):
    top = Tk()
    top.title("Sudoku Solver")
    canvas = Canvas(top,height=400, width =450, bg="#91091e")
    canvas.create_text(160,40, text="Masukkan angka yang kamu inginkan", fill="white", font=("Cambria",13,BOLD))
    canvas.create_text(160,60, text="atau pilih masukan acak!", fill="white", font=("Cambria",13,BOLD))

    createRow(canvas)#buat garis baris-baris
    createCol(canvas)#buat garis kolom-kolom
    createEntry(top)#buat kotak-kotak yg diisi
    createButtons(top,maze)#buat tombol-tombol
    button_quit = Button(top, text="Keluar", fg="white",command=top.destroy, bg="black", font=("Cambria",15))
    button_quit.place(x=100, y=350,height=40, width=150)

    canvas.pack(side = 'top')
    top.mainloop()
    
def createButtons(top,maze):
    # button_easy = Button(top, text="Easy", justify='left', default='active',bg="#ffaaa7", command = lambda: easy(top,maze),font=("Cambria",12,BOLD))
    # button_medium = Button(top, text="Medium", justify='left', default='active',bg="#fed049", command = lambda: medium(top,maze),font=("Cambria",12,BOLD))
    button_hard = Button(top, text="Acak", justify='left', default='active', bg= "#98ddca", command = lambda: hard(top,maze),font=("Cambria",12,BOLD))
    button_solve = Button(top, text="Selesaikan", justify='left', default='active', command = lambda: play_Game(top,maze),bg="#b8b5ff",font=("Cambria",12,BOLD))
    button_manual = Button(top, text="Manual", justify='left', command = lambda: clean_Mess(),bg="#a1cae2",font=("Cambria",12,BOLD))
   
    # button_easy.place(x=350, y=30, height=40, width=80)
    # button_medium.place(x=350, y=80, height=40, width=80)
    button_hard.place(x=350, y=130 ,height=40, width=85)
    button_solve.place(x=350, y=180 ,height=40, width=85)
    button_manual.place(x=350, y=230 ,height=40, width=85)
    
def clean_Mess():
    for e in entries:
        e.delete(0, END)
    
def play_Game(top,maze):
    initialize(top,maze)
    # BFS_solve(maze)
    result = BFS_solve(maze)
    print(result)
    if(result[0] == 1):
        print_maze(result[1])
        messagebox.showinfo("SOLVED", "yey solusi didapatkan")
    elif(result[0] == 0):
        messagebox.showerror("FAILED", "BFS spend too many nodes")
        clean_Mess()
    else:
        messagebox.showerror("FAILED","No Solution Found!")
        clean_Mess()
        
def createEntry(top):
    p,q=39.5,81 #41.4,41.4
    for i in range(9):
        for j in range(9):
            E = Entry(top, width=3, font = 'BOLD')
            E.grid(row=i, column=j)
            E.place(x=p, y=q, height=19, width=24)
            entries.append(E)
            p+=30.0
        q+=24.5
        p=39.5
    
def createRow(canvas):
    i,j=38,79
    p=38
    q=299
    for m in range(10):
        if m % 3 == 0 :
            canvas.create_line(i,j,p,q,width=3.5)
        else:
            canvas.create_line(i,j,p,q,width=1)
        i+=30
        p+=30
    
def createCol(canvas):
    i,j=38,79
    p,q=308,79
    for m in range(10):
        if m % 3 == 0 :
            canvas.create_line(i,j,p,q,width=3.5)
        else :
            canvas.create_line(i,j,p,q,width=1)
        j+=24.5
        q+=24.5

if __name__=="__main__":
    
    maze=[[0 for x in range(9)]for y in range(9)]
    createGUI(maze)
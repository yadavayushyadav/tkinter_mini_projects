from tkinter import Tk, Entry, Button, Label, messagebox

win_w = 450
win_h = 500

root = Tk()
root.title("Sudoku Solver")
root.geometry(f'{win_w}x{win_h}')

matrix = [[0]*9 for i in range(9)]
fix = [[False]*9 for i in range(9)]

def row(i):
    return matrix[i]

def col(j):
    return [matrix[i][j] for i in range(9)]

def grid(i, j):
    i, j = i - i%3, j - j%3
    temp = []
    for ii in range(3):
        for jj in range(3):
            temp.append(matrix[i+ii][j+jj])
    return temp

def get_matrix(e):
    global matrix, fix
    for j in range(9):
        for i in range(9):
            temp = e[i][j].get()
            if temp in [i for i in '123456789']:
                matrix[j][i] = int(temp)
                fix[j][i] = True
            else:
                matrix[j][i] = 0
                fix[j][i] = False
    return matrix

def is_valid_board():
    global matrix, fix
    for i in range(9):
        for j in range(9):
            if fix[i][j]:
                num = matrix[i][j]
                matrix[i][j] = 0 
                invalid = num in row(i) + col(j) + grid(i, j)
                matrix[i][j] = num 
                if invalid:
                    return False
    return True

def nxt(i, j):
    if j == 8:
        return (i+1, 0)
    return (i, j+1)

def backtrack(i, j):
    global matrix, fix
    if i == 9:
        return True
    if fix[i][j]:
        ni, nj = nxt(i, j)
        return backtrack(ni, nj)
    for num in range(1, 10):
        if num not in row(i) + col(j) + grid(i, j):
            matrix[i][j] = num
            ni, nj = nxt(i, j)
            if backtrack(ni, nj):
                return True
    matrix[i][j] = 0
    return False

def solve():
    global matrix, fix
    get_matrix(e)
    if not is_valid_board():
        messagebox.showerror("Error", "Invalid starting board! Conflicting numbers found.")
        return
    is_empty = all(matrix[i][j] == 0 for i in range(9) for j in range(9))
    if is_empty:
        messagebox.showwarning("Warning", "The board is entirely empty. I will generate a solution from scratch!")
    if backtrack(0, 0):
        for j in range(9):
            for i in range(9):
                if not fix[j][i]:
                    e[i][j].delete(0, 'end')
                    e[i][j].insert(0, str(matrix[j][i]))
                    e[i][j].config(bg="#d4edda") 
        messagebox.showinfo("Success", "Sudoku solved successfully!")
    else:
        messagebox.showerror("Error", "No solution exists for this board! Please check your numbers.")

def reset():
    global matrix
    for i in range(9):
        for j in range(9):
            matrix[i][j] = 0
            e[i][j].delete(0, 'end')
            e[i][j].config(bg="white")

e = [[None]*9 for i in range(9)]
for j in range(9):
    for i in range(9):
        e[i][j] = Entry(root, justify = 'center')
        e[i][j].place(relx = i*50/win_w, rely = j*50/win_h, relwidth = 50/win_w, relheight = 50/win_h)
s = Button(root, text = "Solve", command = solve)
s.place(relx = 0, rely = 450/win_h, relwidth = .5, relheight = 50/win_h)
r = Button(root, text = "Reset", command = reset)
r.place(relx = .5, rely = 450/win_h, relwidth = .5, relheight = 50/win_h)

h1 = Label(root, bg = 'black')
h2 = Label(root, bg = 'black')
v1 = Label(root, bg = 'black')
v2 = Label(root, bg = 'black')

h1.place(relx = 0, rely = 150/win_h, relwidth = 1, height = 1)
h2.place(relx = 0, rely = 300/win_h, relwidth = 1, height = 1)
v1.place(rely = 0, relx = 150/win_w, relheight = .9, width = 1)
v2.place(rely = 0, relx = 300/win_w, relheight = .9, width = 1)

from tkinter import messagebox, Label, Tk, Button, DISABLED, NORMAL
from random import choice

wh = 640
ww = 600

win = Tk()
win.title('Tic tac toe')
win.geometry(f'{ww}x{wh}')

current_turn = choice(['X', 'O'])
lo = []
lx = []
wins = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [1, 4, 7], [2, 5, 8], [3, 6, 9], [1, 5, 9], [3, 5, 7]]

buttons = []

l2 = Label(win, text='', font=('Begonia', '17'))
l2.place(relx=20/ww, rely=4/wh)

def turn_config():
    global current_turn
    l2.configure(text=f"{current_turn}'s turn")

def check():
    win_found = False
    for i in wins:
        if (i[0] in lx) and (i[1] in lx) and (i[2] in lx):
            messagebox.showinfo('Game Over', 'X has won the game!')
            win_found = True
            break
        elif (i[0] in lo) and (i[1] in lo) and (i[2] in lo):
            messagebox.showinfo('Game Over', 'O has won the game!')
            win_found = True
            break
    if not win_found and (len(lx) + len(lo) == 9):
        messagebox.showinfo('Game Over', 'Match ended in draw!')
        win_found = True
    if win_found:
        reset()

def click(index):
    global current_turn
    buttons[index].configure(text=current_turn, state=DISABLED)
    if current_turn == 'X':
        lx.append(index + 1)
        current_turn = 'O'
    else:
        lo.append(index + 1)
        current_turn = 'X'
        
    turn_config()
    check()

def reset():
    global current_turn, lo, lx
    current_turn = choice(['X', 'O'])
    lo.clear()
    lx.clear()
    for btn in buttons:
        btn.configure(text=' ', state=NORMAL)
    turn_config()

def resize_font(event):
    if event.widget == win:
        btn_width = event.width / 3
        btn_height = event.height / 3
        new_size = int(min(btn_width, btn_height) * 0.4)
        new_size = max(8, min(new_size, 90))
        new_font = ('arial', new_size, 'bold')
        for btn in buttons:
            btn.configure(font=new_font)
                
        label_size = max(10, min(int(min(event.width, event.height) * 0.03), 20))
        lt.configure(font=('Castellar', label_size, 'underline'))
        l2.configure(font=('Begonia', label_size))
coords = [(0, 40), (200, 40), (400, 40), (0, 240), (200, 240), (400, 240), (0, 440), (200, 440), (400, 440)]

for i in range(9):
    btn = Button(win, text=' ', font=('arial', '90', 'bold'), command=lambda i=i: click(i), relief='sunken')
    
    x, y = coords[i]
    btn.place(relheight=200/wh, relwidth=200/ww, relx=x/ww, rely=y/wh)
    buttons.append(btn)

resb = Button(win, text='RESET', command=reset)
resb.place(relx=1-0.253, rely=5/wh, relheight = .05, relwidth = .22)

lt = Label(win, text='T I C   T A C   T O E', font=('Castellar', '20', 'underline'))
lt.place(relx=0.26, rely=0, relwidth = 0.48, relheight = 0.06)

turn_config()
win.bind('<Configure>', resize_font)

if __name__=='__main__':
    win.mainloop()

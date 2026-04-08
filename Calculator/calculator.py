from tkinter import Tk, Entry, Button
import re

WINDOW_WIDTH = 380
WINDOW_HEIGHT = 450

is_evaluated = False
ans = ''

win = Tk()
win.title('Calculator')
win.geometry(f'{WINDOW_WIDTH}x{WINDOW_HEIGHT}')

std_buttons = []   
small_buttons = [] 
bold_buttons = []  

entry = Entry(win, bg='light grey', font=('DS-Digital', 24), justify='right')
entry.place(
    relheight=60/WINDOW_HEIGHT, 
    relwidth=360/WINDOW_WIDTH, 
    relx=10/WINDOW_WIDTH, 
    rely=10/WINDOW_HEIGHT
)
entry.focus()

def insert_text(value):
    global is_evaluated
    if is_evaluated:
        if value in ['+', '-', 'x', '÷', '*']:
            is_evaluated = False
        else:
            entry.delete(0, 'end')
            is_evaluated = False
    entry.insert('end', value)

def clear_all():
    global is_evaluated
    entry.delete(0, 'end')
    is_evaluated = False

def backspace():
    global is_evaluated
    if is_evaluated:
        entry.delete(0, 'end')
        is_evaluated = False
    else:
        entry.delete(len(entry.get())-1)

def handle_keypress(event):
    global is_evaluated
    if is_evaluated and event.char:
        if event.char in '0123456789.()':
            entry.delete(0, 'end')
            is_evaluated = False
        elif event.char in '+-*/x÷':
            is_evaluated = False
        elif event.keysym == 'BackSpace':
            entry.delete(0, 'end')
            is_evaluated = False
            return "break"

def be():
    global is_evaluated, ans
    s1 = entry.get()
    s2 = ''
    for i in s1:
        if i == '÷':
            s2 += '/'
        elif i == 'x':
            s2 += '*'
        else:
            s2 += i
            
    s2 = re.sub(r'\b0+(?=\d)', '', s2)
    
    try:
        result = eval(s2)
        if result % 1 == 0:
            out = int(result)
        else:
            out = round(result, 8)
        ans = str(out)
    except ZeroDivisionError:
        out = "Division by zero"
    except (SyntaxError, NameError):
        out = "Invalid input"
    except Exception as e:
        out = "Error"
        print(f"Developer log - Unexpected error: {e}")
        
    entry.delete(0, 'end')
    entry.insert(0, out)
    is_evaluated = True 

def numbers():
    bac = Button(win, text='AC', font=(None, 34), command=clear_all)
    bac.place(relheight=60/WINDOW_HEIGHT, relwidth=90/WINDOW_WIDTH, relx=10/WINDOW_WIDTH, rely=80/WINDOW_HEIGHT)
    
    bc = Button(win, text='C', font=(None, 34), command=backspace)
    bc.place(relheight=60/WINDOW_HEIGHT, relwidth=90/WINDOW_WIDTH, relx=100/WINDOW_WIDTH, rely=80/WINDOW_HEIGHT)
    
    bopen = Button(win, text='(', font=(None, 34), command=lambda: insert_text(r'('))
    bopen.place(relheight=60/WINDOW_HEIGHT, relwidth=90/WINDOW_WIDTH, relx=190/WINDOW_WIDTH, rely=80/WINDOW_HEIGHT)
    
    bclose = Button(win, text=')', font=(None, 34), command=lambda: insert_text(r')'))
    bclose.place(relheight=60/WINDOW_HEIGHT, relwidth=90/WINDOW_WIDTH, relx=280/WINDOW_WIDTH, rely=80/WINDOW_HEIGHT)
    
    small_buttons.extend([bac, bc, bopen, bclose])

    b7 = Button(win, text=7, font=(None, 36), command=lambda: insert_text('7'))
    b7.place(relheight=60/WINDOW_HEIGHT, relwidth=90/WINDOW_WIDTH, relx=10/WINDOW_WIDTH, rely=140/WINDOW_HEIGHT)
    
    b8 = Button(win, text=8, font=(None, 36), command=lambda: insert_text('8'))
    b8.place(relheight=60/WINDOW_HEIGHT, relwidth=90/WINDOW_WIDTH, relx=100/WINDOW_WIDTH, rely=140/WINDOW_HEIGHT)
    
    b9 = Button(win, text=9, font=(None, 36), command=lambda: insert_text('9'))
    b9.place(relheight=60/WINDOW_HEIGHT, relwidth=90/WINDOW_WIDTH, relx=190/WINDOW_WIDTH, rely=140/WINDOW_HEIGHT)
    
    bq = Button(win, text='÷', font=(None, 36), command=lambda: insert_text('÷'))
    bq.place(relheight=60/WINDOW_HEIGHT, relwidth=90/WINDOW_WIDTH, relx=280/WINDOW_WIDTH, rely=140/WINDOW_HEIGHT)

    b4 = Button(win, text=4, font=(None, 36), command=lambda: insert_text('4'))
    b4.place(relheight=60/WINDOW_HEIGHT, relwidth=90/WINDOW_WIDTH, relx=10/WINDOW_WIDTH, rely=200/WINDOW_HEIGHT)
    
    b5 = Button(win, text=5, font=(None, 36), command=lambda: insert_text('5'))
    b5.place(relheight=60/WINDOW_HEIGHT, relwidth=90/WINDOW_WIDTH, relx=100/WINDOW_WIDTH, rely=200/WINDOW_HEIGHT)
    
    b6 = Button(win, text=6, font=(None, 36), command=lambda: insert_text('6'))
    b6.place(relheight=60/WINDOW_HEIGHT, relwidth=90/WINDOW_WIDTH, relx=190/WINDOW_WIDTH, rely=200/WINDOW_HEIGHT)
    
    bm = Button(win, text='×', font=(None, 36), command=lambda: insert_text('x'))
    bm.place(relheight=60/WINDOW_HEIGHT, relwidth=90/WINDOW_WIDTH, relx=280/WINDOW_WIDTH, rely=200/WINDOW_HEIGHT)

    b1 = Button(win, text=1, font=(None, 36), command=lambda: insert_text('1'))
    b1.place(relheight=60/WINDOW_HEIGHT, relwidth=90/WINDOW_WIDTH, relx=10/WINDOW_WIDTH, rely=260/WINDOW_HEIGHT)
    
    b2 = Button(win, text=2, font=(None, 36), command=lambda: insert_text('2'))
    b2.place(relheight=60/WINDOW_HEIGHT, relwidth=90/WINDOW_WIDTH, relx=100/WINDOW_WIDTH, rely=260/WINDOW_HEIGHT)
    
    b3 = Button(win, text=3, font=(None, 36), command=lambda: insert_text('3'))
    b3.place(relheight=60/WINDOW_HEIGHT, relwidth=90/WINDOW_WIDTH, relx=190/WINDOW_WIDTH, rely=260/WINDOW_HEIGHT)
    
    bs = Button(win, text='-', font=(None, 36), command=lambda: insert_text('-'))
    bs.place(relheight=60/WINDOW_HEIGHT, relwidth=90/WINDOW_WIDTH, relx=280/WINDOW_WIDTH, rely=260/WINDOW_HEIGHT)

    bd = Button(win, text='.', font=(None, 36, 'bold'), command=lambda: insert_text('.'))
    bd.place(relheight=60/WINDOW_HEIGHT, relwidth=90/WINDOW_WIDTH, relx=10/WINDOW_WIDTH, rely=320/WINDOW_HEIGHT)
    bold_buttons.append(bd)
    
    b0 = Button(win, text=0, font=(None, 36), command=lambda: insert_text('0'))
    b0.place(relheight=60/WINDOW_HEIGHT, relwidth=90/WINDOW_WIDTH, relx=100/WINDOW_WIDTH, rely=320/WINDOW_HEIGHT)
    
    bans = Button(win, text='Ans', font=(None, 34), command=lambda: insert_text(ans))
    bans.place(relheight=60/WINDOW_HEIGHT, relwidth=90/WINDOW_WIDTH, relx=190/WINDOW_WIDTH, rely=320/WINDOW_HEIGHT)
    small_buttons.append(bans)
    
    ba = Button(win, text='+', font=(None, 36), command=lambda: insert_text('+'))
    ba.place(relheight=60/WINDOW_HEIGHT, relwidth=90/WINDOW_WIDTH, relx=280/WINDOW_WIDTH, rely=320/WINDOW_HEIGHT)

    be_btn = Button(win, text='=', font=(None, 36), command=be)
    be_btn.place(relheight=60/WINDOW_HEIGHT, relwidth=360/WINDOW_WIDTH, relx=10/WINDOW_WIDTH, rely=380/WINDOW_HEIGHT)
    
    std_buttons.extend([b7, b8, b9, bq, b4, b5, b6, bm, b1, b2, b3, bs, b0, be_btn, ba])


def resize_fonts(event):
    if event.widget == win:
        width_ratio = event.width / WINDOW_WIDTH
        height_ratio = event.height / WINDOW_HEIGHT
        
        scale_factor = min(width_ratio, height_ratio, 1.0)
        
        new_entry_size = max(int(24 * scale_factor), 1)
        new_std_size = max(int(36 * scale_factor), 1)
        new_small_size = max(int(34 * scale_factor), 1)
        
        entry.config(font=('DS-Digital', new_entry_size))
        
        for btn in std_buttons:
            btn.config(font=(None, new_std_size))
        for btn in small_buttons:
            btn.config(font=(None, new_small_size))
        for btn in bold_buttons:
            btn.config(font=(None, new_std_size, 'bold'))

win.bind('<Configure>', resize_fonts)
entry.bind('<Return>', lambda event: be())
entry.bind('<Key>', handle_keypress)

if __name__ == '__main__':
    numbers()
    win.mainloop()

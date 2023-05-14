from tkinter import *

root = Tk()
root.title('Number Speller')
root.geometry('1300x400')
root.resizable(height=False,width=False)

try:
    root.iconbitmap(r'Number-Speller\100.ico')
except:
    pass

unit = {0: '', 3: 'Thousand', 6: 'Million', 9: 'Billion', 12: 'Trillion', 15: 'Quadrillion', 18: 'Quintillion'}
ones = {1: 'One', 2: 'Two', 3: 'Three', 4: 'Four', 5: 'Five', 6: 'Six', 7: 'Seven', 8: 'Eight', 9: 'Nine',0:''}
one_11 = {1: 'Eleven', 2: 'Twelve', 3: 'Thirteen', 4: 'Fourteen', 5: 'Fifteen', 6: 'Sixteen', 7: 'Seventeen',
          8: 'Eighteen', 9: 'Nineteen', 0: 'Ten'}
tens = {2: 'Twenty', 3: 'Thirty', 4: 'Forty', 5: 'Fifty', 6: 'Sixty', 7: 'Seventy', 8: 'Eighty', 9: 'Ninety', 0: ''}


def reset(n=None):
    global e1,l5
    e1.delete(0,END)
    l5.delete('1.0','end')


def teller(n=None):
    global e1,l5
    global e1 
    number = find(e1.get())
    try:
        l5.insert(END,number)
        num = int(e1.get())
        num = f'{num:,}'
        e1.delete(0,END)
        e1.insert(0,num)
        root.bind('<Return>',reset)
    except:
        pass

def backspace():
    number = str(e1.get())
    e1.delete(len(number)-1,END)


def check(num):
    from tkinter import messagebox
    if (num.char).isalpha():      
        error = messagebox.showerror('Error','Please enter a proper positive natural number without , or underscore ')
        reset()
    for i in num.char:
        if i in  ['[',']','{','}','/','<','.','>','?',':',';','-','+','=',]:
            messagebox.showerror('Error','Please enter a proper positive natural number')
            reset()



def find(n):
    a = 21
    n = str(n)
    number = ''
    if len(n) > 21:
            from tkinter import messagebox
            messagebox.showerror("Error",'Please enter a number smaller than 999 Quintillion')
            reset()
            return None
    if n=='0':
        return 'Zero'
    
    while len(n) != 0:
        a = a - 3       
        if len(n) > a:
            data = int(int(n) // pow(10, a))
            data = str(data)
            if len(data) == 3:
                if data[1] == '1':
                    number += f'{ones.get(int(data[0]))}  Hundred {one_11.get(int(data[2]))} '
                else:
                    number+=f'{ones.get(int(data[0])) } Hundred {tens.get(int(data[1]))} {ones.get(int(data[2]))} '
            elif len(data) == 2:
                if data[0] == '1':
                    number += f'{one_11.get(int(data[1]))} '
                else:
                    number += f'{tens.get(int(data[0]))} {ones.get(int(data[1]))} '
            elif len(data) == 1:
                number += f'{ones.get(int(data[0]))} '

            if a != 0:
                number += f'{unit.get(a)}, '
            else:
                number += f'{unit.get(a)}'
                break
        n = int(n) % pow(10, a)
        n = str(n)
    return number    

l1 = Label(root,text='Number speller',fg='blue', padx=250, font=('Comic Sans MS', '40'),
               )
l1.grid(row=0,column=0,columnspan=3)
l2 = Label(root,text='Enter the number-',fg='blue', font=('Comic Sans MS', '20'),
               )
l2.grid(row=1,column=0)
e1 = Entry(root, fg='blue',bg='light grey',font=('Comic Sans MS', '20'), width=45, borderwidth=2)
e1.grid(row =1,column=1,columnspan=2)
l3 = Label(root,text='-'*80,fg='blue', font=('Comic Sans MS', '20'),              )
l3.grid(row=2,column=0,columnspan=3)
b1 = Button(root,text = 'Reset',fg='blue',font= ('Comic Sans MS', '20'),command=reset,width=15,)
b1.grid(row=3,column=0,sticky=W+E)
b2 = Button(root,text = 'Enter',fg='blue',font= ('Comic Sans MS', '20'),command=teller,width=20,)
b2.grid(row=3,column=2,sticky=W+E)
b3 = Button(root,text = 'Backspace',fg='blue',font= ('Comic Sans MS', '20'),command=backspace,width=20,)
b3.grid(row=3,column=1,sticky=W+E)
l4 = Label(root,text='-'*80,fg='blue', font=('Comic Sans MS', '20'),              )
l4.grid(row=4,column=0,columnspan=3)
l5 = Text(root,fg='blue', bg='light grey',font=('Comic Sans MS', '20'), wrap='word')
l5.insert(END,'')
l5.grid(row=5,column=0,columnspan=3)
l4 = Label(root,text='',fg='blue',bg='light grey', font=('Comic Sans MS', '20'),)

l4.grid(row=6,column=0,columnspan=3)
root.bind('<Key>',check)
root.bind('<Return>',teller)
root.bind('<Escape>',lambda n:root.quit())
mainloop()
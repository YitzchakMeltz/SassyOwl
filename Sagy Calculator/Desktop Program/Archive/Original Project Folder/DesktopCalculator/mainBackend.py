from tkinter import*
from tkinter.ttk import*
import math
from fractions import*

mathEq=""
sum=0

def button_click(userClick):
    global mathEq
    mathEq += userClick
    #update_screen()
    return

def button_equals_click():
    global mathEq
    global sum
    sum=mathEq.replace('×','*')
    sum=sum.replace('÷','/')
    
    try:
        sum=eval(sum)
    except (SyntaxError):
        sum="Equation was not entered correctly"
        return

    print(mathEq)
    if isinstance(sum, int):
        sum = int(sum)
    else:
        sum=Fraction(str(sum)).limit_denominator()


    print('=',sum)
    return

def button_clear_click():
    global mathEq
    mathEq=""
    return
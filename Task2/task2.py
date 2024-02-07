import turtle
import math

def draw_pythagoras_tree(t, order, size):
    if order == 0:
        return
    
    t.forward(size)
    t.left(45)

    draw_pythagoras_tree(t, order-1, size*0.8)
    
    t.right(90)
    draw_pythagoras_tree(t, order-1, size*0.8)
    
    t.left(45)
    t.backward(size)

def pythagoras_tree(order, size):
    window = turtle.Screen()
    window.bgcolor("black")
    
    turtle.TurtleScreen._RUNNING = True
    t = turtle.Turtle()
    t.setpos(0, -200)
    t.left(90)
    t.speed(0)
    t.color("orange")
    t.pensize(2)
    
    draw_pythagoras_tree(t, order, size)
    
    window.mainloop()

def task2():
    while True:
        try:
            input_arg = int(input('Enter the level of recursion: (close to -1)):   ' ))
        except ValueError:
            print('Incorrect level of recursion. Please use positive numbers only')
            continue
        if input_arg ==-1:
            print('Good bye!')
            break
    
        if input_arg < 0:
            print('Incorrect level of recursion. Please use positive numbers or -1 for exit')
            continue
        
        pythagoras_tree(int(input_arg), 100)

if __name__ == '__main__':
    task2()
# from graphics import Canvas

# # each patch is a square with this width and height:
# PATCH_SIZE = 100
# CANVAS_WIDTH = PATCH_SIZE * 4
# CANVAS_HEIGHT = PATCH_SIZE * 2

# def main():
#     canvas = Canvas(CANVAS_WIDTH, CANVAS_HEIGHT)
#     # draw the first row of patches
#     draw_square_patch(canvas, 0, 0)
#     draw_circle_patch(canvas, PATCH_SIZE, 0)
#     draw_square_patch(canvas, PATCH_SIZE*2, 0)
#     draw_circle_patch(canvas, PATCH_SIZE*3, 0)
#     # TODO: your code here
#     draw_circle_patch(canvas, 0, PATCH_SIZE)
#     draw_square_patch(canvas, PATCH_SIZE, PATCH_SIZE)
#     draw_circle_patch(canvas, PATCH_SIZE*2, PATCH_SIZE)
#     draw_square_patch(canvas, PATCH_SIZE*3, PATCH_SIZE)

    
# def draw_circle_patch(canvas, start_x, start_y):
#     # TODO: your code here
#     end_x = start_x + PATCH_SIZE
#     end_y = start_y + PATCH_SIZE
#     canvas.create_oval(start_x, start_y, end_x, end_y, 'salmon')

# def draw_square_patch(canvas, start_x, start_y):
#     # draws a purple frame at (start_x, start_y)
#     end_x = start_x + PATCH_SIZE
#     end_y = start_y + PATCH_SIZE
#     inset = 20
#     # first draw a purple square over the entire patch
#     canvas.create_rectangle(start_x, start_y, end_x, end_y, 'purple')
#     # then draw a smaller white square on top
#     canvas.create_rectangle(start_x+inset, start_y+inset, 
#         end_x-inset, end_y-inset, 'white')
    
# if __name__ == '__main__':
#     main()

# from tkinter import *
# from tkinter import ttk


# root = Tk()
# frm = ttk.Frame(root, padding=10)
# frm.grid()
# ttk.Label(frm, text="Hello World!").grid(column=0, row=0)
# ttk.Button(frm, text="Quit", command=root.destroy).grid(column=1, row=0)


# # --- MAIN LOOP --- GOES LAST --- #
# root.mainloop()

# import tkinter as tk

# class App(tk.Frame):
#     def __init__(self, master):
#         super().__init__(master)
#         self.pack()

#         self.entrythingy = tk.Entry()
#         self.entrythingy.pack()

#         # Create the application variable.
#         self.contents = tk.StringVar()
#         # Set it to some value.
#         self.contents.set("this is a variable")
#         # Tell the entry widget to watch this variable.
#         self.entrythingy["textvariable"] = self.contents

#         # Define a callback for when the user hits return.
#         # It prints the current value of the variable.
#         self.entrythingy.bind('<Key-Return>',
#                              self.print_contents)

#     def print_contents(self, event):
#         print("Hi. The current entry content is:",
#               self.contents.get())

# root = tk.Tk()
# myapp = App(root)
# myapp.mainloop()


# import tkinter as tk

# class App(tk.Frame):
#     def __init__(self, master=None):
#         super().__init__(master)
#         self.pack()

# # create the application
# myapp = App()

# #
# # here are method calls to the window manager class
# #
# myapp.master.title("My Do-Nothing Application")
# myapp.master.maxsize(1000, 400)

# # start the program
# myapp.mainloop()


# text = open('sometext.txt', 'r+')
# keyword = " i "
# keyword2 = "-i-"
# replacement = " I "
# replacement2 = "-I-"

# for line in text:    
#     if keyword in line:
#         text.write(line.replace(keyword, replacement))
#         print(line)
#     elif keyword2 in line:
#         text.write(line.replace(keyword2, replacement2))
#         print(line)
#     else:
#         print(line)
# text.close()

# Moving Square

# from graphics import Canvas
# import time

# CANVAS_WIDTH = 400
# CANVAS_HEIGHT = 400
# SQUARE_SIZE = 40
# VELOCITY = 2
# DELAY = 0.01

# def main():
#     canvas = Canvas(CANVAS_WIDTH, CANVAS_HEIGHT)
#     start_x = 0
#     start_y = CANVAS_HEIGHT / 2 - SQUARE_SIZE / 2
#     square = canvas.create_rectangle(start_x, start_y,
#                     SQUARE_SIZE,
#                     start_y + SQUARE_SIZE)
                    
#     while (start_x + SQUARE_SIZE / 2) < (CANVAS_WIDTH / 2):
#         start_x += VELOCITY
#         print("x:", start_x)
#         canvas.moveto(square, start_x, start_y)
#         time.sleep(DELAY)
        
#     print("Done!")

# if __name__ == '__main__':
#     main()


# from graphics import Canvas
# import time

# CANVAS_WIDTH = 400
# CANVAS_HEIGHT = 450
# BALL_DIAMETER = 30
# INITIAL_VELOCITY = 5
# START_X = 0
# START_Y = 0
# DELAY = 0.001

# def main():
#     canvas = Canvas(CANVAS_WIDTH, CANVAS_HEIGHT)
#     x_velocity = INITIAL_VELOCITY
#     y_velocity = INITIAL_VELOCITY
#     ball_x = START_X
#     ball_y = START_Y
#     ball = canvas.create_oval(ball_x, ball_y,
#                               ball_x + BALL_DIAMETER,
#                               ball_y + BALL_DIAMETER,
#                               'blue')
                              
#     while True:
#         if (ball_x < 0) or (ball_x + BALL_DIAMETER >= CANVAS_WIDTH):
#             x_velocity = -x_velocity
#         if (ball_y < 0) or (ball_y + BALL_DIAMETER >= CANVAS_HEIGHT):
#             y_velocity = -y_velocity
#         ball_x += x_velocity
#         ball_y += y_velocity
#         canvas.moveto(ball, ball_x, ball_y)
#         time.sleep(DELAY)

# if __name__ == '__main__':
#     main()

# # Mouse Tracker
# from graphics import Canvas
# import time

# CANVAS_SIZE = 400
# PAUSE_TIME = 1/50

# def main():
#     canvas = Canvas(CANVAS_SIZE, CANVAS_SIZE)
#     while True:
#         mouse_x = canvas.get_mouse_x()
#         mouse_y = canvas.get_mouse_y()
#         time.sleep(PAUSE_TIME)
#         print("Mouse location: (" + str(mouse_x) + ", " + str(mouse_y) + ")")

# if __name__ == '__main__':
#     main() 


from graphics import Canvas
import random

CANVAS_WIDTH = 300
CANVAS_HEIGHT = 300
CIRCLE_SIZE = 20
DELAY = 0.05

def main():
    canvas = Canvas(CANVAS_WIDTH, CANVAS_HEIGHT)
    # your animation code here :)
    while True:
        mouse_location = locate_mouse(canvas)
        print(mouse_location)
        if is_inside(mouse_location):
            draw_circle(canvas, mouse_location[0], mouse_location[1], CIRCLE_SIZE, random_color(), random_color())
        else:
            continue
        time.sleep(DELAY)
        

def locate_mouse(canvas):
    mouse_x = canvas.get_mouse_x()
    mouse_y = canvas.get_mouse_y()
    return(mouse_x, mouse_y)
    
def draw_circle(canvas, left_x, top_y, size, color, outline):
    canvas.create_oval(left_x, top_y, left_x + size, top_y + size, color, outline)
    
def is_inside(mouse_location):
    if mouse_location[0]<0 or mouse_location[1]<0:
        return False
    elif (mouse_location[0]+CIRCLE_SIZE)>300 or (mouse_location[1]+CIRCLE_SIZE)>300:
        return False
    return True
    
def random_color():
    color_list = ['red', 'blue', 'green', 'yellow', 'beige', 'purple', 'brown', 'orange', 'pink', 'cyan', 'magenta']
    return random.choice(color_list)

if __name__ == "__main__":
    main()
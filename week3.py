import random

def main():
    print("Khansole Academy")
    # TODO: your code here
    def my_ints():
        a = random.randint(10, 100)
        b = random.randint(10, 100)
        return(a, b)
    
    my_sum = my_ints()
    correct = my_sum[0] + my_sum[1]
    
    print(f'What is {my_sum[0]} + {my_sum[1]}?' )
    
    answer = int(input('Your answer: '))
    
    if answer == correct:
        print('Correct!')
    else:
        print('Incorrect.')
        print(f'The expected answer is {correct}')

main()

# from graphics import Canvas
# import random

# CANVAS_WIDTH = 450
# CANVAS_HEIGHT = 300

# def main():
#     canvas = Canvas(CANVAS_WIDTH, CANVAS_HEIGHT)
#     # TODO, your code here
#     canvas.create_rectangle(0, 0, 450, 100, "cyan")
#     canvas.create_rectangle(0, 200, 450, 300, "cyan")
    
#     canvas.create_oval(190, 115, 260, 185, "yellow" )
    

# if __name__ == '__main__':
#     main()

# from graphics import Canvas
# import random

# CANVAS_WIDTH = 400
# CANVAS_HEIGHT = CANVAS_WIDTH
# N_ROWS = 8
# N_COLS = N_ROWS
# SIZE = CANVAS_WIDTH / N_ROWS

# def main():
#     canvas = Canvas(CANVAS_WIDTH, CANVAS_HEIGHT)
#     for r in range(N_ROWS):
#         for c in range(N_COLS):
#             draw_square(canvas, r, c)
            
# def draw_square(canvas, r, c):
#     print(r, c)
#     color = get_color(r, c)
#     x = c * SIZE
#     y = r * SIZE
#     end_x = x + SIZE
#     end_y = y + SIZE
    
#     canvas.create_rectangle(x, y, end_x, end_y, color, 'black')
            
        
# def get_color(r, c):
#     if is_even(r+c):
#         return "green"
#     else:
#         return "beige"
        
# def is_even(value):
#     return value % 2 == 0
            
# if __name__ == '__main__':
#     main()


import random as rd
import turtle as t

t.bgcolor('yellow')

caterpillar = t.Turtle()
caterpillar .shape('square')
caterpillar .color('red')
caterpillar .speed(0)
caterpillar .penup()
caterpillar .hideturtle()

leaf = t.Turtle
leaf_shape[(0,0),(14,2),(18,6),(20,20),(6,18),(2,14)]
t.register_shape('leaf', leaf_shape)
leaf .shape('leaf')
leaf .color('green')
leaf .penup()
leaf .hideturtle()
leaf .speed()

game_started = False
text_turtle = t.Turtle()
text_turtle.write('Press SPACE key to start a game',align='center',font=('Arial',16,'bold'))
text_turtle .hideturtle()

score_turtle = t.Turtle()
score_turtle.hideturtle()
score_turtle>speed(0)

def outside_window():
    left_wall = -t.window_width()/2
    right_wall = t.window_width()/2
    top_wall = t.window_width()/2
    bottom_wall = -t.window_height()/2
    (x, y) = caterpillar.pos()
    oustside = x < left_wall or x > right_wall or y > top_wall or y <  bottom_wall 
    return outside

def game_over():
    caterpillar .color('yellow')
    leaf.color('yellow')
    t.penup()
    t.hideturtle()
    t.write('GAME OVER ', align='center', font=('Aerial', 30, 'normal'))

def display_score():
    score_turtle.clear( )
    score_turtle.penup()
    x = (t.window_width() / 2)-50
    y = (t.window_height() / 2)-50
    score_turtle.setpos(x,y)
    score_turtle.write(str(current_score) , align = 'right',font=('Arial',40,'bold'))




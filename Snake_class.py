from turtle import Turtle
starting_postion=[(0,0),(-20,0),(-40,0)]
Move_distance=20
UP=90
DOWN=270
LEFT=180
RIGHT=0
class Snake:
        
    def __init__(self):
        self.all_snake_part=[]
        self.create_snake()
        self.head=self.all_snake_part[0]
    def create_snake(self):
        for snake_cre in starting_postion:
            self.add_sanke_part(snake_cre)
            
    def add_sanke_part(self,snake_cre):
        tim=Turtle(shape="square")
        tim.color("white")
        tim.penup()
        tim.goto(snake_cre)
        self.all_snake_part.append(tim)

    def reset(self):
        for seg in self.all_snake_part:
            seg.goto(10000,10000)
        self.all_snake_part.clear() 
        self.create_snake()
        self.head=self.all_snake_part[0]


    def extend(self):
        self.add_sanke_part(self.all_snake_part[-1].position())
    def move(self):
                for seg_snake_part in range(len(self.all_snake_part)-1,0,-1):
                    new_x=self.all_snake_part[seg_snake_part-1].xcor()
                    new_y=self.all_snake_part[seg_snake_part-1].ycor() 
                    self.all_snake_part[seg_snake_part].goto(new_x,new_y)
                self.head.fd(Move_distance)

    def up(self):
        if self.head.heading()!=DOWN:
            self.head.setheading(UP) 

    def left(self):
        if self.head.heading()!=RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading()!=LEFT:
           self.head.setheading(RIGHT)

    def down(self):
        if self.head.heading()!=UP:
           self.head.setheading(DOWN)                       

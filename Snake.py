from turtle import Turtle,Screen
# import time
screen = Screen()
positions = [(0,0),(-20,0),(-40,0)]
MOVE_DISTANCE = 20
class Snake1():
    
    def __init__(self):
        
        
        self.segments = []
        
        self.make_snake()
        self.head = self.segments[0]
        
    def make_snake(self):    
        for i in positions:
            self.add_segment(i)
            
    def reset_snake(self):
        for seg in self.segments:
            seg.goto(1000,1000)
        self.segments.clear()
        self.make_snake()
        self.head = self.segments[0]
         
            
    def add_segment(self,position):
            turtle =Turtle("square")
            turtle.color("white")
            turtle.penup()
            turtle.goto(position)
            
            self.segments.append(turtle)  
            
    def extend(self):
        self.add_segment(self.segments[-1].position())
    
    def move(self):
       
    
        for seg in range(len(self.segments) - 1,0,-1):
            new_x = self.segments[seg-1].xcor()
            new_y = self.segments[seg-1].ycor()
            self.segments[seg].goto(new_x,new_y)
        
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != 270:
            self.head.setheading(90)
        
    def down(self):
        if self.head.heading() != 90:
            self.head.setheading(270)   

    def left(self):
        if self.head.heading() != 0:
            self.head.setheading(180)
        
    def right(self):
        if self.head.heading() != 180:
            self.head.setheading(0)
        
from turtle import Turtle,Screen
from snack import Snake
from food import Food
from scoreboard import Scoreboard
import time
window = Screen()
window.setup(800,800)
window.bgcolor("black")
window.title("Snake Game")
window.tracer(0)

snakes = Snake()
food = Food()
score = Scoreboard()
game_on = True


while game_on:
    snakes.move()
    window.update()
    time.sleep(0.1)
    window.listen()
    window.onkey(snakes.up,"Up")
    window.onkey(snakes.down,"Down")
    window.onkey(snakes.right,"Right")
    window.onkey(snakes.left,"Left")
    if snakes.head.distance(food) < 15:
        food.apper()
        snakes.extend()
        score.increase_score()
    if snakes.head.xcor() > 370 or snakes.head.xcor() < -370 or snakes.head.ycor() > 370 or snakes.head.ycor() < -370:
        game_on = False
        score.game_over()

    
   

window.exitonclick()


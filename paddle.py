from turtle import *
import random
from time import sleep
from padle import Paddle
from ball import Ball
from scoreboard import Scoreboard
window=Screen()
window.setup(width=800,height=600)
window.bgcolor("black")
window.listen()
window.tracer(0)
penny=Paddle((350,0))
pep=Paddle((-350,0))
balon=Ball()
tablo=Scoreboard()
window.onkey(penny.move_forward,"w")
window.onkey(penny.move_backward,"s")
window.onkey(pep.move_forward,"Up")
window.onkey(pep.move_backward,"Down")
game_on=True
sleep_time=0.1
while game_on :
    window.update()
    sleep(sleep_time)
    ## u can also develeop the speed  To do
    balon.move()
    if balon.xcor() < -350:
        balon.spawn()
        tablo.y_score+=1
        tablo.inscrease()
    elif balon.xcor() > 350:
        balon.spawn()
        tablo.x_score+=1
        tablo.inscrease()
    if balon.ycor() >280 or balon.ycor() < -280:
        balon.bounce()
    if balon.distance(pep) < 50 and balon.xcor() < -330  or  balon.distance(penny) < 50 and balon.xcor() >330 :
        balon.bounce_paddle()
        sleep_time *=0.9
 
 
   



#Space Invador - part 1
#Set up the screen 

import turtle
import math
import random
import winsound

#setting up the screen
wn = turtle.Screen()
wn.bgcolor('black')
wn.title("SPACE INVADERS")
wn.bgpic('stars.gif')
wn.tracer(0)

#adding images in turtle
turtle.register_shape('invader.gif')
turtle.register_shape('hello.gif')

#drawing a border 
borderPen= turtle.Turtle()
borderPen.speed(0)
borderPen.color('cyan')
borderPen.penup()
borderPen.setposition(-300,-256)
borderPen.pendown()
borderPen.pensize(3)
for side in range(4):
    if side%2==0: #x side
        borderPen.fd(290)
        borderPen.fd(308)
    else: #y side
        borderPen.fd(250)
        borderPen.fd(259)
    borderPen.lt(90)
borderPen.hideturtle()
#scoring 
score=0
score_pen=turtle.Turtle()
score_pen.speed(0)
score_pen.color('white')
score_pen.penup()
score_pen.setposition(-290,255)
scorestring='Score=%s'%score
score_pen.write(scorestring,False,align='left',font=('Arial',14,'normal'))
score_pen.hideturtle()

title_pen=turtle.Turtle()
title_pen.speed()
title_pen.color('white')
title_pen.penup()
title_pen.setposition(0,260)
title_pen.write('Space Invader',False,align='center',font=('Arial',20,'normal'))
title_pen.hideturtle()

#create the player turtle

player=turtle.Turtle()
player.color('yellow')
player.shape('hello.gif')
player.penup()
player.speed(0)
player.setposition(0,-215)
player.setheading(90)

player.speed=1

#choosing a number of enemies 
number_of_enemies = 10
#creating an empty list of enemies
enemies=[]

#add enemies to the list 
for i in range(number_of_enemies):
    #create the array
    enemies.append(turtle.Turtle())
enemy_start_x=-225
enemy_start_y=225
enemy_number=1
for enemy in enemies:
    enemy.color('red')
    enemy.shape('invader.gif')
    enemy.penup()
    enemy.speed(0)
    x=enemy_start_x+(50*enemy_number)
    y=enemy_start_y
    enemy.setposition(x,y)
    if enemy_number==10:
        enemy_start_y-=50
        enemy_number=0
    enemy_number+=1
    

enemySpeed=0.1

#creating the player's bullet
bullet= turtle.Turtle()
bullet.color('white')
bullet.shape('triangle')
bullet.penup()
bullet.speed(0)
bullet.setheading(90)
bullet.shapesize(0.5,0.5)
bullet.hideturtle()

bulletSpeed=3

#define bullet state 
#ready-  ready to fire 
#fire- bullet is firing 
bulletstate='ready'


# Moving the player to left 
def moveLeft():
    player.speed=-1

# Moving the player to right 
def moveRight():
    player.speed=1

def movePlayer():
    x=player.xcor()
    x+=player.speed
    if x>280:
        x=280
    if x<-280:
        x=-280
    player.setx(x)
    pass

def isCollision(t1,t2):
    distance=math.sqrt(math.pow(t1.xcor()-t2.xcor(),2)+math.pow(t1.ycor()-t2.ycor(),2))
    if distance<15:
        return True
    else:
        return False

def FireBullet():
    #Declare bullet state as global if it need changed
    global bulletstate
    

    #move the bullet to the just above the player
    if bulletstate=='ready':
        bulletstate='fire'
        winsound.PlaySound('Lazer',winsound.SND_ASYNC)
        x=player.xcor()
        y=player.ycor()+10
        bullet.setposition(x,y)
        bullet.showturtle()

#Create keyboard binding
turtle.listen()
turtle.onkey(moveLeft,"Left")
turtle.onkey(moveRight,"Right")
turtle.onkey(FireBullet,'space')

gameOver=False


enemy_dead_count=0


#main game loop
while True:

    wn.update()

    movePlayer()


    for i in range(len(enemies)):
        #move the enemy
        x = enemies[i].xcor()
        x+= enemySpeed
        enemies[i].setx(x) 

        #Move enemy back and down
        if enemies[i].xcor()>280 or enemies[i].xcor()<-280:        
            for e in enemies:
                y = e.ycor()
                y -= 40
                e.sety(y)
            enemySpeed *= -1
            
    #cheak for a collision between the bullet and enemy
        if isCollision(bullet,enemies[i]):
            #reset the bullet 
            bullet.hideturtle()
            bulletstate='ready'
            bullet.setposition(0,-400)
            #counting the dead enemy
            enemy_dead_count+=1 

            winsound.PlaySound('oof',winsound.SND_ASYNC)
            enemies[i].setposition(0,10000)  
            #Update the score 
            score_pen.clear()
            score+=10
            scorestring='Score=%s'%score
            score_pen.write(scorestring,False,align='left',font=('Arial',14,'normal')) 
        if isCollision(player,enemies[i]):
            player.hideturtle()
            enemies[i].hideturtle()
            wn.bgpic('roll.gif')
            winsound.PlaySound('rickroll',winsound.SND_ASYNC)
            gameOver=True
            print("GAME OVER!")
            break 
    #breaking out of the loop after winning the game
    
    #breaking out of the loop after losing the game
    if(gameOver or (enemy_dead_count==number_of_enemies)):
        break

    if bulletstate=='fire':    
        y=bullet.ycor()
        y+= bulletSpeed
        bullet.sety(y)

    #cheake to see if the bullet has gone to the top
    if bullet.ycor()>250:
        bullet.hideturtle()
        bulletstate='ready'

    


if(enemy_dead_count==number_of_enemies):
    won=turtle.Turtle()
    won.speed(0)   
    won.color('orange')
    won.penup()
    won.setposition(0,0)
    won.write("YOU WON!!",False,align='center',font=('Ariel',30,'bold'))
    won.hideturtle()


        
    








   






delay= input('Press enter to finish.')
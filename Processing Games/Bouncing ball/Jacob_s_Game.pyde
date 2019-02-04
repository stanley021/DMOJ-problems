ball_horizontal = 400
ball_vertical = 350
speedX = random(3,5)
speedY = random(3,5)
num_of_power = 0
power_vertical = -1
game = 0
hits = 0
score = 0
restart = 1
blocks = [[0,175,True,False],[100,175,True,False],[200,175,True,False],[300,175,True,False],[400,175,True,False],[500,175,True,False],[600,175,True,False],[700,175,True,False],[20,200,True,False],[120,200,True,False],[220,200,True,False],[320,200,True,False],[420,200,True,False],[520,200,True,False],[620,200,True,False],[720,200,True,False], [10,250,True,False],[110,250,True,False],[210,250,True,False],[310,250,True,False],[410,250,True,False],[510,250,True,False],[610,250,True,False],[710,250,True,False]]
paddlex = 400
def setup():
    global sound1, sound2,this, SoundFile
    size(800,600);
    frameRate(60)
    #sound1 = SoundFile(this,"Sound1.wav")
    #sound2 = SoundFile(this,"Sound2.wav")
def draw():
    global ball_vertical, ball_horizontal, gravity, speedX, speedY, game, blocks, hits, score, restart, num_of_power, paddlex
    background (255)
    stroke(0)
    strokeWeight(2)
    textSize(26)
    text(score,700,50)
    line(0,100,800,100)
    strokeWeight(7)
    if num_of_power == 0:
        power = random(0,24)
        power = int(power)
        blocks[power][3] = True
        num_of_power = 1
    elif num_of_power == 1:
        pass

    if game == 0 or game == 1:
        line(paddlex-50,575,50+paddlex,575)
    if restart == 1:
        fill(0)
        ellipse(ball_horizontal,ball_vertical,25,25)
        #draw blocks

        if game == 1:

            ball_horizontal += speedX
            ball_vertical += speedY

            if ball_vertical >= 558 and ball_horizontal >= paddlex-48 and ball_horizontal <= paddlex+52:
                #sound2.amp(100)
                #sound2.play
                speedY = speedY * random(-1.05,-1.03)

            elif ball_vertical <= 162:
                speedY = speedY * random(-1.05,-1.03)

            elif ball_horizontal <= 12.5 or ball_horizontal >= 788.5:
                speedX = speedX * -1

            elif ball_vertical >= 600:
                restart = 0
        elif game == 0:
            if score == 0:
                text("Press s on the screen to play",200,80)
        elif game == 2:
                text("Press s on the screen to resume the game", 125,80)


        if key == "a":
            paddlex = paddlex - 6
        #move paddle right
        if key == "d":
            paddlex = paddlex + 6



    elif restart == 0:
        text("gameover",500,50)
        strokeWeight(2)
        fill(255)
        rect(100,50,120,30)
        fill(0)
        text("restart",110,75)
        textSize(26)
        text(score,700,50)


def keyPressed():
    global game
    if game == 1:
        if key == 's':

            game = 2
    elif game == 0:
        if key == 's':

            game = 1
    elif game == 2:
        if key == 's':
            game = 1



def mousePressed():
    global ball_vertical, ball_horizontal, gravity, speedX, speedY, game, blocks, hits, score, restart
    if restart == 0:
        if 100 < mouseX < 220 and 50 < mouseY < 80:

            restart = 1
            ball_horizontal = 400
            ball_vertical = 350
            speedX = random(3,5)
            speedY = random(3,5)
            game = 0
            hits = 0
            score = 0
            for n in range(0,24):
                blocks[n][2] = True

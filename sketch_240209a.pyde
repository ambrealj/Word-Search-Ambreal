import string

game_pages=0
game_levels={0:"Welcome",1:"Easy",2:"Medium",3:"Hard"}
moveX = moveY = dragX = dragY = -20

word_list_easy = ["waolosa", 
                  "ebnkeei", 
                  "yinapae", 
                  "lywekjl", 
                  "sokeail",
                  "buawhon",
                  "lavurcx"]
words_easy =  ["luke", "leia", "solo", "chewie", "anakin"]
word_list_medium = ["ewgdqhibo", 
                    "rhyddusbe",
                    "afseuceei",
                    "ludurhmeu",
                    "gikaloidn",
                    "rvnhplrrh",
                    "jerxmegoq",
                    "sntvgirlw",
                    "tkzseixip"]
words_medium = ["ride", "glare", "lush", "pixies", "cranes", "hole", "queen", "tvgirl", "lorde", "grimes"]
word_list_hard = ["djkjfccevmca",
                  "rgamobabqaav",
                  "twibgyrsueia",
                  "senemyrtdrdt",
                  "ohcyspivscoa",
                  "nuhwjuenrszr",
                  "lexahfayljcx",
                  "blvshtkswjlq",
                  "oraecleonroc",
                  "mrihsamnedsi",
                  "cxtcxirtamef",
                  "kfokkvhbavro"]
                  
words_hard = ["psycho", "jaws", "carrie", "jfk", "leon", "crash", "scream", "seven", "matrix", "snatch", "closer", "brick", "zodiac", "avatar", "enemy"]

def setup(): 
    size(800,800)
    frameRate(100)
    background(100)
    noStroke()

def draw():     
    global moveX, moveY, dragX, dragY
    stroke(255,0,0,3)
    fill(255,0,0,3)
    ellipse(dragX, dragY, 20, 20)  
    if game_pages==0:
        welcome_display()
        fill(255)
        ellipse(moveX, moveY, 20, 20) 
        stroke(255,0,0)
        strokeWeight(8)
    elif (game_pages ==1 and mousePressed): 
        strokeWeight(5)
        if 300<dragY<350 and 50<dragX<150 :
            line(25, 325, 175, 325)
            line(400, 95, 450, 95)
        elif 150<dragY<250 and 0<dragX<50 :
            line(25, 125, 25, 275)
            line(400, 145, 450, 145)
        elif 300 <dragX<350 and 0<dragY<50:
            line(325, 25, 175, 175)
            line(400, 45, 450, 45)
        elif 250 <dragX<300 and 300<dragY<350:
            line(25, 75, 275, 325)
            line(400, 245, 450, 245)
        elif 50 <dragX<100 and 0<dragY<50:
            line(325, 275, 75, 25)
            line(400, 195, 450, 195)              
    elif (game_pages ==2 and mousePressed): 
        if 0<dragY<50 and 0<dragX<50 :      
            line(25, 25, 225, 25)   
            line(500, 95, 550, 95)               
        elif 200<dragY<250 and 0<dragX<50 :      
            line(25, 225, 225, 425) 
            line(500, 345, 550, 345)                   
        elif 50<dragY<100 and 50<dragX<100 :      
            line(75, 75, 225, 225)  
            line(500, 145, 550, 145)         
        elif 50<dragY<100 and 200<dragX<250 :      
            line(275, 25, 125, 175)  
            line(500, 45, 550, 45)               
        elif 0<dragY<50 and 350<dragX<400 :      
            line(375, 25, 125, 275)
            line(500, 245, 550, 245)               
        elif 250<dragY<300 and 250<dragX<300 :      
            line(175,275, 325, 275) 
            line(500, 296, 550, 295)               
        elif 300<dragY<350 and 200<dragX<250 :      
            line(75, 325, 325, 325)  
            line(500, 495, 550, 495)               
        elif 350<dragY<400 and 250<dragX<300 :      
            line(175, 375, 375, 375) 
            line(500, 445, 550, 445)               
        elif 100<dragY<150 and 350<dragX<400 :      
            line(375, 125, 375, 375) 
            line(500, 395, 550, 395)               
        elif 150<dragY<200 and 400<dragX<450 :      
            line(425, 175, 425, 425) 
            line(500, 195, 550, 195)         
    elif (game_pages ==3 and mousePressed): 
        if 150<dragY<200 and 0<dragX<50 :
            line(25, 175, 175, 25)
            line(650, 95, 700, 95)
        elif 300<dragY<350 and 0<dragX<50 :
            line(25, 325, 275, 325)
            line(650, 145, 700,145)              
        elif 450<dragY<500 and 0<dragX<50 :
            line(25, 475, 275, 475)
            line(650, 345, 700,345)              
        elif 500<dragY<550 and 0<dragX<50 :
            line(25, 525, 275, 525)
            line(650, 645, 700,645)        
        elif 550<dragY<600 and 0<dragX<50 :
            line(25, 575, 275, 575)
            line(650, 695, 700,695)        
        elif 200<dragY<250 and 150<dragX<200 :
            line(175, 75, 175, 275)
            line(650, 745, 700,745)        
        elif 0<dragY<50 and 200<dragX<250 :
            line(225, 25, 225, 275)
            line(650, 45, 700,45)        
        elif 200<dragY<250 and 250<dragX<300 :
            line(275, 225, 375, 325)
            line(650, 195, 700,195)              
        elif 50<dragY<100 and 300<dragX<350 :
            line(275, 25, 475, 225)
            line(650, 395, 700,395)              
        elif 0<dragY<50 and 500<dragX<550 :
            line(525, 25, 325, 225)
            line(650, 295, 700,295)              
        elif 200<dragY<250 and 550<dragX<600 :
            line(375, 25, 575, 225)
            line(650, 595, 700,595)              
        elif 400<dragY<450 and 200<dragX<250 :
            line(225, 425, 475, 175)
            line(650, 495, 700,495)              
        elif 400<dragY<450 and 400<dragX<450 :
            line(425, 275, 425, 425)
            line(650, 245, 700,245)        
        elif 450<dragY<500 and 500<dragX<550 :
            line(525, 475, 525, 225)
            line(650, 445, 700,445)
        elif 500<dragY<550 and 550<dragX<600 :
            line(325, 525, 575, 525)
            line(650, 545, 700,545)
      
def mouseMoved(): 
    global moveX, moveY
    moveX = mouseX
    moveY = mouseY

def mouseDragged():   
    global dragX, dragY
    dragX = mouseX
    dragY = mouseY

def welcome_display():
    background("#FFCCE5")
    stroke(255)
    fill("#FF3399")
    textSize(60)
    text("Word Search Game", 125, 200)
    textSize(20)
    text("Drag/press down on your mouse over the entirety of each word", 125, 400)
    text("Select your difficulty level below:", 125, 450)
    strokeWeight(2)
    rect(100,500,200,80)
    rect(300,500,200,80)
    rect(500,500,200,80)
    fill("#FFCCE5")
    text ("Easy: Star Wars", 125,545)
    text ("Medium: Music", 325,545)
    text ("Hard: Films", 525,545)
    fill("#FF3399")
    text ("9x9 - 10 words", 325,610)
    text ("7x7 - 5 words", 125,610)
    text ("12x12 - 15 words", 525,610)
    if mousePressed: 
        if( 100<mouseX<300 and 500<mouseY<580):
            game_pages=1
            easy_display()
        elif( 300<mouseX<500 and 500<mouseY<580):
            game_pages=2
            medium_display()
        elif( 500<mouseX<700 and 500<mouseY<580):
            game_pages=3
            hard_display()

def easy_display():
    global game_pages
    game_pages=1
    draw_words(1)

def medium_display():
    global game_pages
    game_pages=2
    draw_words(2)
         
def hard_display():
    global game_pages
    game_pages=3
    draw_words(3)

def draw_grid(game_level):
    stroke(192,192,192)
    strokeWeight(1)
    if (game_level==1):
        background("#CCE5FF")
        for x in range(7):
            line(0, x*50,350,x*50) 
            line(x*50, 0, x*50,350)
        line(0, 350,350, 350)
        line(350,0,350, 350)
    elif (game_level==2):
        background("#E5CCFF")
        for x in range(9):
            line(0, x*50,450,x*50) 
            line(x*50, 0, x*50,450)
        line(0, 450,450, 450)
        line(450,0,450, 450)
    elif (game_level==3):
        background("#CCCCFF")
        for x in range(12):
            line(0, x*50,600,x*50) 
            line(x*50, 0, x*50,600)
        line(0, 600, 600, 600)
        line(600,0,600, 600)

def draw_words(game_level): 
    textSize(16)
    if (game_level==1):
        draw_grid(1)
        fill("#001933")
        text ("Easy: Star Wars", 325,650)
        text ("7x7 - 5 words", 325,700)
        for x in range(5):
            text(words_easy[x], 400, 50+(50*x))
        for x in range(7):
            for y in range(7):
                text(word_list_easy[x][y],(x*50)+25, (y*50)+25)
    elif (game_level==2):
        draw_grid(2)
        fill("#190033")
        text ("Medium: Music", 325,650)
        text ("9x9 - 10 words", 325,700)
        for x in range(10):
            text(words_medium[x], 500, 50+(50*x))
        for x in range(9):
            for y in range(9):
                text(word_list_medium[x][y],(x*50)+25, (y*50)+25)
    elif (game_level==3):
        draw_grid(3)
        fill("#000033")
        text ("Hard: Films", 325,650)
        text ("12x12 - 15 words", 325,700)
        for x in range(15):
            text(words_hard[x], 650, 50+(50*x))
        for x in range(12):
            for y in range(12):
                text(word_list_hard[x][y],(x*50)+25, (y*50)+25)

        

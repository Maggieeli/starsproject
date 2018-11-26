import random
stars = []
counter = 0

def setup():
    size(640, 480)

        
def draw():
    background(0)
    noStroke()
    fill(255)
    global stars
    global counter
    counter += 1
    
    if counter == 60:
        counter = 0
        y = random.randint(0,480)
        stars.append([-5,y])
    
    i = 0
    while i < len(stars):
        ellipse(stars[i][0], stars[i][1], 5, 5)
        stars[i][0] += 0.5
        i += 1

    i = 0 
    while i < len(stars):
        if [i][0] > 640:
            stars.remove(i)
        i += 1


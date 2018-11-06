# two lists with three stars' xy coordinates
# (50, 200), (100, 250), (150, 300)

stars_x = [50, 100, 150, 200, 250]
stars_y = [200, 250, 300, 350, 400]

def setup():
    size(640, 480)


def draw():
    background(0)
    
    # draw stars
    noStroke()
    fill(255)
    
    ellipse(stars_x[0], stars_y[0], 5, 5)
    ellipse(stars_x[1], stars_y[1], 5, 5)
    ellipse(stars_x[2], stars_y[2], 5, 5)
    ellipse(stars_x[3], stars_y[3], 5, 5)
    ellipse(stars_x[4], stars_y[4], 5, 5)

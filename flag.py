from flag_utils import *

width     = 720
height    = 480
numstar   = 4
pw        = 16 # pw,ph control size of points
ph        = 60
npoint    =  6  # num points on a star
barheight = 80
starRGB       = [   1,    0,    0] # red
barRGB        = [.702, .867, .949] # light-blue
backgroundRGB = [   1,    1,    0] # white

def setcolor(rgb):
    setrgbcolor(*rgb)

    

    
def background():
    setcolor(backgroundRGB)
    rectfill(0,0,width,height)

    
def bars():
    moveto(0,     120)
    rlineto(width, 0)

    moveto(0,     360)
    rlineto(width, 0)
  
    setlinewidth(barheight)
    setcolor(barRGB)
    stroke()

    
def point():
    "draw one point in a star (a triangle)"
    moveto(-pw, 0)
    rlineto(pw, ph)
    rlineto(pw, -ph)


def star():
    "draw one star"
    degrees = 360 / float(npoint)
    for i in range(npoint):
        point()
        rotate(degrees)


        
def stars():
    
    # compute horiz distance between stars
    # (equally spaced with pad 10 on both sides)
    # 
    sdist = (width - 20)/(numstar+1)

    # move to first:
    translate(10+sdist, height/2)
    for i in range(numstar):
        star()
        translate(sdist,0)

        
    setcolor(starRGB)
    fill()

    
if __name__ == "__main__":
    background()
    bars()
    stars()

    write_png("/tmp/py-flag.png", globals())

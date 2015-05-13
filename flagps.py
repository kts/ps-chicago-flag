"""
NOTE: this is not meant to be run.
It is meant to be be viewed side-by-side
with flag.ps to explain the PostScript code.
"""
numstar   = 4
width     = 720
height    = 480
pw        = 16
ph        = 60
star0     = 150
barheight = 80
redRGB    = [   1,    0,    0,]
blueRGB   = [.702, .867, .949,]

def setcolor(rgb):
    setrgbcolor(*rgb)

def bars():
    moveto(0,     120)
    rlineto(width, 0)

    moveto(0,     360)
    rlineto(width, 0)
  
    setlinewidth(barheight)
    setcolor(blueRGB)
    stroke()

def point():
    "draw one point for six-pointed star"
    moveto(-pw, 0)
    rlineto(pw, ph)
    rlineto(pw, -ph)

def star():
    "draw one star"
    for i in xrange(6):
        point()
        rotate(60)

def stars():
    #% compute horiz distance between stars
    #% (equally spaced with pad 10 on both sides)
    #% sdist = (width - 20)/(numstar+1)
    #/sdist width 20 sub numstar 1 add div def

    #10 sdist add height 2 div translate % move to first
    for i in xrange(numstar):
        star()
        translate(sdist,0)
   
    setcolor(redRGB)
    fill()

#---main---
bars()
stars()

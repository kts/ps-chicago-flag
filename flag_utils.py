"""
This is a set of tools and weird hacks to get
./flag.py to work and closely resemble ./flag.ps.

Here, we define functions that match some of the
PostScript operators (moveto, rectfill, setcolor, etc.).

ISSUES:
- ps bg color white?
- 'lw' in PathPatch are wrong units?
- subclassing 'matplotlib.transforms.Affine2D'
  lead to some weird problems.

"""
import matplotlib.pyplot as plt
from matplotlib.path import Path
import matplotlib.patches as patches
import matplotlib.transforms
import math

class Writer:
    def __init__(self):

        self.width = 720
        self.height = 480
        dpi = 100 #?
        self.dpi = dpi
        
        self.fig = plt.figure(figsize=(self.width/dpi,
                                       self.height/dpi),
                              dpi=dpi)

        self.ax = self.fig.add_axes((0,0,1,1))
        self.reset()

    def reset(self):

        self.x = 0
        self.y = 0

        #path data:
        self.vertices = []
        self.codes    = []

        #store 
        self.rotation_rad = 0
        self.tx = 0
        self.ty = 0
        
#global holds state of drawer
wr = Writer()

#def tr(pt):
#    return wr.transform(pt)

def moveto(x,y):
    """
    """
    t = matplotlib.transforms.Affine2D()
    t.rotate(wr.rotation_rad)
    t.translate(wr.tx, wr.ty)
    xx,yy = t.transform_point((x,y))
    
    wr.x = xx
    wr.y = yy
    wr.vertices.append((wr.x, wr.y))
    wr.codes.append(Path.MOVETO)

def rlineto(x,y):

    #ugly? rlineto shouldn't
    # include translation but should include rotation?

    # zero-out translation entries:
    #M = wr.transform.get_matrix().copy()
    #M[:2,2] = 0
    #wr0 = MyTransform(M)
    #dx,dy = wr0((x,y))

    tr = matplotlib.transforms.Affine2D()
    tr.rotate(wr.rotation_rad)
    dx,dy = tr.transform_point((x,y))

    #relative:
    wr.x += dx
    wr.y += dy
    
    wr.vertices.append((wr.x, wr.y))
    wr.codes.append(Path.LINETO)


def setlinewidth(lw):
    wr.linewidth = lw #default?

def setrgbcolor(r,g,b):
    wr.rgb = (r,g,b) #default?

def translate(dx,dy):
    wr.tx += dx
    wr.ty += dy

def rotate(theta):
    wr.rotation_rad += math.radians(theta)

def _add_patch(patch):
    wr.ax.add_patch(patch)
    wr.reset()

def fill():
    path = Path(wr.vertices, wr.codes)
    _add_patch(
        patches.PathPatch(
            path,
            facecolor = wr.rgb,
            edgecolor = 'none',
            lw = 1,
        ))

def rectfill(x,y,width,height):
    matplotlib.patches.Rectangle
    _add_patch(
        patches.Rectangle(
            (x,y),
            width,
            height,
            facecolor = wr.rgb,
            edgecolor = 'none',
            lw = 1,
        ))

def stroke():
    """
    """
    path = Path(wr.vertices, wr.codes)
    _add_patch(patches.PathPatch(
        path,
        facecolor = 'none',
        edgecolor = wr.rgb,
        lw = wr.linewidth,
    ))

def write_png(path, globals_):

    wr.ax.set_xbound((0, globals_['width']))
    wr.ax.set_ybound((0, globals_['height']))

    wr.ax.figure.savefig(path,dpi=wr.dpi)

    print("WROTE:", path)
    

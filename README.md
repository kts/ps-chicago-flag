# PostScript Chicago flag

`flag.ps` is a PostScript program to generate 
the [Chicago Flag](http://en.wikipedia.org/wiki/Flag_of_Chicago).
This is meant as a demo of the PostScript language.

Run (using convert utility from ImageMagick):

    $ convert -page 720x480 flag.ps flag.png

![flag](https://raw.githubusercontent.com/kts/ps-chicago-flag/master/flag.png)

View a Postscript / Python comparison of the code
[here](http://kenschutte.com/chipy-postscript/translated.html)

Note that it is written in a very parametric way. For example,
try changing some of the values at the top,

    /numstar 3 def
    /npoint  5 def
    /starRGB [1 .5 0] def
    /barRGB  [0  0 1] def

and run `convert` again to get a different result:

![flag](https://raw.githubusercontent.com/kts/ps-chicago-flag/master/mod.png)

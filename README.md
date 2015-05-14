# Postscript Chicago flag

`flag.ps` is a PostScript program to generate 
the [Chicago Flag](http://en.wikipedia.org/wiki/Flag_of_Chicago).
This is meant as a demo of the PostScript language.

Run (using convert utility from ImageMagick):

    $ convert -page 720x480 flag.ps flag.png

![flag](https://raw.githubusercontent.com/kts/ps-chicago-flag/master/flag.png)

View a Postscript / Python comparison of the code
[here](https://raw.githubusercontent.com/kts/ps-chicago-flag/master/translated.html)

Note that it is written in a very parametric way. For example,
try changing the first line,

    /numstar   4   def

to a different number and run `convert` again.

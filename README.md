
Code for the blog post [Learning PostScript by comparing it to Python](https://kenschutte.com/postscript-vs-python/)

Render the PostScript as a PNG image:

```
convert -page 720x480 flag.ps flag.png
```

Run the Python version (writes `/tmp/py-flag.png`):

```
python flag.py
```

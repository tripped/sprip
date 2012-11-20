sprip
=====

Rips sprites from a thing for no raisin.

Usage
-----

    python sprip.py <spritefile> <palettefile> [outformat]

Example:

    python sprip.py quarantine/wall1.spr quarantine/floor.img sample%02d.png

Produces a neat set of files:

    $ ls
    sample00.png
    sample01.png
    sample02.png
    sample03.png
    ...

![](https://raw.github.com/mraccident/sprip/master/sample00.png)
![](https://raw.github.com/mraccident/sprip/master/sample01.png)
![](https://raw.github.com/mraccident/sprip/master/sample02.png)
![](https://raw.github.com/mraccident/sprip/master/sample03.png)
...

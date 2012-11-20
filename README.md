sprip
=====

Rips sprites from a thing for no raisin.

Usage
-----

    python sprip.py <spritefile> <palettefile> [outformat]

Example:

    mkdir samples
    python sprip.py quarantine/wall1.spr quarantine/floor.img samples/%02d.png

Produces a neat set of files:

    $ ls samples
    00.png
    01.png
    02.png
    03.png
    ...

And the files are pretty, like so:

![](https://raw.github.com/mraccident/sprip/master/samples/00.png)  
![](https://raw.github.com/mraccident/sprip/master/samples/01.png)  
![](https://raw.github.com/mraccident/sprip/master/samples/02.png)  
![](https://raw.github.com/mraccident/sprip/master/samples/03.png) ...


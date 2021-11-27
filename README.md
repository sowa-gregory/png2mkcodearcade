# png2mkcodearcade

## Tool
Png2mkcodearcade is a tool to convert png images into textual image interpretation used by game creation platform MakeCode Arcade. 
Image colors are mapped onto 16 colors palettes used in the platform. Actually active colors are limited to 15 as palette at index 0 indicates trasparent pixel.
Mapping finds color from the pallete which has closest RGB values (shortest Euclidian distance in three dimensional space) for each image pixel.

Output of the tool is displayed on the console - you can just copy it and paste in MakeCode editor. For the reference **output.png** image is generated in the current directory to demonstrate color mapping results.

Alternative palette definition files can be used - for the format please refer to default.pal.json, which contains default MakeCode palette.

## Textual image format
Each text line represent one line of pixels in the image. Characters values 1-f refers to palette indexes.
Resolution of the image is deducted by MakeCode platform from length and number of text lines.
The platform uses global palette for each project, shared among all graphics assets.

Example of the bird sprite:
```
sprite = sprites.create(img`
3 2 2 2 . . . . 
4 3 2 2 . 2 2 . 
. 4 3 2 2 2 2 . 
. . 4 2 2 2 . . 
. 4 3 2 2 2 2 2 
. 4 3 3 4 3 2 2 
. . 4 4 . 4 3 2 
. . . . . . 4 3 
`)
```

## Alternative palettes in MakeCode
Per project palette in MakeCode Arcade is stored in 

## Usage
```
usage: png2makecodearcade.py [-h] [--pal PAL] image

positional arguments:
  image       image to convert

optional arguments:
  -h, --help  show this help message and exit
  --pal PAL   palette file
```



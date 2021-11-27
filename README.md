# png2mkcodearcade

## Tool
Tool to convert png images into textual image interpretation used by game creation platform MakeCode Arcade. 
Image colors are mapped onto 16 colors palettes used in the platform. Actually active colors are limited to 15 as palette at index 0 indicates trasparent pixel.
Mapping finds color from the pallete which has closest RGB values (shortest Euclidian distance in three dimensional space).

Alternative palette definition files can be used - for the format please refer to default.pal.json, which contains default MakeCode palette.

## Textual image format
Each text line represent one line of pixels in the image. Characters values 1-f refers to palette indexes.
Resolution of the image is deducted by MakeCode platform from length and number of text lines.
The platform uses global palette for each project, shared among all graphics assets.

## Alternative palettes in MakeCode
Per project palette in MakeCode Arcade is stored in 




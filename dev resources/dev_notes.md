# Dev Notes

## Information resoures
* INAV6 analog
  * github: https://github.com/iNavFlight/inav-configurator/tree/master/resources/osd/analogue
  * glyph dimensions: 12x18
  * bitmap dimensions: 209x609 = 192 + 17 1px dividers x 576 + 33 1px dividers
  * bitmap raster: 16 x 32 glyphs
  * logo
    * dimmension: 120x72 -> 10x4 glyphs
    * glyphs: 257-296

* BF analog
  * github: https://github.com/iNavFlight/inav-configurator/tree/master/resources/osd/analogue
  * glyph dimensions: 12x18
  * bitmap dimensions: 207x303 = 192 + 15 1px dividers x 288 + 15 1px dividers
  * bitmap raster: 16x16 glyphs
  * logo
    * dimmension: 288x72 -> 24x4 glyphs
    * glyphs: 160-255
    * logo for BF configurator: 288x72 bitmap, green is transparent

* MCM
  * format: https://www.analog.com/en/design-notes/generating-custom-characters-and-graphics-by-using-the-max7456s-memory-and-ev-kit-file-formats.html
  * glyph dimensions: 12x18
  * each pixel 2 bits -> one glyph row 3 bytes -> one glyph 54 bytes + 10 unused bytes
  * one glyph -> 64 rows in MCM file -> 16384 rows for 256 glyphs (BTFL), 32768 for 512 glyphs (INAV)
  * pixels
    * 00 - black
    * 10 - white
    * 01, 11 - transparent  

* HDZ VRX font
  * github: https://github.com/hd-zero/hdzero-osd-font-library

## HDZERO HD OSD Font Properties

* glyph dimensions: 24x36
* bitmap dimensions
  * 384x1152
  * 486x1350 ->  384 + 17 6px dividers x 1152 + 33 6px dividers
* bitmap raster: 16x32 glyphs
* BF
  * characters
  * glyphs
  * logo
    * dimmension: 576x144 -> 24x4 glyphs
    * transparency: color (127,127,127)
    * glyphs: 160-255
  * units
  * variables
  * numbers
  * letters
  * special characters
  * ...
* INAV
  * logo
    * dimmension: 240x144 -> 10x4 glyphs
    * transparency: color (127,127,127)
    * glyphs: 257-296

## TODOs

* gather info
  * [x] dimmensions, rasters etc. for all font variants
* initial tests
  * [x] command line arguments
  * [x] open image to Surface
    * [x] get image dimensions
    * [x] Surface from image work with transparency (color vs. alpha in PNG)
      * [x] zkusit otevrit image s transparenci a bez a zkusit metodu get_flags()
      * [x] zkusit otevrit image s transparenci a vnutit mu color key
  * [x] save Surface to BMP / PNG
  * [ ] open text file to read
  * [ ] parse MCM, draw font preview
  * [x] ttf font rendering - outline without antialias, inside antialiased character
  * [x] ttf font rendering - double size + smootscale a scale
* resource kit
  * [x] fix Pixlr template file
  * [x] example logos
  * [x] example fonts
  * [ ] example font parts
* Opening input file(s)
  * [ ] input file as argument
  * [ ] check if file exists
  * [ ] image / mcm ?
  * [ ] guess format

## Ideas

* Detect what the input files are
  * according to extension
    * is it image of allowed formats?
      * does it have known dimensions? -> assume what is it
    * is it MCM?
* Kopirovani glyphu z velke bitmapy pres Surface blit
* kazdy glyph je mala surfcace
* object Font
  * volitelny rozmer glyphu
  * volitelny rastr fontu
  * Font obsahuje 2D pole glyphu ? Nebo jen celou surface s metodami na vraceni glyphu a loga
  * Font metoda na vraceni Surface glyphu
  * Font metoda na vraceni Surface fontu
  * Font metoda na vraceni Surface loga
  * Font metoda ulozeni bitmapy fontu do souboru, volitelny spacing
  * Font metoda ulozrni bitmapy loga
  * Font init, volitelne na vstupu pripravena Surface, pak rozpad do glyphu
* Vyroba font Surface z:
  * image, detekce rozmeru (normal, exploded, analog bitmapa)
  * mcm
* Import loga
  * resize pokud potreba
  * detekce "zelene" bitmapy pro analog logo. Nastaveni transparence a double size
  * logo bf, inav (varianty)
* Presety na kopirovani glyphu z fontu do fontu
* * demo fontu, staticke a dynamicke 
  * Nad obrazkovym pozadim
  * Nad chess boardem
  * Nad kombinaci

### Command line concept

switches:
* -base
  * base OSD font file to be opened and act as a source for manipulation
  * can be image of different dimensions (autodetect what it might be)
  * can be MCM
* -blank
  * blank OSD font (blank grey surface)
* -logo
  * image to be scaled and sliced as boot / arming logo
* -numbers
* -letters
* -specials
* -values
* -units
* -ahi
* -compass
* -battery
  * OSD font file, the said part will be coppied a pasted to output font
* -ttf
  * .ttf font file for rendering all the characters
  * size
  * color, default (255,255,255)
  * outline, default (0,0,0)
  * outline_size, default ?
* -ttfnumbers
* -ttfletters
* -ttfletterslow
* -ttfspecials
  * .ttf font files for rendering of a subset of characters
* -o
  * output OSD font file

### General

* ? Python own private modules for different projects

## Tests

### Load image vs. transparency

* loading an image with transparency -> its surface has glag = pygame.SRCALPHA (65536)
* loading an image without transparency -> its surface has glag = pygame.SWSURFACE (0)
* adding a colorkey adds a transparency of the key to the existing alpha
* blitting with alpha and colorkey transparency
* saving to BMP -> transparent is alpha and colorkey
* saving to PNG -> transparent is alpha only
* conclusion -> open whatever, add grey colorkey transparency. Will be always OK

# Dev Notes

## Information resoures
* INAV analog
  * github
  * bitmap dimmensions
  * bitmap raster
  * logo
* BF analog
  * github
    * https://github.com/iNavFlight/inav-configurator/tree/master/resources/osd/analogue
  * bitmap dimmensions
  * bitmap raster
  * logo
* MCM
* HDZERO HD OSD
* BF HD font
* INAV HD font

## HDZERO HD OSD Font Properties

* glyph dimmensions
* bitmap dimmensions
* bitmap raster
* BF
  * characters
  * glyphs
  * logo
  * units
  * variables
  * numbers
  * letters
  * special characters
  * ...
* INAV


## TODOs

* gather info
  * [ ] dimmensions, rasters etc. for all font variants
* initial tests
  * [ ] open image to Surface
  * [ ] Surface from image work with transparency
  * [ ] save Surface to BMP / PNG
  * [ ] parse MCM


## Ideas
* Kopirovani glyphu z velke bitmapy pres Surface blit
* kazdy glyph je mala surfcace
* demo fontu, staticke a dynamicke 
  * Nad obrazkovym pozadim
  * Nad chess boardem
  * Nad kombinaci
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

### General
* ? Python own private modules for different projects

# HD OSD Font Tools

A tool for building and manipulating the HD OSD fonts for HDZERO VRXs and goggles. The initial version is supposed to build HD OSD fonts for the Betaflight (BTLF) FC variant. For the INAV6 FC variant the tool has a limited support to create the logo.

## Usage

The tool is command line based with a graphical preview of the built font. User can choose one or more sources to build the font.

The source can be:

- HDZERO OSD font (.bmp)
- true type font file (.ttf)
- Analog OSD font file (.mcm)
- Analog OSD font preview file (.png / .bmp)
- Generic bitmap, typically containing a logo (.png / .bmp / .jpg)

The source can be used as a part of the built font such as:

- all glyphs
- characters
- numbers
- letters
- special characters
- values icons
- units symbols
- home arrow
- AHI elements
- logo
- etc.



### Command line switches and values


| switch | primary value | additional values | source glyphs | valid source files        | note                                                      |
| ------ | --------- | ----------------- | ------------- | ------------------------- | --------------------------------------------------------- |
| -base  | file name |                   | all           | .bmp .png .ttf .mmc | base font source. Can be used without the `-base` switch. |
|        | file name |                   |               |


### Usage Examples

1. Open .mcm font file and save as .bmp HDZERO HD OSD font

```
py fontbuilder.py -base resources/fonts/BTFL_analog_default.mcm -o BTFL_default.bmp
```

2. following example will produce the same results. The switch `-base` can be left off

```
py fontbuilder.py resources/fonts/BTFL_analog_default.mcm -o BTFL_default.bmp
```

## HDZERO HD OSD Font Example

![](resources/fonts/BTFL_ondrascz_minimal_lowercase_color_ondras_V1.0.0.bmp)

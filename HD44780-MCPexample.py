#!/usr/bin/env python3

"""HD44780-MCPexample, example program to use with the HD44780-MCP.py module

created June 11, 2020 OM
modified June 19, 2020 OM """

"""
Copyright 2020 Owain Martin

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""

import HD44780MCP
import time
import MCP230XX

#initialize MCP
i2cAddr = 0x20  # MCP23008/17 i2c address
MCP = MCP230XX.MCP230XX('MCP23008', i2cAddr)
#MCP = MCP230XX.MCP230XX('MCP23017', i2cAddr)

# turn on backlight if using Adafruit i2c LCD backpack (uses MCP23008)
#blPin = 7 # Back light pin when using Adafruit LCD backpack
#MCP.set_mode(blPin, 'output')
#MCP.output(blPin, True) # turn backlight on - for Adafruit LCD backpack use

# set 16 character x 2 row LCD screen without rw pin, 4 bit mode
#LCD = HD44780MCP.HD44780(MCP, 1, -1, 2, [3,4,5,6], rows = 2, characters = 16, mode = 0, font = 0)

# set 20 character x 4 row LCD screen without rw pin, 4 bit mode
LCD = HD44780MCP.HD44780(MCP, 1, -1, 2, [3,4,5,6], rows = 4, characters = 20, mode = 0, font = 0)

# set 20 character x 4 row LCD screen without rw pin, 8 bit mode
#LCD = HD44780MCP.HD44780(MCP, 1, -1, 2, [3,4,5,6,8,9,10,11], rows = 4, characters = 20, mode = 1, font = 0)

LCD.display_string("glue")
time.sleep(1)
LCD.display(False)              # turn display off
time.sleep(2)
LCD.display()                   # turn display on
LCD.set_cursor(2,1)             # move cursor to 2nd row, 1st position
LCD.display_string("stick")
time.sleep(2)

LCD.blink()         # blink cursor position
time.sleep(2)
LCD.blink(False)    # turn blinking off
time.sleep(2)

LCD.cursor(False)   # turn cursor off
time.sleep(2)
LCD.cursor()        # turn cursor on
time.sleep(2)

LCD.scroll_right(4, 0.5) # scoll display right with 0.5s delay between steps
time.sleep(1)
LCD.scroll_left(4, 0.5) # scoll display left with 0.5s delay between steps
time.sleep(1)
LCD.cursor_left(2) # move cursor left
time.sleep(2)
LCD.cursor_right(2) # move cursor right
time.sleep(2)

LCD.clear_display()


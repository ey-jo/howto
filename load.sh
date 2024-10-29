#!/bin/sh

file="$1"
path="$(pwd)"

echo "$path/$file"

avr-gcc -g -Os -DF_CPU=16000000UL -mmcu=atmega328p "$path/$file" -o /tmp/atmega.elf
avr-objcopy -O ihex -R.eeprom /tmp/atmega.elf /tmp/atmega.hex
sudo avrdude -v -p atmega328p -D -b 115200 -c arduino -U /tmp/atmega.hex -P /dev/ttyUSB0
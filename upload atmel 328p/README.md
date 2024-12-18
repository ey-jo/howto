## Uploading to arduino nano atmel 328p

install the following packages:
```bash
base-devel
avr-libc
avr-gcc
avrdude
```


```upload.sh```:
```bash
avr-gcc -g -Os -DF_CPU=16000000UL -mmcu=atmega328p programm.c -o programm.elf           # from c file to elf
avr-objcopy -O ihex -R.eeprom programm.elf output.hex                                   # from elf to hex
sudo avrdude -v -p atmega328p -D -b 115200 -c arduino -U output.hex -P /dev/ttyUSB0     # upload to arduino nano connected to USB0
```


USB0 is the first device to be connected.\
If this is not working list all connected USB devices and choose the right one.

Command to list all devices:
```bash
ls /dev/tty*
```
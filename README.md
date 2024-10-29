install
```bash
base-devel
avr-libc
avr-gcc
avrdude
```


commands
```bash
avr-gcc -g -Os -DF_CPU=16000000UL -mmcu=atmega328p programm.c -o programm.elf   #from c file to elf
avr-objcopy -O ihex -R.eeprom programm.elf output.hex   #from elf to hex
sudo avrdude -v -p atmega328p -D -b 115200 -c arduino -U output.hex -P /dev/ttyUSB0    #write on nano
```

find port
```bash
ls /dev/tty*
```
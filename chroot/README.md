# chroot
Commands to chroot a arch system encrypted with LUKS.
First boot from a live usb. Then connect to the internet and run the following commands

the use of pacman is recommended, other package managers will work

## Commands
All
```bash
sudo cryptsetup open /dev/nvme0n1p2 crypto_LUKS
sudo mount /dev/mapper/crypto_LUKS /mnt
sudo mount /dev/nvme0n1p1 /mnt/efi
sudo arch-chroot /mnt
sudo pacman -Syu linux-headers linux
```

Display drives
```bash
sudo lsblk -f
```

Decrypt
```bash
sudo cryptsetup open /dev/nvme0n1p2 crypto_LUKS
```

Mount drive
```bash
sudo mount /dev/mapper/crypto_LUKS /mnt
sudo mount /dev/nvme0n1p1 /mnt/efi
```

Chroot into
```bash
sudo arch-chroot /mnt
```


Now you can perform every command as if you were using the arch based OS.


For example update and reinstall linux and headers. Useful if an update went wrong and the OS is not booting.
```bash
sudo pacman -Syu linux-headers linux
```

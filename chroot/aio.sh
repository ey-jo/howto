# execute this file on an arch live iso to fix failed updates

# keybaord layout (example to german)
loadkeys de-latin1

# wifi
wctl station wlan0 scan
iwctl station wlan0 get-networks
read -s -p "Network Name: " network
read -s -p "Password: " password
iwctl --passphrase $password station wlan0 connect $network

if ping -c 1 archlinux.org | grep "Temporary failure in name resolution"
then
    exit 1
fi
timedatectl


# mounting and chrooting
sudo cryptsetup open /dev/nvme0n1p2 crypto_LUKS
sudo mount /dev/mapper/crypto_LUKS /mnt
sudo mount /dev/nvme0n1p1 /mnt/efi
sudo arch-chroot /mnt

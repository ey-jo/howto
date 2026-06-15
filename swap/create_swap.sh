# create swap with 32G in size

sudo swapoff /dev/zram0
sudo zramctl --reset /dev/zram0
sudo zramctl --find --size 32G
sudo mkswap /dev/zram0
sudo swapon /dev/zram0

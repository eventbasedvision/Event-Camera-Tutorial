# Booting up the FPGA and connecting to a camera

-    (optional) Create an account with Prophesee to access the Petalinux image file.
    - create a bootable SD card (minimum 16 GB required) using the above image or either Ubuntu 22.04 image from [AMD's official page](https://ubuntu.com/download/amd). The setup would be similar for other boot images, although this document assumes the Petalinux image is being used.
    - create a bootable micro SD card using Balena etcher on linux or Win32 Disk Manager on Windows. Instructions for MacOS can be found [here](https://www.amd.com/en/products/system-on-modules/kria/k26/kv260-vision-starter-kit/getting-started/setting-up-the-sd-card-image.html).
    - Connect the SD card, USB cable, Ethernet, HDMI, and power cable as described {here}(https://www.amd.com/en/products/system-on-modules/kria/k26/kv260-vision-starter-kit/getting-started/connecting-everything.html).
    - Set up terminal access:
        - `dmesg | grep tty`
        fetch the USB interfaces that might host the connection with the board
        - `sudo putty /dev/ttyUSB1 -serial -sercfg 115200,8,n,1,N`
        connect to the USB device using a 115200 baud, 8 data bits, no parity, 1 stop bit, and no flow control. Try this command on each ttyUSB interface and use the one displaying information from the board as it boots up.
        - Instructions for other operating systems can be found [here](https://www.amd.com/en/products/system-on-modules/kria/k26/kv260-vision-starter-kit/getting-started/booting-your-starter-kit.html).    
   
    - ### NOTES FOR USING UBUNTU 22.04:
    
    - KRIA boards shipped before a certain date come with outdated boot firmware that doesn't allow Ubuntu 22.04 to boot properly (Petalinux images work fine). If Ubuntu 22.04 fails to boot up, you may need to update the pre-installed boot firmware:    
        - Download boot firmware update from [here](https://xilinx-wiki.atlassian.net/wiki/spaces/A/pages/1641152513/Kria+SOMs+Starter+Kits#Boot-FW-Update-Process) and copy the *BOOT.BIN* file to the board.
        - Run `sudo xmutil bootfw_update -i <path to boot.bin>`. This updates the image and marks it for the next time the board is booted. Check update status using `sudo xmutil bootfw_status`
        - After restart, it is required to manually validate the new FW by executing `sudo xmutil bootfw_update -v`. **This must be done immediately after the reboot**, otherwise the board will fall back to the older firmware on next boot.        
    
    - load custom hardware platforms for the Zynq UltraScale+ boards other than the standard standard platforms delivered as part of the Certified Ubuntu for Xilinx Devices Image (use \textit{channel= 1.x} if using Ubuntu 20.04. For sys-init, use all default settings and choose "update flash-kernel with package maintainer's version" when prompted.
    ```bash
    sudo snap install xlnx-config --classic --channel=2.x
    xlnx-config.sysinit
    ```
   
    - Viewing event camera feed using supplied binaries with Petalinux (if using Ubuntu, OpenEB must be compiled from source first- see below)
        - Configure the video pipeline, requires HDMI to be connected
        `/usr/bin/load-prophesee-kv260-<sensor>.sh`
        
        - power up the sensor so that its registers can be accessed 
        `echo on > /sys/class/video4linux/v4l-subdev3/device/power/control`
        
        - Start a X server on the board and run Metavision Viewer using the monitor as display:   
        `Xorg &`
        `DISPLAY=:0.0 V4L2_HEAP=reserved V4L2_SENSOR_PATH=/dev/v4l-subdev3 metavision_viewer`
        

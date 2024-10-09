# Compiling OpenEB SDK from source
[The Metavision SDK page](https://docs.prophesee.ai/stable/installation/linux_openeb.html?highlight=openeb) contains details for compiling openEB from source on Ubuntu with x86 CPU, but not for FPGAs. Compiling Openeb from source on the KRIA KV260 allows us to build vision applications from scratch using the Metavision API without being restricted to the provided binaries. 

```bash
    export CC=/usr/bin/aarch64-xilinx-linux-gcc-11.2.0
    export CXX=/usr/bin/aarch64-xilinx-linux-g++
    
    dnf install boost-dev.cortexa72_cortexa53
    dnf install opencv-dev.cortexa72_cortexa53    
    dnf install libglew-dev.cortexa72_cortexa53    
    dnf install libusb-1.0-dev.cortexa72_cortexa53
    
    ## Install PyBind11 from source
    wget https://github.com/pybind/pybind11/archive/v2.6.0.zip
    cd pybind11-2.6.0/build
    cmake .. -DPYBIND11_TEST=OFF
    cmake --build . --target install
    
    ## Install GLFW from source}
    git clone https://github.com/glfw/glfw.git
    cd glfw/build
    dnf install wayland-dev.cortexa72_cortexa53
    dnf install xwayland-dev.cortexa72_cortexa53
    dnf install libxinerama-dev.cortexa72_cortexa53
    cmake .. -D GLFW_BUILD_WAYLAND=0
    cmake --build . --target install

    ## Compile OpenEB
    git clone https://github.com/prophesee-ai/openeb.git --branch 4.6.2
    cd openeb
    mkdir build && cd build
    dnf install libusb-1.0-dev.cortexa72_cortexa53
    cp  /lib/libusb-1.0* /usr/lib/
    cp /usr/include/libusb-1.0/libusb.h /usr/include/
    cmake --build . --config Release -- -j `nproc`
    sudo cmake --build . --target install    
```

Update library paths, add the following to .bashrc:
```bash
    export CC=/usr/bin/aarch64-xilinx-linux-gcc-11.2.0
    export CXX=/usr/bin/aarch64-xilinx-linux-g++
    export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/usr/local/lib
    export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/usr/lib
    export MV_HAL_PLUGIN_PATH=/usr/local/lib/metavision/hal/plugins/
    
```

<!-- TODO:
	Opening and saving event streams
	Interfacing with one/more event cameras
	Metavision API: timiing and synch interafces	
 -->

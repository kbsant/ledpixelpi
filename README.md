# ledpixelpi
Led Pixel Design App for Raspberry Pi

This is a small web app for editing pixel patterns.

Intended to run on a Raspberry Pi or similar device.


# Status

Very early stage. Fixed palette, 8x8 pixel grid.

# Requirements

* Requires python3.
* Uses pip to install flask. 
* Has static web dependencies on bootstrap css, react, and clojurescript (see Platform - client).

# Platform

* Server - python (Flask)
* Client - web (clojurescript/scittle + react/reagent + bootstrap)

# Build instructions

Use python3 venv:

    git clone https://github.com/kbsant/ledpixelpi
    cd ledpixelpi
    python3 -m venv ledpixelpi-venv
    source ledpixelpi-venv/bin/activate
	python3 -m pip install -r requirements.txt

# Run instructions

Debug mode

    python3 -m flask --debug run --host 0.0.0.0 --port 3000

And point your browser at: http://localhost:3000
If it doesnt work, try changing the port as there may be some conflict.


# Running with RPI 

RPI would need dependencies. For example, setting up with WS2812 pixel board:

    sudo pip3 install rpi_ws281x
    sudo pip3 install adafruit-circuitpython-neopixel
    sudo python3 -m pip install --force-reinstall adafruit-blinka
	
 Thanks to Adafruit (i'm not affiliated. just tried it and it works)

To run with the RPI, add a hook to the `/px` method:

    # requires root to work.
	# this can be initialized only once per process
    import board
    import neopixel
    pixels = neopixel.NeoPixel(board.D18, 64)

    # trigger this in the /px method
    pixels[int(index)] = (int(red)/4,int(green)/4,int(blue)/4)



# To-Do

* Support various layouts - for example, snake-like 8x8 layout wraps around continuously
* Paint while dragging/moving
* Background color/erase
* Save to json file
* Load from json file
* Live update to gpio
* Layers, Frames and animation
* Audio
* Save to svg 
* Save to gif

# Limitations

Very early stage. Use at your own risk.

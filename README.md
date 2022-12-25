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

# Limitations

Very early stage. Use at your own risk.

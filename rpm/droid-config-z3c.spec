# These and other macros are documented in ../droid-configs-device/droid-configs.inc

%define device z3c
%define vendor sony

%define vendor_pretty Sony
%define device_pretty Xperia Z3 Compact

%define dcd_path ./

# Adjust this for your device
%define pixel_ratio 1.25

# We assume most devices will
%define have_modem 1

%include droid-configs-device/droid-configs.inc


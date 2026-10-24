#!/bin/bash

if [ ! -d "vendor/mediatek/ims" ]; then
    echo "Cloning IMS"
    git clone -b android-16-qpr2 https://github.com/Adarsh0127-Elite/android_vendor_mediatek_ims.git vendor/mediatek/ims
fi



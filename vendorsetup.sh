#!/bin/bash

echo "Clonning IMS"
git clone -b android-16-qpr2 https://github.com/Adarsh0127-Elite/android_vendor_mediatek_ims.git vendor/mediatek/ims

echo "Unlock 4K 60FPS Cam Recording"
cd p*/a*/Aperture
git fetch https://github.com/Adarsh0127-Elite/android_packages_apps_Aperture.git
git cherry-pick 9509277efc852ad8bdcce204e0d9cfe104b6d190
cd ../../..

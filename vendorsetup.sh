#!/bin/bash

echo "Clonning Private keys"
croot && git clone https://github.com/ProjectMatrixx/vendor_matrixx-priv_keys-template vendor/lumine-priv/keys
cd vendor/lumine-priv/keys
./keys.sh
cd ../../..

echo "Clonning IMS"
git clone -b android-16-qpr2 https://github.com/Adarsh0127-Elite/android_vendor_mediatek_ims.git vendor/mediatek/ims

echo "Cloning BCR"
git clone https://github.com/Chaitanyakm/vendor_bcr.git vendor/bcr


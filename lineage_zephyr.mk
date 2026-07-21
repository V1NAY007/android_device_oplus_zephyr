# SPDX-FileCopyrightText: The LineageOS Project
# SPDX-License-Identifier: Apache-2.0

# Inherit from the custom device configuration.
$(call inherit-product, device/oplus/zephyr/device.mk)

# Inherit from the LineageOS configuration.
TARGET_DISABLE_EPPE := true
$(call inherit-product, vendor/lineage/config/common_full_phone.mk)

PRODUCT_BRAND := Oplus
PRODUCT_DEVICE := zephyr
PRODUCT_MANUFACTURER := Oplus
PRODUCT_MODEL := mt6895
PRODUCT_NAME := lineage_zephyr

PRODUCT_GMS_CLIENTID_BASE := android-oneplus

PRODUCT_BUILD_PROP_OVERRIDES += \
    BuildDesc="sys_mssi_64_cn_armv82-user 15 AP3A.240617.008 1755697740151 release-keys" \
    BuildFingerprint=OnePlus/PGKM10/OP5565:15/AP3A.240617.008/S.1f56c75-1-a469:user/release-keys \
    DeviceName=PGKM10 \
    DeviceProduct=PGKM10 \
    SystemDevice=PGKM10 \
    SystemName=PGKM10

#Axion Stuff
TARGET_ENABLE_BLUR := true
TARGET_INCLUDE_AXFX := true
# Camera information (multiple sensors supported)
AXION_CAMERA_REAR_INFO := 50,8,2
AXION_CAMERA_FRONT_INFO := 16
# Maintainer name (underscores become spaces in the UI)
AXION_MAINTAINER := V1NAY007
# Processor name (underscores become spaces)
AXION_PROCESSOR := Dimensity_8100
# CPU governor support
PERF_GOV_SUPPORTED := true
PERF_DEFAULT_GOV := performance
PERF_ANIM_OVERRIDE := true
HBM_SUPPORTED := true
HBM_NODE := /sys/class/backlight/panel0-backlight/hbm_mode
TORCH_STR_SUPPORTED := true
TARGET_INCLUDES_LOS_PREBUILTS := true
TARGET_NEEDS_DOZE_FIX := true
TARGET_SUPPORTED_REFRESH_RATES := 60,75,90,120

# SPDX-FileCopyrightText: The LineageOS Project
# SPDX-License-Identifier: Apache-2.0

# Inherit from the custom device configuration.
$(call inherit-product, device/oplus/zephyr/device.mk)

# Inherit from the LineageOS configuration.
$(call inherit-product, vendor/lumine/config/common_full_phone.mk)

PRODUCT_NAME := lumine_zephyr
PRODUCT_DEVICE := zephyr
PRODUCT_MANUFACTURER := OPlus
PRODUCT_BRAND := OPlus
PRODUCT_MODEL := mt6895
PRODUCT_SYSTEM_NAME := zephyr

PRODUCT_GMS_CLIENTID_BASE := android-oneplus

PRODUCT_BUILD_PROP_OVERRIDES += \
    BuildFingerprint=OnePlus/PGKM10/OP5565:15/AP3A.240617.008/S.1f56c75-1-a469:user/release-keys \
    DeviceProduct=$(PRODUCT_SYSTEM_NAME)

LUMINE_MAINTAINER := V1NAY007
TARGET_BOOT_ANIMATION_RES := 1080
PERF_ANIM_OVERRIDE := true

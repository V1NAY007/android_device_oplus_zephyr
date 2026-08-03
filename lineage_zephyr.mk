# SPDX-FileCopyrightText: The LineageOS Project
# SPDX-License-Identifier: Apache-2.0

# Inherit from the custom device configuration.
$(call inherit-product, device/oplus/zephyr/device.mk)

# Inherit from the LineageOS configuration.
$(call inherit-product, vendor/lineage/config/common_full_phone.mk)

PRODUCT_NAME := lineage_zephyr
PRODUCT_DEVICE := zephyr
PRODUCT_MANUFACTURER := OPlus
PRODUCT_BRAND := OPlus
PRODUCT_MODEL := mt6895
PRODUCT_SYSTEM_NAME := zephyr

PRODUCT_GMS_CLIENTID_BASE := android-oneplus

PRODUCT_BUILD_PROP_OVERRIDES += \
    BuildFingerprint=OnePlus/PGKM10/OP5565:15/AP3A.240617.008/S.1f56c75-1-a469:user/release-keys \
    DeviceProduct=$(PRODUCT_SYSTEM_NAME)


WITH_GMS := true
WITH_GMS_COMMS_SUITE := false
TARGET_USE_WALLPAPERS := true
TARGET_USE_GPHOTOS := false
TARGET_USE_FILES := false
TARGET_USE_MAPS := false
TARGET_OPTIMIZED_DEXOPT := true
TARGET_CUSTOM_UDFPS := true
TARGET_BOOT_ANIMATION_RES := 1080
USE_REALITY_ENGINE := false
TARGET_USE_WALLPAPERS := true
WITH_PIXEL_LAUNCHER := false
USE_DEFAULT_VULKAN := false

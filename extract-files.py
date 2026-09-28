#!/usr/bin/env -S PYTHONPATH=../../../tools/extract-utils python3
# SPDX-FileCopyrightText: 2024 The LineageOS Project
# SPDX-License-Identifier: Apache-2.0

from extract_utils.file import File
from extract_utils.fixups_blob import (
    blob_fixup,
    blob_fixups_user_type,
)
from extract_utils.fixups_lib import (
    lib_fixup_remove,
    lib_fixups,
    lib_fixups_user_type,
)
from extract_utils.main import (
    ExtractUtils,
    ExtractUtilsModule,
)

namespace_imports = [
    'device/oplus/zephyr',
    'hardware/mediatek',
    'hardware/mediatek/libmtkperf_client',
    'hardware/oplus',
]

lib_fixups: lib_fixups_user_type = {
    **lib_fixups,
    ('libsink',): lib_fixup_remove,
}


blob_fixups: blob_fixups_user_type = {
    'odm/bin/hw/android.hardware.ir-service': blob_fixup()
        .replace_needed('android.hardware.ir-V1-ndk_platform.so', 'android.hardware.ir-V1-ndk.so'),

    'odm/bin/touchDaemo': blob_fixup()
        .replace_needed('libtinyxml2.so', 'libtinyxml2-v34.so'),

    'odm/lib64/liblvimfs_wrapper.so': blob_fixup()
        .remove_needed('libstdc++.so'),

    'odm/lib64/vendor.oplus.hardware.hdcp-V1-ndk_platform.so': blob_fixup()
        .replace_needed('android.hardware.common-V2-ndk_platform.so', 'android.hardware.common-V2-ndk.so'),

    'vendor/etc/init/android.hardware.neuralnetworks-shim-service-mtk.rc': blob_fixup()
        .regex_replace('start', 'enable'),

    'system_ext/lib64/libsink-mtk.so': blob_fixup()
        .add_needed('libaudioclient_mt6895_shim.so'),

    'system_ext/lib64/libimsma.so': blob_fixup()
        .replace_needed('libsink.so', 'libsink-mtk.so'),

    'system_ext/lib64/libsource.so': blob_fixup()
        .add_needed('libui_shim.so'),

    (
        'vendor/bin/hw/android.hardware.gnss-service.mediatek',
        'vendor/lib64/hw/android.hardware.gnss-impl-mediatek.so'
    ): blob_fixup()
        .replace_needed('android.hardware.gnss-V1-ndk_platform.so', 'android.hardware.gnss-V1-ndk.so'),

    'vendor/bin/hw/android.hardware.media.c2@1.2-mediatek-64b': blob_fixup()
        .add_needed('libstagefright_foundation-v33.so')
        .replace_needed('libavservices_minijail_vendor.so', 'libavservices_minijail.so'),

    'vendor/bin/hw/android.hardware.security.keymint-service.trustonic': blob_fixup()
        .add_needed('android.hardware.security.rkp-V3-ndk.so')
        .replace_needed('android.hardware.security.keymint-V1-ndk_platform.so', 'android.hardware.security.keymint-V1-ndk.so')
        .replace_needed('android.hardware.security.sharedsecret-V1-ndk_platform.so', 'android.hardware.security.sharedsecret-V1-ndk.so')
        .replace_needed('android.hardware.security.secureclock-V1-ndk_platform.so', 'android.hardware.security.secureclock-V1-ndk.so'),

    'vendor/bin/hw/mtkfusionrild': blob_fixup()
        .add_needed('libutils-v32.so'),

    (
        'vendor/bin/mnld',
        'vendor/lib64/liboplus_mtkcam_lightsensorprovider.so',
        'vendor/lib64/hw/android.hardware.sensors@2.X-subhal-mediatek.so',
        'vendor/lib64/mt6895/libaalservice.so'
    ): blob_fixup()
        .replace_needed('libsensorndkbridge.so', 'android.hardware.sensors@1.0-convert-shared.so'),

    'vendor/lib64/hw/audio.primary.mediatek.so': blob_fixup()
        .add_needed('libstagefright_foundation-v33.so')
        .replace_needed('libalsautils.so', 'libalsautils-v31.so')
        .replace_needed('libtinyxml2.so', 'libtinyxml2-v34.so'),

    (
        'vendor/lib64/mt6895/libcam.hal3a.so',
        'vendor/lib64/mt6895/libcam.hal3a.ctrl.so',
        'vendor/lib64/mt6895/libmtkcam_request_requlator.so',
        'vendor/lib64/libcustomer_cameradata.so'
    ): blob_fixup()
        .add_needed('libprocessgroup_shim.so'),

    'vendor/lib64/hw/hwcomposer.mtk_common.so': blob_fixup()
        .add_needed('libprocessgroup_shim.so'),

    'vendor/lib64/hw/mt6895/android.hardware.camera.provider@2.6-impl-mediatek.so': blob_fixup()
        .add_needed('libcamera_metadata_shim.so')
        .replace_needed('libutils.so', 'libutils-v32.so'),

    'vendor/bin/hw/vendor.mediatek.hardware.pq@2.2-service': blob_fixup()
        .replace_needed('libutils.so', 'libutils-v32.so'),

    'vendor/lib64/hw/mt6895/vendor.mediatek.hardware.pq@2.15-impl.so': blob_fixup()
        .replace_needed('libsensorndkbridge.so', 'android.hardware.sensors@1.0-convert-shared.so')
        .binary_regex_replace(
            b'/my_product/vendor/etc/cust_silky_brightness_%s_%s.xml',
            b'/vendor/etc/cust_silky_brightness_%s_%s.xml\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
        )
        .binary_regex_replace(
            b'/my_product/vendor/etc/cust_silky_brightness_%s.xml',
            b'/vendor/etc/cust_silky_brightness_%s.xml\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
        )
        .replace_needed('libutils.so', 'libutils-v32.so')
        .replace_needed('libtinyxml2.so', 'libtinyxml2-v34.so'),

    (
        'vendor/lib64/lib3a.ae.pipe.so',
        'vendor/lib64/mt6895/lib3a.awbsync.so',
        'vendor/lib64/mt6895/lib3a.flash.so',
        'vendor/lib64/mt6895/lib3a.sensors.color.so',
        'vendor/lib64/mt6895/lib3a.sensors.flicker.so'
    ): blob_fixup()
        .add_needed('liblog.so'),

    'vendor/lib64/librt_extamp_intf.so': blob_fixup()
        .replace_needed('libtinyxml2.so', 'libtinyxml2-v34.so'),

    'vendor/lib64/libmidasserviceintf_aidl.so': blob_fixup()
        .replace_needed('android.frameworks.stats-V1-ndk_platform.so', 'android.frameworks.stats-V1-ndk.so'),

    'vendor/lib64/mt6895/libneuralnetworks_sl_driver_mtk_prebuilt.so': blob_fixup()
        .clear_symbol_version('AHardwareBuffer_allocate')
        .clear_symbol_version('AHardwareBuffer_createFromHandle')
        .clear_symbol_version('AHardwareBuffer_describe')
        .clear_symbol_version('AHardwareBuffer_getNativeHandle')
        .clear_symbol_version('AHardwareBuffer_lock')
        .clear_symbol_version('AHardwareBuffer_release')
        .clear_symbol_version('AHardwareBuffer_unlock')
        .add_needed('libbase_shim.so'),

    (
        'vendor/lib64/libnvram.so',
        'vendor/lib64/libsysenv.so'
    ): blob_fixup()
        .add_needed('libbase_shim.so'),

    'vendor/lib64/mt6895/libmnl.so': blob_fixup()
        .add_needed('libcutils.so'),

    'vendor/lib64/mt6895/libmtkcam_stdutils.so': blob_fixup()
        .replace_needed('libutils.so', 'libutils-v32.so'),
}  # fmt: skip

module = ExtractUtilsModule(
    'zephyr',
    'oplus',
    add_firmware_proprietary_file=True,
    blob_fixups=blob_fixups,
    lib_fixups=lib_fixups,
    namespace_imports=namespace_imports,
)

if __name__ == '__main__':
    utils = ExtractUtils.device(module)
    utils.run()

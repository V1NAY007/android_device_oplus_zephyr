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
    'hardware/mediatek/libion_mtk',
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

    'vendor/etc/init/camerahalserver.rc': blob_fixup()
        .regex_replace(
            r'on post-fs-data\n(?!\s*mkdir /mnt/vendor/persist/camera)',
            'on post-fs-data\n    mkdir /mnt/vendor/persist/camera 0755 cameraserver cameraserver\n'
        ),

    'vendor/etc/public.libraries.txt': blob_fixup()
        .add_line_if_missing('libAlgoProcess.so'),

    'system_ext/lib64/libimsma.so': blob_fixup()
        .replace_needed('libsink.so', 'libsink-mtk.so'),

    'system_ext/lib64/libsink-mtk.so': blob_fixup()
        .add_needed('libaudioclient_shim.so'),

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

    'vendor/etc/seccomp_policy/android.hardware.media.c2@1.2-extended-seccomp-policy': blob_fixup()
        .add_line_if_missing('fcntl: 1')
        .add_line_if_missing('geteuid: 1')
        .add_line_if_missing('getgid: 1')
        .add_line_if_missing('getegid: 1')
        .add_line_if_missing('getgroups: 1')
        .add_line_if_missing('prlimit64: 1')
        .add_line_if_missing('faccessat2: 1')
        .add_line_if_missing('clone3: 1')
        .add_line_if_missing('rseq: 1')
        .add_line_if_missing('sendto: 1')
        .add_line_if_missing('epoll_create1: 1')
        .add_line_if_missing('epoll_ctl: 1')
        .add_line_if_missing('epoll_pwait: 1')
        .add_line_if_missing('timerfd_create: 1')
        .add_line_if_missing('timerfd_settime: 1')
        .add_line_if_missing('timerfd_gettime: 1'),

    'vendor/bin/hw/android.hardware.security.keymint-service.trustonic': blob_fixup()
        .add_needed('android.hardware.security.rkp-V3-ndk.so')
        .replace_needed('android.hardware.security.keymint-V1-ndk_platform.so', 'android.hardware.security.keymint-V1-ndk.so')
        .replace_needed('android.hardware.security.sharedsecret-V1-ndk_platform.so', 'android.hardware.security.sharedsecret-V1-ndk.so')
        .replace_needed('android.hardware.security.secureclock-V1-ndk_platform.so', 'android.hardware.security.secureclock-V1-ndk.so'),

    'vendor/bin/mnld' : blob_fixup()
        .replace_needed('libmnl.so', 'libmnl_mtk.so'),

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
    ): blob_fixup()
        .add_needed('libprocessgroup_shim.so'),

    'vendor/lib64/libcustomer_cameradata.so': blob_fixup()
        .add_needed('libprocessgroup_shim.so')
        .sig_replace(
            'ff c3 01 d1 fd 7b 03 a9 f7 23 00 f9 f6 57 05 a9 f4 4f 06 a9 fd c3 00 91 f5 03 02 2a f3 03 01 2a',
            'c0 03 5f d6',
        )
        .sig_replace(
            'fd 7b bb a9 fc 0b 00 f9 f8 5f 02 a9 f6 57 03 a9 f4 4f 04 a9 fd 03 00 91 ff 43 13 d1 f3 03 02 2a e0 03 01 2a',
            'c0 03 5f d6',
        )
        .sig_replace(
            'fd 7b be a9 f3 0b 00 f9 fd 03 00 91 f3 03 01 2a 44 7c 00 94',
            'c0 03 5f d6',
        )
        .sig_replace(
            'fd 7b bb a9 fc 0b 00 f9 f8 5f 02 a9 f6 57 03 a9 f4 4f 04 a9 fd 03 00 91 ff 43 13 d1 f3 03 01 2a',
            'c0 03 5f d6',
        ),

    'vendor/lib64/hw/hwcomposer.mtk_common.so': blob_fixup()
        .add_needed('libprocessgroup_shim.so'),

    'vendor/lib64/hw/mt6895/android.hardware.camera.provider@2.6-impl-mediatek.so': blob_fixup()
        .add_needed('libcamera_metadata_shim.so')
        .replace_needed('libutils.so', 'libutils-v32.so'),

    'vendor/lib64/hw/vendor.oplus.hardware.camera_rfi-V1-service-impl.so': blob_fixup()
        .sig_replace(
            'fd 7b ba a9 fc 6f 01 a9 fa 67 02 a9 f8 5f 03 a9 f6 57 04 a9 f4 4f 05 a9 fd 03 00 91 ff 03 12 d1 f6 03 01 aa f4 03 00 aa',
            'c0 03 5f d6',
        )
        .sig_replace(
            'fd 7b ba a9 fc 6f 01 a9 fa 67 02 a9 f8 5f 03 a9 f6 57 04 a9 f4 4f 05 a9 fd 03 00 91 ff 03 12 d1 f5 03 01 aa f4 03 00 aa',
            'c0 03 5f d6',
        ),

    'vendor/lib64/mt6895/libmtkcam_hwutils_poweronoffcontroller.so': blob_fixup()
        .sig_replace(
            'a4 11 00 94 e1 23 00 91 a6 11 00 94',
            '1f 20 03 d5 1f 20 03 d5 1f 20 03 d5',
        )
        .sig_replace(
            '13 0c 00 94 e1 03 15 aa 69 0c 00 94',
            '1f 20 03 d5 1f 20 03 d5 1f 20 03 d5',
        ),

    'vendor/lib64/libmtkcam_3rdparty.arc.sateis.custom.so': blob_fixup()
        .sig_replace(
            '69 6c 00 94 00 28 00 35',
            '69 6c 00 94 00 1a 00 35',
        )
        .sig_replace(
            'ff ff 06 a9 ff 3f 00 f9',
            '90 ff ff 17 1f 20 03 d5',
        ),

    'vendor/bin/hw/vendor.mediatek.hardware.pq@2.2-service': blob_fixup()
        .replace_needed('libutils.so', 'libutils-v32.so'),

    (
        'vendor/lib64/libcodec2_mtk_venc.so',
        'vendor/lib64/libcodec2_mtk_vdec.so'
    ): blob_fixup()
        .replace_needed('libformatter.so', 'libformatter_mtk.so'),

    'vendor/lib64/hw/android.hardware.audio@7.0-impl-mediatek.so': blob_fixup()
        .replace_needed('android.hardware.audio@7.0-util.so', 'android.hardware.audio@7.0-util-v33.so'),

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

    'vendor/lib64/mt6895/libmnl_mtk.so': blob_fixup()
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

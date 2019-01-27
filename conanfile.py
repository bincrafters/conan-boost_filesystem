#!/usr/bin/env python
# -*- coding: utf-8 -*-

from conans import python_requires


base = python_requires("boost_base/1.68.0@bincrafters/testing")

class BoostFilesystemConan(base.BoostBaseConan):
    name = "boost_filesystem"
    version = "1.68.0"
    url = "https://github.com/bincrafters/conan-boost_filesystem"
    lib_short_names = ["filesystem"]
    options = {"shared": [True, False]}
    default_options = "shared=False"
    b2_requires = [
        "boost_assert",
        "boost_config",
        "boost_container_hash",
        "boost_core",
        "boost_detail",
        "boost_io",
        "boost_iterator",
        "boost_range",
        "boost_smart_ptr",
        "boost_static_assert",
        "boost_system",
        "boost_type_traits"
    ]

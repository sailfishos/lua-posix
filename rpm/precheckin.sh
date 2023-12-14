#!/bin/sh

buildflavors="lua53 lua54"
modname=posix

for build_flavor in $buildflavors ; do
    sed -e "s/@BUILD_FLAVOR@/${build_flavor}/g" \
        lua-${modname}.spec > ${build_flavor}-${modname}.spec
done

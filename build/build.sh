#!/bin/sh
gopy build --rename=true --no-make=true -vm=python3 -output=vrf vrf
cp build/__init__.py vrf/__init__.py
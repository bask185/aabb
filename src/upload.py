#!/usr/bin/env python
import os
os.system("python src/build.py")
print("UPLOADING")
os.system("arduino-cli upload -b ATtiny:avr:attinyx5 -p COM7 -i ./build/ATtiny.avr.attinyx5/aabb.ino.hex")
exit
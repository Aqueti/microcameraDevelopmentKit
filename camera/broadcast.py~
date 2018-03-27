#!/usr/bin/python
#
# simple python script to capture a video sequence
# input[0] is the sensor-id
# input[1] is the number of frames
# input[2] is the sensor operating mode. Available modes are
# mode 1 3864 x 2174 FR=60.000000 CF=0x1009208a10 SensorModeType=4 CSIPixelBitDepth=10 DynPixelBitDepth=10
# mode 2 1932 x 1094 FR=120.000000 CF=0x1009208a10 SensorModeType=4 CSIPixelBitDepth=10 DynPixelBitDepth=10
# mode 3 1288 x 734 FR=120.000000 CF=0x1009208a10 SensorModeType=4 CSIPixelBitDepth=10 DynPixelBitDepth=10
# mode 4 1288 x 546 FR=240.000000 CF=0x1009208a10 SensorModeType=4 CSIPixelBitDepth=10 DynPixelBitDepth=10

#


import sys
import atexit
import subprocess

def printHelp():
    print("grab video at various frame rates")
    print("---------------------------------")
    print("to run type grabVideo.py sensor-id number-of-frames operating-mode(1-4)")
    print("--help or -h prints help message and exits")

def main():
        inputs=sys.argv[1:]
        if len(inputs)==3:
            if inputs[2]==str(1):
                cmd="gst-launch-1.0 -e nvcamerasrc intent=3 sensor-id="
                cmd=cmd+str(inputs[0])+" num-buffers="+str(inputs[1])
                cmd=cmd+""" fpsRange=\"60 60\""""
                cmd=cmd+" ! 'video/x-raw(memory:NVMM), width=(int)3864, height=(int)2174, format=(string)I420, "
                cmd=cmd+"framerate=(fraction)60/1' ! nvvidconv flip-method=2 ! 'video/x-raw(memory:NVMM),"
                cmd=cmd+"format=(string)I420' ! omxh264enc ! 'video/x-h264, "
                cmd=cmd+"stream-format=(string)byte-stream' ! filesink location=grabVid.h264"
                subprocess.call(cmd,shell=True)
            elif inputs[2]==str(2):
                cmd="gst-launch-1.0 -e nvcamerasrc intent=3 sensor-id="
                cmd=cmd+str(inputs[0])+" num-buffers="+str(inputs[1])
                cmd=cmd+""" fpsRange=\"120 120\""""
                cmd=cmd+" ! 'video/x-raw(memory:NVMM), width=(int)1932, height=(int)1094, format=(string)I420, "
                cmd=cmd+"framerate=(fraction)120/1' ! nvvidconv flip-method=2 ! 'video/x-raw(memory:NVMM),"
                cmd=cmd+"format=(string)I420' ! omxh264enc ! 'video/x-h264, "
                cmd=cmd+"stream-format=(string)byte-stream' ! filesink location=grabVid.h264"
                subprocess.call(cmd,shell=True)
            elif inputs[2]==str(3):
                cmd="gst-launch-1.0 -e nvcamerasrc intent=3 sensor-id="
                cmd=cmd+str(inputs[0])+" num-buffers="+str(inputs[1])
                cmd=cmd+""" fpsRange=\"120 120\""""
                cmd=cmd+" ! 'video/x-raw(memory:NVMM), width=(int)1288, height=(int)734, format=(string)I420, "
                cmd=cmd+"framerate=(fraction)120/1' ! nvvidconv flip-method=2 ! 'video/x-raw(memory:NVMM),"
                cmd=cmd+"format=(string)I420' ! omxh264enc ! 'video/x-h264, "
                cmd=cmd+"stream-format=(string)byte-stream' ! filesink location=grabVid.h264"
                subprocess.call(cmd,shell=True)
            elif inputs[2]==str(4):
                cmd="gst-launch-1.0 -e nvcamerasrc intent=3 sensor-id="
                cmd=cmd+str(inputs[0])+" num-buffers="+str(inputs[1])
                cmd=cmd+""" fpsRange=\"240 240\""""
                cmd=cmd+" ! 'video/x-raw(memory:NVMM), width=(int)1288, height=(int)546, format=(string)I420, "
                cmd=cmd+"framerate=(fraction)240/1' ! nvvidconv flip-method=2 ! 'video/x-raw(memory:NVMM),"
                cmd=cmd+"format=(string)I420' ! omxh264enc ! 'video/x-h264, "
                cmd=cmd+"stream-format=(string)byte-stream' ! filesink location=grabVid.h264"
                subprocess.call(cmd,shell=True)
            else:
                printHelp()
        else:
                printHelp()


if __name__ == '__main__':
        main()

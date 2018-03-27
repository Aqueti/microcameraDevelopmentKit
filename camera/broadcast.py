#!/usr/bin/python
#
# This script broadcasts a live video stream from the camera to a remote render machine.
# the script receiveJPEG.sh or receive264.sh must be running on the remote machine.
# input[0] is the sensor-id allowed values are 0,1,2
# input[1] the ip address of the remote machine
# input[2] is the streaming mode 0 for jpeg, 1 for h.264
#


import sys
import atexit
import subprocess

def printHelp():
    print("grab broadcast video from camera to remote machine")
    print("---------------------------------")
    print("broadcast.py sensor-id remoteMachineIP streamingFormat(0 for jpeg, 1 for h.264")
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

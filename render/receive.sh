port=5000
#receive command for viewing a jpeg stream over the network  
cmd="/usr/bin/gst-launch-1.0 udpsrc port=$port ! application/x-rtp,encoding-name=JPEG,payload=26 ! rtpjpegdepay ! jpegdec ! autovideosink"
cmd264="gst-launch-1.0 udpsrc port=$port ! application/x-rtp,encoding-name=H264,payload=96 ! rtph264depay ! h264parse ! queue ! avdec_h264 ! videorate ! \"video/x-raw,framerate=30/1\" ! xvimagesink sync=false async=false -e"


echo "setting up pipeline with command " $cmd
eval $cmd

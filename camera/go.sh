#put in the IP address of the computer you are streaming to here
hostip=10.0.1.101
port=5000

#streaming command for sending jpegs over the network
cmd="gst-launch-1.0  nvcamerasrc fpsRange=\"30.0 30.0\" sensor-id=0 ! 'video/x-raw(memory:NVMM), width=(int)1920, height=(int)1080, format=(string)I420, framerate=(fraction)30/1'  ! nvjpegenc ! rtpjpegpay ! udpsink host=$hostip port=$port"
fname=test.h264
#h264 encode+stream over network
#cmd264="gst-launch-1.0 -e nvcamerasrc num-buffers=300  fpsRange=\"30.0 30.0\" ! 'video/x-raw(memory:NVMM), width=(int)1920, height=(int)1080, format=(string)I420, framerate=(fraction)30/1' ! nvvidconv flip-method=2 ! 'video/x-raw(memory:NVMM), format=(string)I420' ! tee name=streams streams. ! omxh264enc ! 'video/x-h264, stream-format=(string)byte-stream' ! h264parse ! rtph264pay mtu=1400 ! udpsink host=$hostip port=$port streams. ! omxh264enc bitrate=8000000 ! 'video/x-h264, stream-format=(string)byte-stream' ! filesink location=$fname"

echo "setting up pipeline with command $cmd"
eval $cmd

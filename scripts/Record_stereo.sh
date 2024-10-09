xmutil unloadapp
pkill metavision_view
mkdir -p $1/cam1 $1/cam2
DISPLAY=:0.0 V4L2_HEAP=reserved V4L2_SENSOR_PATH=/dev/v4l-subdev3 metavision_viewer -o $1/cam1/rec.raw  &
/usr/bin/load-prophesee-kv260-imx636.sh
echo on > /sys/class/video4linux/v4l-subdev3/device/power/control
echo "PRESS SPACE TO START CAM1"
sleep 5
DISPLAY=:0.0 V4L2_HEAP=reserved V4L2_SENSOR_PATH=/dev/v4l-subdev3 metavision_viewer -o $1/cam2/rec.raw  &
echo "PRESS SPACE TO START CAM2"
sleep $2
pkill metavision_view
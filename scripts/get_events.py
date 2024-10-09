from metavision_core.event_io.raw_reader import initiate_device
from metavision_core.event_io import EventsIterator
from metavision_sdk_core import PeriodicFrameGenerationAlgorithm
from metavision_sdk_ui import EventLoop, BaseWindow, Window, UIAction, UIKeyEvent

import argparse
import time
import os

def parse_args():
    """Parse command line arguments."""
    parser = argparse.ArgumentParser(description='Metavision RAW file Recorder sample.',
                                     formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument(
        '-o', '--output-dir', default="", help="Directory where to create RAW file with recorded event data")
    args = parser.parse_args()
    return args

def main():
	""" Main """
	args = parse_args()

	# HAL Device on live camera
	# device = initiate_device("v4l2_device23")
	device = initiate_device("")
	
	print(device)
	# Start the recording
	if device.get_i_events_stream():
		log_path = "recording_" + time.strftime("%y%m%d_%H%M%S", time.localtime()) + ".raw"
		if args.output_dir != "":
			log_path = os.path.join(args.output_dir, log_path)
		print(f'Recording to {log_path}')
		device.get_i_events_stream().log_raw_data(log_path)	

	mv_iterator = EventsIterator.from_device(device=device)
	try:
		for evs in mv_iterator:
			# Process events 
			pass

	except KeyboardInterrupt:
		device.get_i_events_stream().stop_log_raw_data()
		print("STOPPED!")  

if __name__ == "__main__":
    main()

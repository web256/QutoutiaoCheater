import os
import random
import time

DIFF = 10
SCREEN_WIDTH = 1200
SCREEN_LENGTH = 1920


def swipe_screen(start_xy, end_xy):
	""""""
	cmd = "adb shell input swipe " \
		+ str(start_xy[0]) + " " \
		+ str(start_xy[1]) + " " \
		+ str(end_xy[0]) + " " \
		+ str(end_xy[1]) + " " 
	print("cmd: ", cmd)
	os.system(cmd)
	
	
def tap_screen(xy):
	""""""
	cmd = "adb shell input tap " \
		+ str(xy[0]) + " " \
		+ str(xy[1]) + " " \
		
	print("cmd: ", cmd)
	os.system(cmd)

	
def main():
	while True:
		# fresh page
		times = random.randint(2, 3)
		print("fresh page: ", times, "times")
		for i in range(times):
			FRESH_BUTTON_X = random.randint(0 + DIFF, SCREEN_WIDTH / 4 - DIFF)
			FRESH_BUTTON_Y = random.randint(SCREEN_LENGTH - 120 + DIFF, SCREEN_LENGTH - DIFF)
			FRESH_BUTTON = (FRESH_BUTTON_X, FRESH_BUTTON_Y)
			tap_screen(FRESH_BUTTON)
			time.sleep(2)
		
		time.sleep(3)

		# open text
		TEXT_LAYER1_X = random.randint(SCREEN_WIDTH / 4 + DIFF, 3 * SCREEN_WIDTH / 4 - DIFF)
		TEXT_LAYER1_Y = random.randint(250 + DIFF, 560 - DIFF)
		TEXT_LAYER1 = (TEXT_LAYER1_X, TEXT_LAYER1_Y)
		tap_screen(TEXT_LAYER1)
		time.sleep(5)

		# swipe screen
		times = random.randint(8, 13)
		print("swipe screen: ", times, "times")
		for i in range(times):
			print("time", i)
			SWIPE_START_AREA_X = random.randint(SCREEN_WIDTH * 3 / 8, SCREEN_WIDTH * 5 / 8)
			SWIPE_START_AREA_Y = random.randint(SCREEN_LENGTH * 5 / 8, SCREEN_LENGTH * 6 / 8)
			SWIPE_START_AREA = (SWIPE_START_AREA_X, SWIPE_START_AREA_Y)
			SWIPE_END_AREA_X = random.randint(SCREEN_WIDTH * 3 / 8, SCREEN_WIDTH * 5 / 8)
			SWIPE_END_AREA_Y = random.randint(SCREEN_LENGTH * 2 / 8, SCREEN_LENGTH * 3 / 8)
			SWIPE_END_AREA = (SWIPE_END_AREA_X, SWIPE_END_AREA_Y)
			swipe_screen(SWIPE_START_AREA, SWIPE_END_AREA)
			time.sleep(3)
		
		# back
		BACK_BUTTON_X = random.randint(0 + DIFF, 100 - DIFF)
		BACK_BUTTON_Y = random.randint(50 + DIFF, 150 - DIFF)
		BACK_BUTTON = (BACK_BUTTON_X, BACK_BUTTON_Y )
		tap_screen(BACK_BUTTON)
		time.sleep(1)
		

if __name__ == "__main__":
	main()

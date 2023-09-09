# python code
# script_name: demo1
#
# author: vinay
# description: composition practice

# set up
from earsketch import *

init()
setTempo(120)
# Music
#fitMedia(RD_UK_HOUSE__5THCHORD_2, 1, 4, 6)
fitMedia(RD_UK_HOUSE_WURLITZER_1, 1, 3, 14)
setEffect(1, VOLUME, GAIN, -60, 1, 5, 12)
setEffect(1, VOLUME, GAIN, 5, 12, -60, 16)
fitMedia(HIPHOP_BASSSUB_001, 2, 5, 15.4)
#  Add effect
setEffect(2, DELAY, DELAY_TIME, 500, 8)
fitMedia(HOUSE_MAIN_BEAT_003, 3, 7, 12)
# ADD EFFECT
setEffect(3, REVERB, REVERB_TIME, 200)

fitMedia(AK_UNDOG_808_2, 4, 1, 15)
#setEffect()
# Finish
finish()


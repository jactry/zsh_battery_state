#!/usr/bin/env python
# -*- coding: utf-8 -*-
# zsh_battery_state 0.1
# 13:04:03 2012.03.10
# Jactry Zeng <jactry92@gmail.com>

import math
import sys, os
import re

s = open("/proc/acpi/battery/BAT1/state")
line = s.read()
where1 = line.find("capacity:")
where2 = line.find("mAh")
a = where1 + 15
b= where2-1
remaining_capacity = line[a:b]
s.close()

s = open("/proc/acpi/battery/BAT1/info")
line = s.read()
where1 = line.find("last full capacity:")
line = line[where1:]
where2 = line.find("mAh")
where1 = line.find(":")
a = where2-1
b = where1 + 7
last_full_capacity = line[b:a]
s.close()

s = open("/proc/acpi/battery/BAT1/state")
line = s.read()
line = line[82:]
where1 = line.find("\n")
state = line[:where1]
s.close()



remaining_capacity = int(remaining_capacity)
last_full_capacity = int(last_full_capacity)
power=int((remaining_capacity*100/last_full_capacity)/10.0)

full_power = 10
power_filled = int(math.ceil(power * (full_power / 10.0))) * u'▰'
used = (full_power - len(power_filled)) * u'▱'
charged =  (u'✓').encode('utf-8')
discharging =  (u'↯').encode('utf-8')
out = (power_filled + used).encode('utf-8')


color_green = '%{[32m%}'
color_yellow = '%{[1;33m%}'
color_red = '%{[31m%}'
color_reset = '%{[00m%}'

if len(power_filled) > 6 :
	color_of_out = color_green
	color_of_discharging = color_green
elif len(power_filled) > 4:
	color_of_out = color_yellow
	color_of_discharging = color_yellow
else:
	color_of_out = color_red
	color_of_discharging = color_red


show_discharging = color_of_discharging + discharging + color_reset
show_charging = color_green + charged + color_reset
bar = color_of_out + out + color_reset

if state == "charged":
    sys.stdout.write(show_charging)
elif state == "discharging":
    sys.stdout.write(show_discharging+" "+bar)
else:
    sys.stdout.write(bar)

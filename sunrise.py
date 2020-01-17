#!/usr/bin/env python
import datetime
import ephem # to install, run `pip install pyephem`

o = ephem.Observer()
o.lat = '55.45'
o.long = '-1.93'
o.date = datetime.datetime.now()
sun = ephem.Sun()
print str(o.next_rising(sun)).split()[1]

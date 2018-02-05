import os.path, time
print("%s" % time.ctime(os.path.getmtime("/home/hass/.homeassistant/.git/index")))
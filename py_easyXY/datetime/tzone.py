"""
def toLocal(dt, offset = 8):
	dt: datetime
	offset: default 8 china time
"""

import datetime

def toLocal(dt, offset = 8):
	localDateTime = dt + datetime.timedelta(hours=offset)
	return localDateTime


if __name__ == '__main__':
	now = datetime.datetime.utcnow()
	print now
	print toLocal(now)
	print now
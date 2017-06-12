import datetime
from operator import itemgetter

year = datetime.date.today().year
_defDate = datetime.date(year, 1, 1)

class song(object):
    """Store song name, number of times sung and last time sung."""
    def __init__(self, name, reps=0, date=_defDate):
        self.name = name
        self.reps = reps
        self.date = date

    def __str__(self):
        s = '{0:35} | {1:3} | {2:%d, %b %Y}'
        return s.format(self.name, self.reps, self.date)

    @classmethod
    def from_str(cls, s):
        name = s[:35].strip()
        reps = int(s[38:41])
        date = datetime.datetime.strptime(s[44:56],'%d, %b %Y').date()
        return cls(name, reps, date)
    
class songList(object):
    """Store list of songs and useful methods."""
    pass

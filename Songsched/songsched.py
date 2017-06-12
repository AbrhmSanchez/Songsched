import datetime
from operator import itemgetter

today = datetime.date.today()
defaultDate = datetime.date(today.year, 1, 1)

class song(object):
    """Store song name, number of times sung and last time sung."""
    def __init__(self, name, reps=0, date=defaultDate):
        self.name = name
        self.reps = reps
        self.date = date

    def __str__(self):
        s = '{0:35} | {1:3} | {2:%d/%m/%Y}'
        return s.format(self.name, self.reps, self.date)

    @classmethod
    def from_str(cls, s):
        """Return a song object from the string representation."""
        name = s[:35].strip()
        reps = int(s[38:41])
        date = datetime.date(int(s[50:54]), int(s[47:49]), int(s[44:46]))
        return cls(name, reps, date)

class songList(object):
    """Store list of songs and useful methods."""
    pass

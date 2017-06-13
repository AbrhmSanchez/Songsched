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

    def to_csv(self):
        """Return a string in csv format."""
        return '{0},{1},{2:%d/%m/%Y}'.format(self.name, self.reps, self.date)

    @classmethod
    def from_str(cls, s):
        """Return a song object from the string representation."""
        name = s[:35].strip()
        reps = int(s[38:41])
        date = datetime.date(int(s[50:54]), int(s[47:49]), int(s[44:46]))
        return cls(name, reps, date)

    @classmethod
    def from_csv(cls, s):
        """Return a song object from a csv file line."""
        name, reps, s = s.split(',')
        date = datetime.date(int(s[6:10]), int(s[3:5]), int(s[:2]))
        return cls(name, int(reps), date)

class songList(object):
    """Store a list of songs and some useful methods."""
    def __init__(self, songList=[]):
        self.songList = songList

    @classmethod
    def from_file(cls, file):
        """Return songList object from a csv file."""
        try:
            with open(file+'.csv') as f:
                songList = [song.from_csv(line) for line in f]
                return cls(songList)
        except Exception as e:
            print('There was an exception:', e)
            return cls()

    def to_file(self, file):
        """Writes songList to file using the song.to_csv() method.
        
        This method backs up the file if it already exists.
        """
        try:
            with open(file+'.csv') as f:
                with open(file+'.BAK', 'w') as b:
                    b.write(f.read())
        except:
            pass
        with open(file+'.csv', 'w') as f:
            str_list = [song.to_csv() for song in self.songList]
            f.write('\n'.join(str_list))

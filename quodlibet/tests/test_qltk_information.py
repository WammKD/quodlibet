from tests import add, TestCase
from qltk.information import Information
from formats._audio import AudioFile

def AF(*args, **kwargs):
    a = AudioFile(*args, **kwargs)
    a.sanitize()
    return a

class TInformation(TestCase):
    def setUp(self):
        from qltk.watcher import SongWatcher
        self.watcher = SongWatcher()

    def test_none(self):
        Information(self.watcher, []).destroy()

    def test_one(self):
        f = AF({"~filename": "/dev/null"})
        Information(self.watcher, [f]).destroy()

    def test_two(self):
        f = AF({"~filename": "/dev/null"})
        f2 = AF({"~filename": "/dev/null2"})
        Information(self.watcher, [f, f2]).destroy()

    def test_album(self):
        f = AF({"~filename": "/dev/null", "album": "woo"})
        f2 = AF({"~filename": "/dev/null2", "album": "woo"})
        Information(self.watcher, [f, f2]).destroy()

    def test_artist(self):
        f = AF({"~filename": "/dev/null", "artist": "woo"})
        f2 = AF({"~filename": "/dev/null2", "artist": "woo"})
        Information(self.watcher, [f, f2]).destroy()

    def tearDown(self):
        self.watcher.destroy()
add(TInformation)

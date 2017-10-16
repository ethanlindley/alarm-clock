import random
import time
import pyaudio
import wave


"""

todo::

properly allow users to select a time that they would like to wake up rather than
asking them how many hours they want to sleep for. could be done using a GUI framework,
such as PyQT or Tk.

"""


class AlarmClock:
    def __init__(self):
        self.chunk = 1024
        # add desired music here under the music package
        self.songs = ["", "", ""]
        self.choice = random.choice(self.songs)
        self.hour = input("how many hours would you like to sleep for?: ")
        self.real_hour = self.hour * 3600
        self.p = pyaudio.PyAudio()
        self.wakeywakey()

    def wakeywakey(self):
        time.sleep(self.real_hour)

        wf = wave.open(self.choice, "rb")  # 16 - bit float scm signed wav

        stream = self.p.open(
            format=self.p.get_format_from_width(wf.getsampwidth()),
            channels=wf.getnchannels(),
            rate=wf.getframerate(),
            output=True
        )
        data = wf.readframes(self.chunk)

        while data != '':
            stream.write(data)
            data = wf.readframes(self.chunk)

        stream.close()
        self.p.terminate()

    def links(self):
        return self.songs

    def hour(self):
        return self.hour


main = AlarmClock()

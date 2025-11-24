

class Television:
    MIN_VOLUME = 0
    MAX_VOLUME = 2
    MIN_CHANNEL = 0
    MAX_CHANNEL = 3

    def __init__(self, status=False, muted=False, volume=MIN_VOLUME, channel=MIN_CHANNEL):
        self.__status = status
        self.__muted = muted
        self.__volume = volume
        self.__channel = channel

    #turn the TV on and off
    def power(self):
        if not self.__status:
            self.__status = True
        else:
            self.__status = False

    #mute and unmute the volume
    def mute(self):
        if not self.__muted:
            self.__muted = True
        else:
            self.__muted = False

    #increase the TV channel by 1, go to first channel if already at last one
    def channel_up(self):
        if self.__channel == self.MAX_CHANNEL:
            self.__channel = self.MIN_CHANNEL
        else:
            self.__channel += 1

    #decrease the TV channel by 1, go to last channel if at first channel
    def channel_down(self):
        if self.__channel == self.MIN_CHANNEL:
            self.__channel = self.MAX_CHANNEL
        else:
            self.__channel -= 1

    #increase the volume
    def volume_up(self):
        self.__muted = False
        if self.__volume == self.MAX_VOLUME:
            pass
        else:
            self.__volume += 1

    #decrease the volume
    def volume_down(self):
        self.__muted = False
        if self.__volume == self.MIN_VOLUME:
            pass
        else:
            self.__volume -= 1

    def __str__(self):
        return f'Power = {self.__status}, Channel = {self.__channel}, Volume = {self.__volume}'


    ...
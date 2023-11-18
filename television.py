class Television:
    """
    A class representing a television with basic functionalities.
    """

    MIN_VOLUME: int = 0
    MAX_VOLUME: int = 2
    MIN_CHANNEL: int = 0
    MAX_CHANNEL: int = 3

    def __init__(self) -> None:
        """
        Initialize a Television object.

        The initial state has power off, not muted, minimum volume, and minimum channel.
        """
        self.__status: bool = False
        self.__muted: bool = False
        self.__volume: int = Television.MIN_VOLUME
        self.__channel: int = Television.MIN_CHANNEL
        self.__temp: int = 0

    def power(self) -> None:
        """
        Toggle the power status of the television.
        """
        if self.__status:
            self.__status = False
        else:
            self.__status = True

    def mute(self) -> None:
        """
        Toggle the mute status of the television.
        """
        if self.__status:
            if self.__muted:
                self.__muted = False
                self.__volume = self.__temp
            else:
                self.__muted = True
                self.__temp = self.__volume
                self.__volume = Television.MIN_VOLUME

    def channel_up(self) -> None:
        """
        Increase the channel by 1, wrapping around if it exceeds the maximum channel.
        """
        if self.__status:
            if self.__channel < Television.MAX_CHANNEL:
                self.__channel += 1
            else:
                self.__channel = Television.MIN_CHANNEL

    def channel_down(self) -> None:
        """
        Decrease the channel by 1, wrapping around if it goes below the minimum channel.
        """
        if self.__status:
            if self.__channel > Television.MIN_CHANNEL:
                self.__channel -= 1
            else:
                self.__channel = Television.MAX_CHANNEL

    def volume_up(self) -> None:
        """
        Increase the volume by 1, ensuring it does not exceed the maximum volume.
        """
        if self.__status:
            self.__muted = False
            self.__volume = self.__temp
            if self.__volume < Television.MAX_VOLUME:
                self.__volume += 1

    def volume_down(self) -> None:
        """
        Decrease the volume by 1, ensuring it does not go below the minimum volume.
        """
        if self.__status:
            self.__muted = False
            self.__volume = self.__temp
            if self.__volume > Television.MIN_VOLUME:
                self.__volume -= 1

    def __str__(self) -> str:
        """
        Return a string representation of the television's status.
        """
        return f'Power = {self.__status}, Channel = {self.__channel}, Volume = {self.__volume}'

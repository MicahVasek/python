class Television
    
    The television class and constants
    

    MIN_VOLUME int = 0
    MAX_VOLUME int = 2
    MIN_CHANNEL int = 0
    MAX_CHANNEL int = 3

    def __init__(self) - None
        
        Initialize the object and private variables
        
        self.__status bool = False
        self.__muted bool = False
        self.__volume int = Television.MIN_VOLUME
        self.__channel int = Television.MIN_CHANNEL
        self.__temp int = 0

    def power(self) - None
        
        Toggle power
        
        if self.__status
            self.__status = False
        else
            self.__status = True

    def mute(self) - None
        
        Toggle mute
        
        if self.__muted
            self.__muted = False
            self.__volume = self.__temp
        else
            self.__muted = True
            self.__temp = self.__volume
            self.__volume = Television.MIN_VOLUME

    def channel_up(self) - None
        
        Increase channel by 1, wrap around if it goes above max
        
        if self.__status
            if self.__channel  Television.MAX_CHANNEL
                self.__channel += 1
            else
                self.__channel = Television.MIN_CHANNEL

    def channel_down(self) - None
        
        Decrease channel by 1, wrap around if it goes below min
        
        if self.__status
            if self.__channel  Television.MIN_CHANNEL
                self.__channel -= 1
            else
                self.__channel = Television.MAX_CHANNEL

    def volume_up(self) - None
        
        Increase volume by 1, does not go above max
        
        if self.__status
            self.__muted = False
            self.__volume = self.__temp
            if self.__volume  Television.MAX_VOLUME
                self.__volume += 1

    def volume_down(self) - None
        
        Decrease volume by 1, does not go below min
        
        if self.__status
            self.__muted = False
            self.__volume = self.__temp
            if self.__volume  Television.MIN_VOLUME
                self.__volume -= 1

    def __str__(self) - str
        
        Return a string checking all statuses
        
        return f'Power = {self.__status}, Channel = {self.__channel}, Volume = {self.__volume}'

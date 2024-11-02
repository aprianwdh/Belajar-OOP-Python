from abc import ABC,abstractmethod

class Button(ABC):

    def __init__(self,inputLink):
        self.link = inputLink

    @abstractmethod
    def Click(self):
        pass

    @property
    @abstractmethod
    def link(self,set_link):
        pass

class PushButton(Button):

    def Click(self):
        return f"Go To : {self.link}"
    
    @Button.link.setter
    def link(self,set_link):
        self.__link = set_link

    @link.getter
    def link(self):
        return self.__link
    

tombol1 = PushButton("WWW.com")

print(tombol1.Click())
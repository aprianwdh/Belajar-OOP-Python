from abc import ABC,abstractclassmethod,abstractmethod

class Button(ABC):

    @abstractmethod
    def click(self,word):
        return word

class RadioButton(Button):

    def click(self):
        return 'Radio click'
    def oiaios(self):
        print("adeada")
    pass


class Checklist(Button):
    def click(self, word="Checklist"):
        return super().click(word)


button1 = RadioButton()
print(button1.click())

button2 = Checklist()
print(button2.click())
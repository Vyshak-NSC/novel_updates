from kivy.app import App
from util import LNChecker
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout

class CardTemplate(BoxLayout):
    def shorten(self, name):
        if len(name) > 20:
            return name[:30] + "..."
        else:
            return name
    def __init__(self,card_name='',chap_name='',**kwargs):
        super().__init__(**kwargs)
        self.ids.card_label.text = card_name.title()
        title = self.shorten(chap_name.title())
        
        if title == "Novel Not found":
            display_txt = "Novel not Found"
        else:
            display_text = title
        self.ids.chapter_name.text = title# "Latest Chapter: " + self.shorten(chap_name.title())


class Screen(FloatLayout):
    def __init__(self,**kwargs):
        super(Screen,self).__init__(**kwargs)
        self.last_cardy = self.ids.card_scroll.y +100

    def add_card(self,text):
        cardx = self.ids.input.x
        cardy = self.last_cardy -50
        name = self.ids.novel_name.text
        chap = self.get_chap(text)
        
        card = CardTemplate(card_name=name,chap_name=chap)
        card.pos = (cardx, cardy)
        

        self.ids.card_scroll.add_widget(card)
        self.last_cardy = cardy
    
    def get_chap(self,name):
        inst = LNChecker(name)
        current_chap = inst.get_curr_chap()
        #inst.run()
        return current_chap

class LNUpdateApp(App):
    def build(self):
        return Screen()


if __name__ == '__main__':
    LNUpdateApp().run()

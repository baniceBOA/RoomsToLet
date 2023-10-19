from kivymd.uix.list import BaseListItem, OneLineRightIconListItem, TwoLineRightIconListItem, IRightBodyTouch
from kivymd.uix.selectioncontrol import MDSwitch
from kivy.properties import BooleanProperty
from kivy.metrics import dp
from kivy.lang import Builder
import os
Builder.load_file(os.path.join(os.path.dirname(__file__), 'listitem.kv'))
class BaseListItemWithSwitch(BaseListItem):
    active = BooleanProperty(False)
    def on_size(self, *args):
        pass

class RightContainerWithSwitch(IRightBodyTouch, MDSwitch):
    pass

class OnelineIconListItemWithSwitch(OneLineRightIconListItem, BaseListItemWithSwitch):
    pass
class TwoLineIconListItemWithSwitch(TwoLineRightIconListItem, BaseListItemWithSwitch):
    pass


import kivy
kivy.require('1.0.7')

import kivy.utils as utils
from kivy.base import EventLoop
from kivy.graphics.instructions import Instruction,InstructionGroup
from kivy.graphics import Color, Rectangle
from kivy.core.window import Window
from kivy.uix.label import Label
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.uix.boxlayout import BoxLayout
from kivy.graphics import Color, Rectangle
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.image import Image
from kivy.adapters.listadapter import ListAdapter
from kivy.uix.listview import ListItemButton, ListView
from kivy.uix.gridlayout import GridLayout
from kivy.uix.screenmanager import Screen
from kivy.graphics import BorderImage
from kivy.app import App
from kivy.uix.button import Button
from kivy.graphics import Color, Line, Rectangle
from kivy.properties import StringProperty
from kivy.properties import ListProperty
from kivy.properties import NumericProperty


class Table(Widget):
    primary_color = StringProperty('ffffcc')
    secondary_color = StringProperty('ffffcc')
    header_color = StringProperty('ffffcc')
    cols_titles = ListProperty({"d","f"})
    table_columns = NumericProperty(3)
    table_rows = NumericProperty(5)

    primaryorsecondary = 1


    class MyLabelPrimary(Label):
        def on_size(self, *args):
            self.canvas.before.clear()
            with self.canvas.before:
                # c = utils.get_color_from_hex(TV.primary)
                Color(0, 0, 1, .5)
                Rectangle(pos=self.pos, size=self.size)
                BorderImage(pos=(self.x, self.y + 1), size=(self.width, self.height - 2), border=(0, 0, 0, 50),
                            Color=Table.primary_color)
    "=============================================================================================================================================="

    class MyLabelSecondary(Label):
        def on_size(self, *args):
            self.canvas.before.clear()
            with self.canvas.before:
                # Color=TV.currentColor
                c = (0, 2, 0, 1)
                Color(0, 7, 0, .5)
                Rectangle(pos=self.pos, size=self.size)
                BorderImage(pos=(self.x, self.y + 1), size=(self.width, self.height - 2), border=(0, 0, 0, 50),
                            Color=Table.secondary_color)

    "=============================================================================================================================================="

    class MyLabelHeader(Label):
        def on_size(self, *args):
            self.canvas.before.clear()
            with self.canvas.before:
                # Color=TV.currentColor
                # text_size: self.size
                # c = (0, 2, 0, 1)
                Color(1, 0, 0, .5)
                Rectangle(pos=self.pos, size=self.size)
                BorderImage(pos=(self.x, self.y + 1), size=(self.width, self.height - 2), border=(0, 0, 0, 50),
                            Color=Table.header_color)
    "=============================================================================================================================================="
    "Outline the size of the grid and add the headers"
    grid = GridLayout(cols=cols_titles.get(0).length,rows=table_rows)
    for i in cols_titles:
        label = MyLabelHeader(text=i)

    "How I handle adding of new data, not sure if this is the ideal way"
    def addCollumn(list):
        if Table.primaryorsecondary == 1:
            for i in list:
                label = Table.MyLabelPrimary(text=str(i))
                Table.grid.add_widget(label)
            Table.primaryorsecondary=Table.primaryorsecondary*-1
        else:
            for i in list:
                label = Table.MyLabelSecondary(text=str(i))
                Table.grid.add_widget(label)
            Table.primaryorsecondary = Table.primaryorsecondary * -1


class TestApp(App):

    def build(self):
        self.root = root = Table(cols_titles={"test","this"})
        root.addCollumn(["test","this"])
        # print("success")
        return root
"=============================================================================================================================================="

if __name__ == '__main__':
    TestApp().run()

# table=createTable()
# table=createTable()

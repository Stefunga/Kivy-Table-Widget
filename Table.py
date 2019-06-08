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
from kivy.core.window import Window

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



# class Table(Widget):
#     primary_color = StringProperty('ffffcc')
#     secondary_color = StringProperty('ffffcc')
#     header_color = StringProperty('ffffcc')
#     cols_titles = ListProperty({"d","f"})
#
#     '''Number of the columns, defaults to 3'''
#     table_columns = NumericProperty(3)
#
#     '''Number of the rows, defaults to 5'''
#     table_rows = NumericProperty(5)
#
#     "Outline the size of the grid and add the headers"
#     grid = GridLayout(cols=cols_titles.get(0).length,rows=table_rows)
#
#     for i in cols_titles:
#         label = MyLabelHeader(text=i)
#
#     "How I handle adding of new data, not sure if this is the ideal way"
#     def addCollumn(list):
#         if Table.primaryorsecondary == 1:
#             for i in list:
#                 label = Table.MyLabelPrimary(text=str(i))
#                 Table.grid.add_widget(label)
#             Table.primaryorsecondary=Table.primaryorsecondary*-1
#         else:
#             for i in list:
#                 label = Table.MyLabelSecondary(text=str(i))
#                 Table.grid.add_widget(label)
#             # Table.primaryorsecondary = Table.primarimport

class Table(Widget):

    primary_color = StringProperty('ffffcc')
    secondary_color = StringProperty('ffffcc')

    header_color = StringProperty('ffffcc')
    
    cols_titles = ListProperty({"d", "f"})

    table_height = NumericProperty(3)

    table_width = NumericProperty(3)
    '''Number of the columns, defaults to 3'''
    table_columns = NumericProperty(3)

    '''Number of the rows, defaults to 5'''
    table_rows = NumericProperty(5)

    '''Table data in 2 dimensional array'''
    # table_rows = ListProperty()
    table_data = []

    def addRow(self,list):
        # if(len(list)>self.table_rows):
        #     print("Incorrect size")
        self.table_data.insert(0,list)

        # if Table.primaryorsecondary == 1:
        #     for i in list:
        #         label = Table.MyLabelPrimary(text=str(i))
        #         Table.grid.add_widget(label)
        #     Table.primaryorsecondary = Table.primaryorsecondary * -1
        # else:
        #     for i in list:
        #         label = Table.MyLabelSecondary(text=str(i))
        #         Table.grid.add_widget(label)
        #     Table.primaryorsecondary = Table.primaryorsecondary * -1
    def __init__(self, **kwargs):
        super(Table, self).__init__(**kwargs)

        primaryorsecondary = 1
        "=============================================================================================================================================="
        "Outline the size of the grid and add the headers"
        with self.canvas:
            self.grid = GridLayout(cols=self.table_columns, rows=self.table_rows,size=[self.table_width,self.table_height])
        print("test:"+str(self.table_columns))
        primaryorsecondary = 1
        rowCheck = 0
        while rowCheck < self.table_rows:
            columnCheck = 0
            while columnCheck < self.table_columns:
                if primaryorsecondary == 1:
                    label = MyLabelPrimary(text="primary")
                else:
                    label = MyLabelSecondary(text="secondary")
                self.grid.add_widget(label)
                columnCheck = columnCheck+1
            rowCheck = rowCheck + 1
            primaryorsecondary = primaryorsecondary*-1

class TestApp(App):

    def build(self):
        self.root = root = Table(table_columns=6,table_rows=6,table_height =500,table_width=600)
        root.addRow(["2"])
        return root
"=============================================================================================================================================="

if __name__ == '__main__':
    TestApp().run()                                                                                          
                                                                                                                                                        

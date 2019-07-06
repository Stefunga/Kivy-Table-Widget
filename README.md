# Kivy-Table-Widget
small widget for creating tables
## Use
This widget is to be used in any Kivy Python application.
widget creation, can be instantiated with all or no variables.
```
Table(table_columns=6,table_rows=6,table_height =500,table_width=800,header_color=[0,1,1,.3])
```
How to add a row of data to the table, needs to be added in list form.
```
addRow(["Data","Data2","Data3","Data4","Data5","Data6"])
```
How to add headers of to the table, needs to be added in list form.
```
root.addHeader(["a","b","c","d","e","f","g"])
```

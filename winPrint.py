from win32com.client import Dispatch
import pathlib

name = "Chase Brown"
access = "Escort Required"
company = "Aunalytics"

tag_path = pathlib.Path('./tag.label')

printer_com = Dispatch('Dymo.DymoAddIn')
my_printer = printer_com.GetDymoPrinters()
printer_com.SelectPrinter(my_printer)

printer_com.Open(tag_path)

printer_label = Dispatch('Dymo.DymoLabels')

printer_label.SetField('Access', access)
printer_label.SetField('Name', name)
printer_label.SetField('Company', company)

printer_com.StartPrintJob()
printer_com.Print(1, False)
printer_com.EndPrintJob()


# print(printer_com.GetDymoPrinters())
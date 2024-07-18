# from blabel import LabelWriter
# import os
# # import subprocess
#
# label_writer = LabelWriter("template.html",
#                            default_stylesheets=("style.css",))
# records= [
#     dict(sample_id=arg, sample_name="google is google")
# ]
#
# label_writer.write_labels(records, target='label.pdf')
#
# os.system('PDFtoPrinter.exe label.pdf -p "TSC TTP-244 Pro"')
#

# count = 234
# print(f"{count:04d}")

# result = subprocess.run("Get-Printer | Select-Object Name, ShareName")
# print(result.stdout)

# import subprocess
#
# # Define the PowerShell command to get printer names and shared names
# command = 'powershell "Get-Printer | Select-Object Name"'
# # command = "Get-Printer | Select-Object -ExpandProperty Name | Format-Table -HideTableHeaders"
#
# # Run the command
# process = subprocess.run(command, capture_output=True, text=True, shell=True)
#
# # Capture the output
# output = process.stdout
# # print(output)
#
# # # Print the output
# output_split = output.split("\n")
# printer_name = output_split[3:len(output_split)-3]
# for printer in printer_name:
#     printer_name_no_space = printer.rstrip(" ")
#     print(printer_name_no_space, len(printer_name_no_space))

# import socket
#
# # Get the computer name
# computer_name = socket.gethostname()
#
# # Print the computer name
# print("Computer Name:", computer_name)


# google = 39
# print(f"{54}".zfill(google))


# from blabel import LabelWriter
# import os
# label_writer = LabelWriter("template.html",
#                            default_stylesheets=("style.css",))
# arg = ["google", "apple"]
# records= [
#     dict(sample_id=arg, sample_name="google is google")
# ]

# label_writer.write_labels(records, target='label1.pdf')

# os.system('PDFtoPrinter.exe label1.pdf -p "TSC TTP-244 Pro"')



# import yaml
# with open('Recipes\Station_01\google\label_spec.yaml', 'r') as file:
#     data = yaml.load(file, Loader=yaml.SafeLoader)

# print(data['serialNo'])
# data['serialNo'] += 1

# with open('Recipes\Station_01\google\label_spec.yaml', 'w') as file:
#     yaml.dump(data, file, default_flow_style=False)

# with open('Recipes\Station_01\google\label_spec.yaml', 'r') as file:
#     data = yaml.load(file, Loader=yaml.SafeLoader)

# print(data['serialNo'])

# x = "00286409130118C3M706710724001444"
# y=2
# for i in range(y):
#     print(len(x))


import pymelsec  as pymc
from pymelsec.constants import DT
import time
data_reg = {
    'model' : 'D520',              # 0 - without flenz, 1 - with flenz
    'rh_scan' : 'D400',            # right side scanner data
    'lh_scan' : 'D500',            # left side scanner data
    'repeated_popup' : 'D700',     # repeated barcode popup
    'data1' : 'D100',
    'data2' : 'D101',
    'data3' : 'D102',
    'data4' : 'D103'
}

host = '192.168.1.50'
port = '1200'
plc = pymc.Type3E(host=host, port=int(port))
plc.connect(ip=host, port=int(port))
# plc._set_comm_type("ascii")
value = []

while True:
    for i in range(19):
        data = plc.batch_read(ref_device=f'{data_reg["rh_scan"]}', read_size=19, data_type=DT.UWORD)[i].value

        value.append(data)
    # data = plc.batch_read(ref_device=f'{data_reg["data2"]}', read_size=1, data_type=DT.UWORD)[0].value
    print(value)
    value.clear()
    print('')
    print('')
    time.sleep(1)
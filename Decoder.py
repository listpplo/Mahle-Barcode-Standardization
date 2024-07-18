from datetime import datetime
import yaml
import re
from datetime import datetime
from PySide6.QtCore import QTime

"""
Action table
0 -- No Action
1 -- date -- format provided
2 -- time -- format provided
3 -- custom text -- add as it is
4 -- serial no -- provide total no of char.
5 -- shift -- to be decoded with the current time
"""


def natural_sort_key(s):
    return [int(text) if text.isdigit() else text.lower() for text in re.split('([0-9]+)', s)]


def Decoder(constructFile: str, serialNo: int = 1) -> str:
    decoded_data = ""

    with open(constructFile, "r+") as file:
        data: dict = yaml.load(file, Loader=yaml.SafeLoader)

    sorted_keys = sorted(data.keys(), key=natural_sort_key)
    print(sorted_keys)
    if data["enable"]:
        for key in sorted_keys:
            if key != "enable":
                try:
                    typ, value = data[f"{key}"].split("~")
                    print(typ)
                except Exception as e:
                    print(f"Printed ---- {e}")
                    typ = 0

                match typ:
                    case "0":
                        pass
                    case "1":
                        decoded_data = decoded_data + datetime.now().__format__(value)
                    case "2":
                        decoded_data = decoded_data + datetime.now().__format__(value)
                    case "3":
                        decoded_data = decoded_data + value
                    case "4":
                        decoded_data = decoded_data + f"{serialNo}".zfill(int(value))
                    case "5":
                        try:
                            time_now = datetime.now().time()

                            with open("Config/Timer.yaml", "r+") as file:
                                data = yaml.load(file, Loader=yaml.SafeLoader)

                            shift_A = QTime.fromString(data["Shift_A"]).toPython()
                            shift_B = QTime.fromString(data["Shift_B"]).toPython()
                            shift_C = QTime.fromString(data["Shift_C"]).toPython()

                            if shift_A <= time_now < shift_B:
                                decoded_data = decoded_data + "A"
                            elif shift_B <= time_now < shift_C:
                                decoded_data = decoded_data + "B"
                            else:
                                decoded_data = decoded_data + "C"
                        except Exception as e:
                            print(e)
        print(decoded_data)

        return decoded_data

    else:
        return ""


if __name__ == "__main__":
    print(Decoder("Recipes/Station_01/google/barcode.yaml"))

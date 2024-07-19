import os

os.system("pyside6-uic UI/MainWindow.ui -o MainWindow.py")
os.system("pyside6-uic UI/RecipeWindow.ui -o RecipeWindow.py")
os.system("pyside6-uic UI/ConnectionWindow.ui -o ConnectionWindow.py")
os.system("pyside6-uic UI/popWindow.ui -o popWindow.py")
os.system("pyside6-uic UI/SubRecipeWindow.ui -o subRecipe.py")
os.system("pyside6-uic UI/namePopup.ui -o namePopup.py")
os.system("pyside6-uic UI/DataWindow.ui -o DataWindow.py")
os.system("pyside6-uic UI/plcMapping.ui -o plcMapping.py")
os.system("pyside6-uic UI/passwordPopUp.ui -o passwordUI.py")
os.system("pyside6-rcc UI/asset.qrc -o asset_rc.py")
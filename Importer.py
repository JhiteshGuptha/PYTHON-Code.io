print(f"In Importer.py, __name__ is {__name__}")
print()

# Everything in the NameMain.py will be executed instead of if __name__ == "__main__"
# Importer.py cannot access anything inside if __name__ == "__main__ of NameMain.py

import NameMain

print("--------------------------------------------------")
print("Running Functions from NameMain.py by Importing It")
print("--------------------------------------------------\n")
NameMain.greet("Code.io")
print(NameMain.square(10))


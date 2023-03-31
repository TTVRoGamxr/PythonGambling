import os, requests

GambleScriptVersion = {1: "https://raw.githubusercontent.com/TTVRoGamxr/PythonGambling/main/GamblingExtravanganza_V1.py", 2: "https://raw.githubusercontent.com/TTVRoGamxr/PythonGambling/main/GamblingExtravaganza_V2.py"}

def Clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def CheckInput(NewInput):
    try:
        NewInput = int(NewInput)
        return "Int", int(NewInput)
    except ValueError:
        pass
    try:
        NewInput = float(NewInput)
        return "Float", float(NewInput)
    except ValueError:
        pass
    try:
        NewInput = str(NewInput)
        return "String", str(NewInput)
    except ValueError:
        pass

Clear()
print("Legacy [Discontinued] - 1")
print("New - 2")

print()

print("• - Input '1' Or '2' - •")
print()
NewInput, NewVersion = CheckInput(input("What version would you like to load: "))

if NewInput == "Int" and (NewVersion == 1 or NewVersion == 2):
    Script = requests.get(GambleScriptVersion[NewVersion])
    Code = Script.text

    exec(Code)

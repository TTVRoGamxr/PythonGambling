# Libraries
import random, time, os, math, requests

# Main Settings

LoadingBar = {0: "▯▯▯▯▯▯▯▯▯▯", 1: "▮▯▯▯▯▯▯▯▯▯", 2: "▮▮▯▯▯▯▯▯▯▯", 3: "▮▮▮▯▯▯▯▯▯▯", 4: "▮▮▮▮▯▯▯▯▯▯", 5: "▮▮▮▮▮▯▯▯▯▯", 6: "▮▮▮▮▮▮▯▯▯▯", 7: "▮▮▮▮▮▮▮▯▯▯", 8: "▮▮▮▮▮▮▮▮▯▯", 9: "▮▮▮▮▮▮▮▮▮▯", 10: "▮▮▮▮▮▮▮▮▮▮"}

GameSettings = {"Icons": {"Money": "💵", "Insurance": "🩹", "Spin": "💫", "Win": "⭐", "Lose": "❌", "Save": "⏏️"}, "BetData": {"Min": 10, "Max": 30000}, "MaxPreviousAttempts": 5}
InsuranceShopData = {"PricePerPercent": 30, "PricePerDuration": 100, "MaxPercent": 50, "MaxDuration": 100, "Discounts": {"Percent": {"Amount": 20, "Discount": 0.05}, "Duration": {"Amount": 10, "Discount": 0.025}}}
BegActionData = {"Phrases": {"Good": ["Oh you poor thing", "Awww", "Here you go", "Have a great day", "Hopefully this helps", "Enjoy", "Here money :D"], "Bad": ["Imagine begging", "Ewww, a beggar", "Bro's actually begging", "smh... You beggars", "Oh my god, go away!"]}, "PeopleType": ["Celebrity", "Business Owner", "Rich Kid", "Kind Random Person", "Annoying Random Person"], "Chances": ["Celebrity"] + ["Business Owner"]*49 + ["Rich Kid"]*150 + ["Kind Random Person"]*200 + ["Annoying Random Person"]*600, "MainData": {"MinMoney": 0, "MaxMoney": 175, "VisitAmounts": [1]*75 + [2]*15 + [5]*9 + [10]}, "Multipliers": {"Celebrity": {"Min": 500, "Max": 1000}, "Business Owner": {"Min": 200, "Max": 500}, "Rich Kid": {"Min": 75, "Max": 200}, "Kind Random Person": {"Min": 10, "Max": 100}, "Annoying Random Person": {"Min": 0, "Max": 0}}}

Icons = GameSettings["Icons"]
BetData = GameSettings["BetData"]

GamblingActive = False

UpdateData = {"UpdateVersion": "1.6.1", "UpdateLog": ["• Beg Action", "• All In Gamemode", "• Decreased Starting Money", "• Decreased Starting Insurance", "• Fixed Crate Chances", "• Bug Fixes"], "SpecialShoutouts": ["• CesarTheGamer#2616", "• neji#6958"], "ScriptVersion": 2, "LatestVersion": None}

# Gambling Data

GamblingFunctions = {}

DiceData = {"RollNumbers": {"MaxRoll": 100, "MediumRoll": 90, "SmallRoll": 55, "LoseRoll": 54}, "Multipliers": {"MaxWin": 15, "MediumWin": 5, "SmallWin": 1.75, "Lose": 0}}
SlotsData = {"SlotIcons": {"Jackpot": "⭐", "Win": "💵", "Lose": "❌", "IconsList": "⭐" + "💵"*4 + "❌"*5}, "Multipliers": {"Jackpot": 50, "Win": 2, "Lose": 0}}
CoinflipData = {"CoinflipIcons": {"heads": "⬆️ ", "tails": "⬇️ "}, "Multipliers": {"Win": 1.75, "Lose": 0}, "Chances": ["heads", "tails"]}
RPSData = {"RPSIcons": {"rock": "🦴", "paper": "📃", "scissors": "✂️ "}, "RPSList": ["rock", "paper", "scissors"], "Multipliers": {"Win": 2.15, "Tie": 0.95, "Lose": 0}}
CupsData = {"CupsIcons": {"WinItem": "💎", "LoseItem": "🕳️"}, "Multipliers": {"Win": 2.25, "Lose": 0}}
EggsData = {"EggIcons": {"Safe": "🥚", "Bust": "💣"}, "RangeNumbers": {"Exact": 0, "SmallRange": 5, "MainRange": 15}, "Multipliers": {"Exact": 15, "SmallRange": 3.25, "MainRange": 1.75, "BaseRange": 1.35, "Lose": 0}}
BJData = {"BJIcons": {"BJ": "🃏", "Win": "⭐", "Tie": "🤝", "Bust": "💣"}, "CardRange": {"Min": 1, "Max": 11}, "Multipliers": {"BJ": 3, "Win": 2, "Tie": 0.95, "Lose": 0}}
AllInData = {"Chances": {"Big Win": 30, "Win": 21, "Lose": 20, "Insurance": ["Successful"]*50 + ["Unsuccessful"]*50}, "Multipliers": {"Big Win": 3.5, "Win": 1.65, "Lose": 0}}
CratesData = {1: {"CrateName": "Randomizer Crate", "Cost": 175, "PrintedChances": [], "Items": {1: {"Name": "Stick", "Weight": 100, "Value": 50}, 2: {"Name": "Scrap", "Weight": 75, "Value": 150}, 3: {"Name": "Egg", "Weight": 20, "Value": 200}, 4: {"Name": "Old Coin", "Weight": 4, "Value": 275}, 5: {"Name": "Weathered Medal", "Weight": 1, "Value": 500}}},
              2: {"CrateName": "Basic Old Crate", "Cost": 250, "PrintedChances": [], "Items": {1: {"Name": "Old Rag", "Weight": 120, "Value": 125}, 2: {"Name": "Old Blanket", "Weight": 60, "Value": 200}, 3: {"Name": "Old Jar", "Weight": 45, "Value": 275}, 4: {"Name": "Old Golden Medal", "Weight": 25, "Value": 450}, 5: {"Name": "Old Gold Piece", "Weight": 9, "Value": 600}, 6: {"Name": "Old Gold Bar", "Weight": 1, "Value": 800}}},
              3: {"CrateName": "Riksy Rates Crate", "Cost": 450, "PrintedChances": [], "Items": {1: {"Name": "Counterfeit Coin", "Weight": 150, "Value": 400}, 2: {"Name": "Silver Coin", "Weight": 49, "Value": 650}, 3: {"Name": "Handmade Gold Coin", "Weight": 1, "Value": 2000}}},
              4: {"CrateName": "Matter Crate", "Cost": 750, "PrintedChances": [], "Items": {1: {"Name": "Useless Matter", "Weight": 500, "Value": 500}, 2: {"Name": "Light Matter", "Weight": 300, "Value": 750}, 3: {"Name": "Handmade Gold Coin", "Weight": 140, "Value": 1250}, 4: {"Name": "Silver Matter", "Weight": 50, "Value": 4500}, 5: {"Name": "Dark Matter", "Weight": 9, "Value": 7500}, 6: {"Name": "Mystery Matter", "Weight": 1, "Value": 15000}}},
              5: {"CrateName": "Mysterious Crate", "Cost": 850, "PrintedChances": [], "Items": {1: {"Name": "Mystery Card", "Weight": 210, "Value": 650}, 2: {"Name": "Mystery Rag", "Weight": 170, "Value": 800}, 3: {"Name": "Mystery Cloak", "Weight": 110, "Value": 900}, 4: {"Name": "Mysterious Figure", "Weight": 9, "Value": 1250}, 5: {"Name": "Mystery Mix", "Weight": 1, "Value": 7500}}},
              }

# Starting Values

StartingData = {"Money": 125, "Insurance": 0.15, "InsuranceDuration": 3}

# Player Data

PlayerData = {"Money": 0, "Insurance": 0, "InsuranceDuration": 0, "Spins": 0, "Wins": 0, "Losses": 0, "SaveFile": None}
PreviousData = {"Method": None, "Bet": 0, "Side":None, "Cup": None, "RPS": None, "Egg": 0, "Crate": 0, "Attempts": 0}

# Functions

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

def SaveData():
    global PlayerData

    if PlayerData["SaveFile"] != None:
        FileName = "C:\PythonGambling\DataSave_" + str(PlayerData["SaveFile"]) + ".txt"
        FileName2 = "C:\PythonGambling\GlobalData.txt"

        if os.path.exists(FileName) and os.path.exists(FileName2):
            SavedData = [str(PlayerData["Money"]) + ",", str(PlayerData["Insurance"]) + ",", str(PlayerData["InsuranceDuration"])]
            SavedData2 = [str(PlayerData["Spins"]) + ",", str(PlayerData["Wins"]) + ",", str(PlayerData["Losses"])]

            WriteData = open(FileName, "w")
            WriteData.writelines(SavedData)
            WriteData.close()

            WriteData2 = open(FileName2, "w")
            WriteData2.writelines(SavedData2)
            WriteData2.close()
            return "SaveSuccess"
        
        else:
           Clear()
           print("• - Save File Doesn't Exist - •") 
           exit()
           
    
    else:
        Clear()
        print("• - No Save File Selected - •")
        exit()

def PrintCrateData(CrateNumber):
    global CratesData

    CrateInfo = CratesData[CrateNumber]
    CratePrintChances = CrateInfo["PrintedChances"]
    CrateItemData = CrateInfo["Items"]
    NewCounter = 0

    print(str(CrateNumber), "• -", CrateInfo["CrateName"], Icons["Money"], str(format(CrateInfo["Cost"], ",")), "- •")
    print()

    for ItemToAdd in range(len(CrateItemData)):
        NewItemData = CrateItemData[ItemToAdd + 1]
        NewItemList = []

        for i in range(NewItemData["Weight"]):
            NewItemList.append(NewItemData["Name"])
        
        for i in range(len(NewItemList)):
            CratePrintChances.append(NewItemList[i])
    
    for Item in range(len(CrateItemData)):
        WantedItem = CrateItemData[Item + 1]
        PrintedItem = WantedItem["Name"]

        for i in range(len(CratePrintChances)):
            if PrintedItem == CratePrintChances[i]:
                NewCounter += 1
            
        ItemPercentage = NewCounter / len(CratePrintChances) * 10000 / 100
        ItemPercentage = str(ItemPercentage)

        PercentageDecimal = ItemPercentage.find(".")
        ItemPercentage = ItemPercentage[:(PercentageDecimal + 3)]

        print("  • -", PrintedItem, "[" + Icons["Money"], str(format(WantedItem["Value"], ",")) + "] -", ItemPercentage + "% - •")
        NewCounter = 0

def ChangePlayerData(DataName, DataValue):
    global PlayerData
    PlayerData[DataName] += DataValue
    SaveData()

def SetSaveFile(SafeSave):
    global PlayerData
    global GamblingActive

    Clear()

    print("• - Available Saves - •")
    print()

    for i in range(5):
        PrintSaveData(i + 1)

    FileName = "C:\PythonGambling\GlobalData.txt"
    FileData = []

    if os.path.exists(FileName):
        DataFile = open(FileName, "r")

        for DataValue in DataFile: 
            Value = DataValue.split(",")
            FileData += Value
            
        print("• - Global Data - •")

        if len(FileData) == 3:
            print(" • Total Spins •", Icons["Spin"], str(format(int(FileData[0]), ",")))
            print(" • Total Wins •", Icons["Win"], str(format(int(FileData[1]), ",")))
            print(" • Total Losses •", Icons["Lose"], str(format(int(FileData[2]), ",")))
        
        else:
            print("• - Error Getting Data - •")

    else:  
        print("• - Error Getting Data - •")

    print()
    print("• - Please Choose A Save File - •")
    print("• - Input A Number Between 1 and 5 - •")
    print()

    InputType, NewInput = CheckInput(input("Choose a save file: "))

    if InputType == "Int":
        if NewInput >= 1 and NewInput <= 5:
            if SafeSave == True:
                SaveData()

            PlayerData["SaveFile"] = NewInput

            FileName = "C:\PythonGambling\DataSave_" + str(PlayerData["SaveFile"]) + ".txt"
            FileData = []

            FileName2 = "C:\PythonGambling\GlobalData.txt"
            FileData2 = []

            if os.path.exists(FileName) and os.path.exists(FileName2):
                DataFile = open(FileName, "r")
                DataFile2 = open(FileName2, "r")

                for DataValue in DataFile:
                    Value = DataValue.split(",")
                    FileData += Value
                
                for DataValue2 in DataFile2:
                    Value2 = DataValue2.split(",")
                    FileData2 += Value2
                
                if len(FileData) == 3 and len(FileData2) == 3:
                    PlayerData["Money"] = int(FileData[0])
                    PlayerData["Insurance"] = float(FileData[1])
                    PlayerData["InsuranceDuration"] = int(FileData[2])
                    PlayerData["Spins"] = int(FileData2[0])
                    PlayerData["Wins"] = int(FileData2[1])
                    PlayerData["Losses"] = int(FileData2[2])

                    Clear()
                    print("• - Save File Successfully Changed - •")
                    GamblingActive = True
                    return "ActionSuccess"
                
                else:
                    Clear()
                    print("• - Error Getting Data - •")
                    GamblingActive = False
                    return "ActionError"
            
            else:
                Clear()
                print("• - Save File Doesn't Exist - •")
                return "ActionError"
        
        else:
            Clear()
            print("• - Invalid Save File - •")
            print("• - Save File Must Be A Number Between 1 And 5 - •")
            return "ActionError"
    
    else:
        Clear()
        print("• - Invalid Save File - •")
        print("• - Save File Must Be A Number Between 1 And 5 - •")
        return "ActionError"

def PrintSaveData(SaveNumber):
    FileName = "C:\PythonGambling\DataSave_" + str(SaveNumber) + ".txt"
    FileData = []

    if os.path.exists(FileName):
        DataFile = open(FileName, "r")

        print("• -", Icons["Save"], " Save", str(SaveNumber), "- •")

        for DataValue in DataFile:
            Value = DataValue.split(",")
            FileData += Value
        
        if len(FileData) == 3:
            print(" • Money •", Icons["Money"], str(format(int(FileData[0]), ",")))

            if int(FileData[2]) == 0:
                print(" • Insurance •", Icons["Insurance"], str(format(int(float(FileData[1]) * 0), ",")) + "%")
                print(" • Insurance Duration •", Icons["Insurance"], str(format(int(FileData[2]), ",")), "Rounds")

                SavedData = [FileData[0] + ",", str(0) + ",", FileData[2]]

                WriteData = open(FileName, "w")
                WriteData.writelines(SavedData)
                WriteData.close()

            else:
                print(" • Insurance •", Icons["Insurance"], str(format(int(float(FileData[1]) * 100), ",")) + "%")
                print(" • Insurance Duration •", Icons["Insurance"], str(format(int(FileData[2]), ",")), "Rounds") 

            print()
        
        else:
            print("• - Error Getting Data - •")
            print()
    
    else:
       print("• - Error Getting Data - •")
       print()

def PrintPlayerData():
    if PlayerData["InsuranceDuration"] == 0:
        PlayerData["Insurance"] = 0

    if PlayerData["Insurance"] > InsuranceShopData["MaxPercent"] / 100:
        ChangePlayerData("Insurance", -(PlayerData["Insurance"]))
        ChangePlayerData("Insurance", InsuranceShopData["MaxPercent"] / 100)
            
    if PlayerData["InsuranceDuration"] > InsuranceShopData["MaxDuration"]:
        ChangePlayerData("InsuranceDuration", -(PlayerData["InsuranceDuration"]))
        ChangePlayerData("InsuranceDuration", InsuranceShopData["MaxDuration"])
    
    InsurancePercentage = str(format(PlayerData["Insurance"] * 100, ","))

    PercentageDecimal = InsurancePercentage.find(".")
    InsurancePercentage = InsurancePercentage[:(PercentageDecimal + 2)]

    Clear()
    print("• - Player Data - •")
    print()
    print(" • Money •", Icons["Money"], str(format(PlayerData["Money"], ",")))
    print(" • Insurance •", Icons["Insurance"], InsurancePercentage + "%")
    print(" • Insurance Duration •", Icons["Insurance"], str(format(PlayerData["InsuranceDuration"], ",")))
    print(" • Spins •", Icons["Spin"], str(format(PlayerData["Spins"], ",")))
    print(" • Wins •", Icons["Win"], str(format(PlayerData["Wins"], ",")))
    print(" • Losses •", Icons["Lose"], str(format(PlayerData["Losses"], ",")))
    print(" • Save File •", Icons["Save"], " " + str(PlayerData["SaveFile"]))

def HardReset():
    global PlayerData

    Clear()
    print("• - Hard Reset Selected - •")
    print("• - Hard Reset Removes All Data And Is Irreversible - •")

    print()
    print("• - Input 'Yes' Or 'No' - •")
    print()
    NewInput, NewChoice = CheckInput(input("Are you sure: "))

    if NewInput == "String":
        if NewChoice.lower() == "yes" or NewChoice.lower() == "no":
            if NewChoice.lower() == "yes":
                for i in range(5):

                    WrittenStartData = [str(StartingData["Money"]) + ",", str(StartingData["Insurance"]) + ",", str(StartingData["InsuranceDuration"])]

                    WriteData = open("C:\PythonGambling\DataSave_" + str(i + 1) + ".txt", "w")
                    WriteData.writelines(WrittenStartData)
                    WriteData.close()
                
                WrittenGlobalData = ["0,", "0,", "0"]

                WriteData = open("C:\PythonGambling\GlobalData.txt", "w")
                WriteData.writelines(WrittenGlobalData)
                WriteData.close()

                
                for i in range(11):
                    Clear()
                    print("• - Hard Rest Initiated - •")
                    print()
                    print("      " + LoadingBar[i], str(i * 10) + "%")
                    time.sleep(random.randint(1, 2) / 2)
                
                time.sleep(1)
                Clear()

                PlayerData["SaveFile"] = None
                PlayerData["Money"] = 0
                PlayerData["Insurance"] = 0
                PlayerData['InsuranceDuration'] = 0
                PlayerData["Spins"] = 0
                PlayerData["Wins"] = 0
                PlayerData["Losses"] = 0

                print("• - Hard Reset Complete - •")
                return "ActionSuccess"
            
            elif NewChoice.lower() == "no":
                return "ActionSuccess"
        
        else:
            Clear()
            print("• - Input Must Be 'Yes' Or 'No' - •")
            return "ActionError"
    
    else:
        Clear()
        print("• - Input Must Be 'Yes' Or 'No' - •")
        return "ActionError"

def ResetSaveData():
    global PlayerData

    Clear()
    print("• - Reset Data Selected - •")
    print()

    print("1 - Reset 1 Data File")
    print("2 - Reset All Data")

    print()
    print("• - Input '1' Or '2' - •")
    print()
    NewInput, NewChoice = CheckInput(input("What would you like to do: "))

    if NewInput == "Int" and (NewChoice == 1 or NewChoice == 2):
        if NewChoice == 1:
            Clear()
            print("• - Available Saves - •")
            print()

            for i in range(5):
                PrintSaveData(i + 1)

            print("• - Choose A File To Reset - •")
            print("• - Input Must A Number Between '1' And '5' - •")
            print()

            InputType, NewFile = CheckInput(input("What file would you like to reset: "))

            if InputType == "Int" and NewFile >= 1 and NewFile <= 5:
                FileName = "C:\PythonGambling\DataSave_" + str(NewFile) + ".txt"

                if os.path.exists(FileName):
                    SavedData = [str(StartingData["Money"]) + ",", str(StartingData["Insurance"]) + ",", str(StartingData["InsuranceDuration"])]

                    WriteData = open(FileName, "w")
                    WriteData.writelines(SavedData)
                    WriteData.close()

                    for i in range(11):
                        Clear()
                        print("• - Resetting Data - •")
                        print()
                        print("    " + LoadingBar[i], str(i * 10) + "%")
                        time.sleep(random.randint(1, 3) / 5)
                    
                    time.sleep(1)
                    Clear()

                    print("• - Data Successfully Reset - •")
                    PlayerData["SaveFile"] = None
                    PlayerData["Money"] = 0
                    PlayerData["Insurance"] = 0
                    PlayerData['InsuranceDuration'] = 0
                    return "ActionSuccess"
                    
                
                else:
                    Clear()
                    print("• - Error Getting File - •")
                    return "ActionError"
            
            else:
                Clear()
                print("• - Input Must A Number Between '1' And '5' - •")
                return "ActionError"
            
        elif NewChoice == 2:
            for i in range(5):
                FileName = "C:\PythonGambling\DataSave_" + str(i + 1) + ".txt"

                if os.path.exists(FileName):
                    SavedData = [str(StartingData["Money"]) + ",", str(StartingData["Insurance"]) + ",", str(StartingData["InsuranceDuration"])]

                    WriteData = open(FileName, "w")
                    WriteData.writelines(SavedData)
                    WriteData.close()
                
                else:
                    Clear()
                    print("• - Error Getting File - •")
                    return "ActionError"
            
            for i in range(11):
                Clear()
                print("• - Resetting Data - •")
                print()
                print("    " + LoadingBar[i], str(i * 10) + "%")
                time.sleep(random.randint(1, 2) / 2)
            
            time.sleep(1)
            Clear()

            print("• - Data Successfully Reset - •")
            PlayerData["SaveFile"] = None
            PlayerData["Money"] = 0
            PlayerData["Insurance"] = 0
            PlayerData['InsuranceDuration'] = 0
            return "ActionSuccess"
    
    else:
        Clear()
        print("• - Input Must Be '1' Or '2' - •")
        return "ActionError"

def MethodDice(GambleType):
    DiceMultipliers = DiceData["Multipliers"]
    DiceRollNumbers = DiceData["RollNumbers"]
    
    if GambleType == "New":
        PrintPlayerData()
        print()

        print("• - Roll Dice Selected - •")
        print()

        print(str(DiceRollNumbers["MaxRoll"]), "• x" + str(DiceMultipliers["MaxWin"]))
        print(str(DiceRollNumbers["MediumRoll"]), "And Above • x" + str(DiceMultipliers["MediumWin"]))
        print(str(DiceRollNumbers["SmallRoll"]), "And Above • x" + str(DiceMultipliers["SmallWin"]))
        print(str(DiceRollNumbers["LoseRoll"]), "And Below • x" + str(DiceMultipliers["Lose"]))

        print()
        print("• - Input A Number Between", Icons["Money"], str(format(BetData["Min"], ",")), "And", Icons["Money"], str(format(BetData["Max"], ",")), "- •")
        print()
        InputType, NewBet = CheckInput(input("How much would you like to bet: "))

        if InputType == "Int":
            if NewBet <= PlayerData["Money"]:
                if NewBet >= BetData["Min"] and NewBet <= BetData["Max"]:
                    RolledNumber = random.randint(1, DiceRollNumbers["MaxRoll"])

                    PreviousData["Method"] = MethodDice
                    PreviousData["Bet"] = NewBet
                    PreviousData["Attempts"] = 0

                    ChangePlayerData("Money", -(NewBet))
                    ChangePlayerData("Spins", 1)

                    Clear()

                    print("• - You Rolled A", str(RolledNumber), "- •")
                    print()

                    if RolledNumber == DiceRollNumbers["MaxRoll"]:
                        WinAmount = math.ceil(NewBet * DiceMultipliers["MaxWin"])

                        print("• -", Icons["Win"], "You Won", Icons["Win"], "- •")
                        print("• - You Earned", Icons["Money"], str(format(WinAmount, ",")), "•", Icons["Money"], str(format(WinAmount - NewBet, ",")), "Profit - •")
                        ChangePlayerData("Money", WinAmount)
                        ChangePlayerData("Wins", 1)
                    
                    elif RolledNumber >= DiceRollNumbers["MediumRoll"]:
                        WinAmount = math.ceil(NewBet * DiceMultipliers["MediumWin"])

                        print("• -", Icons["Win"], "You Won", Icons["Win"], "- •")
                        print("• - You Earned", Icons["Money"], str(format(WinAmount, ",")), "•", Icons["Money"], str(format(WinAmount - NewBet, ",")), "Profit - •")
                        ChangePlayerData("Money", WinAmount)
                        ChangePlayerData("Wins", 1)

                    elif RolledNumber >= DiceRollNumbers["SmallRoll"]:
                        WinAmount = math.ceil(NewBet * DiceMultipliers["SmallWin"])

                        print("• -", Icons["Win"], "You Won", Icons["Win"], "- •")
                        print("• - You Earned", Icons["Money"], str(format(WinAmount, ",")), "•", Icons["Money"], str(format(WinAmount - NewBet, ",")), "Profit - •")
                        ChangePlayerData("Money", WinAmount)
                        ChangePlayerData("Wins", 1)

                    elif RolledNumber <= DiceRollNumbers["LoseRoll"]:
                        if PlayerData["InsuranceDuration"] >= 1:
                            LossAmount = math.ceil(NewBet * (1 - PlayerData["Insurance"]))

                            print("• -", Icons["Lose"], "You Lose", Icons["Lose"], "- •")
                            print("• - You Lost", Icons["Money"], str(format(LossAmount, ",")), "- •")

                            ChangePlayerData("Money", math.ceil(NewBet - LossAmount))
                        
                        else:
                            print("• -", Icons["Lose"], "You Lose", Icons["Lose"], "- •")
                            print("• - You Lost", Icons["Money"], str(format(NewBet, ",")), "- •")

                            ChangePlayerData("Money", (NewBet * DiceMultipliers["Lose"]))

                        ChangePlayerData("Losses", 1)
                    
                    if PlayerData["InsuranceDuration"] >= 1:
                        ChangePlayerData("InsuranceDuration", -1)
                    
                    SaveData()
                    return "GambleSuccess"

                else:
                    Clear()
                    print("• - Bet Must Be A Number Between", Icons["Money"], str(format(BetData["Min"], ",")), "And", Icons["Money"], str(format(BetData["Max"], ",")), "- •")
                    return "GambleError"
            
            else:
                Clear()
                print("• - Bet Must Be Below Your Balance - •")
                return "GambleError"
        
        else:
            Clear()
            print("• - Bet Must Be A Number Between", Icons["Money"], str(format(BetData["Min"], ",")), "And", Icons["Money"], str(format(BetData["Max"], ",")), "- •")
            return "GambleError"
    
    elif GambleType == "Previous":
        NewBet = PreviousData["Bet"]
        InputType = "Int"

        if InputType == "Int":
            if NewBet <= PlayerData["Money"]:
                if NewBet >= BetData["Min"] and NewBet <= BetData["Max"]:
                    RolledNumber = random.randint(1, DiceRollNumbers["MaxRoll"])

                    PreviousData["Method"] = MethodDice
                    PreviousData["Bet"] = NewBet
                    PreviousData["Attempts"] += 1

                    ChangePlayerData("Money", -(NewBet))
                    ChangePlayerData("Spins", 1)

                    Clear()

                    print("• - You Rolled A", str(RolledNumber), "- •")
                    print()

                    if RolledNumber == DiceRollNumbers["MaxRoll"]:
                        WinAmount = math.ceil(NewBet * DiceMultipliers["MaxWin"])

                        print("• -", Icons["Win"], "You Won", Icons["Win"], "- •")
                        print("• - You Earned", Icons["Money"], str(format(WinAmount, ",")), "•", Icons["Money"], str(format(WinAmount - NewBet, ",")), "Profit - •")
                        ChangePlayerData("Money", WinAmount)
                        ChangePlayerData("Wins", 1)
                    
                    elif RolledNumber >= DiceRollNumbers["MediumRoll"]:
                        WinAmount = math.ceil(NewBet * DiceMultipliers["MediumWin"])

                        print("• -", Icons["Win"], "You Won", Icons["Win"], "- •")
                        print("• - You Earned", Icons["Money"], str(format(WinAmount, ",")), "•", Icons["Money"], str(format(WinAmount - NewBet, ",")), "Profit - •")
                        ChangePlayerData("Money", WinAmount)
                        ChangePlayerData("Wins", 1)

                    elif RolledNumber >= DiceRollNumbers["SmallRoll"]:
                        WinAmount = math.ceil(NewBet * DiceMultipliers["SmallWin"])

                        print("• -", Icons["Win"], "You Won", Icons["Win"], "- •")
                        print("• - You Earned", Icons["Money"], str(format(WinAmount, ",")), "•", Icons["Money"], str(format(WinAmount - NewBet, ",")), "Profit - •")
                        ChangePlayerData("Money", WinAmount)
                        ChangePlayerData("Wins", 1)

                    elif RolledNumber <= DiceRollNumbers["LoseRoll"]:
                        if PlayerData["InsuranceDuration"] >= 1:
                            LossAmount = math.ceil(NewBet * (1 - PlayerData["Insurance"]))

                            print("• -", Icons["Lose"], "You Lose", Icons["Lose"], "- •")
                            print("• - You Lost", Icons["Money"], str(format(LossAmount, ",")), "- •")

                            ChangePlayerData("Money", math.ceil(NewBet - LossAmount))
                        
                        else:
                            print("• -", Icons["Lose"], "You Lose", Icons["Lose"], "- •")
                            print("• - You Lost", Icons["Money"], str(format(NewBet, ",")), "- •")

                            ChangePlayerData("Money", (NewBet * DiceMultipliers["Lose"]))

                        ChangePlayerData("Losses", 1)
                    
                    if PlayerData["InsuranceDuration"] >= 1:
                        ChangePlayerData("InsuranceDuration", -1)
                    
                    SaveData()
                    return "GambleSuccess"

                else:
                    Clear()
                    print("• - Bet Must Be A Number Between", Icons["Money"], str(format(BetData["Min"], ",")), "And", Icons["Money"], str(format(BetData["Max"], ",")), "- •")
                    return "GambleError"
            
            else:
                Clear()
                print("• - Bet Must Be Below Your Balance - •")
                return "GambleError"
        
        else:
            Clear()
            print("• - Bet Must Be A Number Between", Icons["Money"], str(format(BetData["Min"], ",")), "And", Icons["Money"], str(format(BetData["Max"], ",")), "- •")
            return "GambleError"

def MethodSlots(GambleType):
    SlotsIcons = SlotsData["SlotIcons"]
    SlotsIconList = SlotsIcons["IconsList"]
    SlotsMultiplier = SlotsData["Multipliers"]
    
    if GambleType == "New":

        PrintPlayerData()
        print()

        print("• - Slots Selected - •")
        print()

        print("1+", SlotsIcons["Jackpot"], "• x" + str(SlotsMultiplier["Jackpot"]))
        print("2+", SlotsIcons["Win"], "• x" + str(SlotsMultiplier["Win"]))
        print("1+", SlotsIcons["Lose"], "• x" + str(SlotsMultiplier["Lose"]))

        print()
        print("• - Input A Number Between", Icons["Money"], str(format(BetData["Min"], ",")), "And", Icons["Money"], str(format(BetData["Max"], ",")), "- •")
        print()
        InputType, NewBet = CheckInput(input("How much would you like to bet: "))

        if InputType == "Int":
            if NewBet <= PlayerData["Money"]:
                if NewBet >= BetData["Min"] and NewBet <= BetData["Max"]:
                    SlotOutcome = []

                    PreviousData["Method"] = MethodSlots
                    PreviousData["Bet"] = NewBet
                    PreviousData["Attempts"] = 0

                    ChangePlayerData("Money", -(NewBet))
                    ChangePlayerData("Spins", 1)

                    for i in range(3):
                        SlotOutcome.append(random.choice(SlotsIconList))

                    Clear()
                    print("• -", SlotOutcome[0], "|", SlotOutcome[1], "|", SlotOutcome[2], "- •")
                    print()
                    
                    if SlotOutcome.count(SlotsIcons["Jackpot"]) == 3:
                        WinAmount = math.ceil(NewBet * SlotsMultiplier["Jackpot"])

                        print("• -", Icons["Win"], "You Won", Icons["Win"], "- •")
                        print("• - You Earned", Icons["Money"], str(format(WinAmount, ",")), "•", Icons["Money"], str(format(WinAmount - NewBet, ",")), "Profit - •")
                        ChangePlayerData("Money", WinAmount)
                        ChangePlayerData("Wins", 1)

                    elif (SlotOutcome.count(SlotsIcons["Win"]) >= 2 or SlotOutcome.count(SlotsIcons["Jackpot"])) and SlotOutcome.count(SlotsIcons["Lose"]) == 0:
                        WinAmount = math.ceil(NewBet * SlotsMultiplier["Win"])

                        print("• -", Icons["Win"], "You Won", Icons["Win"], "- •")
                        print("• - You Earned", Icons["Money"], str(format(WinAmount, ",")), "•", Icons["Money"], str(format(WinAmount - NewBet, ",")), "Profit - •")
                        ChangePlayerData("Money", WinAmount)
                        ChangePlayerData("Wins", 1)
                    
                    elif SlotOutcome.count(SlotsIcons["Lose"]) >= 1:
                        if PlayerData["InsuranceDuration"] >= 1:
                            LossAmount = math.ceil(NewBet * (1 - PlayerData["Insurance"]))

                            print("• -", Icons["Lose"], "You Lose", Icons["Lose"], "- •")
                            print("• - You Lost", Icons["Money"], str(format(LossAmount, ",")), "- •")

                            ChangePlayerData("Money", math.ceil(NewBet - LossAmount))
                        
                        else:
                            print("• -", Icons["Lose"], "You Lose", Icons["Lose"], "- •")
                            print("• - You Lost", Icons["Money"], str(format(NewBet, ",")), "- •")

                            ChangePlayerData("Money", (NewBet * SlotsMultiplier["Lose"]))

                        ChangePlayerData("Losses", 1)
                    
                    if PlayerData["InsuranceDuration"] >= 1:
                        ChangePlayerData("InsuranceDuration", -1)
                    
                    SaveData()
                    return "GambleSuccess"
                
                else:
                    Clear()
                    print("• - Bet Must Be A Number Between", Icons["Money"], str(format(BetData["Min"], ",")), "And", Icons["Money"], str(format(BetData["Max"], ",")), "- •")
                    return "GambleError"
            
            else:
                Clear()
                print("• - Bet Must Be Below Your Balance - •")
                return "GambleError"
        
        else:
            Clear()
            print("• - Bet Must Be A Number Between", Icons["Money"], str(format(BetData["Min"], ",")), "And", Icons["Money"], str(format(BetData["Max"], ",")), "- •")
            return "GambleError"
    
    elif GambleType == "Previous":
        NewBet = PreviousData["Bet"]
        InputType = "Int"

        if InputType == "Int":
            if NewBet <= PlayerData["Money"]:
                if NewBet >= BetData["Min"] and NewBet <= BetData["Max"]:
                    SlotOutcome = []

                    PreviousData["Method"] = MethodSlots
                    PreviousData["Bet"] = NewBet
                    PreviousData["Attempts"] += 1

                    ChangePlayerData("Money", -(NewBet))
                    ChangePlayerData("Spins", 1)

                    for i in range(3):
                        SlotOutcome.append(random.choice(SlotsIconList))

                    Clear()
                    print("• -", SlotOutcome[0], "|", SlotOutcome[1], "|", SlotOutcome[2], "- •")
                    print()
                    
                    if SlotOutcome.count(SlotsIcons["Jackpot"]) == 3:
                        WinAmount = math.ceil(NewBet * SlotsMultiplier["Jackpot"])

                        print("• -", Icons["Win"], "You Won", Icons["Win"], "- •")
                        print("• - You Earned", Icons["Money"], str(format(WinAmount, ",")), "•", Icons["Money"], str(format(WinAmount - NewBet, ",")), "Profit - •")
                        ChangePlayerData("Money", WinAmount)
                        ChangePlayerData("Wins", 1)

                    elif (SlotOutcome.count(SlotsIcons["Win"]) >= 2 or SlotOutcome.count(SlotsIcons["Jackpot"])) and SlotOutcome.count(SlotsIcons["Lose"]) == 0:
                        WinAmount = math.ceil(NewBet * SlotsMultiplier["Win"])

                        print("• -", Icons["Win"], "You Won", Icons["Win"], "- •")
                        print("• - You Earned", Icons["Money"], str(format(WinAmount, ",")), "•", Icons["Money"], str(format(WinAmount - NewBet, ",")), "Profit - •")
                        ChangePlayerData("Money", WinAmount)
                        ChangePlayerData("Wins", 1)
                    
                    elif SlotOutcome.count(SlotsIcons["Lose"]) >= 1:
                        if PlayerData["InsuranceDuration"] >= 1:
                            LossAmount = math.ceil(NewBet * (1 - PlayerData["Insurance"]))

                            print("• -", Icons["Lose"], "You Lose", Icons["Lose"], "- •")
                            print("• - You Lost", Icons["Money"], str(format(LossAmount, ",")), "- •")

                            ChangePlayerData("Money", math.ceil(NewBet - LossAmount))
                        
                        else:
                            print("• -", Icons["Lose"], "You Lose", Icons["Lose"], "- •")
                            print("• - You Lost", Icons["Money"], str(format(NewBet, ",")), "- •")

                            ChangePlayerData("Money", (NewBet * SlotsMultiplier["Lose"]))

                        ChangePlayerData("Losses", 1)
                    
                    if PlayerData["InsuranceDuration"] >= 1:
                        ChangePlayerData("InsuranceDuration", -1)
                    
                    SaveData()
                    return "GambleSuccess"
                
                else:
                    Clear()
                    print("• - Bet Must Be A Number Between", Icons["Money"], str(format(BetData["Min"], ",")), "And", Icons["Money"], str(format(BetData["Max"], ",")), "- •")
                    return "GambleError"
            
            else:
                Clear()
                print("• - Bet Must Be Below Your Balance - •")
                return "GambleError"
        
        else:
            Clear()
            print("• - Bet Must Be A Number Between", Icons["Money"], str(format(BetData["Min"], ",")), "And", Icons["Money"], str(format(BetData["Max"], ",")), "- •")
            return "GambleError"
        
def MethodCoinflip(GambleType):
    CoinflipIcons = CoinflipData["CoinflipIcons"]
    CoinflipMultipliers = CoinflipData["Multipliers"]
    CoinflipChances = CoinflipData["Chances"]
    if GambleType == "New":
        PrintPlayerData()
        print()

        print("• - Coinflip Selected - •")
        print()

        print("Guess Correct • x" + str(CoinflipMultipliers["Win"]))
        print("Guess Incorrect • x" + str(CoinflipMultipliers["Lose"]))

        print()
        print("• - Input A Number Between", Icons["Money"], str(format(BetData["Min"], ",")), "And", Icons["Money"], str(format(BetData["Max"], ",")), "- •")
        print()
        InputType, NewBet = CheckInput(input("How much would you like to bet: "))

        print()
        print("• - Input 'Heads' Or 'Tails' - •")
        print()
        InputType2, NewSide = CheckInput(input("Choose a side: "))

        if InputType == "Int" and InputType2 == "String" and NewSide.lower() in CoinflipChances:
            if NewBet <= PlayerData["Money"]:
                if NewBet >= BetData["Min"] and NewBet <= BetData["Max"]:
                    SelectedCoinflip = random.choice(CoinflipChances)

                    PreviousData["Method"] = MethodCoinflip
                    PreviousData["Bet"] = NewBet
                    PreviousData["Side"] = NewSide
                    PreviousData["Attempts"] = 0

                    ChangePlayerData("Money", -(NewBet))
                    ChangePlayerData("Spins", 1)

                    Clear()

                    print("• -", "Flipped", CoinflipIcons[SelectedCoinflip], SelectedCoinflip, "- •")
                    print()

                    if SelectedCoinflip == NewSide.lower():
                        WinAmount = math.ceil(NewBet * CoinflipMultipliers["Win"])

                        print("• -", Icons["Win"], "You Won", Icons["Win"], "- •")
                        print("• - You Earned", Icons["Money"], str(format(WinAmount, ",")), "•", Icons["Money"], str(format(WinAmount - NewBet, ",")), "Profit - •")
                        ChangePlayerData("Money", WinAmount)
                        ChangePlayerData("Wins", 1)
                    
                    elif SelectedCoinflip != NewSide.lower():
                        if PlayerData["InsuranceDuration"] >= 1:
                            LossAmount = math.ceil(NewBet * (1 - PlayerData["Insurance"]))

                            print("• -", Icons["Lose"], "You Lose", Icons["Lose"], "- •")
                            print("• - You Lost", Icons["Money"], str(format(LossAmount, ",")), "- •")

                            ChangePlayerData("Money", math.ceil(NewBet - LossAmount))
                        
                        else:
                            print("• -", Icons["Lose"], "You Lose", Icons["Lose"], "- •")
                            print("• - You Lost", Icons["Money"], str(format(NewBet, ",")), "- •")

                            ChangePlayerData("Money", (NewBet * CoinflipMultipliers["Lose"]))

                        ChangePlayerData("Losses", 1)
                    
                    if PlayerData["InsuranceDuration"] >= 1:
                        ChangePlayerData("InsuranceDuration", -1)
                    
                    SaveData()
                    return "GambleSuccess"

                else:
                    Clear()
                    print("• - Bet Must Be A Number Between", Icons["Money"], str(format(BetData["Min"], ",")), "And", Icons["Money"], str(format(BetData["Max"], ",")), "- •")
                    return "GambleError"
            
            else:
                Clear()
                print("• - Bet Must Be Below Your Balance - •")
                return "GambleError"
            
        else:
            Clear()
            print("• - Bet Must Be A Number Between", Icons["Money"], str(format(BetData["Min"], ",")), "And", Icons["Money"], str(format(BetData["Max"], ",")), "- •")
            print("• - Side Must Be 'Heads' Or 'Tails' - •")
            return "GambleError"
        
    elif GambleType == "Previous":
        InputType = "Int"
        InputType2 = "String"
        NewBet = PreviousData["Bet"]
        NewSide = PreviousData["Side"]
        if InputType == "Int" and InputType2 == "String" and NewSide.lower() in CoinflipChances:
            if NewBet <= PlayerData["Money"]:
                if NewBet >= BetData["Min"] and NewBet <= BetData["Max"]:
                    SelectedCoinflip = random.choice(CoinflipChances)

                    PreviousData["Method"] = MethodCoinflip
                    PreviousData["Bet"] = NewBet
                    PreviousData["Side"] = NewSide
                    PreviousData["Attempts"] += 1

                    ChangePlayerData("Money", -(NewBet))
                    ChangePlayerData("Spins", 1)

                    Clear()

                    print("• -", "Flipped", CoinflipIcons[SelectedCoinflip], SelectedCoinflip, "- •")
                    print()

                    if SelectedCoinflip == NewSide.lower():
                        WinAmount = math.ceil(NewBet * CoinflipMultipliers["Win"])

                        print("• -", Icons["Win"], "You Won", Icons["Win"], "- •")
                        print("• - You Earned", Icons["Money"], str(format(WinAmount, ",")), "•", Icons["Money"], str(format(WinAmount - NewBet, ",")), "Profit - •")
                        ChangePlayerData("Money", WinAmount)
                        ChangePlayerData("Wins", 1)
                    
                    elif SelectedCoinflip != NewSide.lower():
                        if PlayerData["InsuranceDuration"] >= 1:
                            LossAmount = math.ceil(NewBet * (1 - PlayerData["Insurance"]))

                            print("• -", Icons["Lose"], "You Lose", Icons["Lose"], "- •")
                            print("• - You Lost", Icons["Money"], str(format(LossAmount, ",")), "- •")

                            ChangePlayerData("Money", math.ceil(NewBet - LossAmount))
                        
                        else:
                            print("• -", Icons["Lose"], "You Lose", Icons["Lose"], "- •")
                            print("• - You Lost", Icons["Money"], str(format(NewBet, ",")), "- •")

                            ChangePlayerData("Money", (NewBet * CoinflipMultipliers["Lose"]))

                        ChangePlayerData("Losses", 1)

                    if PlayerData["InsuranceDuration"] >= 1:
                        ChangePlayerData("InsuranceDuration", -1)
                    
                    SaveData()
                    return "GambleSuccess"

                else:
                    Clear()
                    print("• - Bet Must Be A Number Between", Icons["Money"], str(format(BetData["Min"], ",")), "And", Icons["Money"], str(format(BetData["Max"], ",")), "- •")
                    return "GambleError"
            
            else:
                Clear()
                print("• - Bet Must Be Below Your Balance - •")
                return "GambleError"
            
        else:
            Clear()
            print("• - Bet Must Be A Number Between", Icons["Money"], str(format(BetData["Min"], ",")), "And", Icons["Money"], str(format(BetData["Max"], ",")), "- •")
            print("• - Side Must Be 'Heads' Or 'Tails' - •")
            return "GambleError"

def MethodRPS(GambleType):
    RPSIcons = RPSData["RPSIcons"]
    RPSMultipliers = RPSData["Multipliers"]
    RPSChances = RPSData["RPSList"]

    if GambleType == "New":
        PrintPlayerData()
        print()

        print("• - Rock Paper Scissors Selected - •")
        print()

        print("Win • x" + str(RPSMultipliers["Win"]))
        print("Tie • x" + str(RPSMultipliers["Tie"]))
        print("Lose • x" + str(RPSMultipliers["Lose"]))

        print()
        print("• - Input A Number Between", Icons["Money"], str(format(BetData["Min"], ",")), "And", Icons["Money"], str(format(BetData["Max"], ",")), "- •")
        print()
        InputType, NewBet = CheckInput(input("How much would you like to bet: "))

        print()
        print("• - Input 'Rock' Or 'Paper' Or 'Scissors' - •")
        print()
        InputType2, NewRPS = CheckInput(input("Choose an item: "))

        if InputType == "Int" and InputType2 == "String" and NewRPS.lower() in RPSChances:
            if NewBet <= PlayerData["Money"]:
                if NewBet >= BetData["Min"] and NewBet <= BetData["Max"]:
                    SelectedItem = random.choice(RPSChances)

                    PreviousData["Method"] = MethodRPS
                    PreviousData["Bet"] = NewBet
                    PreviousData["RPS"] = NewRPS
                    PreviousData["Attempts"] = 0

                    ChangePlayerData("Money", -(NewBet))
                    ChangePlayerData("Spins", 1)

                    Clear()

                    print("• -", RPSIcons[NewRPS.lower()], "-", RPSIcons[SelectedItem], "- •")
                    print()

                    if SelectedItem == NewRPS.lower():
                        WinAmount = math.ceil(NewBet * RPSMultipliers["Tie"])

                        print("• - You Tied - •")
                        print("• - You Earned", Icons["Money"], str(format(WinAmount, ",")), "•", Icons["Money"], str(format(WinAmount - NewBet, ",")), "Profit [5% Tie Tax] - •")
                        ChangePlayerData("Money", WinAmount)
                    
                    elif (SelectedItem == "scissors" and NewRPS.lower() == "rock") or (SelectedItem == "rock" and NewRPS.lower() == "paper") or (SelectedItem == "paper" and NewRPS.lower() == "scissors"):
                        WinAmount = math.ceil(NewBet * RPSMultipliers["Win"])

                        print("• -", Icons["Win"], "You Won", Icons["Win"], "- •")
                        print("• - You Earned", Icons["Money"], str(format(WinAmount, ",")), "•", Icons["Money"], str(format(WinAmount - NewBet, ",")), "Profit - •")
                        ChangePlayerData("Money", WinAmount)
                        ChangePlayerData("Wins", 1)
                    
                    elif (SelectedItem == "rock" and NewRPS.lower() == "scissors") or (SelectedItem == "paper" and NewRPS.lower() == "rock") or (SelectedItem == "scissors" and NewRPS.lower() == "paper"):
                        if PlayerData["InsuranceDuration"] >= 1:
                            LossAmount = math.ceil(NewBet * (1 - PlayerData["Insurance"]))

                            print("• -", Icons["Lose"], "You Lose", Icons["Lose"], "- •")
                            print("• - You Lost", Icons["Money"], str(format(LossAmount, ",")), "- •")
                            
                            ChangePlayerData("Money", math.ceil(NewBet - LossAmount))
                        
                        else:
                            print("• -", Icons["Lose"], "You Lose", Icons["Lose"], "- •")
                            print("• - You Lost", Icons["Money"], str(format(NewBet, ",")), "- •")

                            ChangePlayerData("Money", (NewBet * RPSMultipliers["Lose"]))

                        ChangePlayerData("Losses", 1)
                    
                    if PlayerData["InsuranceDuration"] >= 1:
                        ChangePlayerData("InsuranceDuration", -1)
                    
                    SaveData()
                    return "GambleSuccess"

                else:
                    Clear()
                    print("• - Bet Must Be A Number Between", Icons["Money"], str(format(BetData["Min"], ",")), "And", Icons["Money"], str(format(BetData["Max"], ",")), "- •")
                    return "GambleError"

            else:
                Clear()
                print("• - Bet Must Be Below Your Balance - •")
                return "GambleError"

        else:
            Clear()
            print("• - Bet Must Be A Number Between", Icons["Money"], str(format(BetData["Min"], ",")), "And", Icons["Money"], str(format(BetData["Max"], ",")), "- •")
            print("• - Side Must Be 'Rock' Or 'Paper' Or 'Scissors' - •")
            return "GambleError"
        
    elif GambleType == "Previous":
        InputType = "Int"
        InputType2 = "String"
        NewBet = PreviousData["Bet"]
        NewRPS = PreviousData["RPS"]

        if InputType == "Int" and InputType2 == "String" and NewRPS.lower() in RPSChances:
            if NewBet <= PlayerData["Money"]:
                if NewBet >= BetData["Min"] and NewBet <= BetData["Max"]:
                    SelectedItem = random.choice(RPSChances)

                    PreviousData["Method"] = MethodRPS
                    PreviousData["Bet"] = NewBet
                    PreviousData["RPS"] = NewRPS
                    PreviousData["Attempts"] += 1

                    ChangePlayerData("Money", -(NewBet))
                    ChangePlayerData("Spins", 1)

                    Clear()

                    print("• -", RPSIcons[NewRPS.lower()], "-", RPSIcons[SelectedItem], "- •")
                    print()

                    if SelectedItem == NewRPS.lower():
                        WinAmount = math.ceil(NewBet * RPSMultipliers["Tie"])

                        print("• - You Tied - •")
                        print("• - You Earned", Icons["Money"], str(format(WinAmount, ",")), "•", Icons["Money"], str(format(WinAmount - NewBet, ",")), "Profit [5% Tie Tax] - •")
                        ChangePlayerData("Money", WinAmount)
                    
                    elif (SelectedItem == "scissors" and NewRPS.lower() == "rock") or (SelectedItem == "rock" and NewRPS.lower() == "paper") or (SelectedItem == "paper" and NewRPS.lower() == "scissors"):
                        WinAmount = math.ceil(NewBet * RPSMultipliers["Win"])

                        print("• -", Icons["Win"], "You Won", Icons["Win"], "- •")
                        print("• - You Earned", Icons["Money"], str(format(WinAmount, ",")), "•", Icons["Money"], str(format(WinAmount - NewBet, ",")), "Profit - •")
                        ChangePlayerData("Money", WinAmount)
                        ChangePlayerData("Wins", 1)
                    
                    elif (SelectedItem == "rock" and NewRPS.lower() == "scissors") or (SelectedItem == "paper" and NewRPS.lower() == "rock") or (SelectedItem == "scissors" and NewRPS.lower() == "paper"):
                        if PlayerData["InsuranceDuration"] >= 1:
                            LossAmount = math.ceil(NewBet * (1 - PlayerData["Insurance"]))

                            print("• -", Icons["Lose"], "You Lose", Icons["Lose"], "- •")
                            print("• - You Lost", Icons["Money"], str(format(LossAmount, ",")), "- •")

                            ChangePlayerData("Money", math.ceil(NewBet - LossAmount))
                        
                        else:
                            print("• -", Icons["Lose"], "You Lose", Icons["Lose"], "- •")
                            print("• - You Lost", Icons["Money"], str(format(NewBet, ",")), "- •")

                            ChangePlayerData("Money", (NewBet * RPSMultipliers["Lose"]))

                        ChangePlayerData("Losses", 1)

                    if PlayerData["InsuranceDuration"] >= 1:
                        ChangePlayerData("InsuranceDuration", -1)
                    
                    SaveData()
                    return "GambleSuccess"

                else:
                    Clear()
                    print("• - Bet Must Be A Number Between", Icons["Money"], str(format(BetData["Min"], ",")), "And", Icons["Money"], str(format(BetData["Max"], ",")), "- •")
                    return "GambleError"

            else:
                Clear()
                print("• - Bet Must Be Below Your Balance - •")
                return "GambleError"

        else:
            Clear()
            print("• - Bet Must Be A Number Between", Icons["Money"], str(format(BetData["Min"], ",")), "And", Icons["Money"], str(format(BetData["Max"], ",")), "- •")
            print("• - Item Must Be 'Rock' Or 'Paper' Or 'Scissors' - •")
            return "GambleError"
        
def MethodCups(GambleType):
    CupsIcons = CupsData["CupsIcons"]
    CupsMultiplier = CupsData["Multipliers"]

    if GambleType == "New":

        PrintPlayerData()
        print()

        print("• - Cups Selected - •")
        print()

        print("Guess Correct • x" + str(CupsMultiplier["Win"]))
        print("Guess Incorrect • x" + str(CupsMultiplier["Lose"]))

        print()
        print("• - Input A Number Between", Icons["Money"], str(format(BetData["Min"], ",")), "And", Icons["Money"], str(format(BetData["Max"], ",")), "- •")
        print()
        InputType, NewBet = CheckInput(input("How much would you like to bet: "))

        print()
        print("• - Input A Number Between 1 And 3 - •")
        print()
        InputType2, NewCup = CheckInput(input("Choose a cup: "))

        if InputType == "Int" and InputType2 == "Int" and NewCup >= 1 and NewCup <= 3:
            if NewBet <= PlayerData["Money"]:
                if NewBet >= BetData["Min"] and NewBet <= BetData["Max"]:
                    SelectedCup = random.randint(1, 3)
                    CupOutcome = []

                    for i in range(3):
                        if i == 1:
                            if (i + 1) == SelectedCup:
                                CupOutcome.append(CupsIcons["WinItem"] + " ")
                            
                            else:
                                CupOutcome.append(CupsIcons["LoseItem"] + " ")
                        
                        elif i < 3:
                            if (i + 1) == SelectedCup:
                                CupOutcome.append(" " + CupsIcons["WinItem"] + " ")
                            
                            else:
                                CupOutcome.append(CupsIcons["LoseItem"] + " ")
                        
                        elif i == 3:
                            if (i + 1) == SelectedCup:
                                CupOutcome.append(CupsIcons["WinItem"])
                            
                            else:
                                CupOutcome.append(CupsIcons["LoseItem"])

                    PreviousData["Method"] = MethodCups
                    PreviousData["Bet"] = NewBet
                    PreviousData["Cup"] = NewCup
                    PreviousData["Attempts"] = 0

                    ChangePlayerData("Money", -(NewBet))
                    ChangePlayerData("Spins", 1)

                    Clear()

                    print("• -", CupOutcome[0], "•", CupOutcome[1], "•", CupOutcome[2], "- •")
                    print()

                    if NewCup == SelectedCup:
                        WinAmount = math.ceil(NewBet * CupsMultiplier["Win"])

                        print("• -", Icons["Win"], "You Won", Icons["Win"], "- •")
                        print("• - You Earned", Icons["Money"], str(format(WinAmount, ",")), "•", Icons["Money"], str(format(WinAmount - NewBet, ",")), "Profit - •")
                        ChangePlayerData("Money", WinAmount)
                        ChangePlayerData("Wins", 1)
                    
                    elif NewCup != SelectedCup:
                        if PlayerData["InsuranceDuration"] >= 1:
                            LossAmount = math.ceil(NewBet * (1 - PlayerData["Insurance"]))

                            print("• -", Icons["Lose"], "You Lose", Icons["Lose"], "- •")
                            print("• - You Lost", Icons["Money"], str(format(LossAmount, ",")), "- •")

                            ChangePlayerData("Money", math.ceil(NewBet - LossAmount))
                        
                        else:
                            print("• -", Icons["Lose"], "You Lose", Icons["Lose"], "- •")
                            print("• - You Lost", Icons["Money"], str(format(NewBet, ",")), "- •")

                            ChangePlayerData("Money", (NewBet * CupsMultiplier["Lose"]))

                        ChangePlayerData("Losses", 1)
                    
                    if PlayerData["InsuranceDuration"] >= 1:
                        ChangePlayerData("InsuranceDuration", -1)
                    
                    SaveData()
                    return "GambleSuccess"
                
                else:
                    Clear()
                    print("• - Bet Must Be A Number Between", Icons["Money"], str(format(BetData["Min"], ",")), "And", Icons["Money"], str(format(BetData["Max"], ",")), "- •")
                    return "GambleError"
            
            else:
                Clear()
                print("• - Bet Must Be Below Your Balance - •")
                return "GambleError"
        
        else:
            Clear()
            print("• - Bet Must Be A Number Between", Icons["Money"], str(format(BetData["Min"], ",")), "And", Icons["Money"], str(format(BetData["Max"], ",")), "- •")
            print("• - Cup Must Be A Number Between 1 And 3 - •")
            return "GambleError"
    
    elif GambleType == "Previous":
        InputType = "Int"
        InputType2 = "Int"
        NewBet = PreviousData["Bet"]
        NewCup = PreviousData["Cup"]

        if InputType == "Int" and InputType2 == "Int" and NewCup >= 1 and NewCup <= 3:
            if NewBet <= PlayerData["Money"]:
                if NewBet >= BetData["Min"] and NewBet <= BetData["Max"]:
                    SelectedCup = random.randint(1, 3)
                    CupOutcome = []

                    for i in range(3):
                        if i == 1:
                            if (i + 1) == SelectedCup:
                                CupOutcome.append(CupsIcons["WinItem"] + " ")
                            
                            else:
                                CupOutcome.append(CupsIcons["LoseItem"] + " ")
                        
                        elif i < 3:
                            if (i + 1) == SelectedCup:
                                CupOutcome.append(" " + CupsIcons["WinItem"] + " ")
                            
                            else:
                                CupOutcome.append(CupsIcons["LoseItem"] + " ")
                        
                        elif i == 3:
                            if (i + 1) == SelectedCup:
                                CupOutcome.append(CupsIcons["WinItem"])
                            
                            else:
                                CupOutcome.append(CupsIcons["LoseItem"])

                    PreviousData["Method"] = MethodCups
                    PreviousData["Bet"] = NewBet
                    PreviousData["Cup"] = NewCup
                    PreviousData["Attempts"] += 1

                    ChangePlayerData("Money", -(NewBet))
                    ChangePlayerData("Spins", 1)

                    Clear()

                    print("• -", CupOutcome[0], "•", CupOutcome[1], "•", CupOutcome[2], "- •")
                    print()

                    if NewCup == SelectedCup:
                        WinAmount = math.ceil(NewBet * CupsMultiplier["Win"])

                        print("• -", Icons["Win"], "You Won", Icons["Win"], "- •")
                        print("• - You Earned", Icons["Money"], str(format(WinAmount, ",")), "•", Icons["Money"], str(format(WinAmount - NewBet, ",")), "Profit - •")
                        ChangePlayerData("Money", WinAmount)
                        ChangePlayerData("Wins", 1)
                    
                    elif NewCup != SelectedCup:
                        if PlayerData["InsuranceDuration"] >= 1:
                            LossAmount = math.ceil(NewBet * (1 - PlayerData["Insurance"]))

                            print("• -", Icons["Lose"], "You Lose", Icons["Lose"], "- •")
                            print("• - You Lost", Icons["Money"], str(format(LossAmount, ",")), "- •")

                            ChangePlayerData("Money", math.ceil(NewBet - LossAmount))
                        
                        else:
                            print("• -", Icons["Lose"], "You Lose", Icons["Lose"], "- •")
                            print("• - You Lost", Icons["Money"], str(format(NewBet, ",")), "- •")

                            ChangePlayerData("Money", (NewBet * CupsMultiplier["Lose"]))

                        ChangePlayerData("Losses", 1)
                    
                    if PlayerData["InsuranceDuration"] >= 1:
                        ChangePlayerData("InsuranceDuration", -1)
                    
                    SaveData()
                    return "GambleSuccess"
                
                else:
                    Clear()
                    print("• - Bet Must Be A Number Between", Icons["Money"], str(format(BetData["Min"], ",")), "And", Icons["Money"], str(format(BetData["Max"], ",")), "- •")
                    return "GambleError"
            
            else:
                Clear()
                print("• - Bet Must Be Below Your Balance - •")
                return "GambleError"
        
        else:
            Clear()
            print("• - Bet Must Be A Number Between", Icons["Money"], str(format(BetData["Min"], ",")), "And", Icons["Money"], str(format(BetData["Max"], ",")), "- •")
            print("• - Cup Must Be A Number Between 1 And 3 - •")
            return "GambleError"
    
def MethodEgg(GambleMethod):
    EggIcons = EggsData["EggIcons"]
    EggMultipliers = EggsData["Multipliers"]
    EggRanges = EggsData["RangeNumbers"]

    if GambleMethod == "New":
        PrintPlayerData()
        print()

        print("• - Egg Selected - •")
        print()

        print("Guess Sweetspot • x" + str(EggMultipliers["Exact"]))
        print("Guess Within", EggRanges["SmallRange"], "Of Sweetspot • x" + str(EggMultipliers["SmallRange"]))
        print("Guess Within", EggRanges["MainRange"], "Of Sweetspot • x" + str(EggMultipliers["MainRange"]))
        print("Guess Within Range • x" + str(EggMultipliers["BaseRange"]))
        print("Guess Out Of Range • x" + str(EggMultipliers["Lose"]))

        print()
        print("• - Input A Number Between", Icons["Money"], str(format(BetData["Min"], ",")), "And", Icons["Money"], str(format(BetData["Max"], ",")), "- •")
        print()
        InputType, NewBet = CheckInput(input("How much would you like to bet: "))

        print()
        print("• - Input A Number Between 1 And 100 - •")
        print()
        InputType2, NewEgg = CheckInput(input("Choose a number: "))

        if InputType == "Int" and InputType2 == "Int" and NewEgg >= 1 and NewEgg <= 100:
            if NewBet <= PlayerData["Money"]:
                if NewBet >= BetData["Min"] and NewBet <= BetData["Max"]:
                    EggSweetspot = random.randint(1, 100)
                    EggMin = (EggSweetspot - random.randint(5, 15))
                    EggMax = (EggSweetspot + random.randint(5, 15))

                    if EggMin <= 0:
                        EggMin = 1
                    
                    if EggMax >= 100:
                        EggMax = 100
                    
                    PreviousData["Method"] = MethodEgg
                    PreviousData["Bet"] = NewBet
                    PreviousData["Egg"] = NewEgg
                    PreviousData["Attempts"] = 0

                    ChangePlayerData("Money", -(NewBet))
                    ChangePlayerData("Spins", 1)

                    Clear()

                    if NewEgg < EggMin or NewEgg > EggMax:
                        print("• -", EggIcons["Bust"], "The Egg Cracked", EggIcons["Bust"], "- •")
                        print("• - Range Was", str(EggMin), "Through", str(EggMax), "With A Sweetspot Of", str(EggSweetspot), "- •")
                        print()
                    
                    elif NewEgg >= EggMin and NewEgg <= EggMax:
                        print("• -", EggIcons["Safe"], "The Egg Is Safe", EggIcons["Safe"], "- •")
                        print("• - Range Was", str(EggMin), "Through", str(EggMax), "With A Sweetspot Of", str(EggSweetspot), "- •")
                        print()
                    
                    if NewEgg >= EggMin and NewEgg <= EggMax:
                        if NewEgg == EggSweetspot:
                            WinAmount = math.ceil(NewBet * EggMultipliers["Exact"])

                            print("• -", Icons["Win"], "You Won", Icons["Win"], "- •")
                            print("• - You Guessed The Sweetspot - •")
                            print("• - You Earned", Icons["Money"], str(format(WinAmount, ",")), "•", Icons["Money"], str(format(WinAmount - NewBet, ",")), "Profit - •")
                            ChangePlayerData("Money", WinAmount)
                            ChangePlayerData("Wins", 1)
                        
                        elif NewEgg >= (EggSweetspot - EggRanges["SmallRange"]) and NewEgg <= (EggSweetspot + EggRanges["SmallRange"]):
                            WinAmount = math.ceil(NewBet * EggMultipliers["SmallRange"])

                            print("• -", Icons["Win"], "You Won", Icons["Win"], "- •")
                            print("• - You Guessed Within", str(EggRanges["SmallRange"]), "Of The Sweetspot - •")
                            print("• - You Earned", Icons["Money"], str(format(WinAmount, ",")), "•", Icons["Money"], str(format(WinAmount - NewBet, ",")), "Profit - •")
                            ChangePlayerData("Money", WinAmount)
                            ChangePlayerData("Wins", 1)
                        
                        elif NewEgg >= (EggSweetspot - EggRanges["MainRange"]) and NewEgg <= (EggSweetspot + EggRanges["MainRange"]):
                            WinAmount = math.ceil(NewBet * EggMultipliers["MainRange"])

                            print("• -", Icons["Win"], "You Won", Icons["Win"], "- •")
                            print("• - You Guessed Within", str(EggRanges["MainRange"]), "Of The Sweetspot - •")
                            print("• - You Earned", Icons["Money"], str(format(WinAmount, ",")), "•", Icons["Money"], str(format(WinAmount - NewBet, ",")), "Profit - •")
                            ChangePlayerData("Money", WinAmount)
                            ChangePlayerData("Wins", 1)
                        
                        elif NewEgg >= EggMin and NewEgg <= EggMax:
                            WinAmount = math.ceil(NewBet * EggMultipliers["BaseRange"])

                            print("• -", Icons["Win"], "You Won", Icons["Win"], "- •")
                            print("• - You Guessed Within Range - •")
                            print("• - You Earned", Icons["Money"], str(format(WinAmount, ",")), "•", Icons["Money"], str(format(WinAmount - NewBet, ",")), "Profit - •")
                            ChangePlayerData("Money", WinAmount)
                            ChangePlayerData("Wins", 1)
                    
                    elif NewEgg < EggMin or NewEgg > EggMax:
                        if PlayerData["InsuranceDuration"] >= 1:
                            LossAmount = math.ceil(NewBet * (1 - PlayerData["Insurance"]))

                            print("• -", Icons["Lose"], "You Lose", Icons["Lose"], "- •")
                            print("• - You Guessed Out Of Range - •")
                            print("• - You Lost", Icons["Money"], str(format(LossAmount, ",")), "- •")

                            ChangePlayerData("Money", math.ceil(NewBet - LossAmount))
                        
                        else:
                            print("• -", Icons["Lose"], "You Lose", Icons["Lose"], "- •")
                            print("• - You Guessed Out Of Range - •")
                            print("• - You Lost", Icons["Money"], str(format(NewBet, ",")), "- •")

                            ChangePlayerData("Money", (NewBet * EggMultipliers["Lose"]))

                        ChangePlayerData("Losses", 1)
                    
                    if PlayerData["InsuranceDuration"] >= 1:
                        ChangePlayerData("InsuranceDuration", -1)
                    
                    SaveData()
                    return "GambleSuccess"
                
                else:
                    Clear()
                    print("• - Bet Must Be A Number Between", Icons["Money"], str(format(BetData["Min"], ",")), "And", Icons["Money"], str(format(BetData["Max"], ",")), "- •")
                    return "GambleError"
            
            else:
                Clear()
                print("• - Bet Must Be Below Your Balance - •")
                return "GambleError"
        
        else:
            Clear()
            print("• - Bet Must Be A Number Between", Icons["Money"], str(format(BetData["Min"], ",")), "And", Icons["Money"], str(format(BetData["Max"], ",")), "- •")
            print("• - Guess Must Be A Number Between 1 And 100 - •")
            return "GambleError"
    
    elif GambleMethod == "Previous":
        InputType = "Int"
        InputType2 = "Int"
        NewBet = PreviousData["Bet"]
        NewEgg = PreviousData["Egg"]

        if InputType == "Int" and InputType2 == "Int" and NewEgg >= 1 and NewEgg <= 100:
            if NewBet <= PlayerData["Money"]:
                if NewBet >= BetData["Min"] and NewBet <= BetData["Max"]:
                    EggSweetspot = random.randint(1, 100)
                    EggMin = (EggSweetspot - random.randint(5, 15))
                    EggMax = (EggSweetspot + random.randint(5, 15))

                    if EggMin <= 0:
                        EggMin = 1
                    
                    if EggMax >= 100:
                        EggMax = 100
                    
                    PreviousData["Method"] = MethodEgg
                    PreviousData["Bet"] = NewBet
                    PreviousData["Egg"] = NewEgg
                    PreviousData["Attempts"] += 1

                    ChangePlayerData("Money", -(NewBet))
                    ChangePlayerData("Spins", 1)

                    Clear()

                    if NewEgg < EggMin or NewEgg > EggMax:
                        print("• -", EggIcons["Bust"], "The Egg Cracked", EggIcons["Bust"], "- •")
                        print("• - Range Was", str(EggMin), "Through", str(EggMax), "With A Sweetspot Of", str(EggSweetspot), "- •")
                        print()
                    
                    elif NewEgg >= EggMin and NewEgg <= EggMax:
                        print("• -", EggIcons["Safe"], "The Egg Is Safe", EggIcons["Safe"], "- •")
                        print("• - Range Was", str(EggMin), "Through", str(EggMax), "With A Sweetspot Of", str(EggSweetspot), "- •")
                        print()
                    
                    if NewEgg >= EggMin and NewEgg <= EggMax:
                        if NewEgg == EggSweetspot:
                            WinAmount = math.ceil(NewBet * EggMultipliers["Exact"])

                            print("• -", Icons["Win"], "You Won", Icons["Win"], "- •")
                            print("• - You Guessed The Sweetspot - •")
                            print("• - You Earned", Icons["Money"], str(format(WinAmount, ",")), "•", Icons["Money"], str(format(WinAmount - NewBet, ",")), "Profit - •")
                            ChangePlayerData("Money", WinAmount)
                            ChangePlayerData("Wins", 1)
                        
                        elif NewEgg >= (EggSweetspot - EggRanges["SmallRange"]) and NewEgg <= (EggSweetspot + EggRanges["SmallRange"]):
                            WinAmount = math.ceil(NewBet * EggMultipliers["SmallRange"])

                            print("• -", Icons["Win"], "You Won", Icons["Win"], "- •")
                            print("• - You Guessed Within", str(EggRanges["SmallRange"]), "Of The Sweetspot - •")
                            print("• - You Earned", Icons["Money"], str(format(WinAmount, ",")), "•", Icons["Money"], str(format(WinAmount - NewBet, ",")), "Profit - •")
                            ChangePlayerData("Money", WinAmount)
                            ChangePlayerData("Wins", 1)
                        
                        elif NewEgg >= (EggSweetspot - EggRanges["MainRange"]) and NewEgg <= (EggSweetspot + EggRanges["MainRange"]):
                            WinAmount = math.ceil(NewBet * EggMultipliers["MainRange"])

                            print("• -", Icons["Win"], "You Won", Icons["Win"], "- •")
                            print("• - You Guessed Within", str(EggRanges["MainRange"]), "Of The Sweetspot - •")
                            print("• - You Earned", Icons["Money"], str(format(WinAmount, ",")), "•", Icons["Money"], str(format(WinAmount - NewBet, ",")), "Profit - •")
                            ChangePlayerData("Money", WinAmount)
                            ChangePlayerData("Wins", 1)
                        
                        elif NewEgg >= EggMin and NewEgg <= EggMax:
                            WinAmount = math.ceil(NewBet * EggMultipliers["BaseRange"])

                            print("• -", Icons["Win"], "You Won", Icons["Win"], "- •")
                            print("• - You Guessed Within Range - •")
                            print("• - You Earned", Icons["Money"], str(format(WinAmount, ",")), "•", Icons["Money"], str(format(WinAmount - NewBet, ",")), "Profit - •")
                            ChangePlayerData("Money", WinAmount)
                            ChangePlayerData("Wins", 1)
                    
                    elif NewEgg < EggMin or NewEgg > EggMax:
                        if PlayerData["InsuranceDuration"] >= 1:
                            LossAmount = math.ceil(NewBet * (1 - PlayerData["Insurance"]))

                            print("• -", Icons["Lose"], "You Lose", Icons["Lose"], "- •")
                            print("• - You Guessed Out Of Range - •")
                            print("• - You Lost", Icons["Money"], str(format(LossAmount, ",")), "- •")

                            ChangePlayerData("Money", math.ceil(NewBet - LossAmount))
                        
                        else:
                            print("• -", Icons["Lose"], "You Lose", Icons["Lose"], "- •")
                            print("• - You Guessed Out Of Range - •")
                            print("• - You Lost", Icons["Money"], str(format(NewBet, ",")), "- •")

                            ChangePlayerData("Money", (NewBet * EggMultipliers["Lose"]))

                        ChangePlayerData("Losses", 1)
                    
                    if PlayerData["InsuranceDuration"] >= 1:
                        ChangePlayerData("InsuranceDuration", -1)
                    
                    SaveData()
                    return "GambleSuccess"
                
                else:
                    Clear()
                    print("• - Bet Must Be A Number Between", Icons["Money"], str(format(BetData["Min"], ",")), "And", Icons["Money"], str(format(BetData["Max"], ",")), "- •")
                    return "GambleError"
            
            else:
                Clear()
                print("• - Bet Must Be Below Your Balance - •")
                return "GambleError"
        
        else:
            Clear()
            print("• - Bet Must Be A Number Between", Icons["Money"], str(format(BetData["Min"], ",")), "And", Icons["Money"], str(format(BetData["Max"], ",")), "- •")
            print("• - Guess Must Be A Number Between 1 And 100 - •")
            return "GambleError"

def MethodCrates(GambleType):
    if GambleType == "New":
        PrintPlayerData()
        print()

        print("• - Crates Selected - •")
        print()

        for i in range(len(CratesData)):
            CrateInfo = CratesData[i + 1]
            print(str(i + 1), "• -", CrateInfo["CrateName"], Icons["Money"], str(format(CrateInfo["Cost"], ",")), "- •")

        print()
        print("• - Input A Number Between 1 And", str(len(CratesData)), "- •")
        print()

        InputType, NewCrate = CheckInput(input("What crate would you like to view: "))

        if InputType == "Int" and NewCrate >= 1 and NewCrate <= len(CratesData):

            Clear()
            PrintCrateData(NewCrate)
            print()

            print("1 - Buy Crate")
            print("2 - Go Back")

            print()
            print("• - Input '1' Or '2' - •")
            print()

            InputType2, NewChoice = CheckInput(input("Would you like to buy this crate: "))

            if InputType2 == "Int" and NewChoice == 1 or NewChoice == 2:
                if NewChoice == 1:
                    NewCrateData = CratesData[NewCrate]
                    NewCrateChances = NewCrateData["PrintedChances"]
                    NewCrateItems = NewCrateData["Items"]

                    CratePrice = NewCrateData["Cost"]

                    if CratePrice <= PlayerData["Money"]:
                        PreviousData["Method"] = MethodCrates
                        PreviousData["Crate"] = NewCrate
                        PreviousData["Attempts"] = 0
                        
                        ChangePlayerData("Money", -(CratePrice))
                        ChangePlayerData("Spins", 1)

                        Clear()

                        RandomCrateItem = random.choice(NewCrateChances)
                        WinningAmount = 0

                        for i in range(len(NewCrateItems)):
                            RolledCrateData = NewCrateItems[i + 1]

                            if RolledCrateData["Name"] == RandomCrateItem:
                                WinningAmount = RolledCrateData["Value"]

                        print("• - You Opened A •", NewCrateData["CrateName"], "- •")
                        print("• - You Got", RandomCrateItem, "- •")
                        print()
                            
                        if (WinningAmount - CratePrice) <= -1:
                            print("• - Your Item Is Worth", Icons["Money"], str(format(WinningAmount, ",")), "• -" + Icons["Money"], str(format((CratePrice - WinningAmount), ",")), "Profit - •")
                        
                        elif (WinningAmount - CratePrice) >= 0:
                            print("• - Your Item Is Worth", Icons["Money"], str(format(WinningAmount, ",")), "•", Icons["Money"], str(format((WinningAmount - CratePrice), ",")), "Profit - •")
                        
                        if PlayerData["InsuranceDuration"] >= 1:
                            ChangePlayerData("InsuranceDuration", -1)

                        ChangePlayerData("Money", WinningAmount)
                        return "GambleSuccess"
                    
                    else:
                        Clear()
                        print("• - You Don't Have Enough Money - •")
                        return "GambleError"
                    
                elif NewChoice == 2:
                    return MethodCrates("New")
            
            else:
                Clear()
                print("• - Input Must Be '1' Or '2' - •")
                return "GambleError" 
        
        else:
            Clear()
            print("• - Crate Must Be A Number Between 1 And", str(len(CratesData)), "- •")
            return "GambleError"
    
    elif GambleType == "Previous":
        InputType = "Int"
        NewCrate = PreviousData["Crate"]

        if InputType == "Int" and NewCrate >= 1 and NewCrate <= len(CratesData):
            NewCrateData = CratesData[NewCrate]
            NewCrateChances = NewCrateData["PrintedChances"]
            NewCrateItems = NewCrateData["Items"]

            CratePrice = NewCrateData["Cost"]

            if CratePrice <= PlayerData["Money"]:
                PreviousData["Method"] = MethodCrates
                PreviousData["Crate"] = NewCrate
                PreviousData["Attempts"] += 1
                
                ChangePlayerData("Money", -(CratePrice))
                ChangePlayerData("Spins", 1)

                Clear()

                RandomCrateItem = random.choice(NewCrateChances)
                WinningAmount = 0

                for i in range(len(NewCrateItems)):
                    RolledCrateData = NewCrateItems[i + 1]

                    if RolledCrateData["Name"] == RandomCrateItem:
                        WinningAmount = RolledCrateData["Value"]

                print("• - You Opened", NewCrateData["CrateName"], "- •")
                print("• - You Got", RandomCrateItem, "- •")
                print()
                    
                if (WinningAmount - CratePrice) <= -1:
                    print("• - Your Item Is Worth", Icons["Money"], str(format(WinningAmount, ",")), "• -" + Icons["Money"], str(CratePrice - WinningAmount), "Profit - •")
                
                elif (WinningAmount - CratePrice) >= 0:
                    print("• - Your Item Is Worth", Icons["Money"], str(format(WinningAmount, ",")), "•", Icons["Money"], str(WinningAmount - CratePrice), "Profit - •")
                
                if PlayerData["InsuranceDuration"] >= 1:
                    ChangePlayerData("InsuranceDuration", -1)

                ChangePlayerData("Money", WinningAmount)
                return "GambleSuccess"
            
            else:
                Clear()
                print("• - You Don't Have Enough Money - •")
                return "GambleError" 
        
        else:
            Clear()
            print("• - Bet Must Be A Number Between", Icons["Money"], str(format(BetData["Min"], ",")), "And", Icons["Money"], str(format(BetData["Max"], ",")), "- •")
            print("• - Crate Must Be A Number Between 1 And", str(len(CratesData)), "- •")
            return "GambleError"
    
def MethodBJ(GambleType):
    BJIcons = BJData["BJIcons"]
    BJCardRange = BJData["CardRange"]
    BJMultipliers = BJData["Multipliers"]

    if GambleType == "New":
        PreviousData["Method"] = MethodBJ
        PrintPlayerData()
        print()

        print("• - Blackjack Selected - •")
        print()

        print("Blackjack • x" + str(BJMultipliers["BJ"]))
        print("Win • x" + str(BJMultipliers["Win"]))
        print("Tie • x" + str(BJMultipliers["Tie"]))
        print("Lose • x" + str(BJMultipliers["Lose"]))

        BotCards = random.randint(BJCardRange["Min"], BJCardRange["Max"])
        PlayerCards = random.randint(BJCardRange["Min"], BJCardRange["Max"])

        GameRunning = True
        GameOver = False

        def PrintRoundData():
            print("• - Your Cards Add Up To", PlayerCards, "- •")
            print("• - Bots Cards Add Up To", BotCards, "- •")
        
        print()
        print("• - Input A Number Between", Icons["Money"], str(format(BetData["Min"], ",")), "And", Icons["Money"], str(format(BetData["Max"], ",")), "- •")
        print()
        InputType, NewBet = CheckInput(input("How much would you like to bet: "))

        if InputType == "Int":
            if NewBet <= PlayerData["Money"]:
                if NewBet >= BetData["Min"] and NewBet <= BetData["Max"]:
                    ChangePlayerData("Money", -(NewBet))
                    ChangePlayerData("Spins", 1)

                    while GameRunning:
                        Clear()
                        PrintRoundData()

                        print()
                        print("1 • - Hit - •")
                        print("2 • - Stand - •")

                        print()
                        print("• - Input '1' Or '2' - •")
                        print()

                        InputType2, NewAction = CheckInput(input("What action would you like: "))

                        if InputType2 == "Int" and NewAction == 1 or NewAction == 2:
                            if NewAction == 1:
                                NewPlayerAmount = random.randint(BJCardRange["Min"], BJCardRange["Max"])
                                NewBotAmount = random.randint(BJCardRange["Min"], BJCardRange["Max"])

                                Clear()

                                print("• - You Got •", str(NewPlayerAmount), "- •")

                                if BotCards < 17 and PlayerCards <= 21:
                                    print("• - The Bot Got •", str(NewBotAmount), "- •")
                                    BotCards += NewBotAmount
                                PlayerCards += NewPlayerAmount

                                print()
                                input("Press Enter To Continue: ")

                                Clear()
                                PrintRoundData()
                                print()

                                if PlayerCards < 21 and BotCards < 21:
                                    pass

                                elif PlayerCards == 21 and BotCards != 21:
                                    WinAmount = math.ceil(NewBet * BJMultipliers["BJ"])

                                    print("• -", Icons["Win"], "You Won", Icons["Win"], "- •")
                                    print("• -", BJIcons["BJ"], "You Got A Blackjack", BJIcons["BJ"], "- •")
                                    print("• - You Earned", Icons["Money"], str(format(WinAmount, ",")), "•", Icons["Money"], str(format(WinAmount - NewBet, ",")), "Profit - •")
                                    ChangePlayerData("Money", WinAmount)
                                    ChangePlayerData("Wins", 1)
                                    if PlayerData["InsuranceDuration"] >= 1:
                                        ChangePlayerData("InsuranceDuration", -1)

                                    GameRunning = False
                                    return "GambleSuccess"

                                elif BotCards > 21 and PlayerCards < 21:
                                    WinAmount = math.ceil(NewBet * BJMultipliers["Win"])

                                    print("• -", Icons["Win"], "You Won", Icons["Win"], "- •")
                                    print("• -", BJIcons["Win"], "The Bot Busted", BJIcons["Win"], "- •")
                                    print("• - You Earned", Icons["Money"], str(format(WinAmount, ",")), "•", Icons["Money"], str(format(WinAmount - NewBet, ",")), "Profit - •")
                                    ChangePlayerData("Money", WinAmount)
                                    ChangePlayerData("Wins", 1)
                                    if PlayerData["InsuranceDuration"] >= 1:
                                        ChangePlayerData("InsuranceDuration", -1)

                                    GameRunning = False
                                    return "GambleSuccess"
                                
                                elif PlayerCards >= 17 and PlayerCards == BotCards:
                                    WinAmount = math.ceil(NewBet * BJMultipliers["Tie"])

                                    print("• - You Tied - •")
                                    print("• - You Earned", Icons["Money"], str(format(WinAmount, ",")), "•", Icons["Money"], str(format(WinAmount - NewBet, ",")), "Profit [5% Tie Tax] - •")
                                    ChangePlayerData("Money", WinAmount)  
                                    if PlayerData["InsuranceDuration"] >= 1:
                                        ChangePlayerData("InsuranceDuration", -1)

                                    GameRunning = False
                                    return "GambleSuccess"  
                                
                                elif PlayerCards > 21:
                                    if PlayerData["InsuranceDuration"] >= 1:
                                        LossAmount = math.ceil(NewBet * (1 - PlayerData["Insurance"]))

                                        print("• -", Icons["Lose"], "You Lose", Icons["Lose"], "- •")
                                        print("• -", BJIcons["Bust"], "You Busted", BJIcons["Bust"], "- •")
                                        print("• - You Lost", Icons["Money"], str(format(LossAmount, ",")), "- •")

                                        ChangePlayerData("Money", math.ceil(NewBet - LossAmount))
                                    
                                    else:
                                        print("• -", Icons["Lose"], "You Lose", Icons["Lose"], "- •")
                                        print("• -", BJIcons["Bust"], "You Busted", BJIcons["Bust"], "- •")
                                        print("• - You Lost", Icons["Money"], str(format(NewBet, ",")), "- •")

                                        ChangePlayerData("Money", (NewBet * BJMultipliers["Lose"]))

                                    ChangePlayerData("Losses", 1)
                                    if PlayerData["InsuranceDuration"] >= 1:
                                        ChangePlayerData("InsuranceDuration", -1)

                                    GameRunning = False
                                    return "GambleSuccess"

                                if GameOver == True:
                                    print("lol")
                            
                            elif NewAction == 2:
                                while BotCards < 17 and PlayerCards <= 21:
                                    BotCards += random.randint(BJCardRange["Min"], BJCardRange["Max"])
                                
                                Clear()
                                PrintRoundData()
                                print()

                                if PlayerCards == 21 and BotCards != 21:
                                    WinAmount = math.ceil(NewBet * BJMultipliers["BJ"])

                                    print("• -", Icons["Win"], "You Won", Icons["Win"], "- •")
                                    print("• -", BJIcons["BJ"], "You Got A Blackjack", BJIcons["BJ"], "- •")
                                    print("• - You Earned", Icons["Money"], str(format(WinAmount, ",")), "•", Icons["Money"], str(format(WinAmount - NewBet, ",")), "Profit - •")
                                    ChangePlayerData("Money", WinAmount)
                                    ChangePlayerData("Wins", 1)
                                    if PlayerData["InsuranceDuration"] >= 1:
                                        ChangePlayerData("InsuranceDuration", -1)

                                    GameRunning = False
                                    return "GambleSuccess"

                                elif BotCards > 21 and PlayerCards < 21:
                                    WinAmount = math.ceil(NewBet * BJMultipliers["Win"])

                                    print("• -", Icons["Win"], "You Won", Icons["Win"], "- •")
                                    print("• -", BJIcons["Win"], "The Bot Busted", BJIcons["Win"], "- •")
                                    print("• - You Earned", Icons["Money"], str(format(WinAmount, ",")), "•", Icons["Money"], str(format(WinAmount - NewBet, ",")), "Profit - •")
                                    ChangePlayerData("Money", WinAmount)
                                    ChangePlayerData("Wins", 1)
                                    if PlayerData["InsuranceDuration"] >= 1:
                                        ChangePlayerData("InsuranceDuration", -1)

                                    GameRunning = False
                                    return "GambleSuccess"
                                
                                elif BotCards < PlayerCards:
                                    WinAmount = math.ceil(NewBet * BJMultipliers["Win"])

                                    print("• -", Icons["Win"], "You Won", Icons["Win"], "- •")
                                    print("• -", BJIcons["Win"], "You Were Higher Than The Bot", BJIcons["Win"], "- •")
                                    print("• - You Earned", Icons["Money"], str(format(WinAmount, ",")), "•", Icons["Money"], str(format(WinAmount - NewBet, ",")), "Profit - •")
                                    ChangePlayerData("Money", WinAmount)
                                    ChangePlayerData("Wins", 1)
                                    if PlayerData["InsuranceDuration"] >= 1:
                                        ChangePlayerData("InsuranceDuration", -1)

                                    GameRunning = False
                                    return "GambleSuccess"
                                
                                elif PlayerCards >= 17 and PlayerCards == BotCards:
                                    WinAmount = math.ceil(NewBet * BJMultipliers["Tie"])

                                    print("• - You Tied - •")
                                    print("• - You Earned", Icons["Money"], str(format(WinAmount, ",")), "•", Icons["Money"], str(format(WinAmount - NewBet, ",")), "Profit [5% Tie Tax] - •")
                                    ChangePlayerData("Money", WinAmount)
                                    if PlayerData["InsuranceDuration"] >= 1:
                                        ChangePlayerData("InsuranceDuration", -1)

                                    GameRunning = False
                                    return "GambleSuccess"  

                                elif PlayerCards < BotCards:
                                    if PlayerData["InsuranceDuration"] >= 1:
                                        LossAmount = math.ceil(NewBet * (1 - PlayerData["Insurance"]))

                                        print("• -", Icons["Lose"], "You Lose", Icons["Lose"], "- •")
                                        print("• -", BJIcons["Bust"], "The Bot Was Higher Than You", BJIcons["Bust"], "- •")
                                        print("• - You Lost", Icons["Money"], str(format(LossAmount, ",")), "- •")

                                        ChangePlayerData("Money", math.ceil(NewBet - LossAmount))
                                    
                                    else:
                                        print("• -", Icons["Lose"], "You Lose", Icons["Lose"], "- •")
                                        print("• -", BJIcons["Bust"], "The Bot Was Higher Than You", BJIcons["Bust"], "- •")
                                        print("• - You Lost", Icons["Money"], str(format(NewBet, ",")), "- •")

                                        ChangePlayerData("Money", (NewBet * BJMultipliers["Lose"]))

                                    ChangePlayerData("Losses", 1)
                                    if PlayerData["InsuranceDuration"] >= 1:
                                        ChangePlayerData("InsuranceDuration", -1)

                                    GameRunning = False
                                    return "GambleSuccess"
                                
                                elif PlayerCards > 21:
                                    if PlayerData["InsuranceDuration"] >= 1:
                                        LossAmount = math.ceil(NewBet * (1 - PlayerData["Insurance"]))

                                        print("• -", Icons["Lose"], "You Lose", Icons["Lose"], "- •")
                                        print("• -", BJIcons["Bust"], "You Busted", BJIcons["Bust"], "- •")
                                        print("• - You Lost", Icons["Money"], str(format(LossAmount, ",")), "- •")

                                        ChangePlayerData("Money", math.ceil(NewBet - LossAmount))
                                    
                                    else:
                                        print("• -", Icons["Lose"], "You Lose", Icons["Lose"], "- •")
                                        print("• -", BJIcons["Bust"], "You Busted", BJIcons["Bust"], "- •")
                                        print("• - You Lost", Icons["Money"], str(format(NewBet, ",")), "- •")

                                        ChangePlayerData("Money", (NewBet * BJMultipliers["Lose"]))

                                    ChangePlayerData("Losses", 1)
                                    if PlayerData["InsuranceDuration"] >= 1:
                                        ChangePlayerData("InsuranceDuration", -1)

                                    GameRunning = False
                                    return "GambleSuccess"
                        
                        else:
                            Clear()
                            print("• - Input Must Be '1' Or '2' - •")

                            print()
                            input("Press Enter To Continue: ")

                else:
                    Clear()
                    print("• - Bet Must Be A Number Between", Icons["Money"], str(format(BetData["Min"], ",")), "And", Icons["Money"], str(format(BetData["Max"], ",")), "- •")
                    return "GambleError"
            
            else:
                Clear()
                print("• - Bet Must Be Below Your Balance - •")
                return "GambleError"
        
        else:
            Clear()
            print("• - Bet Must Be A Number Between", Icons["Money"], str(format(BetData["Min"], ",")), "And", Icons["Money"], str(format(BetData["Max"], ",")), "- •")
            return "GambleError"
    
    elif GambleType == "Previous":
        return MethodBJ("New")

def MethodAllIn(GambleType):
    AllInChances = AllInData["Chances"]
    AllInMultipliers = AllInData["Multipliers"]
            
    if GambleType == "New":
        if PlayerData["Money"] > BetData["Min"]:
            PreviousData["Attempts"] = 0
            PrintPlayerData()
            print()

            print("• - All In Selected - •")
            print()

            print("• - Big Win • x" + str(AllInMultipliers["Big Win"]), "- •")
            print("• - Win • x" + str(AllInMultipliers["Win"]), "- •")
            print("• - Lose • x" + str(AllInMultipliers["Lose"]), "• [50% Chance Insurance Fails]- •")

            print()
            print("Yes - Continue")
            print("No - Quit")

            print()
            print("• - Input 'Yes' Or 'No' - •")
            print()

            InputType, NewChoice = CheckInput(input("Would you like bet all " + Icons["Money"] + " " + str(format(PlayerData["Money"], ","))+ " : "))

            if InputType == "String" and (NewChoice.lower() == "yes" or NewChoice.lower() == "no"):
                if NewChoice.lower() == "yes":
                    NewBet = PlayerData["Money"]
                    RolledNumber = random.randint(1, AllInChances["Big Win"])

                    Clear()
                    ChangePlayerData("Money", -(NewBet))

                    if RolledNumber == AllInChances["Big Win"]:
                        WinAmount = math.ceil(NewBet * AllInMultipliers["Big Win"])

                        print("• -", Icons["Win"], "You Won", Icons["Win"], "- •")
                        print("• - BIG WIN - •")
                        print("• - You Earned", Icons["Money"], str(format(WinAmount, ",")), "•", Icons["Money"], str(format(WinAmount - NewBet, ",")), "Profit - •")
                        ChangePlayerData("Money", WinAmount)
                        ChangePlayerData("Wins", 1)
                        if PlayerData["InsuranceDuration"] >= 1:
                            ChangePlayerData("InsuranceDuration", -1)
                        
                        return "GambleSuccess"
                    
                    elif RolledNumber >= AllInChances["Win"]:
                        WinAmount = math.ceil(NewBet * AllInMultipliers["Win"])

                        print("• -", Icons["Win"], "You Won", Icons["Win"], "- •")
                        print("• - You Earned", Icons["Money"], str(format(WinAmount, ",")), "•", Icons["Money"], str(format(WinAmount - NewBet, ",")), "Profit - •")
                        ChangePlayerData("Money", WinAmount)
                        ChangePlayerData("Wins", 1)
                        if PlayerData["InsuranceDuration"] >= 1:
                            ChangePlayerData("InsuranceDuration", -1)
                        
                        return "GambleSuccess"
                    
                    elif RolledNumber <= AllInChances["Lose"]:
                        InsuranceChance = random.choice(AllInChances["Insurance"])

                        if PlayerData["InsuranceDuration"] >= 1:
                            LossAmount = math.ceil(NewBet * (1 - PlayerData["Insurance"]))

                            if InsuranceChance == "Successful":
                                print("• -", Icons["Lose"], "You Lose", Icons["Lose"], "- •")
                                print("• - Insurance Was Successful - •")
                                print("• - You Lost", Icons["Money"], str(format(LossAmount, ",")), "- •")

                                ChangePlayerData("Money", math.ceil(NewBet - LossAmount))
                            
                            elif InsuranceChance == "Unsuccessful":
                                print("• -", Icons["Lose"], "You Lose", Icons["Lose"], "- •")
                                print("• - Insurance Was Unsuccessful - •")
                                print("• - You Lost", Icons["Money"], str(format(NewBet, ",")), "- •")
                                        
                        else:
                            print("• -", Icons["Lose"], "You Lose", Icons["Lose"], "- •")
                            print("• - You Lost", Icons["Money"], str(format(NewBet, ",")), "- •")

                            ChangePlayerData("Money", (NewBet * AllInMultipliers["Lose"]))

                        ChangePlayerData("Losses", 1)
                        if PlayerData["InsuranceDuration"] >= 1:
                            ChangePlayerData("InsuranceDuration", -1)
                
                elif NewChoice.lower() == "no":
                    return "GambleSuccess"
            
            else:
                Clear()
                print("• - Input Must Be 'Yes' Or 'No' - •")
                return "GambleError"
        
        elif PlayerData["Money"] < BetData["Min"]:
            Clear()
            print("• - You Must Have At Least", Icons["Money"], str(format(BetData["Min"], ",")), "To Go All In- •")
            return "GambleError"

def BuyInsurance():
    DiscountAmount = InsuranceShopData["Discounts"]
    InsuranceDiscount = DiscountAmount["Percent"]
    DurationDiscount = DiscountAmount["Duration"]

    InsuranceDiscountDisplay = InsuranceDiscount["Discount"] * 10000 / 100
    InsuranceDiscountDisplay = str(InsuranceDiscountDisplay)

    InsurancePercentageDecimal = InsuranceDiscountDisplay.find(".")
    InsuranceDiscountDisplay = InsuranceDiscountDisplay[:(InsurancePercentageDecimal + 2)]

    DurationDiscountDisplay = DurationDiscount["Discount"] * 10000 / 100
    DurationDiscountDisplay = str(InsuranceDiscountDisplay)

    DurationPercentageDecimal = DurationDiscountDisplay.find(".")
    DurationDiscountDisplay = DurationDiscountDisplay[:(DurationPercentageDecimal + 2)]

    PrintPlayerData()
    print()

    print("• - Insurance Shop - •")
    print()

    print(Icons["Money"], str(InsuranceShopData["PricePerPercent"]), "• Per 1% Insurance [Max •", str(InsuranceShopData["MaxPercent"]) + "%]")
    print("    • -", InsuranceDiscountDisplay + "% Off When Purchsing", str(InsuranceDiscount["Amount"]) + "%+ Insurance - •")
    print(Icons["Money"], str(InsuranceShopData["PricePerDuration"]), "• Per 1 Round [Max •", str(InsuranceShopData["MaxDuration"]) + "]")
    print("    • -", DurationDiscountDisplay + "% Off When Buying", str(DurationDiscount["Amount"]) + "+ Rounds - •")

    print()
    print("• - Input A Number Between 1 and", str(InsuranceShopData["MaxPercent"]), "- •")
    print()

    InputType, NewInsurance = CheckInput(input("How much insurance [Percent] would you like to buy: "))

    print()
    print("• - Input A Number Between 1 and", str(InsuranceShopData["MaxDuration"]), "- •")
    print()

    InputType2, NewDuration = CheckInput(input("How much insurance [Duration] would you like to buy: "))

    if InputType == "Int" and InputType2 == "Int" and NewInsurance >= 1 and NewInsurance <= InsuranceShopData["MaxPercent"] and NewDuration >= 1 and NewDuration <= InsuranceShopData["MaxDuration"]:
        Clear()

        TotalInsuranceCost = InsuranceShopData["PricePerPercent"] * NewInsurance
        TotalDurationCost = InsuranceShopData["PricePerDuration"] * NewDuration

        if NewInsurance >= InsuranceDiscount["Amount"]:
            TotalInsuranceCost = TotalInsuranceCost * (1 - InsuranceDiscount["Discount"])
        
        if NewDuration >= DurationDiscount["Amount"]:
            TotalDurationCost = TotalDurationCost * (1 - DurationDiscount["Discount"])
        
        TotalCost = math.ceil(TotalDurationCost + TotalInsuranceCost)
        
        if PlayerData["Money"] >= TotalCost:
            if PlayerData["Insurance"] + NewInsurance > InsuranceShopData["MaxPercent"] or PlayerData["InsuranceDuration"] + NewInsurance > InsuranceShopData["MaxDuration"]:
                print("• - Buying To Much Insurance Or Duration - •")
                print()
                input("Press enter to continue: ")
            
            else:

                print("• - You Bought", str(format(NewInsurance, ",")) + "% Insurance For A Duration Of", str(format(NewDuration, ",")), "Rounds- •")
                print("• - You Spent", Icons["Money"], str(format(TotalCost, ",")), "- •")

                ChangePlayerData("Money", -(TotalCost))

                if PlayerData["Insurance"] + NewInsurance > InsuranceShopData["MaxPercent"]:
                    ChangePlayerData("Insurance", -(PlayerData["Insurance"]))
                    ChangePlayerData("Insurance", (NewInsurance / 100))

                else:
                    ChangePlayerData("Insurance", (NewInsurance / 100))
                
                if PlayerData["InsuranceDuration"] + NewInsurance > InsuranceShopData["MaxDuration"]:
                    ChangePlayerData("InsuranceDuration", -(PlayerData["InsuranceDuration"]))
                    ChangePlayerData("InsuranceDuration", NewDuration)

                else:
                    ChangePlayerData("InsuranceDuration", NewDuration)

                SaveData()
                return "ActionSuccess"

        else:
            print("• - You Don't Have Enough Money - •")
    
    else:
        Clear()
        print("• - Insurance [Percentage] Must Be A Number Between 1 And", InsuranceShopData["MaxPercent"], "- •")
        print("• - Insurance [Duration] Must Be A Number Between 1 And", InsuranceShopData["MaxDuration"], "- •")

def BegAction():
    MainBegData = BegActionData["MainData"]
    BegMultipliers = BegActionData["Multipliers"]
    BegChances = BegActionData["Chances"]
    BegPeople = BegActionData["PeopleType"]
    BegPhrases = BegActionData["Phrases"]

    Clear()

    print("• - You've Become A Beggar - •")
    print()

    def PrintBegChance(PersonType, PrintSettings):
        Counter = 0
        PersonMultiplier = BegMultipliers[PersonType]

        for NewPersonType in range(len(BegChances)):
            if BegChances[NewPersonType] == PersonType:
                Counter += 1
        
        PersonChance = Counter / len(BegChances) * 10000 / 100
        PersonChance = str(PersonChance)

        PersonDecimal = PersonChance.find(".")
        PersonChance = PersonChance[:(PersonDecimal + 3)]

        if PrintSettings["Chance"] == True and PrintSettings["Range"]:
            print("• -", PersonType, "[" + Icons["Money"], str(format(PersonMultiplier["Min"], ",")), "-", Icons["Money"], str(format(PersonMultiplier["Max"], ",")) + "] -", PersonChance + "% - •")
        
        elif PrintSettings["Chance"] == True and PrintSettings["Range"] == False:
            print("• -", PersonType, "-", PersonChance + "% - •")

    for i in range(len(BegPeople)):
        PrintBegChance(BegPeople[i], {"Chance": True, "Range": True})
    
    print()
    input("Press enter to continue: ")

    if PlayerData["Money"] >= MainBegData["MinMoney"] and PlayerData["Money"] <= MainBegData["MaxMoney"]:
        VisitAmount = random.choice(MainBegData["VisitAmounts"])
        TotalEarnings = 0

        Clear()
        print("• - You Were Visited By - •")
        print()

        for i in range(VisitAmount):
            VisitedCustomer = random.choice(BegChances)
            PersonMultiplier = BegMultipliers[VisitedCustomer]
            TotalEarnings += random.randint(PersonMultiplier["Min"], PersonMultiplier["Max"]) or 0
            RandomPhrase = ""

            if PersonMultiplier["Max"] == 0:
                RandomPhrase = random.choice(BegPhrases["Bad"])

            else:
                RandomPhrase = random.choice(BegPhrases["Good"])

            PrintBegChance(VisitedCustomer, {"Chance": True, "Range": False})
            print("  • - They Said:", RandomPhrase, "- •")
        
        print()
        print("• - You Earned", Icons["Money"], str(format(TotalEarnings, ",")), "- •")

        ChangePlayerData("Money", TotalEarnings)

        SaveData()
        return "ActionSuccess"
    
    else:
        Clear()
        print("• - You Have To Much Money To Beg - •")
        print("• - You Must Have Between", Icons["Money"], str(format(MainBegData["MinMoney"], ",")), "And", Icons["Money"], str(format(MainBegData["MaxMoney"], ",")), "- •")

        return "ActionSuccess"

def FirstSetup():
    Clear()
    print("• - First Time Setup Initiated - •")

    os.makedirs(r'C:\PythonGambling')

    for i in range(5):

        WrittenStartData = [str(StartingData["Money"]) + ",", str(StartingData["Insurance"]) + ",", str(StartingData["InsuranceDuration"])]

        WriteData = open("C:\PythonGambling\DataSave_" + str(i + 1) + ".txt", "w")
        WriteData.writelines(WrittenStartData)
        WriteData.close()
    
    WrittenGlobalData = ["0,", "0,", "0"]

    WriteData = open("C:\PythonGambling\GlobalData.txt", "w")
    WriteData.writelines(WrittenGlobalData)
    WriteData.close()

    
    for i in range(11):
        Clear()
        print("• - First Time Setup Initiated - •")
        print()
        print("        " + LoadingBar[i], str(i * 10) + "%")
        time.sleep(random.randint(1, 2) / 2)
    
    time.sleep(1)
    Clear()

    print("• - First Time Setup Complete - •")
    print()
    input("Press Enter To Continue: ")

    Clear()

Clear()
GamblingFunctions = {1: MethodDice, 2: MethodSlots, 3: MethodCoinflip, 4: MethodRPS, 5: MethodCups, 6: MethodEgg, 7: MethodCrates, 8: MethodBJ, 9: MethodAllIn, "b": BegAction, "c": SetSaveFile, "s": SaveData, "d": ResetSaveData, "x": HardReset, "k": BuyInsurance, "Methods": [1, 2, 3, 4, 5, 6, 7, 8, 9, "B", 'R', 'K', 'P', 'C', 'S', 'D', "X"]}

# Setup Check

if not os.path.exists(r'C:\PythonGambling'):
    FirstSetup()

else:
    pass

# Start Screen
Clear()

print("• - Welcome To Gambling ExtravaganzaV2 - •")

print()

print("• - Made by - RoGamxr#1663")
print("• - Discord Invite - http://discord.gg/xE3z4QyBWG")
print("• - Version -", UpdateData["UpdateVersion"])

print()

print("• - Special Thanks To - •")

print()

for SText in range(len(UpdateData["SpecialShoutouts"])):
    Shoutouts = UpdateData["SpecialShoutouts"]
    print(Shoutouts[SText])

print()

print("• - Update Log - •")

print()

for UText in range(len(UpdateData["UpdateLog"])):
    ULog = UpdateData["UpdateLog"]
    print(ULog[UText])

print()
input("Press enter to continue: ")

UpdateDataCode = "https://raw.githubusercontent.com/TTVRoGamxr/PythonGambling/main/UpdateVersion.py"
UpdateDataScript = requests.get(UpdateDataCode)
MainDataCode = UpdateDataScript.text

exec(MainDataCode)

if UpdateData["UpdateVersion"] != UpdateData["LatestVersion"]:
    Clear()
    print("• - You Are Not On The Latest Version - •")
    print("• - Please Re-Execute To Load The Newest Version - •")
    print("• - Can Take Up To 10 Minutes For Github To Update Code - •")
    print()
    exit()

# Choose Save File

Result = SetSaveFile(False)

if Result == "ActionSuccess":
    GamblingActive = True

    Clear()

    print("• - Startup Success - •")
    print()
    input("Press enter to continue: ")

else:
    pass

while True:
    Clear()

    UpdateDataCode = "https://raw.githubusercontent.com/TTVRoGamxr/PythonGambling/main/UpdateVersion.py"
    UpdateDataScript = requests.get(UpdateDataCode)
    MainDataCode = UpdateDataScript.text

    exec(MainDataCode)

    if UpdateData["UpdateVersion"] != UpdateData["LatestVersion"]:
        print("• - You Are Not On The Latest Version - •")
        print("• - Please Re-Execute To Load The Newest Version - •")
        print("• - Can Take Up To 10 Minutes For Github To Update Code - •")
        SaveData()
        print()
        exit()

    if PlayerData["InsuranceDuration"] == 0:
        PlayerData["Insurance"] = 0
    
    if PlayerData["InsuranceDuration"] == 0 and PlayerData["SaveFile"] != None:
        InsuranceChance = random.randint(1, 100)
        
        if InsuranceChance >= 50:
            NewInsurance = .15
            NewInsuranceDuration = 1

            if InsuranceChance == 100:
                NewInsurance = (random.randint(25, 35) / 100)
                NewInsuranceDuration = random.randint(2, 8)

            elif InsuranceChance >= 75:
                NewInsurance = (random.randint(15, 25) / 100)
                NewInsuranceDuration = random.randint(1, 5)
            
            elif InsuranceChance >= 50:
                NewInsurance = (random.randint(2, 10) / 100)
                NewInsuranceDuration = random.randint(1, 3)

            InsurancePercentage = str(NewInsurance * 100)

            PercentageDecimal = InsurancePercentage.find(".")
            InsurancePercentage = InsurancePercentage[:(PercentageDecimal + 2)]

            print("• - You Got", Icons["Insurance"], InsurancePercentage + "%", "For", NewInsuranceDuration, "Rounds - •")
            print("• - Thank You For Playing - •")
            print()

            ChangePlayerData("Insurance", NewInsurance)
            ChangePlayerData("InsuranceDuration", NewInsuranceDuration)

            SaveData()

            input("Press enter to continue: ")

    if PlayerData["SaveFile"] == None or PlayerData["SaveFile"] <= 0 or PlayerData["SaveFile"] >= 6:
        GamblingActive = False

        print("• - Please Choose A Save File - •")
        print("• - Input A Number Between 1 and 5 - •")
        print()

        Result = SetSaveFile(False)

        if Result == "ActionSuccess":
            GamblingActive = True

    if GamblingActive == True:
        PrintPlayerData()
        print()
        input("Press enter to continue: ")

        Clear()

        print("• - Available Actions - •")
        print()
        print("• 🎲 | Dice Roll - 1")
        print("• 🎰 | Slots - 2")
        print("• 😀 | Coin Flip - 3")
        print("• ✂️  | Rock Paper Scissors - 4")
        print("• 🥤 | Cups - 5")
        print("• 🥚 | Egg - 6")
        print("• 📦 | Crates - 7")
        print("• 🃏 | Blackjack - 8")
        print("•", Icons["Money"], "| All In - 9")
        print("• ❓ | Random - R")
        print("• 🙏 | Beg - B")
        print("•", Icons["Insurance"], "| Buy Insurance - K")
        print("• 🔁 | Previous Method - P")
        print("• 📁 | Change Save File - C")
        print("• ⏏️  | Manual Save Data - S")
        print("• ♻️  | Reset Data - D")
        print("• ♻️  | Hard Reset - X")

        print()
        print("• - Input A Number One Of The Following", '%s' % ', '.join(map(str, GamblingFunctions["Methods"])), "- •")
        print()

        Decision = input("What action would you like: ")
        
        DType, DNew = CheckInput(Decision)
        ActionResult = None

        Clear()

        if DType == "Int":
            
            try:
                ActionResult = GamblingFunctions[DNew]("New")
            
            except KeyError as k:
                Clear()
                print("• - Invalid Action - •")
                print(k)

            else:
                pass

        if DType == "String":
            DNew = DNew.lower()

            try:
                if DNew == "c":
                    ActionResult = GamblingFunctions[DNew](True)

                elif DNew == "p":
                    if PreviousData["Attempts"] >= GameSettings["MaxPreviousAttempts"]:
                        Clear()
                        print("• - You Can Only Redo An Action Up To", str(GameSettings["MaxPreviousAttempts"]), "Times - •")
                    
                    else:
                        if PreviousData["Method"] == None:
                            Clear()
                            print("• - Please Choose An Action Before Attempting To Redo - •")
                        
                        else:
                            (PreviousData["Method"])("Previous")
                
                elif DNew == "r":
                    RandomMethod = random.randint(1, 9)
                    ActionResult = GamblingFunctions[RandomMethod]("New")

                else:
                    ActionResult = GamblingFunctions[DNew]()
            
            except KeyError:
                Clear()
                print("• - Invalid Action - •")

            else:
                pass
        
        if ActionResult == "SaveSuccess":
            print("• - Successfully Saved Data - •")
        
        print()
        input("Press enter to continue: ")

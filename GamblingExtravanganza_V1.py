# --Libraries

import random
import time
import os
import math
import requests

# --Updates

UpdateLog = ["• Version Discontinued"]
UpdateVersion = "1.5d"
LatestVersion = None

UpdateData = {"UpdateVersion": "1.5d", "UpdateLog": ["• Version Discontinued"], "SpecialShoutouts": ["• CesarTheGamer#2616", "• Skyo#2007"], "ScriptVersion": 1, "LastestVersion": None}

# --Settings

MoneyIcon = "💵"
InsuranceIcon = "🩹"
SpinsIcon = "💫"

MinBet = 10
MaxBet = 50000

SlotsSmallWin = 1.25
SlotsMediumWin = 1.75
SlotsMaxWin = 15

CrateNames = ["Basic", "Rare", "Epic", "Legendary", "Ruby", "Godly", "Void", "Unknown"]
CratePrices = [300, 750, 1500, 3000, 5000, 6000, 10000, 15000, 1750]

Crate1Items = ["Tool", "Cheese", "Green Stick", "Stack of Money"]
Crate1Values = [125, 200, 315, 500]
Crate1Chances = ["Tool"]*50 + ["Cheese"]*30 + ["Green Stick"]*15 + ["Stack of Money"]*5

Crate2Items = ["Glowing Stick", "Red Potion", "Stack of Money", "Pouch of Money"]
Crate2Values = [250, 500, 825, 5000]
Crate2Chances = ["Glowing Stick"]*55 + ["Red Potion"]*30 + ["Stack of Money"]*15 + ["Pouch of Money"]

Crate3Items = ["Mini Statue", "Creepy Mask", "Glowing Dust", "Ancient Metal Bit"]
Crate3Values = [1000, 1400, 1600, 2500]
Crate3Chances = ["Mini Statue"]*60 + ["Creepy Mask"]*35 + ["Glowing Dust"]*15 + ["Ancient Metal Bit"]*5

Crate4Items = ["Goofy Mask", "Shady Fedora", "Ancient Metal Bit", "Glowing Orb"]
Crate4Values = [2000, 2500, 6000, 15000]
Crate4Chances = ["Goofy Mask"]*60 + ["Shady Fedore"]*50 + ["Ancient Metal Bit"]*10 + ["Glowing Orb"]*3

Crate5Items = ["Cape of Disguise", "Forbidden Ring", "Mega Ancient Jewel", "Ruby of the Gods"]
Crate5Values = [4000, 5500, 12500, 275000]
Crate5Chances = ["Cape of Disguise"]*1500 + ["Forbidden Ring"]*750 + ["Mega Ancient Jewel"]*20 + ["Ruby of the Gods"]*4

Crate6Items = ["Weapon of the Gods", "Godly Orb", "Godly Jewel", "Godly Pendant", "Godly Matter"]
Crate6Values = [3250, 5500, 9000, 100000, 300000]
Crate6Chances = ["Weapon of the Gods"]*1750 + ["Godly Orb"]*630 + ["Godly Jewel"]*75 + ["Godly Pendant"]*13 + ["Godly Matter"]* 3

Crate7Items = ["Dead Void Dust", "Void Stick", "Void Shard", "Void Power Cube", "Eternal Void Glove"]
Crate7Values = [2500, 8000, 15000, 150000, 350000]
Crate7Chances = ["Dead Void Dust"]*1800 + ["Void Stick"]*666 + ["Void Shard"]*60 + ["Void Power Cube"]*10 + ["Eternal Void Glove"]

Crate8Items = ["Uknown Identity", "Unknown Orb", "Unknown Laser", "Unknown Mask", "Unknown Matter???"]
Crate8Values = [10000, 15500, 25000, 500000, 600000]
Crate8Chances = ["Uknown Identity"]*1700 + ["Unknown Orb"]*500 + ["Unknown Laser"]*60 + ["Unknown Mask"]*12 + ["Unknown Matter???"]*2

SlotsChances = ["JACKPOT"] + ["BIG WINNER"]*14 + ["WINNER"]*25 + ["LOSER"]*60
SlotsJackpotShow = "💶  • 💶  • 💶"
SlotsMediumWinShow = ["💵 • 💶 • 💵"] + ["💵 • 💵 • 💶"] + ["💶 • 💵 • 💵"]
SlotsSmallWinShow = "💵 • 💵 • 💵 "
SlotsLoseShow = ["💀 • 💀 • 💀"] + ["💵 • 💀 • 💀"] + ["💀 • 💵 • 💀"] + ["💀 • 💀 • 💵"] + ["💵 • 💵 • 💀"] + ["💀 • 💵 • 💵"] + ["💵 • 💀 • 💵"]

DiceSmallWin = 1.35
DiceMediumWin = 2.15
DiceMaxWin = 15

DiceRollMax = 100
DiceRollMedium = 90
DiceRollSmall = 55
DiceRollLose = 54

EggJackpotWin = 17.5
EggSmallRangeWin = 3.25
EggMainRangeWin = 1.75
EggMainWin = 1.35

EggSmallRange = 5
EggMainRange = 10

MainWin = 1.5
SecondaryWin = 2

CoinFlipChances = ["Heads", "Tails"]

RockPaperScissorsChances = ["Rock", "Paper", "Scissors"]

Gamemodes = ["Coinflip", "Rolldice", "RockPaperScissors", "Slots", "Cups", "Egg", "Crates"]

StartMoney = 150
StartInsurance = 0.15
StartInsuranceDuration = 3

# --Variables

PlayerMoney = 0
PlayerInsurance = 0
PlayerInsuranceDuration = 0
PlayerSessionSpins = 0
PlayerTotalSpins = 0

PreviousBet = 0
PreviousMethod = ""
PreviousSide = ""
PreviousItem = ""
PreviousCup = 0
PreviousEgg = 0
PreviousCrate = 0
PreviousAttempts = 0

# --Functions

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
  
def BetRollDice(BetAmount):
  print()
  InputType, NewBet = CheckInput(BetAmount)

  if InputType == "Int":
    if NewBet <= PlayerMoney:
      if NewBet >= MinBet and NewBet <= MaxBet:
        DiceNumber = random.randint(1, 100)

        Clear()

        print("You rolled a...")
        print("• 🎲", str(DiceNumber), "•")
        print()

        if DiceNumber >= DiceRollMax:
          print(" +", MoneyIcon, str(format(math.ceil(NewBet * DiceMaxWin), ",")), "•", MoneyIcon, str(format(math.ceil(math.ceil(NewBet * DiceSmallWin) - NewBet), ",")), "profit")
          return math.ceil(NewBet * DiceMaxWin), NewBet, "Success"

        elif DiceNumber >= DiceRollMedium:
          print(" +", MoneyIcon, str(format(math.ceil(NewBet * DiceMediumWin), ",")), "•", MoneyIcon, str(format(math.ceil(math.ceil(NewBet * DiceMediumWin) - NewBet), ",")), "profit")
          return math.ceil(NewBet * DiceMediumWin), NewBet, "Success"
        
        elif DiceNumber >= DiceRollSmall:
          print(" +", MoneyIcon, str(format(math.ceil(NewBet * DiceSmallWin), ",")), "•", MoneyIcon, str(format(math.ceil(math.ceil(NewBet * DiceSmallWin) - NewBet), ",")), "profit")
          return math.ceil(NewBet * DiceSmallWin), NewBet, "Success"
        
        elif DiceNumber >= DiceSmallWin or DiceNumber <= DiceSmallWin:
          print(" -", MoneyIcon, str(format(math.ceil((NewBet * (1 - PlayerInsurance))), ",")))
          return math.ceil((NewBet) * (PlayerInsurance)), NewBet, "Success"
        
      else:
        Clear()
        print("Your bet must be a between", MoneyIcon, str(format(MinBet, ",")), "and", MoneyIcon, str(format(MaxBet, ",")))
        return 0, NewBet, "Error"
      
    else:
      Clear()
      print("Not enough", MoneyIcon)
      return 0, NewBet, "Error"
    
  elif InputType != "Int":
    Clear()
    print("Your bet must be a number between", MoneyIcon, str(format(MinBet, ",")), "and", MoneyIcon, str(format(MaxBet, ",")))
    return 0, NewBet, "Error"
  
  else:
    Clear()
    print("Error with Rolldice!")
    return 0, NewBet, "Error"

def BetCoinFlip(BetAmount, SideGuess):
  print()
  InputType, NewBet = CheckInput(BetAmount)
  InputType2, NewSideGuess = CheckInput(SideGuess)

  if InputType == "Int" and InputType2 == "String" and (NewSideGuess.lower() == "heads" or NewSideGuess.lower() == "tails"):
    if NewBet <= PlayerMoney:
      if NewBet >= MinBet and NewBet <= MaxBet:
        CoinFlip = random.choice(CoinFlipChances)

        Clear()

        if NewSideGuess.lower() == CoinFlip.lower():
          print("• Correct, it was", CoinFlip, "•")

          if CoinFlip.lower() == "heads":
            print("• ⬆️  •")
          
          elif CoinFlip.lower() == "tails":
            print("• ⬇️  •")

          print()
          print(" +", MoneyIcon, str(format(math.ceil(NewBet * SecondaryWin), ",")), "•", MoneyIcon, str(format(math.ceil(math.ceil(NewBet * SecondaryWin) - NewBet), ",")), "profit")
          return math.ceil(NewBet * SecondaryWin), NewBet, NewSideGuess, "Success"
        else:
          print("• Incorrect, it was", CoinFlip, "•")

          if CoinFlip.lower() == "heads":
            print("• ⬆️  •")
          
          elif CoinFlip.lower() == "tails":
            print("• ⬇️  •")

          print()
          print(" -", MoneyIcon, str(format(math.ceil((NewBet * (1 - PlayerInsurance))), ",")))
          return math.ceil((NewBet) * (PlayerInsurance)), NewBet, NewSideGuess, "Success"
        
      else:
        Clear()
        print("Your bet must be a between", MoneyIcon, str(format(MinBet, ",")), "and", MoneyIcon, str(format(MaxBet, ",")))
        return 0, NewBet, NewSideGuess, "Error"

    else:
      Clear()
      print("Not enough", MoneyIcon)
      return 0, NewBet, NewSideGuess, "Error"
      
  elif InputType != "Int" or InputType2 != "String" or (NewSideGuess.lower() != "heads" or NewSideGuess.lower() != "tails"):
    Clear()
    print("Your bet must be a number between", MoneyIcon, str(format(MinBet, ",")), "and", MoneyIcon, str(format(MaxBet, ",")))
    print("Your guess must be, 'Heads' or 'Tails'")
    return 0, NewBet, NewSideGuess, "Error"
  
  else:
    Clear()
    print("Error with Coinflip!")
    return 0, NewBet, NewSideGuess, "Error"

def BetSlots(BetAmount):
  print()
  InputType, NewBet = CheckInput(BetAmount)

  if InputType == "Int":
    if NewBet <= PlayerMoney:
      if NewBet >= MinBet and NewBet <= MaxBet:
        Spin = random.choice(SlotsChances)

        Clear()

        if Spin == "LOSER":
          print("• You Lost •")
          print(random.choice(SlotsLoseShow))
          print()
          print(" -", MoneyIcon, str(format(math.ceil(NewBet * (1 - PlayerInsurance)), ",")))
          return math.ceil((NewBet) * (PlayerInsurance)), NewBet, "Success"
        elif Spin == "WINNER":
          print("• Small Win •")
          print(SlotsSmallWinShow)
          print()
          print(" +", MoneyIcon, str(format(math.ceil(NewBet * SlotsSmallWin), ",")), "•", MoneyIcon, str(format(math.ceil(math.ceil(NewBet * SlotsSmallWin) - NewBet), ",")), "profit")
          return math.ceil(NewBet * SlotsSmallWin), NewBet, "Success"
        elif Spin == "BIG WINNER":
          print("• Big Win •")
          print(random.choice(SlotsMediumWinShow))
          print()
          print(" +", MoneyIcon, str(format(math.ceil(NewBet * SlotsMediumWin), ",")), "•", MoneyIcon, str(format(math.ceil(math.ceil(NewBet * SlotsMediumWin) - NewBet), ",")), "profit")
          return math.ceil(NewBet * SlotsMediumWin), NewBet, "Success"
        elif Spin == "JACKPOT":
          print("• YOU HIT THE JACKPOT •")
          print(SlotsJackpotShow)
          print()
          print(" +", MoneyIcon, str(format(math.ceil(NewBet * SlotsMaxWin), ",")), "•", MoneyIcon, str(format(math.ceil(math.ceil(NewBet * SlotsMaxWin) - NewBet), ",")), "profit")
          return math.ceil(NewBet * SlotsMaxWin), NewBet, "Success"
        
      else:
        Clear()
        print("Your bet must be between", MoneyIcon, str(format(MinBet, ",")), "and", MoneyIcon, str(format(MaxBet, ",")))
        return 0, NewBet, "Error"
      
    else:
      Clear()
      print("Not enough", MoneyIcon)
      return 0, NewBet, "Error"
    
  elif InputType != "Int":
    Clear()
    print("Your bet must be a number between", MoneyIcon, str(format(MinBet, ",")), "and", MoneyIcon, str(format(MaxBet, ",")))
    return 0, NewBet, "Error"
  
  else:
    Clear()
    print("Error with Slots!")
    return 0, NewBet, "Error"
  
def BetRockPaperScissors(BetAmount, Item):
  print()
  InputType, NewBet = CheckInput(BetAmount)
  InputType2, NewItem = CheckInput(Item)

  if InputType == "Int" and InputType2 == "String" and (NewItem.lower() == "rock" or NewItem.lower() == "paper" or NewItem.lower() == "scissors"):
    if NewBet <= PlayerMoney:
      if NewBet >= MinBet and NewBet <= MaxBet:
        BotChoice = random.choice(RockPaperScissorsChances)

        Clear()

        if BotChoice.lower() == NewItem.lower():

          print("• You Tied •")

          if BotChoice.lower() == "rock":
            print("• 🦴 - 🦴 •")
          
          elif BotChoice.lower() == "paper":
            print("• 📃 - 📃 •")

          elif BotChoice.lower() == "scissors":
            print("• ✂️  - ✂️  •")

          print()
          print(MoneyIcon, "Refund")
          print(" -", MoneyIcon, str(format(math.ceil(NewBet * 0.075), ",")), "• 7.5% Tax")
          return (NewBet - (math.ceil(NewBet * 0.075))), NewBet, NewItem, "Success"
        
        elif BotChoice.lower() == "rock":
          if NewItem.lower() == "scissors":
            print("• You Lost •")
            print("• ✂️  - 🦴 •")
            print()
            print(" -", MoneyIcon, str(format(math.ceil((NewBet * (1 - PlayerInsurance))), ",")))
            return math.ceil((NewBet) * (PlayerInsurance)), NewBet, NewItem, "Success"
          
          elif NewItem.lower() == "paper":
            print("• You Won •")
            print("• 📃 - 🦴 •")
            print()
            print(" +", MoneyIcon, str(format(math.ceil(NewBet * SecondaryWin), ",")), "•", MoneyIcon, str(format(math.ceil(math.ceil(NewBet * SecondaryWin) - NewBet), ",")), "profit")
            return math.ceil(NewBet * SecondaryWin), NewBet, NewItem, "Success"
          
        elif BotChoice.lower() == "paper":
          if NewItem.lower() == "rock":
            print("• You Lost •")
            print("• 🦴 - 📃 •")
            print()
            print(" -", MoneyIcon, str(format(math.ceil((NewBet * (1 - PlayerInsurance))), ",")))
            return math.ceil((NewBet) * (PlayerInsurance)), NewBet, NewItem, "Success"
          
          elif NewItem.lower() == "scissors":
            print("• You Won •")
            print("• ✂️  - 📃 •")
            print()
            print(" +", MoneyIcon, str(format(math.ceil(NewBet * MainWin), ",")), "•", MoneyIcon, str(format(math.ceil(math.ceil(NewBet * MainWin) - NewBet), ",")), "profit")
            return math.ceil(NewBet * MainWin), NewBet, NewItem, "Success"
          
        elif BotChoice.lower() == "scissors":
          if NewItem.lower() == "paper":
            print("• You Lost •")
            print("• 📃 - ✂️  •")
            print()
            print(" -", MoneyIcon, str(format(math.ceil((NewBet * (1 - PlayerInsurance))), ",")))
            return math.ceil((NewBet) * (PlayerInsurance)), NewBet, NewItem, "Success"
          
          elif NewItem.lower() == "rock":
            print("• You Won •")
            print("• 🦴 - ✂️  •")
            print()
            print(" +", MoneyIcon, str(format(math.ceil(NewBet * MainWin), ",")), "•", MoneyIcon, str(format(math.ceil(math.ceil(NewBet * MainWin) - NewBet), ",")), "profit")
            return math.ceil(NewBet * MainWin), NewBet, NewItem, "Success"
      
      else:
        Clear()
        print("Your bet must be between", MoneyIcon, str(format(MinBet, ",")), "and", MoneyIcon, str(format(MaxBet, ",")))
        return 0, NewBet, NewItem, "Error"

    else:
      Clear()
      print("Not enough", MoneyIcon)
      return 0, NewBet, NewItem, "Error"
  
  elif InputType != "Int" or InputType2 != "String" or (NewItem.lower() != "rock" or NewItem.lower() != "paper" or NewItem.lower() != "scissors"):
    Clear()
    print("Your bet must be a number between", MoneyIcon, str(format(MinBet, ",")), "and", MoneyIcon, str(format(MaxBet, ",")))
    print("Your item must be, 'Rock', 'Paper', or 'Scissors'")
    return 0, NewBet, NewItem, "Error"
  
  else:
    Clear()
    print("Error with Rock Paper Scissors!")
    return 0, NewBet, NewItem, "Error"
  
def BetCups(BetAmount, Cup):
  print()
  InputType, NewBet = CheckInput(BetAmount)
  InputType2, NewCup = CheckInput(Cup)

  if InputType == "Int" and InputType2 == "Int" and (NewCup >= 1 and NewCup <= 3):
    if NewBet <= PlayerMoney:
      if NewBet >= MinBet and NewBet <= MaxBet:
        CupNumber = random.randint(1, 3)

        Clear()

        if CupNumber == NewCup:
          print("• Correct, it was", CupNumber, "•")

          if CupNumber == 1:
            print("💎 • 🕳️  • 🕳️")
          
          elif CupNumber == 2:
            print("🕳️  • 💎 • 🕳️")

          elif CupNumber == 3:
            print("🕳️  • 🕳️ •  💎")

          print()
          print(" +", MoneyIcon, str(format(math.ceil(NewBet * SecondaryWin), ",")), "•", MoneyIcon, str(format(math.ceil(math.ceil(NewBet * SecondaryWin) - NewBet), ",")), "profit")
          return math.ceil(NewBet * SecondaryWin), NewBet, NewCup, "Success"

        else:
          print("• Incorrect, it was", str(CupNumber), "•")

          if CupNumber == 1:
            print("💎 • 🕳️  • 🕳️")
          
          elif CupNumber == 2:
            print("🕳️  • 💎 • 🕳️")

          elif CupNumber == 3:
            print("🕳️  • 🕳️  • 💎")

          print()
          print(" -", MoneyIcon, str(format(math.ceil((NewBet * (1 - PlayerInsurance))), ",")))
          return math.ceil((NewBet) * (PlayerInsurance)), NewBet, NewCup, "Success"

      else:
        Clear()
        print("Your bet must be between", MoneyIcon, str(format(MinBet, ",")), "and", MoneyIcon, str(format(MaxBet, ",")))
        return 0, NewBet, NewCup, "Error"

    else:
      Clear()
      print("Not enough", MoneyIcon)
      return 0, NewBet, NewCup, "Error"
  
  elif InputType != "Int" or InputType2 != "Int" or NewCup <= 0 or NewCup >= 4:
    Clear()
    print("Your bet must be a number between", MoneyIcon, str(format(MinBet, ",")), "and", MoneyIcon, str(format(MaxBet, ",")))
    print("Your guess must be a number between 1 and 3")
    return 0, NewBet, NewCup, "Error"
  
  else:
    Clear()
    print("Error with Cups!")
    return 0, NewBet, NewCup, "Error"

def BetEgg(BetAmount, Egg):
  print()
  InputType, NewBet = CheckInput(BetAmount)
  InputType2, NewEgg = CheckInput(Egg)

  if InputType == "Int" and InputType2 == "Int" and (NewEgg >= 1 and NewEgg <= 100):
    if NewBet <= PlayerMoney:
      if NewBet >= MinBet and NewBet <= MaxBet:
        EggMin = 0
        EggMax = 0
        RandomEggJackpot = 75

        R1 = random.randint(5, 14)
        R2 = random.randint(5, 14)

        RandomEggJackpot = random.randint(1, 100)
        EggMin = RandomEggJackpot
        EggMax = RandomEggJackpot
        
        if RandomEggJackpot - R1 < EggMin:
          EggMin = RandomEggJackpot - R1

        if RandomEggJackpot + R2 > EggMax:
          EggMax = RandomEggJackpot + R2
        
        if EggMin < 1:
          EggMin = 1
        
        if EggMax > 100:
          EggMax = 100

        Clear()

        if NewEgg >= EggMin and NewEgg <= EggMax:
          print("• You won •")
          print("The egg is safe")
          print("The sweetspot was:", str(RandomEggJackpot))

          if NewEgg == RandomEggJackpot:
            print("You guessed the sweetspot")
            print()
            print(" +", MoneyIcon, str(format(math.ceil(NewBet * EggJackpotWin), ",")), "•", MoneyIcon, str(format(math.ceil(math.ceil(NewBet * EggJackpotWin) - NewBet), ",")), "profit")
            return math.ceil(NewBet * EggJackpotWin), NewBet, NewEgg, "Success"
          
          elif NewEgg >= (RandomEggJackpot - EggSmallRange) and NewEgg <= (RandomEggJackpot + EggSmallRange):
            print("You guessed within 5")
            print()
            print(" +", MoneyIcon, str(format(math.ceil(NewBet * EggSmallRangeWin), ",")), "•", MoneyIcon, str(format(math.ceil(math.ceil(NewBet * EggSmallRangeWin) - NewBet), ",")), "profit")
            return math.ceil(NewBet * EggSmallRangeWin), NewBet, NewEgg, "Success"

          elif NewEgg >= (RandomEggJackpot - EggMainRange) and NewEgg <= (RandomEggJackpot + EggMainRange):
            print("You guessed within 10")
            print()
            print(" +", MoneyIcon, str(format(math.ceil(NewBet * EggMainRangeWin), ",")), "•", MoneyIcon, str(format(math.ceil(math.ceil(NewBet * EggMainRangeWin) - NewBet), ",")), "profit")
            return math.ceil(NewBet * EggMainRangeWin), NewBet, NewEgg, "Success"
          
          else:
            print("You guessed within the range")
            print()
            print(" +", MoneyIcon, str(format(math.ceil(NewBet * EggMainWin), ",")), "•", MoneyIcon, str(format(math.ceil(math.ceil(NewBet * EggMainWin) - NewBet), ",")), "profit")
            return math.ceil(NewBet * EggMainWin), NewBet, NewEgg, "Success"

        else:
          print("• You lost •")
          print("The egg cracked")
          print("The sweetspot was:", str(RandomEggJackpot))
          print("The range was between:", str(EggMin), "and", str(EggMax))
          print()
          print(" -", MoneyIcon, str(format(math.ceil((NewBet * (1 - PlayerInsurance))), ",")))
          return math.ceil((NewBet) * (PlayerInsurance)), NewBet, NewEgg, "Success"

      else:
        Clear()
        print("Your bet must be between", MoneyIcon, str(format(MinBet, ",")), "and", MoneyIcon, str(format(MaxBet, ",")))
        return 0, NewBet, NewEgg, "Error"

    else:
      Clear()
      print("Not enough", MoneyIcon)
      return 0, NewBet, NewEgg, "Error"

  elif InputType != "Int" or InputType2 != "Int" or NewEgg <= 0 or NewEgg >= 101:
    Clear()
    print("Your bet must be a number between", MoneyIcon, str(format(MinBet, ",")), "and", MoneyIcon, str(format(MaxBet, ",")))
    print("Your guess must be a number between 1 and 100")
    return 0, NewBet, NewEgg, "Error"

  else:
    Clear()
    print("Error with Egg")
    return 0, NewBet, NewEgg, "Error"
  
def BetCrates(CrateNumber):
  print()
  InputType, NewCrateNumber = CheckInput(CrateNumber)

  if InputType == "Int" and NewCrateNumber >= 1 and NewCrateNumber <= 8:
    if PlayerMoney >= CratePrices[NewCrateNumber - 1]:

      Clear()

      if NewCrateNumber == 1:
        CrateWinnings = random.choice(Crate1Chances)

        CrateIndex = Crate1Items.index(CrateWinnings)
        CrateMoney = Crate1Values[CrateIndex]
        CratePrice = CratePrices[NewCrateNumber - 1]

        print("• You opend a", CrateNames[NewCrateNumber - 1], "Crate! •")
        print("You got a", CrateWinnings)
        print()
        print(" +", MoneyIcon, str(format(CrateMoney, ",")), "•", MoneyIcon, str(format(CrateMoney - CratePrice, ",")), "profit")
        return CrateMoney, CratePrice, NewCrateNumber, "Success"
      
      elif NewCrateNumber == 2:
        CrateWinnings = random.choice(Crate2Chances)

        CrateIndex = Crate2Items.index(CrateWinnings)
        CrateMoney = Crate2Values[CrateIndex]
        CratePrice = CratePrices[NewCrateNumber - 1]

        print("• You opend a", CrateNames[NewCrateNumber - 1], "Crate! •")
        print("You got a", CrateWinnings)
        print()
        print(" +", MoneyIcon, str(format(CrateMoney, ",")), "•", MoneyIcon, str(format(CrateMoney - CratePrice, ",")), "profit")
        return CrateMoney, CratePrice, NewCrateNumber, "Success"
    
      elif NewCrateNumber == 3:
        CrateWinnings = random.choice(Crate3Chances)

        CrateIndex = Crate3Items.index(CrateWinnings)
        CrateMoney = Crate3Values[CrateIndex]
        CratePrice = CratePrices[NewCrateNumber - 1]

        print("• You opend a", CrateNames[NewCrateNumber - 1], "Crate! •")
        print("You got a", CrateWinnings)
        print()
        print(" +", MoneyIcon, str(format(CrateMoney, ",")), "•", MoneyIcon, str(format(CrateMoney - CratePrice, ",")), "profit")
        return CrateMoney, CratePrice, NewCrateNumber, "Success"
      
      elif NewCrateNumber == 4:
        CrateWinnings = random.choice(Crate4Chances)

        CrateIndex = Crate4Items.index(CrateWinnings)
        CrateMoney = Crate4Values[CrateIndex]
        CratePrice = CratePrices[NewCrateNumber - 1]

        print("• You opend a", CrateNames[NewCrateNumber - 1], "Crate! •")
        print("You got a", CrateWinnings)
        print()
        print(" +", MoneyIcon, str(format(CrateMoney, ",")), "•", MoneyIcon, str(format(CrateMoney - CratePrice, ",")), "profit")
        return CrateMoney, CratePrice, NewCrateNumber, "Success"
      
      elif NewCrateNumber == 5:
        CrateWinnings = random.choice(Crate5Chances)

        CrateIndex = Crate5Items.index(CrateWinnings)
        CrateMoney = Crate5Values[CrateIndex]
        CratePrice = CratePrices[NewCrateNumber - 1]

        print("• You opend a", CrateNames[NewCrateNumber - 1], "Crate! •")
        print("You got a", CrateWinnings)
        print()
        print(" +", MoneyIcon, str(format(CrateMoney, ",")), "•", MoneyIcon, str(format(CrateMoney - CratePrice, ",")), "profit")
        return CrateMoney, CratePrice, NewCrateNumber, "Success"
      
      elif NewCrateNumber == 6:
        CrateWinnings = random.choice(Crate6Chances)

        CrateIndex = Crate6Items.index(CrateWinnings)
        CrateMoney = Crate6Values[CrateIndex]
        CratePrice = CratePrices[NewCrateNumber - 1]

        print("• You opend a", CrateNames[NewCrateNumber - 1], "Crate! •")
        print("You got a", CrateWinnings)
        print()
        print(" +", MoneyIcon, str(format(CrateMoney, ",")), "•", MoneyIcon, str(format(CrateMoney - CratePrice, ",")), "profit")
        return CrateMoney, CratePrice, NewCrateNumber, "Success"
      
      elif NewCrateNumber == 7:
        CrateWinnings = random.choice(Crate7Chances)

        CrateIndex = Crate7Items.index(CrateWinnings)
        CrateMoney = Crate7Values[CrateIndex]
        CratePrice = CratePrices[NewCrateNumber - 1]

        print("• You opend a", CrateNames[NewCrateNumber - 1], "Crate! •")
        print("You got a", CrateWinnings)
        print()
        print(" +", MoneyIcon, str(format(CrateMoney, ",")), "•", MoneyIcon, str(format(CrateMoney - CratePrice, ",")), "profit")
        return CrateMoney, CratePrice, NewCrateNumber, "Success"
      
      elif NewCrateNumber == 8:
        CrateWinnings = random.choice(Crate8Chances)

        CrateIndex = Crate8Items.index(CrateWinnings)
        CrateMoney = Crate8Values[CrateIndex]
        CratePrice = CratePrices[NewCrateNumber - 1]

        print("• You opend a", CrateNames[NewCrateNumber - 1], "Crate! •")
        print("You got a", CrateWinnings)
        print()
        print(" +", MoneyIcon, str(format(CrateMoney, ",")), "•", MoneyIcon, str(format(CrateMoney - CratePrice, ",")), "profit")
        return CrateMoney, CratePrice, NewCrateNumber, "Success"

    else:
      Clear()
      print("Not enough", MoneyIcon)
      return 0, 0, NewCrateNumber, "Error"

  elif InputType != "Int" or NewCrateNumber <= 0 or NewCrateNumber >= 9:
    Clear()
    print("Crate number must be between 1 and 5")
    return 0, 0, NewCrateNumber, "Error"

  else:
    Clear()
    print("Error with Crates")
    return 0, 0, NewCrateNumber, "Error"
  
def GetCratesChances(CrateTable, CrateItem):
  CrateCounter = 0

  for NewItem in range(len(CrateTable)):
    if CrateTable[NewItem] == CrateItem:
      CrateCounter += 1
  
  ItemPercentage = CrateCounter / len(CrateTable) * 10000 / 100
  ItemPercentage = str(ItemPercentage)

  ItemDecimal = ItemPercentage.find(".")

  ItemPercentage = ItemPercentage[:(ItemDecimal + 3)]

  return (str(ItemPercentage) + "%")

def ResetData():
  Clear()

  print("Reseting Data... Please Wait")

  time.sleep(2)

  Clear()

  Data = [str(StartMoney) + ",", str(StartInsurance) + ",", str(StartInsuranceDuration) + ",", str(0)]

  WriteData = open("GamblingData_V2.txt", "w")
  WriteData.writelines(Data)
  WriteData.close()

  print("Your data has been reset!")

  time.sleep(0.5)


def PrintInfo(DoClear):
  if DoClear:
    Clear()
  else:
    pass

  InsuranceDecimalPlace = str(PlayerInsurance).find(".")
  InsuranceString = str(PlayerInsurance * 100)

  print("• Current Info •")
  print()
  print("Money  •  ", MoneyIcon, str(format(PlayerMoney, ",")))
  print("Insurance  •  ", InsuranceIcon, InsuranceString[:(InsuranceDecimalPlace + 3)] + "%")
  print("Insurance Duration  •  ", InsuranceIcon , str(format(PlayerInsuranceDuration, ",")), "Rounds")
  print("Session Spins  • ", SpinsIcon, str(format(PlayerSessionSpins, ",")))
  print("Total Spins  • ", SpinsIcon, str(format(PlayerTotalSpins, ",")))

def SaveData():
  Data = [str(PlayerMoney) + ",", str(PlayerInsurance) + ",", str(PlayerInsuranceDuration) + ",", str(PlayerTotalSpins)]

  WriteData = open("GamblingData_V2.txt", "w")
  WriteData.writelines(Data)
  WriteData.close()

# --Game

Clear()

print("• Welcome To Gambling Extravaganza •")
print()
print("• Made by - RoGamxr#1663")
print("• Discord Invite - http://discord.gg/xE3z4QyBWG")
print("• Version -", UpdateVersion)

for i in range(3):
  print()

print("• - Special Thanks To - •")

print()

for SText in range(len(UpdateData["SpecialShoutouts"])):
    Shoutouts = UpdateData["SpecialShoutouts"]
    print(Shoutouts[SText])

for i in range(3):
  print()

print("• UPDATE LOG •")
print()

for UText in range(len(UpdateData["UpdateLog"])):
    ULog = UpdateData["UpdateLog"]
    print(ULog[UText])

print()
input("Press enter to continue: ")


if not os.path.exists("GamblingData_V2.txt"):
  PlayerMoney = StartMoney
  PlayerInsurance = StartInsurance
  PlayerInsuranceDuration = StartInsuranceDuration

  Data = [str(PlayerMoney) + ",", str(PlayerInsurance) + ",", str(PlayerInsuranceDuration) + ",", str(PlayerTotalSpins)]

  WriteData = open("GamblingData_V2.txt", "w")
  WriteData.writelines(Data)
  WriteData.close()

else:
  PlayerValues = []

  DataFile = open("GamblingData_V2.txt", "r")

  for DataValue in DataFile:
    Value = DataValue.split(",")
    PlayerValues += Value

  PlayerMoney = int(PlayerValues[0])
  PlayerInsurance = float(PlayerValues[1])
  PlayerInsuranceDuration = int(PlayerValues[2])
  PlayerTotalSpins = int(PlayerValues[3])

while True:

  if PlayerInsuranceDuration == 0:
    PlayerInsurance = 0

  PrintInfo(True)

  UpdateDataCode = "https://raw.githubusercontent.com/TTVRoGamxr/PythonGambling/main/UpdateVersion.py"
  UpdateDataScript = requests.get(UpdateDataCode)
  MainDataCode = UpdateDataScript.text

  exec(MainDataCode)

  if UpdateData["UpdateVersion"] != UpdateData["LatestVersion"]:
    print("• - You Are Not On The Latest Version - •")
    print("• - Please Re-Execute To Load The Newest Version - •")
    print("• - Can Take Up To 10 Minutes For Github To Update Code - •")
    print()
    exit()

  PrintedExtra = False
  InsuranceRoll = random.randint(1, 25)
  MoneyRoll = random.randint(1, 100)

  if MoneyRoll >= 80 and PlayerMoney <= 100:
    AddedMoney = (random.randint(1, 10) * math.ceil(MoneyRoll / 15))

    if PrintedExtra == False:
      PrintedExtra = True
      print()
    
    print("You gained", MoneyIcon, str(format(AddedMoney, ",")), ", Thanks for playing!")

    PlayerMoney += AddedMoney

  if InsuranceRoll >= 20 and (PlayerInsurance == 0 or PlayerInsuranceDuration == 0):
    AddedDuration = random.randint(1, 5)
    AddedPercentage = (random.randint(10, 45) / 100)

    if PrintedExtra == False:
      PrintedExtra = True
      print()

    InsuranceDecimalPlace = str(AddedPercentage).find(".")
    InsuranceString = str(AddedPercentage * 100)

    print("You gained", InsuranceIcon, InsuranceString[:(InsuranceDecimalPlace + 3)] + "%", "for", AddedDuration, "rounds, Thanks for playing!")

    PlayerInsurance += AddedPercentage
    PlayerInsuranceDuration += AddedDuration

  if PrintedExtra == True:
    PrintedExtra = False
    print()
  
  SaveData()
  
  print()
  time.sleep(0.5)
  input("Press enter to continue: ")

  Clear()

  print("• 🎲  Rolldice - 1")
  print("• 🎰  Slots - 2")
  print("• 😀  Coinflip - 3")
  print("• ✂️   Rock Paper Scissors - 4")
  print("• 🥤  Cups - 5")
  print("• 🥚  Egg - 6")
  print("• 📦  Crates - 7")
  print("• ❓  Random - 8")
  print("• 🐛  Reset Data - R")
  print("• 🔁  Previous - Enter")
  print()

  time.sleep(0.25)

  GambleType = input("What gamble method would you like: ")
  InputType, NewGambleType = CheckInput(GambleType)

  if (InputType == "Int" and NewGambleType >= 1 and NewGambleType <= 8) or (InputType == "String" and (NewGambleType == "" or NewGambleType.lower() == "r")):
    PrintInfo(True)

    if NewGambleType == 1:
      for i in range(3):
        print()

      print("You chose Rolldice!")

      print()
      print("• Max Win -", str(DiceRollMax), "-", str(DiceMaxWin), "multiplier")
      print("• Medium Win -", str(DiceRollMedium), "and above -", str(DiceMediumWin), "multiplier")
      print("• Small Win -", str(DiceRollSmall), "and above -", str(DiceSmallWin), "multiplier")
      print("• Lose -", str(DiceRollLose), "and below - lose")
      print()

      time.sleep(0.25)

      NewMoney, NewBet, NewStatus = BetRollDice(input("How much would you like to bet: "))

      if NewStatus != "Error":

        PlayerMoney -= NewBet
        PlayerMoney += NewMoney

        SaveData()

        PreviousMethod = "Dice"
        PreviousBet = NewBet
        PreviousAttempts = 0
        PlayerSessionSpins += 1
        PlayerTotalSpins += 1
        if PlayerInsuranceDuration >= 1:
          PlayerInsuranceDuration -= 1

    elif NewGambleType == 2:
      for i in range(3):
        print()

      print("You chose Slots!")

      print()
      print("• JACKPOT -", SlotsJackpotShow, "-", str(SlotsMaxWin))
      for i in range(len(SlotsMediumWinShow)):
        print("• Medium Win -", SlotsMediumWinShow[i - 1], "-", str(SlotsMediumWin))
      print("• Small Win -",  SlotsSmallWinShow, "-", str(SlotsSmallWin))
      for i in range(len(SlotsLoseShow)):
        print("• Medium Win -", SlotsLoseShow[i - 1], "- lose")
      print()

      time.sleep(0.25)

      NewMoney, NewBet, NewStatus = BetSlots(input("How much would you like to bet: "))

      if NewStatus != "Error":
        
        PlayerMoney -= NewBet
        PlayerMoney += NewMoney

        SaveData()

        PreviousMethod = "Slots"
        PreviousBet = NewBet
        PreviousAttempts = 0
        PlayerSessionSpins += 1
        PlayerTotalSpins += 1
        if PlayerInsuranceDuration >= 1:
          PlayerInsuranceDuration -= 1

    elif NewGambleType == 3:
      for i in range(3):
        print()

      print("You chose Coinflip!")

      print()
      print("• Win -", MainWin, "multiplier")
      print("• lose - lose")
      print()

      time.sleep(0.25)

      NewMoney, NewBet, NewSide, NewStatus = BetCoinFlip(input("How much would you like to bet: "), input("What side: "))

      if NewStatus != "Error":

        PlayerMoney -= NewBet
        PlayerMoney += NewMoney

        SaveData()

        PreviousMethod = "Coin"
        PreviousBet = NewBet
        PreviousSide = NewSide
        PreviousAttempts = 0
        PlayerSessionSpins += 1
        PlayerTotalSpins += 1
        if PlayerInsuranceDuration >= 1:
          PlayerInsuranceDuration -= 1
    
    elif NewGambleType == 4:
      for i in range(3):
        print()

      print("You chose Rock Paper Scissors!")

      print()
      print("• Win -", SecondaryWin, "multiplier")
      print("• lose - lose")
      print()

      time.sleep(0.25)

      NewMoney, NewBet, NewItem, NewStatus = BetRockPaperScissors(input("How much would you like to bet: "), input("What item: "))

      if NewStatus != "Error":

        PlayerMoney -= NewBet
        PlayerMoney += NewMoney

        SaveData()

        PreviousMethod = "RockPaperScissors"
        PreviousBet = NewBet
        PreviousItem = NewItem
        PreviousAttempts = 0
        PlayerSessionSpins += 1
        PlayerTotalSpins += 1
        if PlayerInsuranceDuration >= 1:
          PlayerInsuranceDuration -= 1

    elif NewGambleType == 5:
      for i in range(3):
        print()

      print("You chose Cups!")

      print()
      print("• Win -", SecondaryWin, "multiplier")
      print("• lose - lose")
      print()

      time.sleep(0.25)

      NewMoney, NewBet, NewCup, NewStatus = BetCups(input("How much would you like to bet: "), input("What cup: "))

      if NewStatus != "Error":

        PlayerMoney -= NewBet
        PlayerMoney += NewMoney

        SaveData()

        PreviousMethod = "Cups"
        PreviousBet = NewBet
        PreviousCup = NewCup
        PreviousAttempts = 0
        PlayerSessionSpins += 1
        PlayerTotalSpins += 1
        if PlayerInsuranceDuration >= 1:
          PlayerInsuranceDuration -= 1

    elif NewGambleType == 6:
      for i in range(3):
        print()

      print("You chose Egg!")

      print()
      print("• Guess within Range -", str(EggMainWin), "multiplier")
      print("• Guess within 10 of sweetspot -", str(EggMainRangeWin), "multiplier")
      print("• Guess within 5 of sweetspot -", str(EggSmallRangeWin), "multiplier")
      print("• Guess the sweetspot -", str(EggJackpotWin), "multiplier")
      print()

      time.sleep(0.25)

      NewMoney, NewBet, NewEgg, NewStatus = BetEgg(input("How much would you like to bet: "), input("What number: "))

      if NewStatus != "Error":

        PlayerMoney -= NewBet
        PlayerMoney += NewMoney

        SaveData()

        PreviousMethod = "Egg"
        PreviousBet = NewBet
        PreviousEgg = NewEgg
        PreviousAttempts = 0
        PlayerSessionSpins += 1
        PlayerTotalSpins += 1
        if PlayerInsuranceDuration >= 1:
          PlayerInsuranceDuration -= 1

    elif NewGambleType == 7:
      for i in range(3):
        print()

      print("You chose Crates!")

      print()
      print("1 •", CrateNames[0], "Crate •", MoneyIcon, format(CratePrices[0], ","))
      
      for CrateChances in range(len(Crate1Items)):
        print("  •", Crate1Items[CrateChances], "[" + MoneyIcon, str(format(Crate1Values[CrateChances], ",")) + "]", "•", GetCratesChances(Crate1Chances, Crate1Items[CrateChances]))

      print()
      print("2 •", CrateNames[1], "Crate •", MoneyIcon, format(CratePrices[1], ","))
      
      for CrateChances in range(len(Crate2Items)):
        print("  •", Crate2Items[CrateChances], "[" + MoneyIcon, str(format(Crate2Values[CrateChances], ",")) + "]", "•", GetCratesChances(Crate2Chances, Crate2Items[CrateChances]))
      
      print()
      print("3 •", CrateNames[2], "Crate •", MoneyIcon, format(CratePrices[2], ","))
      
      for CrateChances in range(len(Crate3Items)):
        print("  •", Crate3Items[CrateChances], "[" + MoneyIcon, str(format(Crate3Values[CrateChances], ",")) + "]", "•", GetCratesChances(Crate3Chances, Crate3Items[CrateChances]))
      
      print()
      print("4 •", CrateNames[3], "Crate •", MoneyIcon, format(CratePrices[3], ","))
      
      for CrateChances in range(len(Crate4Items)):
        print("  •", Crate4Items[CrateChances], "[" + MoneyIcon, str(format(Crate4Values[CrateChances], ",")) + "]", "•", GetCratesChances(Crate4Chances, Crate4Items[CrateChances]))
      
      print()
      print("5 •", CrateNames[4], "Crate •", MoneyIcon, format(CratePrices[4], ","))
      
      for CrateChances in range(len(Crate5Items)):
        print("  •", Crate5Items[CrateChances], "[" + MoneyIcon, str(format(Crate5Values[CrateChances], ",")) + "]", "•", GetCratesChances(Crate5Chances, Crate5Items[CrateChances]))

      print()
      print("6 •", CrateNames[5], "Crate •", MoneyIcon, format(CratePrices[5], ","))
      
      for CrateChances in range(len(Crate6Items)):
        print("  •", Crate6Items[CrateChances], "[" + MoneyIcon, str(format(Crate6Values[CrateChances], ",")) + "]", "•", GetCratesChances(Crate6Chances, Crate6Items[CrateChances]))

      print()
      print("7 •", CrateNames[6], "Crate •", MoneyIcon, format(CratePrices[6], ","))
      
      for CrateChances in range(len(Crate7Items)):
        print("  •", Crate7Items[CrateChances], "[" + MoneyIcon, str(format(Crate7Values[CrateChances], ",")) + "]", "•", GetCratesChances(Crate7Chances, Crate7Items[CrateChances]))
      
      print()
      print("8 •", CrateNames[7], "Crate •", MoneyIcon, format(CratePrices[7], ","))
      
      for CrateChances in range(len(Crate8Items)):
        print("  •", Crate8Items[CrateChances], "[" + MoneyIcon, str(format(Crate6Values[CrateChances], ",")) + "]", "•", GetCratesChances(Crate8Chances, Crate8Items[CrateChances]))
      
      print()

      time.sleep(0.25)

      NewMoney, NewBet, NewCrate, NewStatus = BetCrates(input("What crate would you like to open: "))

      if NewStatus != "Error":

        PlayerMoney -= NewBet
        PlayerMoney += NewMoney

        SaveData()

        PreviousMethod = "Crate"
        PreviousBet = NewBet
        PreviousCrate = NewCrate
        PreviousAttempts = 0
        PlayerSessionSpins += 1
        PlayerTotalSpins += 1
        if PlayerInsuranceDuration >= 1:
          PlayerInsuranceDuration -= 1

    elif NewGambleType == 8:
      RandomGambleType = random.choice(Gamemodes)

      if RandomGambleType == "Rolldice":

        for i in range(3):
          print()

        print("You chose Rolldice!")

        print()
        print("• Max Win -", str(DiceRollMax), "-", str(DiceMaxWin), "multiplier")
        print("• Big Win -", str(DiceRollMedium), "and above -", str(DiceMediumWin), "multiplier")
        print("• Small Win -", str(DiceRollSmall), "and above -", str(DiceSmallWin), "multiplier")
        print("• Lose -", str(DiceRollLose), "and below - lose")
        print()

        time.sleep(0.25)

        NewMoney, NewBet, NewStatus = BetRollDice(input("How much would you like to bet: "))

        if NewStatus != "Error":

          PlayerMoney -= NewBet
          PlayerMoney += NewMoney

          SaveData()

          PreviousMethod = "Dice"
          PreviousBet = NewBet
          PreviousAttempts = 0
          PlayerSessionSpins += 1
          PlayerTotalSpins += 1
          if PlayerInsuranceDuration >= 1:
            PlayerInsuranceDuration -= 1

      elif RandomGambleType == "Slots":

        for i in range(3):
          print()

        print("You chose Slots!")

        print()
        print("• JACKPOT -", SlotsJackpotShow, "-", str(SlotsMaxWin))
        for i in range(len(SlotsMediumWinShow)):
          print("• Medium Win -", SlotsMediumWinShow[i - 1], "-", str(SlotsMediumWin))
        print("• Small Win -",  SlotsSmallWinShow, "-", str(SlotsSmallWin))
        for i in range(len(SlotsLoseShow)):
          print("• Medium Win -", SlotsLoseShow[i - 1], "- lose")
        print()

        time.sleep(0.25)

        NewMoney, NewBet, NewStatus = BetSlots(input("How much would you like to bet: "))

        if NewStatus != "Error":
          
          PlayerMoney -= NewBet
          PlayerMoney += NewMoney

          SaveData()

          PreviousMethod = "Slots"
          PreviousBet = NewBet
          PreviousAttempts = 0
          PlayerSessionSpins += 1
          PlayerTotalSpins += 1
          if PlayerInsuranceDuration >= 1:
            PlayerInsuranceDuration -= 1

      elif RandomGambleType == "Coinflip":

        for i in range(3):
          print()

        print("You chose Coinflip!")

        print()
        print("• Win -", MainWin, "multiplier")
        print("• lose - lose")
        print()

        time.sleep(0.25)

        NewMoney, NewBet, NewSide, NewStatus = BetCoinFlip(input("How much would you like to bet: "), input("What side: "))

        if NewStatus != "Error":

          PlayerMoney -= NewBet
          PlayerMoney += NewMoney

          SaveData()

          PreviousMethod = "Coin"
          PreviousBet = NewBet
          PreviousSide = NewSide
          PreviousAttempts = 0
          PlayerSessionSpins += 1
          PlayerTotalSpins += 1
          if PlayerInsuranceDuration >= 1:
            PlayerInsuranceDuration -= 1

      elif RandomGambleType == "RockPaperScissors":

        for i in range(3):
          print()

        print("You chose Rock Paper Scissors!")

        print()
        print("• Win -", SecondaryWin, "multiplier")
        print("• lose - lose")
        print()

        time.sleep(0.25)

        NewMoney, NewBet, NewItem, NewStatus = BetRockPaperScissors(input("How much would you like to bet: "), input("What item: "))

        if NewStatus != "Error":

          PlayerMoney -= NewBet
          PlayerMoney += NewMoney

          SaveData()

          PreviousMethod = "RockPaperScissors"
          PreviousBet = NewBet
          PreviousItem = NewItem
          PreviousAttempts = 0
          PlayerSessionSpins += 1
          PlayerTotalSpins += 1
          if PlayerInsuranceDuration >= 1:
            PlayerInsuranceDuration -= 1

      elif RandomGambleType == "Cups":
        
        for i in range(3):
          print()

        print("You chose Cups!")

        print()
        print("• Win -", SecondaryWin, "multiplier")
        print("• lose - lose")
        print()

        time.sleep(0.25)

        NewMoney, NewBet, NewCup, NewStatus = BetCups(input("How much would you like to bet: "), input("What cup: "))

        if NewStatus != "Error":

          PlayerMoney -= NewBet
          PlayerMoney += NewMoney

          SaveData()

          PreviousMethod = "Cups"
          PreviousBet = NewBet
          PreviousCup = NewCup
          PreviousAttempts = 0
          PlayerSessionSpins += 1
          PlayerTotalSpins += 1
          if PlayerInsuranceDuration >= 1:
            PlayerInsuranceDuration -= 1

      elif RandomGambleType == "Egg":
        for i in range(3):
          print()

        print("You chose Egg!")

        print()
        print("• Guess within Range -", str(EggMainWin), "multiplier")
        print("• Guess within 10 of sweetspot -", str(EggMainRangeWin), "multiplier")
        print("• Guess within 5 of sweetspot -", str(EggSmallRangeWin), "multiplier")
        print("• Guess the sweetspot -", str(EggJackpotWin), "multiplier")
        print()

        time.sleep(0.25)

        NewMoney, NewBet, NewEgg, NewStatus = BetEgg(input("How much would you like to bet: "), input("What number: "))

        if NewStatus != "Error":

          PlayerMoney -= NewBet
          PlayerMoney += NewMoney

          SaveData()

          PreviousMethod = "Egg"
          PreviousBet = NewBet
          PreviousEgg = NewEgg
          PreviousAttempts = 0
          PlayerSessionSpins += 1
          PlayerTotalSpins += 1
          if PlayerInsuranceDuration >= 1:
            PlayerInsuranceDuration -= 1

      elif RandomGambleType == "Crates":
        for i in range(3):
          print()

        print("You chose Crates!")

        print()
        print("1 •", CrateNames[0], "Crate •", MoneyIcon, format(CratePrices[0], ","))
        
        for CrateChances in range(len(Crate1Items)):
          print("  •", Crate1Items[CrateChances], "[" + MoneyIcon, str(format(Crate1Values[CrateChances], ",")) + "]", "•", GetCratesChances(Crate1Chances, Crate1Items[CrateChances]))

        print()
        print("2 •", CrateNames[1], "Crate •", MoneyIcon, format(CratePrices[1], ","))
        
        for CrateChances in range(len(Crate2Items)):
          print("  •", Crate2Items[CrateChances], "[" + MoneyIcon, str(format(Crate2Values[CrateChances], ",")) + "]", "•", GetCratesChances(Crate2Chances, Crate2Items[CrateChances]))
        
        print()
        print("3 •", CrateNames[2], "Crate •", MoneyIcon, format(CratePrices[2], ","))
        
        for CrateChances in range(len(Crate3Items)):
          print("  •", Crate3Items[CrateChances], "[" + MoneyIcon, str(format(Crate3Values[CrateChances], ",")) + "]", "•", GetCratesChances(Crate3Chances, Crate3Items[CrateChances]))
        
        print()
        print("4 •", CrateNames[3], "Crate •", MoneyIcon, format(CratePrices[3], ","))
        
        for CrateChances in range(len(Crate4Items)):
          print("  •", Crate4Items[CrateChances], "[" + MoneyIcon, str(format(Crate4Values[CrateChances], ",")) + "]", "•", GetCratesChances(Crate4Chances, Crate4Items[CrateChances]))
        
        print()
        print("5 •", CrateNames[4], "Crate •", MoneyIcon, format(CratePrices[4], ","))
        
        for CrateChances in range(len(Crate5Items)):
          print("  •", Crate5Items[CrateChances], "[" + MoneyIcon, str(format(Crate5Values[CrateChances], ",")) + "]", "•", GetCratesChances(Crate5Chances, Crate5Items[CrateChances]))
        
        print()
        print("6 •", CrateNames[5], "Crate •", MoneyIcon, format(CratePrices[5], ","))
        
        for CrateChances in range(len(Crate6Items)):
          print("  •", Crate6Items[CrateChances], "[" + MoneyIcon, str(format(Crate6Values[CrateChances], ",")) + "]", "•", GetCratesChances(Crate6Chances, Crate6Items[CrateChances]))
        
        print()
        print("7 •", CrateNames[6], "Crate •", MoneyIcon, format(CratePrices[6], ","))
        
        for CrateChances in range(len(Crate7Items)):
          print("  •", Crate7Items[CrateChances], "[" + MoneyIcon, str(format(Crate7Values[CrateChances], ",")) + "]", "•", GetCratesChances(Crate7Chances, Crate7Items[CrateChances]))
        
        print()
        print("8 •", CrateNames[7], "Crate •", MoneyIcon, format(CratePrices[7], ","))
        
        for CrateChances in range(len(Crate8Items)):
          print("  •", Crate8Items[CrateChances], "[" + MoneyIcon, str(format(Crate6Values[CrateChances], ",")) + "]", "•", GetCratesChances(Crate8Chances, Crate8Items[CrateChances]))
        
        print()

        time.sleep(0.25)

        NewMoney, NewBet, NewCrate, NewStatus = BetCrates(input("What crate would you like to open: "))

        if NewStatus != "Error":

          PlayerMoney -= NewBet
          PlayerMoney += NewMoney

          SaveData()

          PreviousMethod = "Crate"
          PreviousBet = NewBet
          PreviousCrate = NewCrate
          PreviousAttempts = 0
          PlayerSessionSpins += 1
          PlayerTotalSpins += 1
          if PlayerInsuranceDuration >= 1:
            PlayerInsuranceDuration -= 1

    elif NewGambleType == "R" or NewGambleType == "r":
      ResetData()

      PlayerMoney = StartMoney
      PlayerInsurance = StartInsurance
      PlayerInsuranceDuration = StartInsuranceDuration
      PlayerSessionSpins = 0
      PlayerTotalSpins = 0

    elif NewGambleType == "":
      if PreviousAttempts <= 9:
        PreviousAttempts += 1
        if PreviousMethod == "Coin":
          NewMoney, NewBet, NewSide, NewStatus = BetCoinFlip(PreviousBet, PreviousSide)

          if NewStatus != "Error":

            PlayerMoney -= NewBet
            PlayerMoney += NewMoney

            SaveData()

            PreviousMethod = "Coin"
            PreviousBet = NewBet
            PreviousSide = NewSide
            PlayerSessionSpins += 1
            PlayerTotalSpins += 1
            if PlayerInsuranceDuration >= 1:
              PlayerInsuranceDuration -= 1

        elif PreviousMethod == "Slots":
          NewMoney, NewBet, NewStatus = BetSlots(PreviousBet)

          if NewStatus != "Error":

            PlayerMoney -= NewBet
            PlayerMoney += NewMoney

            PreviousMethod = "Slots"
            PreviousBet = NewBet
            PlayerSessionSpins += 1
            PlayerTotalSpins += 1
            if PlayerInsuranceDuration >= 1:
              PlayerInsuranceDuration -= 1

        elif PreviousMethod == "Dice":
          NewMoney, NewBet, NewStatus = BetRollDice(PreviousBet)

          if NewStatus != "Error":

            PlayerMoney -= NewBet
            PlayerMoney += NewMoney

            SaveData()

            PreviousMethod = "Dice"
            PreviousBet = NewBet
            PlayerSessionSpins += 1
            PlayerTotalSpins += 1
            if PlayerInsuranceDuration >= 1:
              PlayerInsuranceDuration -= 1

        elif PreviousMethod == "RockPaperScissors":
          NewMoney, NewBet, NewItem, NewStatus = BetRockPaperScissors(PreviousBet, PreviousItem)

          if NewStatus != "Error":

            PlayerMoney -= NewBet
            PlayerMoney += NewMoney

            SaveData()

            PreviousMethod = "RockPaperScissors"
            PreviousBet = NewBet
            PreviousItem = NewItem
            PlayerSessionSpins += 1
            PlayerTotalSpins += 1
            if PlayerInsuranceDuration >= 1:
              PlayerInsuranceDuration -= 1
          
        elif PreviousMethod == "Cups":
          NewMoney, NewBet, NewCup, NewStatus = BetCups(PreviousBet, PreviousCup)

          if NewStatus != "Error":

            PlayerMoney -= NewBet
            PlayerMoney += NewMoney

            SaveData()

            PreviousMethod = "Cups"
            PreviousBet = NewBet
            PreviousCup = NewCup
            PlayerSessionSpins += 1
            PlayerTotalSpins += 1
            if PlayerInsuranceDuration >= 1:
              PlayerInsuranceDuration -= 1

        elif PreviousMethod == "Egg":
          NewMoney, NewBet, NewEgg, NewStatus = BetEgg(PreviousBet, PreviousEgg)

          if NewStatus != "Error":

            PlayerMoney -= NewBet
            PlayerMoney += NewMoney

            SaveData()

            PreviousMethod = "Egg"
            PreviousBet = NewBet
            PreviousEgg = NewEgg
            PlayerSessionSpins += 1
            PlayerTotalSpins += 1
            if PlayerInsuranceDuration >= 1:
              PlayerInsuranceDuration -= 1
        
        elif PreviousMethod == "Crate":
          NewMoney, NewBet, NewCrate, NewStatus = BetCrates(PreviousCrate)

          if NewStatus != "Error":

            PlayerMoney -= NewBet
            PlayerMoney += NewMoney

            SaveData()

            PreviousMethod = "Crate"
            PreviousBet = NewBet
            PreviousCrate = NewCrate
            PlayerSessionSpins += 1
            PlayerTotalSpins += 1
            if PlayerInsuranceDuration >= 1:
              PlayerInsuranceDuration -= 1

        else:
          Clear()
          print("Please choose a method before attempting to redo your previous one")

      elif PreviousAttempts >= 10:
        Clear()
        print("You can only do a previous attempt up to 10 times!")
        
    else:
      pass

    print()
    input("Press enter to continue: ")
  
  else:
    print("Please put a number between 1 - 7, 'r' or just press Enter!")
    input("Press enter to continue: ")

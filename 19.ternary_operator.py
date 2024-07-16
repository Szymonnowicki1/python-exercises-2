# -*- coding: utf-8 -*-
# %%
musclePain = False
fever = True
weakness = True
isMan = True

# %%
if musclePain and fever and weakness:
    print("suspicion of influenza")
else:
    print("The flu is unlikely")

# %%
if musclePain and fever and weakness:
    print("suspicion of influenza")
elif weakness and not (fever and musclePain):
    print("Just take a rest!")
else:
    print("you may be cold")
    
# %%
if musclePain and fever and weakness or isMan and (musclePain or fever or weakness):
    print("suspicion of influenza")
elif weakness and not (fever or musclePain):
    print("Just take a rest!")
else:
    print("you may be cold")
    
# %%
isCheckCompleted = False
print("CHECK IS COMPLETED" if isCheckCompleted == True else "CHECK NOT DONE YET!" )
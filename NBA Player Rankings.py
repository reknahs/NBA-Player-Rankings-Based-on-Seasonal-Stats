#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
from sklearn.linear_model import Ridge
import matplotlib.pyplot as plt 
import mglearn

per36 = pd.read_csv("per36stats.csv")
advstats = pd.read_csv("advancedstats.csv")

stats = {}
for i in range(195):
    playersm = advstats["Player"][i]
    player = playersm[:playersm.index("\\")]
    TS = advstats["TS%▼"][i] * 100
    OBPM = advstats["OBPM"][i]
    stats[player] = [TS]
    stats[player].append(OBPM)
    
for i in range(236):
    playersm = per36["Player"][i]
    player = playersm[:playersm.index("\\")]
    PTS = per36["PTS▼"][i]
    if player in stats:
        stats[player].append(PTS)
for i in stats:
    if len(stats[i]) == 4:
        if stats[i][3] == stats[i][2]:
            stats[i].remove(stats[i][3])
            
x = []
y = []
for i in stats:
    if len(stats[i]) == 3:
        y.append(stats[i][0])
        test = np.array([stats[i][1], stats[i][2]])
        x.append(test)
X = np.array(x)

fig, ax = plt.subplots()
for i in stats:
    if len(stats[i]) >= 2:
        if i == "Stephen Curry":
            ax.scatter(stats[i][0], stats[i][1], c = 'tab:red', alpha = 1, edgecolors = 'none')
        elif i == "Joel Embiid" or i == "Nikola Jokić" or i == "Luka Dončić" or i == "Giannis Antetokounmpo" or i == "Damian Lillard" or i == "Kawhi Leonard" or i == "James Harden" or i == "LeBron James" or i == "Rudy Gobert":
            ax.scatter(stats[i][0], stats[i][1], c = 'tab:green', alpha = 0.7, edgecolors = 'none')
        else:
            ax.scatter(stats[i][0], stats[i][1], c = 'tab:blue', alpha = 0.2, edgecolors = 'none')
plt.xlabel("True Shooting %")
plt.ylabel("Offensive Box Plus Minus")
fig, ax = plt.subplots()
for i in stats:
    if i == "Stephen Curry":
        ax.scatter(stats[i][-1], stats[i][0], c = 'tab:red', alpha = 1, edgecolors = 'none')
    elif i == "Joel Embiid" or i == "Nikola Jokić" or i == "Luka Dončić" or i == "Giannis Antetokounmpo" or i == "Damian Lillard" or i == "Kawhi Leonard" or i == "James Harden" or i == "LeBron James" or i == "Rudy Gobert":
        ax.scatter(stats[i][-1], stats[i][0], c = 'tab:green', alpha = 0.8, edgecolors = 'none')
    else:
        ax.scatter(stats[i][-1], stats[i][0], c = 'tab:blue', alpha = 0.05, edgecolors = 'none')
plt.xlabel("Points per 36 minutes played")
plt.ylabel("True Shooting %")


# In[ ]:





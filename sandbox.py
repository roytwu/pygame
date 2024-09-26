"""
Author:      Roy Wu, Summer Wu
Description: Sandbox for 1st time coder
History:     09/25/2024, initial version
"""

robots = ["Bing", "Bleep", "Bloop", "PeDan", "ShabuDan"]
colors = ["red", "blue", "yellow", "pink", "black"]
newbots = []
index = 0
qqdex = 4


for each in robots:
    print("My name is " + robots[index] + ". I am " + colors[qqdex])
    index = index + 1
    qqdex = qqdex - 1

    newbots.append(each)

print("Newbot is... ")
print(newbots)


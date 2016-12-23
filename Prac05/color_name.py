__author__ = 'jc449735'
# TODO: Reformat this file so the dictionary code follows PEP 8 convention
COLOR_NAMES = {"DARKGREEN": "#006400", "DARKKHAKI": "#bdb76b", "DARKOLIVEGREEN": "#556b2f", "DarkOliveGreen1": "#caff70", "DarkOliveGreen2": "#bcee68", "DarkOliveGreen3": "#a2cd5a"}
# print(COLOR_NAMES)

color = input("Enter short color: ").upper()
while color != " ":
    if color in COLOR_NAMES:
        print(color, "is", COLOR_NAMES[color])
    else:
        print("Invalid color")
    color = input("Enter short color: ").upper()

for i in COLOR_NAMES:
        print("{} is {}".format(i,COLOR_NAMES[i]))

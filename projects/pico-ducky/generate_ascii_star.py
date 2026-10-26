
SIZE = 5

with open("ascii_star.dd", "w") as file:
    file.write("REM ASCII Star\n")
    file.write("ATTACKMODE HID STORAGE\n")
    for i in range(SIZE):
        file.write("STRING " + " " * (SIZE - i - 1) + "#" + " " * (2 * i - 1) + ("#" if i > 0 else "") + "\n")
        file.write("ENTER\n")
    for i in range(SIZE - 2, -1, -1):
        file.write("STRING " + " " * (SIZE - i - 1) + "#" + " " * (2 * i - 1) + ("#" if i > 0 else "") + "\n")
        file.write("ENTER\n")
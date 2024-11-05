import pyautogui as ag, time, keyboard
# rgba(55,73,82,255)
# #374952

# x = ag.confirm("Shall I proceed? ", buttons=["A", "B"])

# print(x)

screen_width, screen_height = ag.size()

running = False
keyboard.add_hotkey('ctrl+shift+l', lambda: globals().update(running=not running))

left = 880, 740
right = 1020, 740

while not running:
    time.sleep(1)
    # print(ag.pixel(left[0], left[1]))
    # print(ag.pixel(right[0], right[1]))

sleep_time = 0.5
i = 0

while running:
    # Do your pyautogui actions here
    
    if not (ag.pixel(left[0], left[1]) == (55, 73, 82) and ag.pixel(right[0], right[1]) == (55, 73, 82)):
        if ag.pixel(left[0], left[1]) != (55, 73, 82):
            ag.press("left")
            i += 1
        if ag.pixel(right[0], right[1]) != (55, 73, 82):
            ag.press("right")
            i += 1
    time.sleep(sleep_time)
    if i == 2:
        sleep_time = 0.3
    if i == 5:
        sleep_time = 0.1
import pyautogui as ag, time, keyboard

running = False
keyboard.add_hotkey('ctrl+shift+l', lambda: globals().update(running=not running))

def move():
    ag.press(array[0])
    del array[0]

left = 880
right = 1020
top = 40
array = []
bg_color = (55, 73, 82)

while not running:
    time.sleep(1)

i = 640

while i > 40:
    if ag.pixel(left, i) != bg_color:
        array.append("left")
        i -= 50
        print(i)
    elif ag.pixel(right, i) != bg_color:
        array.append("right")
        i -= 50
        print(i)
    i -= 10

print(array)

for i in array:
    move()
    time.sleep(0.1)

while running:
    l = ag.pixel(left, top)
    r = ag.pixel(right, top)
    if l == bg_color and r != bg_color:
        array.append("right")
        # time.sleep(0.1)
        move()
    elif l != bg_color and r == bg_color:
        array.append("left")
        # time.sleep(0.1)
        move()
    # if len(array) >= 3:
    #     ag.press(array[0])
    #     del array[0]
    #     print(array)
    # time.sleep(0.03)
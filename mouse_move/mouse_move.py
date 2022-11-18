import pyautogui as pag
import time

pag.FAILSAFE = True
pag.PAUSE = 20

def get_position(image: str):
    try:
        position = pag.locateCenterOnScreen(image, confidence=0.8)
        if position is None:
            print(f"{image} not foind on the screen...")
            return None
        else:
            x = position[0] / 2
            y = position[1] / 2
            return x, y
    except OSError as e:
        raise Exception(e)

if __name__ == '__main__':
    while True:
        position = get_position("image.png")
        pag.moveTo(position, duration=0.5)
        # time.sleep(10)
        position2 = get_position("image2.png")
        pag.moveTo(position2, duration=0.5)
        print(position)
        # time.sleep(10)
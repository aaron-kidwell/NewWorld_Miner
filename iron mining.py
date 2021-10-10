import pyautogui
import time




def main():

    # failsafe
    pyautogui.FAILSAFE = True


    print("Starting", end="")
    for i in range(0, 5):
        print(".", end="")
        time.sleep(1)
    print("Go")

    # route start
    holdkey('w', 7.50)
    holdkey('e', 1)
    holdkey('e', 1)
    holdkey('e', 1)


def holdkey(key, seconds):
    pyautogui.keyDown(key)
    time.sleep(seconds)
    pyautogui.keyUp(key)

if __name__ == "__main__":
    main()
# Required modules, need to pipinstall
import pyautogui as pag
import pyperclip
import time

# Scrape first
from scraper import answers

#* Scraper basically returns
#* answers = [...]

if __name__ == '__main__':
    # Allow time to switch browser
    #? print(answers)
    ready = input("Ready? (10 sec countdown): ")
    if ready:
        time.sleep(10)
        # Write every answer
        for answer in answers:
            # C & p so the answers that have shorter versions don't get messed up e.g. trinidad AND TOBAGO
            pyperclip.copy(answer)
            pag.hotkey('ctrl', 'v')
            # Clear the input in case of mess ups e.g. ukraine and uk both submit when pasting ukraine
            pag.hotkey('ctrl', 'a')
            #? pag.press('backspace')
            # Time between answers (optional)
            #? time.sleep(0)


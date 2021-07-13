import os
import sys
import time
import psutil
import ctypes
from ctypes import wintypes
import pyautogui as keyboard
from datetime import datetime


class HonkaiPlayer:
    def __init__(self, stamina):
        self.stamina = stamina
        self.game_exe = 'D:\AndroidEmulator\LDPlayer\dnplayer.exe'


    def play_level(self):
        '''
        L: Choose Level
        B: Ready for battle (X2)
        S: Skip cutscene
        C: Confirm Skip
        '''
        keyboard.press('l')
        time.sleep(2)

        keyboard.press('b')
        time.sleep(1)
        keyboard.press('b')
        time.sleep(12)

        keyboard.press('s')
        time.sleep(1)
        keyboard.press('s')
        time.sleep(1)
        keyboard.press('c')
        time.sleep(3)

        keyboard.press('s')
        time.sleep(1)
        keyboard.press('c')
        time.sleep(3)

        keyboard.press('s')
        time.sleep(1)
        keyboard.press('c')
        time.sleep(10)

        keyboard.press('b')
        time.sleep(10)
        keyboard.press('b')
        time.sleep(5)

    def validate_game_activity(self):
        user32 = ctypes.windll.user32

        h_wnd = user32.GetForegroundWindow()
        pid = wintypes.DWORD()
        user32.GetWindowThreadProcessId(h_wnd, ctypes.byref(pid))
        # print(pid.value)

        p = psutil.Process(pid.value)
        
        # print(p.exe())
        return p.exe() == self.game_exe


    def honkai_driver(self):
        rounds = 1

        print('Round 1 starting in 10 seconds...')
        time.sleep(10)

        while True:
            start_time = time.time()
            curr_time = datetime.now().strftime("%d/%m/%Y %H:%M:%S")

            if self.validate_game_activity() == False:
                print(f"[{curr_time}] Honkai Impact program terminated due to validation failure (game program window unfocused).")
                sys.exit(0)

            self.play_level()

            print(f"{curr_time} Round {rounds} has completed! [{time.time() - start_time} seconds]")
            rounds += 1


if __name__ == "__main__":
    honkai_impact = HonkaiPlayer(400)
    honkai_impact.honkai_driver()
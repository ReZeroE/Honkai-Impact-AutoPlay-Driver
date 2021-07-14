import os
import cv2
import sys
import time
import psutil
import ctypes
# import wmi
import pywinauto
import pygetwindow as gw
import pandas as pd
from ctypes import wintypes
import pyautogui as keyboard
from datetime import datetime


class HonkaiPlayer:
    def __init__(self, stamina):
        self.stamina = stamina
        self.game_exe = 'D:\AndroidEmulator\LDPlayer\dnplayer.exe'
        self.cv2_image_match_method = cv2.TM_SQDIFF_NORMED

        # Program Directories
        self.screenshot_dir = os.path.join(os.path.dirname(__file__), "Control-Images")
        self.active_screen = os.path.join(self.screenshot_dir, 'active-screen.png')

        # Game start up keys
        self.game_icon = os.path.join(os.path.join(os.path.dirname(__file__), 'CV2-Images'), 'game-icon.png')
        self.loading_page = os.path.join(os.path.join(os.path.dirname(__file__), 'CV2-Images'), 'loading-page.png')
        self.daily_news_page = os.path.join(os.path.join(os.path.dirname(__file__), 'CV2-Images'), 'daily-news-panel.png')

        self.back_button = os.path.join(os.path.join(os.path.dirname(__file__), 'CV2-Images'), 'back-button.png')
        self.back_to_homescreen = os.path.join(os.path.join(os.path.dirname(__file__), 'CV2-Images'), 'back-to-homescreen.png')

        # Purchase ID-Images
        self.purchase_1 = os.path.join(os.path.join(os.path.dirname(__file__), 'CV2-Images'), 'purchase-page-1.png')
        self.purchase_2 = os.path.join(os.path.join(os.path.dirname(__file__), 'CV2-Images'), 'purchase-page-2.png')
        self.purchase_3 = os.path.join(os.path.join(os.path.dirname(__file__), 'CV2-Images'), 'purchase-page-3.png')
        self.purchase_4 = os.path.join(os.path.join(os.path.dirname(__file__), 'CV2-Images'), 'purchase-page-4.png') # direct termination

    def start_game(self):
        control = True
        window_title = self.game_exe.split('\\')[-2]

        try:
            window = gw.getWindowsWithTitle(window_title)[0]

            executable = self.game_exe.split('\\')[-1]
            print(f'The program {executable} is already running...')

            if window.isActive == False:
                pywinauto.application.Application().connect(handle=window._hWnd).top_window().set_focus()
                control = False
        except IndexError as ie:
            pass

        if control: 
            os.startfile(self.game_exe)
            print('Program Starting...')
            time.sleep(20)


        game_started = False
        game_start_count = 1
        while game_started == False:
            if game_start_count > 50:
                print('Game Start Failure...')
                sys.exit(0)

            print(f'Starting game trial {game_start_count}')
            game_start_count += 1

            self.record_screen()
            
            game_icon = cv2.imread(self.game_icon)
            active_screen = cv2.imread(self.active_screen)

            result = cv2.matchTemplate(game_icon, active_screen, self.cv2_image_match_method)
            mn, _, mnLoc, _ = cv2.minMaxLoc(result)

            coordX, coordY = mnLoc
            if mn < 0.005:
                time.sleep(3)

                keyboard.press('1')
                game_started = True

        time.sleep(20)

        game_entered = False
        game_entered_count = 1
        while game_entered == False:
            if game_entered_count > 50:
                print('Game Enter Failure...')
                sys.exit(0)
            print(f'Entering game trial {game_entered_count}...')
            game_entered_count += 1

            self.record_screen()
            loading_page = cv2.imread(self.loading_page)
            active_screen = cv2.imread(self.active_screen)

            result = cv2.matchTemplate(loading_page, active_screen, self.cv2_image_match_method)
            mn, _, mnLoc, _ = cv2.minMaxLoc(result)

            print(mn)
            coordX, coordY = mnLoc
            if mn < 0.005:
                time.sleep(3)

                keyboard.press('2')
                game_started = True

                print('test complete')
                sys.exit(0)
            time.sleep(1)

        time.sleep(20)

        closed_daily_news = False
        closed_daily_news_count = 1
        while closed_daily_news == False:
            if closed_daily_news_count > 10:
                print('No daily news found')
                break
            print(f'Closing daily news trial {closed_daily_news_count}...')
            closed_daily_news_count += 1

            self.record_screen()
            daily_news_screen = cv2.imread(self.daily_news_page)
            active_screen = cv2.imread(self.active_screen)

            result = cv2.matchTemplate(daily_news_screen, active_screen, self.cv2_image_match_method)
            mn, _, mnLoc, _ = cv2.minMaxLoc(result)

            if mn < 0.005:
                time.sleep(3)

                keyboard.press('3')
                closed_daily_news = True

                print('test complete')
                sys.exit(0)
            time.sleep(1)


    def find_level(self):
        pass


    def record_screen(self):
        screenshot = keyboard.screenshot()
        screenshot.save(f'{self.screenshot_dir}\\active-screen.png')

    def play_level(self):
        '''
        L: Choose Level
        B: Ready for battle (X2)
        S: Skip cutscene
        C: Confirm Skip
        '''
        pass


    def validate_game_activity(self):
        user32 = ctypes.windll.user32

        h_wnd = user32.GetForegroundWindow()
        pid = wintypes.DWORD()
        user32.GetWindowThreadProcessId(h_wnd, ctypes.byref(pid))

        p = psutil.Process(pid.value)
        return p.exe() == self.game_exe


    def honkai_driver(self):
        max_rounds = self.stamina // 10
        rounds = 1

        print('Round 1 starting in 10 seconds...')
        time.sleep(10)

        df = pd.DataFrame(columns = ['Round', 'Experience', 'Time Spent', 'Datetime'])

        while rounds <= max_rounds:
            start_time = time.time()
            curr_time = datetime.now().strftime("%d/%m/%Y %H:%M:%S")

            if self.validate_game_activity() == False:
                print(f"[{curr_time}] Honkai Impact program terminated due to validation failure (game program window unfocused).")
                break

            self.play_level()

            print(f"{curr_time} Round {rounds} has completed! [{time.time() - start_time} seconds]")
            df = df.append({'Round': rounds,
                            'Experience': 25,
                            'Time Spent': time.time() - start_time,
                            'Datetime': curr_time},
                            ignore_index=True)

            rounds += 1
        
        print(df.to_string(index=False))


if __name__ == "__main__":
    honkai_impact = HonkaiPlayer(160)
    # honkai_impact.honkai_driver()

    honkai_impact.record_screen()
    honkai_impact.start_game()
import requests
import json
import os
import random
import urllib.parse
from colorama import *
from datetime import datetime, timedelta, timezone
import time
import pytz

wib = pytz.timezone('Asia/Jakarta')

class Fintopio:
    def __init__(self) -> None:
        self.session = requests.Session()
        self.headers = {
            'Accept': 'application/json, text/plain, */*',
            'Accept-Language': 'en-US,en;q=0.9',
            'Cache-Control': 'no-cache',
            'Host': 'fintopio-tg.fintopio.com',
            'Origin': 'https://fintopio-tg.fintopio.com/',
            'Pragma': 'no-cache',
            'Referer': 'https://fintopio-tg.fintopio.com//',
            'Sec-Fetch-Dest': 'empty',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Site': 'same-origin',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36 Edg/128.0.0.0'
        }

    def clear_terminal(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    def log(self, message):
        print(
            f"{Fore.CYAN + Style.BRIGHT}[ {datetime.now().astimezone(wib).strftime('%x %X %Z')} ]{Style.RESET_ALL}"
            f"{Fore.WHITE + Style.BRIGHT} | {Style.RESET_ALL}{message}",
            flush=True
        )

    def welcome(self):
        print(
            f"""
        {Fore.GREEN + Style.BRIGHT}Auto Claim {Fore.BLUE + Style.BRIGHT}Fintopio - BOT
            """
            f"""
        {Fore.GREEN + Style.BRIGHT}Rey? {Fore.YELLOW + Style.BRIGHT}<INI WATERMARK>
            """
        )

    def format_seconds(self, seconds):
        hours, remainder = divmod(seconds, 3600)
        minutes, seconds = divmod(remainder, 60)
        return f"{int(hours):02}:{int(minutes):02}:{int(seconds):02}"

    def load_data(self, query: str):
        query_params = urllib.parse.parse_qs(query)
        query = query_params.get('user', [None])[0]

        if query:
            user_data_json = urllib.parse.unquote(query)
            user_data = json.loads(user_data_json)
            first_name = user_data['first_name']
            return first_name
        else:
            raise ValueError("User data not found in query.")

    def auth_telegram(self, query: str):
        url = f'https://fintopio-tg.fintopio.com/api/auth/telegram?{query}'
        self.headers.update({
            'Content-Type': 'application/json'
        })

        response = self.session.get(url, headers=self.headers)
        if response.status_code == 200:
            return response.json()['token']
        else:
            return None
        
    def user(self, token: str):
        url = 'https://fintopio-tg.fintopio.com/api/hold/fast/init'
        self.headers.update({
            'Authorization': f'Bearer {token}',
            'Content-Type': 'application/json'
        })

        response = self.session.get(url, headers=self.headers)
        if response.status_code == 200:
            return response.json()
        else:
            return None
        
    def daily_checkin(self, token: str):
        url = 'https://fintopio-tg.fintopio.com/api/daily-checkins'
        self.headers.update({
            'Authorization': f'Bearer {token}',
            'Content-Type': 'application/json'
        })

        response = self.session.get(url, headers=self.headers)
        if response.status_code == 200:
            return response.json()
        else:
            return None
        
    def claim_checkin(self, token: str):
        url = 'https://fintopio-tg.fintopio.com/api/daily-checkins'
        self.headers.update({
            'Authorization': f'Bearer {token}',
            'Content-Type': 'application/json'
        })

        response = self.session.post(url, headers=self.headers)
        if response.status_code in [200, 201]:
            return response.json()
        else:
            return None
        
    def destroyed_asteroid(self, token: str, diamond_id: str):
        url = 'https://fintopio-tg.fintopio.com/api/clicker/diamond/complete'
        data = json.dumps({'diamondNumber': diamond_id})
        self.headers.update({
            'Authorization': f'Bearer {token}',
            'Content-Type': 'application/json'
        })

        response = self.session.post(url, headers=self.headers, data=data)
        if response.status_code in [200, 201]:
            return True
        else:
            return False
        
    def farming_state(self, token: str):
        url = 'https://fintopio-tg.fintopio.com/api/farming/state'
        self.headers.update({
            'Authorization': f'Bearer {token}',
            'Content-Type': 'application/json'
        })

        response = self.session.get(url, headers=self.headers)
        if response.status_code == 200:
            return response.json()
        else:
            return None
        
    def start_farming(self, token: str):
        url = 'https://fintopio-tg.fintopio.com/api/farming/farm'
        self.headers.update({
            'Authorization': f'Bearer {token}',
            'Content-Type': 'application/json'
        })

        response = self.session.post(url, headers=self.headers)
        if response.status_code in [200, 201]:
            return response.json()
        else:
            return None
        
    def claim_farming(self, token: str):
        url = 'https://fintopio-tg.fintopio.com/api/farming/claim'
        self.headers.update({
            'Authorization': f'Bearer {token}',
            'Content-Type': 'application/json'
        })

        response = self.session.post(url, headers=self.headers)
        if response.status_code in [200, 201]:
            return response.json()
        else:
            return None
        
    def start_diamond_breath(self, token: str):
        url = 'https://fintopio-tg.fintopio.com/api/games/diamond-breath'
        self.headers.update({
            'Authorization': f'Bearer {token}',
            'Content-Type': 'application/json'
        })

        response = self.session.get(url, headers=self.headers)
        if response.status_code in [200, 201]:
            return response.json()
        else:
            return None
        
    def finish_diamond_breath(self, token: str, seconds: int):
        url = 'https://fintopio-tg.fintopio.com/api/games/diamond-breath'
        data = json.dumps({'seconds':seconds})
        self.headers.update({
            'Authorization': f'Bearer {token}',
            'Content-Type': 'application/json'
        })

        response = self.session.post(url, headers=self.headers, data=data)
        if response.status_code in [200, 201]:
            return response.json()
        else:
            return None
        
    def start_sapce_tapper(self, token: str):
        url = 'https://fintopio-tg.fintopio.com/api/hold/space-tappers/game-settings'
        self.headers.update({
            'Authorization': f'Bearer {token}',
            'Content-Type': 'application/json'
        })

        response = self.session.get(url, headers=self.headers)
        if response.status_code in [200, 201]:
            return response.json()
        else:
            return None
        
    def claim_space_tapper(self, token: str, score: int):
        url = 'https://fintopio-tg.fintopio.com/api/hold/space-tappers/add-new-result'
        data = json.dumps({'score':score})
        self.headers.update({
            'Authorization': f'Bearer {token}',
            'Content-Type': 'application/json'
        })

        response = self.session.post(url, headers=self.headers, data=data)
        if response.status_code in [200, 201]:
            return response.json()
        else:
            return None
        
    def tasks(self, token: str):
        url = 'https://fintopio-tg.fintopio.com/api/hold/tasks'
        self.headers.update({
            'Authorization': f'Bearer {token}',
            'Content-Type': 'application/json'
        })

        response = self.session.get(url, headers=self.headers)
        if response.status_code == 200:
            return response.json()['tasks']
        else:
            return None
        
    def start_tasks(self, token: str, task_id: int):
        url = f'https://fintopio-tg.fintopio.com/api/hold/tasks/{task_id}/start'
        self.headers.update({
            'Authorization': f'Bearer {token}',
            'Content-Type': 'application/json'
        })

        response = self.session.post(url, headers=self.headers)
        if response.status_code in [200, 201]:
            return response.json()
        else:
            return None
        
    def claim_tasks(self, token: str, task_id: int):
        url = f'https://fintopio-tg.fintopio.com/api/hold/tasks/{task_id}/claim'
        self.headers.update({
            'Authorization': f'Bearer {token}',
            'Content-Type': 'application/json'
        })

        response = self.session.post(url, headers=self.headers)
        if response.status_code in [200, 201]:
            return response.json()
        else:
            return None
        
    def question(self):
        while True:
            play_game = input("Auto Play Space Tapper Game? [y/n] -> ").strip().lower()
            if play_game in ["y", "n"]:
                play_game = play_game == "y"
                break
            else:
                print(f"{Fore.RED+Style.BRIGHT}Invalid Input.{Fore.WHITE+Style.BRIGHT} Choose 'y' to play or 'n' to skip.{Style.RESET_ALL}")

        low_point = 0
        max_point = 0
        if play_game:
            while True:
                try:
                    low_point = int(input("Set Low Point [ex: 1-3000]? -> "))
                    if low_point <= 0 or low_point > 3000:
                        print(f"{Fore.RED+Style.BRIGHT}Low Point must be greater than 0 and less than or equal to 3000.{Style.RESET_ALL}")
                        continue

                    max_point = int(input("Set Max Point [ex: 3000]? -> "))
                    if max_point < low_point:
                        print(f"{Fore.RED+Style.BRIGHT}Max Point must be greater than Low Point.{Style.RESET_ALL}")
                    elif max_point > 3000:
                        print(f"{Fore.RED+Style.BRIGHT}Max Point must be less than or equal to 3000.{Style.RESET_ALL}")
                    else:
                        break
                except ValueError:
                    print(f"{Fore.RED+Style.BRIGHT}Invalid input. Enter a number.{Style.RESET_ALL}")
        
        return play_game, low_point, max_point
        
    def process_query(self, query: str, play_game: bool, low_point: int, max_point: int):

        account = self.load_data(query)

        token = self.auth_telegram(query)
        if not token:
            self.log(
                f"{Fore.MAGENTA+Style.BRIGHT}[ Account{Style.RESET_ALL}"
                f"{Fore.WHITE+Style.BRIGHT} {account} {Style.RESET_ALL}"
                f"{Fore.RED+Style.BRIGHT}Query Isn't Valid{Style.RESET_ALL}"
                f"{Fore.MAGENTA+Style.BRIGHT} ]{Style.RESET_ALL}"
            )
            return

        if token:
            user = self.user(token)
            if user:
                self.log(
                    f"{Fore.MAGENTA+Style.BRIGHT}[ Account{Style.RESET_ALL}"
                    f"{Fore.WHITE+Style.BRIGHT} {account} {Style.RESET_ALL}"
                    f"{Fore.MAGENTA+Style.BRIGHT}] [ Balance{Style.RESET_ALL}"
                    f"{Fore.WHITE+Style.BRIGHT} {user['referralData']['balance']} {Style.RESET_ALL}"
                    f"{Fore.MAGENTA+Style.BRIGHT}]{Style.RESET_ALL}"
                )
                time.sleep(1)

                daily_checkin = self.daily_checkin(token)
                if daily_checkin:
                    for checkin in daily_checkin['rewards']:
                        status = checkin['status']

                        if status == 'now':
                            claim = self.claim_checkin(token)
                            if claim and not claim['claimed']:
                                self.log(
                                    f"{Fore.MAGENTA+Style.BRIGHT}[ Check-In{Style.RESET_ALL}"
                                    f"{Fore.WHITE+Style.BRIGHT} Day {daily_checkin['totalDays']} {Style.RESET_ALL}"
                                    f"{Fore.GREEN+Style.BRIGHT}Is Claimed{Style.RESET_ALL}"
                                    f"{Fore.MAGENTA+Style.BRIGHT} ] [ Reward{Style.RESET_ALL}"
                                    f"{Fore.WHITE+Style.BRIGHT} {checkin['reward']} {Style.RESET_ALL}"
                                    f"{Fore.MAGENTA+Style.BRIGHT}]{Style.RESET_ALL}"
                                )
                            else:
                                self.log(
                                    f"{Fore.MAGENTA+Style.BRIGHT}[ Check-In{Style.RESET_ALL}"
                                    f"{Fore.WHITE+Style.BRIGHT} Day {daily_checkin['totalDays']} {Style.RESET_ALL}"
                                    f"{Fore.YELLOW+Style.BRIGHT}Is Already Checkin{Style.RESET_ALL}"
                                    f"{Fore.MAGENTA+Style.BRIGHT} ]{Style.RESET_ALL}"
                                )
                else:
                    self.log(
                        f"{Fore.MAGENTA+Style.BRIGHT}[ Check-In{Style.RESET_ALL}"
                        f"{Fore.RED+Style.BRIGHT} Is None {Style.RESET_ALL}"
                        f"{Fore.MAGENTA+Style.BRIGHT}]{Style.RESET_ALL}"
                    )
                time.sleep(1)

                diamond_state = user['clickerDiamondState']
                diamond_id = diamond_state['diamondNumber']
                state = diamond_state['state']

                if state == 'available':
                    click = self.destroyed_asteroid(token, diamond_id)
                    if click:
                        self.log(
                            f"{Fore.MAGENTA+Style.BRIGHT}[ Asteroid{Style.RESET_ALL}"
                            f"{Fore.GREEN+Style.BRIGHT} Is Destroyed {Style.RESET_ALL}"
                            f"{Fore.MAGENTA+Style.BRIGHT}] [ Reward{Style.RESET_ALL}"
                            f"{Fore.WHITE+Style.BRIGHT} {diamond_state['settings']['totalReward']} {Style.RESET_ALL}"
                            f"{Fore.MAGENTA+Style.BRIGHT}]{Style.RESET_ALL}"
                        )
                    else:
                        self.log(
                            f"{Fore.MAGENTA+Style.BRIGHT}[ Asteroid{Style.RESET_ALL}"
                            f"{Fore.YELLOW+Style.BRIGHT} Isn't Destroyed {Style.RESET_ALL}"
                            f"{Fore.MAGENTA+Style.BRIGHT}]{Style.RESET_ALL}"
                        )
                else:
                    asteroid_time = diamond_state['timings']['nextAt'] / 1000
                    if asteroid_time:
                        next_asteroid_utc = datetime.fromtimestamp(asteroid_time, tz=timezone.utc)
                        next_asteroid_wib = next_asteroid_utc.astimezone(wib).strftime('%x %X %Z')
                    else:
                        next_asteroid_wib = "N/A"

                    self.log(
                        f"{Fore.MAGENTA+Style.BRIGHT}[ Asteroid{Style.RESET_ALL}"
                        f"{Fore.YELLOW+Style.BRIGHT} Is Already Destroyed {Style.RESET_ALL}"
                        f"{Fore.MAGENTA+Style.BRIGHT}] Next Destroy at{Style.RESET_ALL}"
                        f"{Fore.WHITE+Style.BRIGHT} {next_asteroid_wib} {Style.RESET_ALL}"
                        f"{Fore.MAGENTA+Style.BRIGHT}]{Style.RESET_ALL}"
                    )
                time.sleep(1)

                farming = self.farming_state(token)
                if farming:
                    farming_time = farming['timings']['finish']
                    if farming_time:
                        claim_utc = datetime.fromtimestamp(farming_time / 1000, tz=timezone.utc)
                        claim_wib = claim_utc.astimezone(wib).strftime('%x %X %Z')
                    else:
                        claim_wib = "N/A"

                    state = farming['state']
                    if state == 'idling':
                        start = self.start_farming(token)
                        if start:
                            self.log(
                                f"{Fore.MAGENTA+Style.BRIGHT}[ Farming{Style.RESET_ALL}"
                                f"{Fore.GREEN+Style.BRIGHT} Is Started {Style.RESET_ALL}"
                                f"{Fore.MAGENTA+Style.BRIGHT}]{Style.RESET_ALL}"
                            )
                        else:
                            self.log(
                                f"{Fore.MAGENTA+Style.BRIGHT}[ Farming{Style.RESET_ALL}"
                                f"{Fore.RED+Style.BRIGHT} Isn't Started {Style.RESET_ALL}"
                                f"{Fore.MAGENTA+Style.BRIGHT}]{Style.RESET_ALL}"
                            )
                    elif state == 'farmed':
                        claim = self.claim_farming(token)
                        if claim:
                            self.log(
                                f"{Fore.MAGENTA+Style.BRIGHT}[ Farming{Style.RESET_ALL}"
                                f"{Fore.GREEN+Style.BRIGHT} Is Claimed {Style.RESET_ALL}"
                                f"{Fore.MAGENTA+Style.BRIGHT}] [ Reward{Style.RESET_ALL}"
                                f"{Fore.WHITE+Style.BRIGHT} {farming['farmed']} {Style.RESET_ALL}"
                                f"{Fore.MAGENTA+Style.BRIGHT}]{Style.RESET_ALL}"
                            )
                        else:
                            self.log(
                                f"{Fore.MAGENTA+Style.BRIGHT}[ Farming{Style.RESET_ALL}"
                                f"{Fore.RED+Style.BRIGHT} Isn't Claimed {Style.RESET_ALL}"
                                f"{Fore.MAGENTA+Style.BRIGHT}]{Style.RESET_ALL}"
                            )
                        start = self.start_farming(token)
                        if start:
                            self.log(
                                f"{Fore.MAGENTA+Style.BRIGHT}[ Farming{Style.RESET_ALL}"
                                f"{Fore.GREEN+Style.BRIGHT} Is Started {Style.RESET_ALL}"
                                f"{Fore.MAGENTA+Style.BRIGHT}]{Style.RESET_ALL}"
                            )
                        else:
                            self.log(
                                f"{Fore.MAGENTA+Style.BRIGHT}[ Farming{Style.RESET_ALL}"
                                f"{Fore.RED+Style.BRIGHT} Isn't Started {Style.RESET_ALL}"
                                f"{Fore.MAGENTA+Style.BRIGHT}]{Style.RESET_ALL}"
                            )
                    else:
                        self.log(
                            f"{Fore.MAGENTA+Style.BRIGHT}[ Farming{Style.RESET_ALL}"
                            f"{Fore.YELLOW+Style.BRIGHT} Is Already Started {Style.RESET_ALL}"
                            f"{Fore.MAGENTA+Style.BRIGHT}] [ Claim at{Style.RESET_ALL}"
                            f"{Fore.WHITE+Style.BRIGHT} {claim_wib} {Style.RESET_ALL}"
                            f"{Fore.MAGENTA+Style.BRIGHT}]{Style.RESET_ALL}"
                        )
                else:
                    self.log(
                        f"{Fore.MAGENTA+Style.BRIGHT}[ Farming{Style.RESET_ALL}"
                        f"{Fore.RED+Style.BRIGHT} Is None {Style.RESET_ALL}"
                        f"{Fore.MAGENTA+Style.BRIGHT}]{Style.RESET_ALL}"
                    )
                time.sleep(1)

                diamond_breath = self.start_diamond_breath(token)
                if diamond_breath:
                    reward = 3200
                    score = diamond_breath['rewardPerSecond']
                    is_available = diamond_breath['isAvailableGame']
                    if is_available:
                        seconds = reward / score
                        finish = self.finish_diamond_breath(token, seconds)
                        if finish:
                            self.log(
                                f"{Fore.MAGENTA+Style.BRIGHT}[ Diamond Breath{Style.RESET_ALL}"
                                f"{Fore.GREEN+Style.BRIGHT} Is Success {Style.RESET_ALL}"
                                f"{Fore.MAGENTA+Style.BRIGHT}] [ Reward{Style.RESET_ALL}"
                                f"{Fore.WHITE+Style.BRIGHT} {reward} {Style.RESET_ALL}"
                                f"{Fore.MAGENTA+Style.BRIGHT}]{Style.RESET_ALL}"
                            )
                        else:
                            self.log(
                                f"{Fore.MAGENTA+Style.BRIGHT}[ Diamond Breath{Style.RESET_ALL}"
                                f"{Fore.RED+Style.BRIGHT} Isn't Success {Style.RESET_ALL}"
                                f"{Fore.MAGENTA+Style.BRIGHT}]{Style.RESET_ALL}"
                            )
                    else:
                        last_play = datetime.strptime(diamond_breath['lastPlayDate'], "%Y-%m-%dT%H:%M:%S.%fZ")
                        next_play = (last_play.replace(tzinfo=timezone.utc) + timedelta(hours=7)).astimezone(wib).strftime('%x %X %Z')
                        self.log(
                            f"{Fore.MAGENTA+Style.BRIGHT}[ Diamond Breath{Style.RESET_ALL}"
                            f"{Fore.YELLOW+Style.BRIGHT} Not Available {Style.RESET_ALL}"
                            f"{Fore.MAGENTA+Style.BRIGHT}] [ Next Play at{Style.RESET_ALL}"
                            f"{Fore.WHITE+Style.BRIGHT} {next_play} {Style.RESET_ALL}"
                            f"{Fore.MAGENTA+Style.BRIGHT}]{Style.RESET_ALL}"
                        )
                else:
                    self.log(
                        f"{Fore.MAGENTA+Style.BRIGHT}[ Diamond Breath{Style.RESET_ALL}"
                        f"{Fore.RED+Style.BRIGHT} Data Is None {Style.RESET_ALL}"
                        f"{Fore.MAGENTA+Style.BRIGHT}]{Style.RESET_ALL}"
                    )
                time.sleep(1)

                if play_game:
                    score = random.randint(low_point, max_point) * 10
                    space_tapper = self.start_sapce_tapper(token)
                    if space_tapper:
                        claim = self.claim_space_tapper(token, score)
                        if claim:
                            self.log(
                                f"{Fore.MAGENTA+Style.BRIGHT}[ Space Tapper{Style.RESET_ALL}"
                                f"{Fore.GREEN+Style.BRIGHT} Is Finished {Style.RESET_ALL}"
                                f"{Fore.MAGENTA+Style.BRIGHT}] [ Reward{Style.RESET_ALL}"
                                f"{Fore.WHITE+Style.BRIGHT} {score} {Style.RESET_ALL}"
                                f"{Fore.MAGENTA+Style.BRIGHT}]{Style.RESET_ALL}"
                            )
                        else:
                            self.log(
                                f"{Fore.MAGENTA+Style.BRIGHT}[ Space Tapper{Style.RESET_ALL}"
                                f"{Fore.RED+Style.BRIGHT} Isn't Finished {Style.RESET_ALL}"
                                f"{Fore.MAGENTA+Style.BRIGHT}]{Style.RESET_ALL}"
                            )
                    else:
                        self.log(
                            f"{Fore.MAGENTA+Style.BRIGHT}[ Space Tapper{Style.RESET_ALL}"
                            f"{Fore.RED+Style.BRIGHT} Isn't Started {Style.RESET_ALL}"
                            f"{Fore.MAGENTA+Style.BRIGHT}]{Style.RESET_ALL}"
                        )
                else:
                    self.log(
                        f"{Fore.MAGENTA+Style.BRIGHT}[ Space Tapper{Style.RESET_ALL}"
                        f"{Fore.YELLOW+Style.BRIGHT} Is Skipped {Style.RESET_ALL}"
                        f"{Fore.MAGENTA+Style.BRIGHT}]{Style.RESET_ALL}"
                    )
                time.sleep(1)

                tasks = self.tasks(token)
                if tasks:
                    completed = False
                    for task in tasks:
                        task_id = task['id']
                        slug = task['slug']

                        if task and task['status'] == 'available':
                            start = self.start_tasks(token, task_id)
                            if start and start['status'] == 'verified':
                                self.log(
                                    f"{Fore.MAGENTA+Style.BRIGHT}[ Task{Style.RESET_ALL}"
                                    f"{Fore.WHITE+Style.BRIGHT} {slug.upper()} {Style.RESET_ALL}"
                                    f"{Fore.GREEN+Style.BRIGHT}Is Started{Style.RESET_ALL}"
                                    f"{Fore.MAGENTA+Style.BRIGHT} ]{Style.RESET_ALL}"
                                )

                                claim = self.claim_tasks(token, task_id)
                                if claim and claim['status'] == 'completed':
                                    self.log(
                                        f"{Fore.MAGENTA+Style.BRIGHT}[ Task{Style.RESET_ALL}"
                                        f"{Fore.WHITE+Style.BRIGHT} {slug.upper()} {Style.RESET_ALL}"
                                        f"{Fore.GREEN+Style.BRIGHT}Is Claimed{Style.RESET_ALL}"
                                        f"{Fore.MAGENTA+Style.BRIGHT} ] [ Reward{Style.RESET_ALL}"
                                        f"{Fore.WHITE+Style.BRIGHT} {task['rewardAmount']} {Style.RESET_ALL}"
                                        f"{Fore.MAGENTA+Style.BRIGHT}]{Style.RESET_ALL}"
                                    )
                                else:
                                    self.log(
                                        f"{Fore.MAGENTA+Style.BRIGHT}[ Task{Style.RESET_ALL}"
                                        f"{Fore.WHITE+Style.BRIGHT} {slug.upper()} {Style.RESET_ALL}"
                                        f"{Fore.RED+Style.BRIGHT}Isn't Claimed{Style.RESET_ALL}"
                                        f"{Fore.MAGENTA+Style.BRIGHT} ]{Style.RESET_ALL}"
                                    )
                            else:
                                self.log(
                                    f"{Fore.MAGENTA+Style.BRIGHT}[ Task{Style.RESET_ALL}"
                                    f"{Fore.WHITE+Style.BRIGHT} {slug.upper()} {Style.RESET_ALL}"
                                    f"{Fore.RED+Style.BRIGHT}Isn't Started{Style.RESET_ALL}"
                                    f"{Fore.MAGENTA+Style.BRIGHT} ]{Style.RESET_ALL}"
                                )

                        elif task and task['status'] == 'verified':
                            claim = self.claim_tasks(token, task_id)
                            if claim and claim['status'] == 'completed':
                                self.log(
                                    f"{Fore.MAGENTA+Style.BRIGHT}[ Task{Style.RESET_ALL}"
                                    f"{Fore.WHITE+Style.BRIGHT} {slug.upper()} {Style.RESET_ALL}"
                                    f"{Fore.GREEN+Style.BRIGHT}Is Claimed{Style.RESET_ALL}"
                                    f"{Fore.MAGENTA+Style.BRIGHT} ] [ Reward{Style.RESET_ALL}"
                                    f"{Fore.WHITE+Style.BRIGHT} {task['rewardAmount']} {Style.RESET_ALL}"
                                    f"{Fore.MAGENTA+Style.BRIGHT}]{Style.RESET_ALL}"
                                )
                            else:
                                self.log(
                                    f"{Fore.MAGENTA+Style.BRIGHT}[ Task{Style.RESET_ALL}"
                                    f"{Fore.WHITE+Style.BRIGHT} {slug.upper()} {Style.RESET_ALL}"
                                    f"{Fore.RED+Style.BRIGHT}Isn't Claimed{Style.RESET_ALL}"
                                    f"{Fore.MAGENTA+Style.BRIGHT} ]{Style.RESET_ALL}"
                                )
                        else:
                            completed = True

                    if completed:
                        self.log(
                            f"{Fore.MAGENTA+Style.BRIGHT}[ Task{Style.RESET_ALL}"
                            f"{Fore.GREEN+Style.BRIGHT} Is Completed {Style.RESET_ALL}"
                            f"{Fore.MAGENTA+Style.BRIGHT}]{Style.RESET_ALL}"
                        )
                else:
                    self.log(
                        f"{Fore.MAGENTA+Style.BRIGHT}[ Task{Style.RESET_ALL}"
                        f"{Fore.GREEN+Style.BRIGHT} Is Completed {Style.RESET_ALL}"
                        f"{Fore.MAGENTA+Style.BRIGHT}]{Style.RESET_ALL}"
                    )
            else:
                self.log(
                    f"{Fore.MAGENTA+Style.BRIGHT}[ Account{Style.RESET_ALL}"
                    f"{Fore.RED+Style.BRIGHT} Data Is None {Style.RESET_ALL}"
                    f"{Fore.MAGENTA+Style.BRIGHT}]{Style.RESET_ALL}"
                )


    def main(self):
        try:
            with open('query.txt', 'r') as file:
                queries = [line.strip() for line in file if line.strip()]

            play_game, low_point, max_point = self.question()

            while True:
                self.clear_terminal()
                self.welcome()
                self.log(
                    f"{Fore.GREEN + Style.BRIGHT}Account's Total: {Style.RESET_ALL}"
                    f"{Fore.WHITE + Style.BRIGHT}{len(queries)}{Style.RESET_ALL}"
                )
                self.log(f"{Fore.CYAN + Style.BRIGHT}-{Style.RESET_ALL}"*75)

                for query in queries:
                    query = query.strip()
                    if query:
                        self.process_query(query, play_game, low_point, max_point)
                        self.log(f"{Fore.CYAN + Style.BRIGHT}-{Style.RESET_ALL}"*75)
                        time.sleep(3)

                seconds = 1800
                while seconds > 0:
                    formatted_time = self.format_seconds(seconds)
                    print(
                        f"{Fore.CYAN+Style.BRIGHT}[ Wait for{Style.RESET_ALL}"
                        f"{Fore.WHITE+Style.BRIGHT} {formatted_time} {Style.RESET_ALL}"
                        f"{Fore.CYAN+Style.BRIGHT}... ]{Style.RESET_ALL}",
                        end="\r"
                    )
                    time.sleep(1)
                    seconds -= 1

        except KeyboardInterrupt:
            self.log(f"{Fore.RED + Style.BRIGHT}[ EXIT ] Fintopio - BOT{Style.RESET_ALL}")
        except Exception as e:
            self.log(f"{Fore.RED + Style.BRIGHT}An error occurred: {e}{Style.RESET_ALL}")

if __name__ == "__main__":
    bot = Fintopio()
    bot.main()
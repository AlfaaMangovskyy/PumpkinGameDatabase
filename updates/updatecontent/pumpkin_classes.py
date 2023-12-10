import random as r
from enum import Enum
from typing import Any
import json as j
import os
import requests as rq
import json_obfuscator as jobs
import curses

def get_shop() -> dict:
    "Gets the current online shop from GitHub."
    request = rq.get("https://github.com/AlfaaMangovskyy/PumpkinGameDatabase/raw/master/shop_content.json")
    # log(str(j.loads(request.text)) + "\n") #
    return j.loads(request.text)

# curses.init_pair(1, curses.COLOR_RED, curses.COLOR_BLACK)
# curses.init_pair(2, curses.COLOR_GREEN, curses.COLOR_BLACK)
# curses.init_pair(3, curses.COLOR_BLUE, curses.COLOR_BLACK)
# curses.init_pair(4, curses.COLOR_YELLOW, curses.COLOR_BLACK)
# curses.init_pair(5, curses.COLOR_MAGENTA, curses.COLOR_BLACK)
# curses.init_pair(6, curses.COLOR_CYAN, curses.COLOR_BLACK)
# curses.init_pair(7, curses.COLOR_WHITE, curses.COLOR_BLACK)

STARTDIR = "D:/data/Programy/python/Pumpkin/game"

logfile = open(f"{STARTDIR}/log_classes.txt", "a", encoding="utf-8")
def log(text : str):
    logfile.write(str(text) + "\n")
    logfile.flush()

# {"nick": "bluespaniel", "golden_leaves": 100000, "seeds":{}, "crates":[], "pumpkins":[], "challenges":{}, "completed_challenges":[]} #
ACCOUNT_BASE = {"nick": f"USER", "golden_leaves": 0, "seeds":{}, "crates":[], "pumpkins":[], "challenges":{}, "completed_challenges":[]}
CRATE_OPENING_HEADER = "        # Press Any Key to Open! #"

account_name = "bluespaniel"

TYPE_ICONS = {
    "Sunny": "◎",
    "Windy": "~",
    "Rainy": "▽",
    "Snowy": "*",
    "Special": "※",
}

PASSIVEPOWERS = {
    "FOTON_EMISSION" : {
        "TYPE": "Sunny",
        "NAME": "Foton Emission",
    },
    "FOTON_ATTRACTION" : {
        "TYPE": "Sunny",
        "NAME": "Foton Attraction",
    },
    "BULB_LIGHT" : {
        "TYPE": "Sunny",
        "NAME": "Bulb Light",
    },
    "STANDING_STORM" : {
        "TYPE": "Windy",
        "NAME": "Standing Storm",
    },
    "WIND_AMBUSH" : {
        "TYPE": "Windy",
        "NAME": "Wind Ambush",
    },
    "TURBULENCES" : {
        "TYPE": "Windy",
        "NAME": "Turbulences",
    },
    "AUTUMN_WAVES" : {
        "TYPE": "Rainy",
        "NAME": "Autumn Waves",
    },
    "WATERFALL" : {
        "TYPE": "Rainy",
        "NAME": "Waterfall",
    },
    "HYDRO_HEX" : {
        "TYPE": "Rainy",
        "NAME": "Hydro Hex",
    },
}

ACTIVEPOWERS = {
    "LASER_BEAM" : {
        "TYPE" : "Sunny",
        "NAME" : "Laser Beam",
    },
}

def getfile(extpath : str) -> str | None:
    """
    Gets the file from github
    """

    request = rq.get("https://github.com/AlfaaMangovskyy/PumpkinGameDatabase/raw/master/"+extpath)

    if request.status_code == 200:
        return request.text
    else:
        return None

def get_current_challenges() -> dict | None:
    challenge_list = j.loads(getfile("challenges/challenge_list.json"))
    for challenge_name in challenge_list:
        # challenge_file #
        challenge_steps = getfile(f"challenges/{challenge_name}.json")
        file = open(f"{STARTDIR}/challenges/{challenge_name}.json", "w")
        file.write(jobs.obfuscate(challenge_steps))
        file.flush()#[[]]#
        file.close()#[[]]#
def get_challenge(name : str) -> dict:
    "Gets the challenge content from local files."
    file = open(f"{STARTDIR}/game/challenges/{name}.json", "r")
    data = j.loads(jobs.deobfuscate(file.read()))
    file.close()
    return data

def passive_power(name : str) -> dict:
    "Gets the perfect passivepower."
    return PASSIVEPOWERS[name]
def active_power(name : str) -> dict:
    "Gets the perfect activepower."
    return ACTIVEPOWERS[name]

class PumpkinType:
    def normal(self):
        self.type_name = "Normal"
        self.min_points = 15
        self.max_points = 75
        self.min_size = 0.7
        self.max_size = 3.2
        self.golden_odds = 345
        self.powers_passive = [
            passive_power("FOTON_EMISSION"),
            passive_power("FOTON_ATTRACTION"),
            passive_power("WIND_AMBUSH"),
        ]
        self.powers_active = [
            active_power("LASER_BEAM"),
        ]
        return self
    def giant(self):
        self.type_name = "Giant"
        self.min_points = 25
        self.max_points = 85
        self.min_size = 3.0
        self.max_size = 7.8
        self.golden_odds = 345
        self.powers_passive = [
            passive_power("FOTON_EMISSION"),
            passive_power("FOTON_ATTRACTION"),
            passive_power("WIND_AMBUSH"),
        ]
        self.powers_active = [
            active_power("LASER_BEAM"),
        ]
        return self
    def golden(self):
        self.type_name = "Golden"
        self.min_points = 125
        self.max_points = 545
        self.min_size = 0.7
        self.max_size = 3.2
        self.golden_odds = 345
        self.powers_passive = [
            passive_power("BULB_LIGHT"),
        ]
        self.powers_active = [
            active_power("LASER_BEAM"),
        ]
        return self
    def flaming(self):
        self.type_name = "Flaming"
        self.min_points = 100
        self.max_points = 455
        self.min_size = 0.2
        self.max_size = 1.2
        self.golden_odds = 345
        self.powers_passive = [
            passive_power("FOTON_EMISSION"),
            passive_power("FOTON_ATTRACTION"),
            passive_power("WIND_AMBUSH"),
        ]
        self.powers_active = [
            active_power("LASER_BEAM"),
        ]
        return self
    def onion(self):
        self.type_name = "Onion"
        self.min_points = 455
        self.max_points = 1075
        self.min_size = 0.7
        self.max_size = 4.2
        self.golden_odds = 345
        self.powers_passive = [
            passive_power("FOTON_EMISSION"),
            passive_power("FOTON_ATTRACTION"),
            passive_power("WIND_AMBUSH"),
        ]
        self.powers_active = [
            active_power("LASER_BEAM"),
        ]
        return self
    def autumn(self):
        self.type_name = "Autumn"
        self.min_points = 125
        self.max_points = 327
        self.min_size = 3.2
        self.max_size = 3.7
        self.golden_odds = 345
        self.powers_passive = [
            passive_power("FOTON_EMISSION"),
            passive_power("FOTON_ATTRACTION"),
            passive_power("WIND_AMBUSH"),
        ]
        self.powers_active = [
            active_power("LASER_BEAM"),
        ]
        return self
    def winged(self):
        self.type_name = "Winged"
        self.min_points = 345
        self.max_points = 754
        self.min_size = 5.2
        self.max_size = 5.3
        self.golden_odds = 75
        self.powers_passive = [
            passive_power("FOTON_EMISSION"),
            passive_power("FOTON_ATTRACTION"),
            passive_power("WIND_AMBUSH"),
        ]
        self.powers_active = [
            active_power("LASER_BEAM"),
        ]
        return self
    def royal(self):
        self.type_name = "Royal"
        self.min_points = 745
        self.max_points = 1456
        self.min_size = 4.0
        self.max_size = 4.4
        self.golden_odds = 25
        self.powers_passive = [
            passive_power("FOTON_EMISSION"),
            passive_power("FOTON_ATTRACTION"),
            passive_power("WIND_AMBUSH"),
        ]
        self.powers_active = [
            active_power("LASER_BEAM"),
        ]
        return self

def tabulate(string : str, tab : int) -> str:
    if len(string) > tab:
        return string[0:tab-3] + "..."
    return string + " " * (tab - len(string))

class Pumpkin:
    def __init__(self, pumpkin_type : PumpkinType, points : int, size : float, is_golden : bool, power_active : dict, power_passive : dict):
        self.type = pumpkin_type
        self.points = points
        self.size = size
        self.is_golden = is_golden
        self.power_active = power_active
        self.power_passive = power_passive
    def get_graphic(self) -> str:
        x = round(self.size)
        try:
            # log(f"graphics/pumpkin_{x}_{self.type.type_name}.txt\n") #
            pumpkin_graphics_listdir = os.listdir(f"{STARTDIR}/graphics/pumpkins/")
            if f"n_pumpkin_{x}_{self.type.type_name}_{str(self.is_golden).lower()}.pgraphic" in pumpkin_graphics_listdir:
                file = open(f"{STARTDIR}/graphics/pumpkins/n_pumpkin_{x}_{self.type.type_name}_{str(self.is_golden).lower()}.pgraphic", "r", encoding="utf-8")
                graphics = file.read()
                file.close()
            else:
                file = open(f"{STARTDIR}/graphics/pumpkins/pumpkin_{x}_{self.type.type_name}.txt", "r", encoding="utf-8")
                graphics = file.read()
                file.close()
        except:
            return " "
        return graphics
    def showcase(self) -> str:
        "Returns the collection showcase of a pumpkin."
        n = tabulate(f"{self.type.type_name} Pumpkin", 15)
        p = tabulate(f"{self.points} RP", 8)
        s = tabulate(f"{self.size}m", 5)
        x = " ※" if self.is_golden else ""
        e = " " + TYPE_ICONS[self.power_passive["TYPE"]] + " " + TYPE_ICONS[self.power_active["TYPE"]]
        return f"{n} {p} {s}" + x + f" {e}"
    def __repr__(self) -> str:
        return f"\"{self.showcase()}\""

class CrateTypes(Enum):
    CRATE_CASUAL = {
        900 : PumpkinType().normal(),
        99 : PumpkinType().giant(),
        1 : PumpkinType().golden(),
    }
    CRATE_GOLDEN = {
        1 : PumpkinType().golden(),
    }
    CRATE_AUTUMN = {
        5 : PumpkinType().normal(),
        1 : PumpkinType().autumn(),
    }
    CRATE_LUCKY = {
        900 : PumpkinType().normal(),
        99 : PumpkinType().giant(),
        1 : PumpkinType().golden(),
    }
    CRATE_WINGED = {
        5 : PumpkinType().normal(),
        5 : PumpkinType().winged(),
        1 : PumpkinType().golden(),
    }

shop = get_shop()

def pagesplit(source_list : list[Any], page_length : int) -> list[list[Any]]:
    list_copy = source_list.copy()
    if len(list_copy) == 0: return [[]]
    final_list = []
    n = len(list_copy)
    while True:
        if n > page_length:
            n -= page_length
            final_list.append(list_copy[:page_length])
            list_copy = list_copy[page_length:]
        else:
            final_list.append(list_copy)
            break
    return final_list

CRATE_GOLDEN_ODDS = {
    "CASUAL": 1.0,
    "GOLDEN": 0.8,
    "AUTUMN": 0.8,
    "LUCKY": 0.01,
    "WINGED": 0.5,
}

class Crate:
    def __init__(self, crate_type : str, rates : dict[int, PumpkinType]):
        self.rates = rates
        self.type = crate_type
    def open(self) -> Pumpkin:
        # pumpkin_rates = {} #
        pumpkin_fields = []
        for type_rate, pumpkin_type in self.rates.items():
            for i in range(type_rate):
                pumpkin_fields.append(pumpkin_type)
        selected_pumpkin_type : PumpkinType = r.choice(pumpkin_fields)
        created_pumpkin = Pumpkin(selected_pumpkin_type, r.randint(selected_pumpkin_type.min_points, selected_pumpkin_type.max_points), r.randint(selected_pumpkin_type.min_size * 10, selected_pumpkin_type.max_size * 10) / 10, True if r.randint(1, round(shop["goldenrates"]*selected_pumpkin_type.golden_odds*CRATE_GOLDEN_ODDS[self.type])) == 1 else False, r.choice(selected_pumpkin_type.powers_active), r.choice(selected_pumpkin_type.powers_passive))
        return created_pumpkin
    def showcase(self) -> str:
        "Returns a showcase of a crate."
        return tabulate(f"▢ {self.type}", 15)
    def get_graphics(self) -> list[str]:
        "Returns a graphic representation of a crate."
        x = 0
        graphics = []
        while True:
            try:
                # log(f"graphics/crate_{self.type.lower()}_{x}.txt\n") #
                # log(f"{STARTDIR}/graphics/crate_{self.type.lower()}_{x}.txt")
                # log(os.listdir(f"{STARTDIR}/graphics"))
                if not f"n_crate_{self.type.lower()}_{x}.txt" in os.listdir(f"{STARTDIR}/graphics/crates/"): break
                file = open(f"{STARTDIR}/graphics/crates/n_crate_{self.type.lower()}_{x}.txt", "r", encoding="utf-8")
                g = file.read()
                graphics.append(g)
                x += 1
                file.close()
            except:
                # raise
                # log(f"{STARTDIR}/graphics/crate_{self.type.lower()}_{x}.txt")
                break
        if graphics == []: return [" "]
        return graphics

def get_rp(pumpkin : Pumpkin) -> int:
    "Returns the input pumpkin's rp points."
    return pumpkin.points

class Player:
    def __init__(self, nick : str, golden_leaves : int, crates : list[str], pumpkins : list[dict], seeds : dict[str, int], challenges : dict, completed_challenges : list):
        self.nick = nick
        self.n_crates = crates
        self.n_pumpkins = pumpkins
        self.crates = []
        self.pumpkins = []
        self.golden_leaves = golden_leaves
        if len(self.n_crates) > 10: self.n_crates = self.n_crates[0:10]
        for crate_name in self.n_crates:
            # log(str(getattr(CrateTypes, f"CRATE_{crate_name.upper()}").value) + "\n") #
            # log(str(type(getattr(CrateTypes, f"CRATE_{crate_name.upper()}").value)) + "\n") #
            self.crates.append(Crate(crate_name.upper(), getattr(CrateTypes, f"CRATE_{crate_name.upper()}").value))
        for pumpkin_stats in self.n_pumpkins:
            pt = PumpkinType()
            _type = "TYPE"
            _normal = "normal"
            self.pumpkins.append(Pumpkin(getattr(pt, f"{pumpkin_stats.get(_type, _normal).lower()}")(), pumpkin_stats.get("POINTS", 0), pumpkin_stats.get("SIZE", 1.0), pumpkin_stats.get("GOLDEN", False), pumpkin_stats.get("ACTIVE_POWER", {"TYPE": "Sunny", "NAME": "???"}), pumpkin_stats.get("PASSIVE_POWER", {"TYPE": "Sunny", "NAME": "???"})))
        # self.page_sorted_pumpkins = [] #
        # for p in self.pumpkins: #
        self.page_sorted_pumpkins = pagesplit(self.pumpkins, 10)
        self.selected_page = 0
        self.viewed_pumpkin : Pumpkin | None = None
        self.seeds = seeds
        self.challenges = challenges
        self.completed_challenges = completed_challenges
    def open_crate(self, crate_index : int):
        if crate_index > len(self.crates)-1: return None
        crate = self.crates[crate_index]
        del self.n_crates[crate_index]
        del self.crates[crate_index]
        pumpkin : Pumpkin = crate.open()
        self.pumpkins.append(pumpkin)
        self.n_pumpkins.append(self._transform_pumpkin(pumpkin = pumpkin))
        self.page_sorted_pumpkins = pagesplit(self.pumpkins, 10)
        self.add_seeds(pumpkin.type, r.randint(15, 25))
        # log(f"PUMPKINS: {self.pumpkins}\n")
        # log(f"N_PUMPKINS: {self.n_pumpkins}\n")
        # log(f"PAGE_SORTED_PUMPKINS: {self.page_sorted_pumpkins}\n")
        self.dump_data()
        return pumpkin
    def dump_data(self):
        file = open(f"{STARTDIR}/accounts/{account_name}.json", "w", encoding="utf-8")
        player_data["crates"] = self.n_crates
        # player_data["pumpkins"] = self.n_pumpkins #
        player_data["golden_leaves"] = self.golden_leaves
        player_data["seeds"] = self.seeds
        player_data["challenges"] = self.challenges
        player_data["completed_challenges"] = self.completed_challenges
        x = []
        for i in self.pumpkins:
            x.append(self._transform_pumpkin(pumpkin = i))
        player_data["pumpkins"] = x
        d = j.dumps(player_data)
        file.write(jobs.obfuscate(d))
        file.flush()
        file.close()
        return None
    def getpumpkinsort_most_rp(self):
        l = self.pumpkins.copy()
        l.sort(key = get_rp, reverse = True)
        # log(l) #
        self.page_sorted_pumpkins = pagesplit(l, 10)
        # log(type(self.page_sorted_pumpkins)) #
        # log(self.page_sorted_pumpkins) #
        return pagesplit(l, 10)
    def _transform_pumpkin(self, pumpkin : Pumpkin):
        return {"TYPE": pumpkin.type.type_name, "POINTS": pumpkin.points, "SIZE": pumpkin.size, "GOLDEN": pumpkin.is_golden, "PASSIVE_POWER": pumpkin.power_passive, "ACTIVE_POWER": pumpkin.power_active}
    def add_seeds(self, pumpkin_type : PumpkinType, amount : int) -> None:
        if not pumpkin_type.type_name.upper() in self.seeds: self.seeds[pumpkin_type.type_name.upper()] = amount
        else: self.seeds[pumpkin_type.type_name.upper()] += amount
        self.dump_data()
        return None
    def remove_pumpkin(self, pumpkin : Pumpkin):
        self.n_pumpkins.remove(self._transform_pumpkin(pumpkin = pumpkin))
        self.pumpkins = []
        for pumpkin_stats in self.n_pumpkins:
            pt = PumpkinType()
            _type = "TYPE"
            _normal = "normal"
            self.pumpkins.append(Pumpkin(getattr(pt, f"{pumpkin_stats.get(_type, _normal).lower()}")(), pumpkin_stats.get("POINTS", 0), pumpkin_stats.get("SIZE", 1.0), pumpkin_stats.get("GOLDEN", False)))
        self.page_sorted_pumpkins = pagesplit(self.pumpkins, 10)
        return None
    def check_new_challenges(self):
        for challenge_file in os.listdir(f"{STARTDIR}/game/challenges/"):
            challenge_file = challenge_file.removesuffix(".json")
            if not challenge_file in self.challenges:
                self.challenges[challenge_file] = {"STAGE": 0, "PROGRESS": [0, 0, 0]}
    def progress_GET_ANY_PUMPKINS(self):
        for challenge_name, challenge_player_data in self.challenges.items():
            challenge_file = open(f"{STARTDIR}/game/challenges/{challenge_name}.json")
            challenge_data = j.loads(jobs.deobfuscate(challenge_file.read()))
            current_stage = challenge_data["stages"][challenge_player_data["STAGE"]]
            x = 0
            for task in current_stage:
                if task["challenge_type"] == "GET_ANY_PUMPKINS" and challenge_player_data["PROGRESS"][x] != -1:
                    challenge_player_data["PROGRESS"][x] += 1
                    if task["goal"] <= challenge_player_data["PROGRESS"][x]:
                        challenge_player_data["PROGRESS"][x] = -1
                        # self.claim_reward(task["reward"]) #
                        self.dump_data()
                    break
                x += 1
    def claim_reward(self, reward : dict) -> None:
        "Claims a reward from DICTIONARY `dict`."
        DETAILS = "details"
        match reward["type"]:
            case "golden_leaves":
                self.golden_leaves += reward["details"][0]
                self.dump_data()
            case "crates":
                for i in range(reward["details"][1]):
                    self.n_crates.append(reward["details"][0])
                    self.crates.append(Crate(reward["details"][0].upper(), getattr(CrateTypes, f"CRATE_{reward[DETAILS][0].upper()}").value))
                self.dump_data()
            case "pumpkins":
                pumpkintype = PumpkinType()
                getattr(pumpkintype, f"{reward[DETAILS][0].lower()}")()
                pumpkin_points = r.randint(reward[DETAILS][1], reward[DETAILS][2])
                pumpkin_size = r.randint(reward[DETAILS][3] * 10, reward[DETAILS][4] * 10) / 10
                if reward[DETAILS][5] == None:
                    pumpkin_active_power = active_power(reward[DETAILS][5])
                else:
                    pumpkin_active_power = r.choice(pumpkintype.powers_active)
                if reward[DETAILS][6] == None:
                    pumpkin_passive_power = passive_power(reward[DETAILS][6])
                else:
                    pumpkin_passive_power = r.choice(pumpkintype.powers_passive)
                pumpkin_is_golden = reward[DETAILS][7]
                pumpkin = Pumpkin(pumpkintype, pumpkin_points, pumpkin_size, pumpkin_is_golden, pumpkin_active_power, pumpkin_passive_power)
                self.pumpkins.append(pumpkin)
                self.dump_data()

def get_task_desc(task : dict) -> str:
    "Get the text description of a task."
    DETAILS = "details"
    GOAL = "goal"
    match task["challenge_type"]:
        case "GET_PUMPKINS":
            return f"Get {task[GOAL]} {task[DETAILS][0]} Pumpkins."
        case "GET_ANY_PUMPKINS":
            return f"Get {task[GOAL]} of any pumpkin."
        case "OPEN_CRATES":
            return f"Open {task[GOAL]} {task[DETAILS][0].lower()} crates."
        case "OPEN_ANY_CRATES":
            return f"Open {task[GOAL]} of any crate."
        case "INSTANT_CLAIMS":
            return f"Click to claim!"
        case _:
            return f"Unknown task type"

def get_challenge_task_description(data : dict, completion : dict) -> str:
    "Gets the task description."
    # data_challenge_name = data["name"]
    data_current_stage = data["stages"][completion["STAGE"]]
    descriptions = []
    # STAGE = "STAGE"
    # STAGES = "stages"
    for task in data_current_stage:
        descriptions.append(f" // {get_task_desc(task)}")
    return descriptions

class Selector:
    def __init__(self, screen, base_y : int, base_x : int, header : str, options : list[str], _rewrite_clear_range : int):
        self.screen = screen
        self.header = header
        self.options = options
        # log("\n" + str(self.options)) #
        self.base_y = base_y
        self.base_x = base_x
        self.pos = 0
        self._rewrite_clear_range = _rewrite_clear_range
        self.rewrite()
    def reinit(self, screen, base_y : int, base_x : int, header : str, options : list[str], _rewrite_clear_range : int):
        self.screen = screen
        self.header = header
        self.options = options
        # log("\n" + str(self.options)) #
        self.base_y = base_y
        self.base_x = base_x
        self.pos = 0
        self._rewrite_clear_range = _rewrite_clear_range
        self.rewrite()
    def move_up(self):
        if self.pos > 0:
            self.pos -= 1
        self.rewrite()
    def move_down(self):
        if self.pos < len(self.options) - 1:
            self.pos += 1
        self.rewrite()
    def rewrite(self):
        "Rewrites the content of the selection window.s"
        for i in range(self.base_y + 1, self.base_y + self._rewrite_clear_range + 1):
            self.screen.addstr(i, 0, " "*(35+5))
            self.screen.refresh()
        n = -1
        self.screen.addstr(self.base_y, self.base_x, f"{self.header}")
        for option in self.options:
            n += 1
            if n == self.pos:
                self.screen.addstr(self.base_y + n + 1, self.base_x, f"⁂ {option}")
            else:
                self.screen.addstr(self.base_y + n + 1, self.base_x, f"  {option}")
            n += option.count("\n")
        self.screen.refresh()

# class PlainSelector: #
#     def __init__(self, screen, fields : list[list[str]], tabulator ) #

file = open(f"{STARTDIR}/accounts/{account_name}.json", "r", encoding="utf-8")
d = file.read()
player_data = j.loads(jobs.deobfuscate(d))
file.close()
player = Player(player_data["nick"], player_data["golden_leaves"], player_data["crates"], player_data["pumpkins"], player_data["seeds"], player_data["challenges"], player_data["completed_challenges"])
import random as r
from enum import Enum
from typing import Any
import json as j
import os
import requests as rq

def get_shop() -> dict:
    "Gets the current online shop from GitHub."
    request = rq.get("https://github.com/AlfaaMangovskyy/PumpkinGameDatabase/raw/master/shop_content.json")
    # log(str(j.loads(request.text)) + "\n") #
    return j.loads(request.text)

logfile = open("log_classes.txt", "a", encoding="utf-8")
def log(text : str):
    logfile.write(str(text) + "\n")
    logfile.flush()

CRATE_OPENING_HEADER = "        # Press Any Key to Open! #"

account_name = "bluespaniel"

class PumpkinType:
    def normal(self):
        self.type_name = "Normal"
        self.min_points = 15
        self.max_points = 75
        self.min_size = 0.7
        self.max_size = 3.2
        self.golden_odds = 345
        return self
    def giant(self):
        self.type_name = "Giant"
        self.min_points = 25
        self.max_points = 85
        self.min_size = 3.0
        self.max_size = 7.8
        self.golden_odds = 345
        return self
    def golden(self):
        self.type_name = "Golden"
        self.min_points = 125
        self.max_points = 545
        self.min_size = 0.7
        self.max_size = 3.2
        self.golden_odds = 345
        return self
    def flaming(self):
        self.type_name = "Flaming"
        self.min_points = 100
        self.max_points = 455
        self.min_size = 0.2
        self.max_size = 1.2
        self.golden_odds = 345
        return self
    def onion(self):
        self.type_name = "Onion"
        self.min_points = 455
        self.max_points = 1075
        self.min_size = 0.7
        self.max_size = 4.2
        self.golden_odds = 345
        return self
    def autumn(self):
        self.type_name = "Autumn"
        self.min_points = 125
        self.max_points = 327
        self.min_size = 3.2
        self.max_size = 3.7
        self.golden_odds = 345
        return self
    def winged(self):
        self.type_name = "Winged"
        self.min_points = 345
        self.max_points = 754
        self.min_size = 5.2
        self.max_size = 5.3
        self.golden_odds = 75
        return self

def tabulate(string : str, tab : int) -> str:
    if len(string) > tab:
        return string[0:tab-3] + "..."
    return string + " " * (tab - len(string))

class Pumpkin:
    def __init__(self, pumpkin_type : PumpkinType, points : int, size : float, is_golden : bool):
        self.type = pumpkin_type
        self.points = points
        self.size = size
        self.is_golden = is_golden
    def get_graphic(self) -> str:
        x = round(self.size)
        try:
            # log(f"graphics/pumpkin_{x}_{self.type.type_name}.txt\n") #
            file = open(f"graphics/pumpkin_{x}_{self.type.type_name}.txt", "r", encoding="utf-8")
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
        return f"{n} {p} {s}" + x
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
        created_pumpkin = Pumpkin(selected_pumpkin_type, r.randint(selected_pumpkin_type.min_points, selected_pumpkin_type.max_points), r.randint(selected_pumpkin_type.min_size * 10, selected_pumpkin_type.max_size * 10) / 10, True if r.randint(1, round(shop["goldenrates"]*selected_pumpkin_type.golden_odds*CRATE_GOLDEN_ODDS[self.type])) == 1 else False)
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
                if not f"crate_{self.type.lower()}_{x}.txt" in os.listdir("graphics"): break
                file = open(f"graphics/crate_{self.type.lower()}_{x}.txt", "r", encoding="utf-8")
                g = file.read()
                graphics.append(g)
                x += 1
                file.close()
            except:
                break
        if graphics == []: return [" "]
        return graphics

def get_rp(pumpkin : Pumpkin) -> int:
    "Returns the input pumpkin's rp points."
    return pumpkin.points

class Player:
    def __init__(self, nick : str, golden_leaves : int, crates : list[str], pumpkins : list[dict], seeds : dict[str, int]):
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
            self.pumpkins.append(Pumpkin(getattr(pt, f"{pumpkin_stats.get(_type, _normal).lower()}")(), pumpkin_stats.get("POINTS", 0), pumpkin_stats.get("SIZE", 1.0), pumpkin_stats.get("GOLDEN", False)))
        # self.page_sorted_pumpkins = [] #
        # for p in self.pumpkins: #
        self.page_sorted_pumpkins = pagesplit(self.pumpkins, 10)
        self.selected_page = 0
        self.viewed_pumpkin : Pumpkin | None = None
        self.seeds = seeds
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
        file = open(f"accounts/{account_name}.json", "w", encoding="utf-8")
        player_data["crates"] = self.n_crates
        # player_data["pumpkins"] = self.n_pumpkins #
        player_data["golden_leaves"] = self.golden_leaves
        player_data["seeds"] = self.seeds
        x = []
        for i in self.pumpkins:
            x.append(self._transform_pumpkin(pumpkin = i))
        player_data["pumpkins"] = x
        j.dump(player_data, file)
        file.close()
        return None
    def getpumpkinsort_most_rp(self):
        l = self.pumpkins.copy()
        l.sort(key = get_rp, reverse = True)
        log(l)
        self.page_sorted_pumpkins = pagesplit(l, 10)
        # log(type(self.page_sorted_pumpkins)) #
        # log(self.page_sorted_pumpkins) #
        return pagesplit(l, 10)
    def _transform_pumpkin(self, pumpkin : Pumpkin):
        return {"TYPE": pumpkin.type.type_name, "POINTS": pumpkin.points, "SIZE": pumpkin.size, "GOLDEN": pumpkin.is_golden}
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
        self.screen.refresh()

# class PlainSelector: #
#     def __init__(self, screen, fields : list[list[str]], tabulator ) #

file = open(f"accounts/{account_name}.json", "r", encoding="utf-8")
player_data = j.load(file)
file.close()
player = Player(player_data["nick"], player_data["golden_leaves"], player_data["crates"], player_data["pumpkins"], player_data["seeds"])
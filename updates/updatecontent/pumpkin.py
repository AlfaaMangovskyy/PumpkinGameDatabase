import curses
from pumpkin_classes import *
from enum import Enum
from time import sleep

LOGO = '''
  #####  #   #  #   #  #####  #  #  #  #   #
  #   #  #   #  ## ##  #   #  # #   #  ##  #
  #####  #   #  # # #  #####  ##    #  # # #
  #      #   #  #   #  #      # #   #  #  ##
  #      #####  #   #  #      #  #  #  #   #
'''

# A TOTALLY NEW RELEASE! #

KEY_UP = 259
KEY_DOWN = 258
KEY_ENTER = 10
KEY_ESCAPE1 = 279
KEY_ESCAPE2 = 27
KEY_DELETE = 330

STARTDIR = "D:/data/Programy/python/Pumpkin/game"

# shop = get_shop() #

logfile = open(f"{STARTDIR}/log.txt", "a")
def log(text : str):
    logfile.write(str(text) + "\n")
    logfile.flush()

# bannerfile = open(f"{STARTDIR}/graphics/shopbanner.pgraphic", "r", encoding="utf-8")
# BANNER = bannerfile.read()
# bannerfile.close()

class ScreenTypes(Enum):
    MAINMENU = "MAINMENU"
    COLLECTION = "COLLECTION"
    CRATES = "CRATES"
    SHOP = "SHOP"
    PUMPKIN_VIEW = "PUMPKIN_VIEW"
    CHALLENGES = "CHALLENGES"

selected_screen = ScreenTypes.MAINMENU
shop_pos = 0

def app(screen):
    global selected_screen
    screen.clear()
    screen.addstr(0, 2, LOGO)
    screen.addstr(7, 2, "A pumpkin collecting game")
    curses.init_pair(11, curses.COLOR_BLACK, curses.COLOR_YELLOW)
    GOLDENCOLORPAIR = curses.color_pair(11)
    curses.init_pair(12, curses.COLOR_YELLOW, curses.COLOR_BLACK)
    GOLDENPUMPKINCOLORPAIR = curses.color_pair(12)
    curses.init_pair(21, curses.COLOR_RED, curses.COLOR_BLACK)
    curses.init_pair(22, curses.COLOR_GREEN, curses.COLOR_BLACK)
    curses.init_pair(23, curses.COLOR_BLUE, curses.COLOR_BLACK)
    curses.init_pair(24, curses.COLOR_YELLOW, curses.COLOR_BLACK)
    curses.init_pair(25, curses.COLOR_MAGENTA, curses.COLOR_BLACK)
    curses.init_pair(26, curses.COLOR_CYAN, curses.COLOR_BLACK)
    curses.init_pair(27, curses.COLOR_WHITE, curses.COLOR_BLACK)
    def get_colour(id : int):
        return curses.color_pair(id)
    def place_coloured_graphic(screen, y, x, data : list) -> None:
        line_add = 0
        pos_add = 0
        for line in data:
            pos_add = 0
            for char, colour in line:
                screen.addstr(y + line_add, x + pos_add, char, get_colour(20 + colour))
                pos_add += 1
            line_add += 1
        screen.refresh()
    def coloured_graphic(screen, y, x, filename : str) -> None:
        f"Places the coloured graphic read from the file in `filename` on `screen`'s `x` and `y`."
        file = open(f"{STARTDIR}/graphics/{filename}", encoding="utf-8")
        data = j.load(file)
        file.close()
        place_coloured_graphic(screen, y, x, data)
    # get_current_challenges()
    shop_pos = 0
    while True:
        screen.refresh()
        if selected_screen == ScreenTypes.MAINMENU:
            screen.clear()
            screen.addstr(0, 2, LOGO)
            screen.addstr(7, 2, "A pumpkin collecting game")
            mainscreen_selector = Selector(screen = screen, base_y = 9, base_x = 2, header = "Select an action:", options = ["Collection", "Crates", "Shop", "Challenges"], _rewrite_clear_range = 3)
            # screen.refresh() #
            # screen.getch() #
            while True:
                key = screen.getch()
                if key == KEY_UP:
                    mainscreen_selector.move_up()
                elif key == KEY_DOWN:
                    mainscreen_selector.move_down()
                elif key == KEY_ENTER:
                    break
            match mainscreen_selector.pos:
                case 0:
                    # COLLECTION #
                    selected_screen = ScreenTypes.COLLECTION
                    continue
                case 1:
                    # CRATES #
                    selected_screen = ScreenTypes.CRATES
                    continue
                case 2:
                    # SHOP #
                    selected_screen = ScreenTypes.SHOP
                    continue
                case 3:
                    # CHALLENGES #
                    selected_screen = ScreenTypes.CHALLENGES
                    continue
        elif selected_screen == ScreenTypes.COLLECTION:
            player.getpumpkinsort_most_rp()
            screen.clear()
            screen.addstr(2, 2, f"⁂⁂⁂⁂ Your Pumpkin Collection ⁂⁂⁂⁂")
            screen.addstr(3, 2, f"You own {len(player.pumpkins)} pumpkins for now.")
            screen.addstr(0, 2, "<= Back to main menu: ESCAPE")
            if len(player.pumpkins) == 0:
                screen.addstr(4, 2, f"No pumpkins? Claim your first ones by opening free crates in the store!")
                screen.refresh()
                while True:
                    key = screen.getch()
                    # log(str(key) + "\n") #
                    if key in (KEY_ESCAPE1, KEY_ESCAPE2):
                        selected_screen = ScreenTypes.MAINMENU
                        break
                    screen.refresh()
                screen.refresh()
                continue
            while True:
                if not selected_screen == ScreenTypes.COLLECTION: break
                screen.clear()
                screen.addstr(2, 2, f"⁂⁂⁂⁂ Your Pumpkin Collection ⁂⁂⁂⁂")
                screen.addstr(3, 2, f"You own {len(player.pumpkins)} pumpkins for now.")
                screen.addstr(0, 2, "<= Back to main menu: ESCAPE")
                pumpkin_selector = Selector(screen, 5, 3, f"Page {player.selected_page+1}/{len(player.page_sorted_pumpkins)}", [p.showcase() for p in player.page_sorted_pumpkins[player.selected_page]], 10)
                while True:
                    key = screen.getch()
                    # log("####################################################\n")
                    # log("\n".join([p.showcase() for p in player.page_sorted_pumpkins[player.selected_page]]))
                    # log(str(key) + "\n") #
                    if key == KEY_UP:
                        if pumpkin_selector.pos == 0:
                            if player.selected_page == 0: continue
                            player.selected_page -= 1
                            pumpkin_selector.reinit(screen, 5, 3, f"Page {player.selected_page+1}/{len(player.page_sorted_pumpkins)}", [p.showcase() for p in player.page_sorted_pumpkins[player.selected_page]], 10)
                            pumpkin_selector.pos = 9
                            pumpkin_selector.rewrite()
                            # break #
                            continue
                        pumpkin_selector.move_up()
                    elif key == KEY_DOWN:
                        if pumpkin_selector.pos == 9:
                            if player.selected_page == len(player.page_sorted_pumpkins)-1: continue
                            player.selected_page += 1
                            pumpkin_selector.reinit(screen, 5, 3, f"Page {player.selected_page+1}/{len(player.page_sorted_pumpkins)}", [p.showcase() for p in player.page_sorted_pumpkins[player.selected_page]], 10)
                            pumpkin_selector.pos = 0
                            pumpkin_selector.rewrite()
                            # break #
                            continue
                        pumpkin_selector.move_down()
                    elif key == KEY_ENTER:
                        # player.viewed_pumpkin = pumpkin_selector.pos + 10 * player.selected_page #
                        player.viewed_pumpkin = player.page_sorted_pumpkins[player.selected_page][pumpkin_selector.pos]
                        selected_screen = ScreenTypes.PUMPKIN_VIEW
                        break #
                    elif key in (KEY_ESCAPE1, KEY_ESCAPE2):
                        selected_screen = ScreenTypes.MAINMENU
                        break #
                    elif key == KEY_DELETE:
                        screen.addstr(4, 3, "Are you sure you want to transfer this pumpkin? ANY KEY to cancel, DELETE to continue")
                        if screen.getch() == KEY_DELETE:
                            # player.pumpkins #
                            del player.page_sorted_pumpkins[player.selected_page][pumpkin_selector.pos]
                            del player.n_pumpkins[player.selected_page*10+pumpkin_selector.pos]
                            # continue #
                            selected_screen = ScreenTypes.COLLECTION
                        else: continue
        elif selected_screen == ScreenTypes.PUMPKIN_VIEW:
            screen.clear()
            screen.addstr(0, 2, "<= Back to pumpkin collection: ESCAPE")
            # graphic = player.viewed_pumpkin.get_graphic().replace("\n", "\n  ") #
            log(f"pumpkins/n_pumpkin_{round(player.viewed_pumpkin.size)}_{player.viewed_pumpkin.type.type_name}_{str(player.viewed_pumpkin.is_golden).lower()}.pgraphic")
            if not player.viewed_pumpkin.is_golden:
                coloured_graphic(screen, 2, 2, f"pumpkins/n_pumpkin_{round(player.viewed_pumpkin.size)}_{player.viewed_pumpkin.type.type_name}_{str(player.viewed_pumpkin.is_golden).lower()}.pgraphic")
            else:
                coloured_graphic(screen, 2, 2, f"pumpkins/n_pumpkin_{round(player.viewed_pumpkin.size)}_{player.viewed_pumpkin.type.type_name}_{str(player.viewed_pumpkin.is_golden).lower()}.pgraphic")
            if not player.viewed_pumpkin.is_golden:
                screen.addstr(2, 23, f"{player.viewed_pumpkin.type.type_name} Pumpkin")
            else:
                screen.addstr(2, 23, f"{player.viewed_pumpkin.type.type_name} Pumpkin", GOLDENPUMPKINCOLORPAIR)
            screen.addstr(3, 23, f"⁂ {player.viewed_pumpkin.points} RP ⁂")
            screen.addstr(5, 23, f"◌ {player.viewed_pumpkin.size}m")
            screen.addstr(7, 23, f"| {player.viewed_pumpkin.type.type_name[0].upper() + player.viewed_pumpkin.type.type_name[1:].lower()} Pumpkin Seeds")
            screen.addstr(8, 23, f"| ⁘ {player.seeds[player.viewed_pumpkin.type.type_name.upper()]}")
            TYPE = "TYPE"
            NAME = "NAME"
            screen.addstr(10, 23, f"ACTIVE POWER  | {TYPE_ICONS[player.viewed_pumpkin.power_active[TYPE]]} {player.viewed_pumpkin.power_active[NAME]}")
            screen.addstr(11, 23, f"PASSIVE POWER | {TYPE_ICONS[player.viewed_pumpkin.power_passive[TYPE]]} {player.viewed_pumpkin.power_passive[NAME]}")
            screen.refresh()
            actions = [f"| UPGRADE       ⁘{round(player.viewed_pumpkin.points / 100)}", f"| TRANSFER      + ⁘3"]
            if player.viewed_pumpkin.type.type_name == "Golden" and not player.viewed_pumpkin.is_golden:
                actions.append(f"| GOLDEN COVER  ₡1000")
            action_selector = Selector(screen, 14, 23, f"Actions:", actions, 5)
            while True:
                key = screen.getch()
                # log(key)
                # log(selected_screen)
                if key in (KEY_ESCAPE1, KEY_ESCAPE2):
                    selected_screen = ScreenTypes.COLLECTION
                    break
                elif key == KEY_UP:
                    action_selector.move_up()
                    continue
                elif key == KEY_DOWN:
                    action_selector.move_down()
                    continue
                elif key == KEY_ENTER:
                    break
            if selected_screen != ScreenTypes.PUMPKIN_VIEW: continue
            match action_selector.pos:
                case 0:
                    if player.seeds[player.viewed_pumpkin.type.type_name.upper()] >= round(player.viewed_pumpkin.points / 100):
                        player.seeds[player.viewed_pumpkin.type.type_name.upper()] -= round(player.viewed_pumpkin.points / 100)
                        player.viewed_pumpkin.points += round(player.viewed_pumpkin.points / 100)
                        player.dump_data()
                        screen.addstr(1, 23, f"⁘ PUMPKIN UPGRADED! Any key to continue...")
                        screen.refresh()
                        screen.getch()
                        screen.addstr(1, 23, f" "*42)
                        screen.refresh()
                    else:
                        screen.addstr(1, 23, f"⁘ You don't have enough seeds! Any key to continue...")
                        screen.refresh()
                        screen.getch()
                        screen.addstr(1, 23, f" "*53)
                        screen.refresh()
                case 1:
                    screen.addstr(1, 23, f"⁐ Do you really want to transfer this pumpkin? ENTER/ESC...")
                    screen.refresh()
                    breakout = False
                    while True:
                        key = screen.getch()
                        if key in (KEY_ESCAPE1, KEY_ESCAPE2):
                            breakout = True
                            break
                        elif key == KEY_ENTER:
                            breakout = False
                            break
                        else:
                            breakout = False
                            continue
                    if breakout: continue
                    else:
                        player.seeds[player.viewed_pumpkin.type.type_name.upper()] += 3
                        player.remove_pumpkin(player.viewed_pumpkin)
                        player.dump_data()
                        selected_screen = ScreenTypes.COLLECTION
                        continue
                case 2:
                    match player.viewed_pumpkin.type.type_name.upper():
                        case "GOLDEN":
                            if player.golden_leaves < 1000:
                                screen.addstr(1, 23, f"⁐ You don't have enough golden leaves! Any key to continue...")
                                screen.refresh()
                                screen.getch()
                                screen.addstr(1, 23, f" "*61)
                                screen.refresh()
                                continue
                            screen.addstr(1, 23, f"⁐ Are you sure you want to cover the pumpkin in gold? ENTER/ESC...")
                            screen.refresh()
                            breakout = False
                            while True:
                                key = screen.getch()
                                if key in (KEY_ESCAPE1, KEY_ESCAPE2):
                                    breakout = True
                                    break
                                elif key == KEY_ENTER:
                                    breakout = False
                                    break
                                else:
                                    breakout = False
                                    continue
                            if breakout: continue
                            else:
                                player.viewed_pumpkin.is_golden = True
                                player.golden_leaves -= 1000
                                player.dump_data()
                                continue
            continue
        elif selected_screen == ScreenTypes.CRATES:
            screen.clear()
            screen.addstr(0, 2, "<= Back to main menu: ESCAPE")
            screen.addstr(2, 2, f"⁂⁂⁂⁂ YOUR CRATES ⁂⁂⁂⁂")
            crate_selector = Selector(screen, 3, 2, f"Storage: {len(player.crates)}/10", [x.showcase() for x in player.crates], 10)
            while True:
                crate_selector.rewrite()
                key = screen.getch()
                # log(f"KEY: {key}\n") #
                if key == KEY_UP:
                    crate_selector.move_up()
                elif key == KEY_DOWN:
                    crate_selector.move_down()
                elif key == KEY_ENTER:
                    if len(crate_selector.options) == 0: continue
                    break
                elif key in (KEY_ESCAPE1, KEY_ESCAPE2):
                    selected_screen = ScreenTypes.MAINMENU
                    break
            screen.refresh()
            # log("BROKEN OUT!\n") #
            if selected_screen != ScreenTypes.CRATES: log("BACK TO MAIN MENU!");continue#break#
            selected_crate : Crate = player.crates[crate_selector.pos] #
            graphics = selected_crate.get_graphics()
            # log(graphics) #
            screen.clear()
            screen.addstr(2, 0, CRATE_OPENING_HEADER)
            place_coloured_graphic(screen, 4, 0, graphics[0])
            screen.addstr(0, 0, "<= CANCEL: ESCAPE")
            screen.refresh()
            if screen.getch() in (KEY_ESCAPE1, KEY_ESCAPE2): continue
            pumpkin : Pumpkin = player.open_crate(crate_selector.pos) #
            for g in graphics[1:]:
                screen.clear()
                place_coloured_graphic(screen, 4, 0, g)
                screen.refresh()
                sleep(0.2)
            sleep(0.3)
            screen.clear()
            if not pumpkin.is_golden:
                place_coloured_graphic(screen, 4, 10, pumpkin.get_graphic())
            else:
                place_coloured_graphic(screen, 4, 10, pumpkin.get_graphic())
            screen.refresh()
            sleep(1.00)
            screen.clear()
            screen.refresh()
            continue
        elif selected_screen == ScreenTypes.SHOP:
            screen.clear()
            screen.addstr(0, 2, f"<= Back to main menu: ESCAPE                ₡ {player.golden_leaves}")
            coloured_graphic(screen, 2, 0, f"shopbanner.pgraphic")
            screen.addstr(8, 2, f"₡₡₡₡ SHOP ₡₡₡₡")
            screen.refresh()
            shop_selector_special = Selector(screen, 10, 2, "Offers:", [f"₡{x[2]} " + x[0] for x in shop["special"]], 10)
            shop_selector_special.pos = shop_pos
            while True:
                key = screen.getch()
                if key == KEY_UP:
                    shop_selector_special.move_up()
                    shop_pos = shop_selector_special.pos
                elif key == KEY_DOWN:
                    shop_selector_special.move_down()
                    shop_pos = shop_selector_special.pos
                elif key == KEY_ENTER:
                    # pass #
                    shop_pos = shop_selector_special.pos
                    break
                elif key in (KEY_ESCAPE1, KEY_ESCAPE2):
                    selected_screen = ScreenTypes.MAINMENU
                    shop_pos = shop_selector_special.pos
                    break
                shop_selector_special.rewrite()
            if selected_screen != ScreenTypes.SHOP: continue
            # BUYING STUFF #
            selected_offer = shop["special"][shop_selector_special.pos]
            if player.golden_leaves >= selected_offer[2] and not len(player.crates) == 10:
                player.golden_leaves -= selected_offer[2]
                player.n_crates.append(selected_offer[1])
                player.crates.append(Crate(selected_offer[1].upper(), getattr(CrateTypes, f"CRATE_{selected_offer[1].upper()}").value))
                player.dump_data()
                screen.addstr(9, 2, f"₡ PURCHASE SUCCESSFULL! Any key to continue... ₡")
                screen.refresh()
                screen.getch()
                screen.addstr(9, 2, f" " * 25)
                continue
            elif len(player.crates) == 10:
                screen.addstr(9, 2, f"You have maximum amount of crates!")
                screen.refresh()
                sleep(1.00)
                screen.addstr(9, 2, f" " * 25)
                continue
            else:
                screen.addstr(9, 2, f"You don't have enough golden leaves!")
                screen.refresh()
                sleep(1.00)
                screen.addstr(9, 2, f" " * 25)
                continue
        elif selected_screen == ScreenTypes.CHALLENGES:
            get_current_challenges()
            screen.clear()
            screen.addstr(0, 2, f"<= Back to main menu: ESCAPE")
            screen.addstr(2, 2, f"⇉ CHALLENGES ⇇")
            screen.refresh()
            player.check_new_challenges()
            challenge_selector = Selector(screen, 4, 2, "~  Current Challenges:  ~")
            while True:
                key = screen.getch()
                if key in (KEY_ESCAPE1, KEY_ESCAPE2):
                    selected_screen = ScreenTypes.MAINMENU
                    break
                else:
                    continue
            if selected_screen != ScreenTypes.CHALLENGES: continue
            # player.sus() #

curses.wrapper(app)
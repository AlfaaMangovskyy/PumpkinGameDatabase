CHARTABLES = {
    "a": "XAA",
    "b": "NBA",
    "c": "VCA",
    "d": "XJA",
    "e": "KLA",
    "f": "NUA",
    "g": "WEA",
    "h": "RTA",
    "i": "GYA",
    "j": "RYA",
    "k": "RNA",
    "l": "QWA",
    "m": "EWA",
    "n": "EQA",
    "o": "QEA",
    "p": "TYA",
    "q": "UUA",
    "r": "IOA",
    "s": "PAA",
    "t": "SNA",
    "u": "MQA",
    "v": "QVA",
    "w": "YYA",
    "x": "TGA",
    "y": "FFA",
    "z": "UYA",
    "A": "XAB",
    "B": "NBB",
    "C": "VCB",
    "D": "XJB",
    "E": "KLB",
    "F": "NUB",
    "G": "WEB",
    "H": "RTB",
    "I": "GYB",
    "J": "RYB",
    "K": "RNB",
    "L": "QWB",
    "M": "EWB",
    "N": "EQB",
    "O": "QEB",
    "P": "TYB",
    "Q": "UUB",
    "R": "IOB",
    "S": "PAB",
    "T": "SNB",
    "U": "MQB",
    "V": "QVB",
    "W": "YYB",
    "X": "TGB",
    "Y": "FFB",
    "Z": "UYB",
    "0": "YE",
    "1": "RK",
    "2": "LL",
    "3": "QX",
    "4": "XX",
    "5": "NY",
    "6": "TR",
    "7": "EA",
    "8": "AE",
    "9": "RE",
    "\"": "GF",
    "'": "GT",
    "{": "AK",
    "}": "BK",
    "[": "AY",
    "]": "BY",
    "!": "NT",
    ":": "RR",
    ",": "YT",
    ".": "YU",
    " ": "NG",
    "\n": "NL",
    "_": "YBZ",
}
CHARTABLES_DEOBFUSCATE = {v : k for k, v in CHARTABLES.items()}

def obfuscate(string : str) -> str:
    "Obfuscates the string."
    obf = ""
    for char in string:
        obf += CHARTABLES.get(char, "YF") + "D"
    return obf.removesuffix("D")
def deobfuscate(string : str) -> str:
    "Deobfuscates the string."
    deobf = ""
    for charcombinations in string.split("D"):
        deobf += CHARTABLES_DEOBFUSCATE.get(charcombinations, "?")
    return deobf

if __name__ == "__main__":
    while True:
        print(obfuscate(input(" -=> * <=- ")))
    # print(obfuscate("{\"nick\": \"BlueSpanielProgramming\", \"golden_leaves\": 17400, \"seeds\": {\"NORMAL\": 210, \"GOLDEN\": 19, \"WINGED\": 82, \"ROYAL\": 1}, \"crates\": [], \"pumpkins\": [{\"TYPE\": \"Golden\", \"POINTS\": 329, \"SIZE\": 1.9, \"GOLDEN\": false}, {\"TYPE\": \"Winged\", \"POINTS\": 465, \"SIZE\": 5.3, \"GOLDEN\": false}, {\"TYPE\": \"Winged\", \"POINTS\": 585, \"SIZE\": 5.2, \"GOLDEN\": false}, {\"TYPE\": \"Winged\", \"POINTS\": 375, \"SIZE\": 5.2, \"GOLDEN\": false}, {\"TYPE\": \"Winged\", \"POINTS\": 359, \"SIZE\": 5.3, \"GOLDEN\": false}, {\"TYPE\": \"Winged\", \"POINTS\": 492, \"SIZE\": 5.3, \"GOLDEN\": false}, {\"TYPE\": \"Golden\", \"POINTS\": 409, \"SIZE\": 2.0, \"GOLDEN\": true}, {\"TYPE\": \"Golden\", \"POINTS\": 127, \"SIZE\": 3.0, \"GOLDEN\": false}, {\"TYPE\": \"Winged\", \"POINTS\": 857, \"SIZE\": 5.3, \"GOLDEN\": false}, {\"TYPE\": \"Winged\", \"POINTS\": 585, \"SIZE\": 5.3, \"GOLDEN\": false}, {\"TYPE\": \"Winged\", \"POINTS\": 651, \"SIZE\": 5.2, \"GOLDEN\": false}, {\"TYPE\": \"Winged\", \"POINTS\": 681, \"SIZE\": 5.2, \"GOLDEN\": false}, {\"TYPE\": \"Golden\", \"POINTS\": 182, \"SIZE\": 2.6, \"GOLDEN\": false}, {\"TYPE\": \"Winged\", \"POINTS\": 480, \"SIZE\": 5.2, \"GOLDEN\": false}, {\"TYPE\": \"Royal\", \"POINTS\": 2194, \"SIZE\": 4.2, \"GOLDEN\": true}, {\"TYPE\": \"Winged\", \"POINTS\": 698, \"SIZE\": 5.2, \"GOLDEN\": false}]}"))
    # print(deobfuscate(obfuscate("{\"nick\": \"BlueSpanielProgramming\", \"golden_leaves\": 17400, \"seeds\": {\"NORMAL\": 210, \"GOLDEN\": 19, \"WINGED\": 82, \"ROYAL\": 1}, \"crates\": [], \"pumpkins\": [{\"TYPE\": \"Golden\", \"POINTS\": 329, \"SIZE\": 1.9, \"GOLDEN\": false}, {\"TYPE\": \"Winged\", \"POINTS\": 465, \"SIZE\": 5.3, \"GOLDEN\": false}, {\"TYPE\": \"Winged\", \"POINTS\": 585, \"SIZE\": 5.2, \"GOLDEN\": false}, {\"TYPE\": \"Winged\", \"POINTS\": 375, \"SIZE\": 5.2, \"GOLDEN\": false}, {\"TYPE\": \"Winged\", \"POINTS\": 359, \"SIZE\": 5.3, \"GOLDEN\": false}, {\"TYPE\": \"Winged\", \"POINTS\": 492, \"SIZE\": 5.3, \"GOLDEN\": false}, {\"TYPE\": \"Golden\", \"POINTS\": 409, \"SIZE\": 2.0, \"GOLDEN\": true}, {\"TYPE\": \"Golden\", \"POINTS\": 127, \"SIZE\": 3.0, \"GOLDEN\": false}, {\"TYPE\": \"Winged\", \"POINTS\": 857, \"SIZE\": 5.3, \"GOLDEN\": false}, {\"TYPE\": \"Winged\", \"POINTS\": 585, \"SIZE\": 5.3, \"GOLDEN\": false}, {\"TYPE\": \"Winged\", \"POINTS\": 651, \"SIZE\": 5.2, \"GOLDEN\": false}, {\"TYPE\": \"Winged\", \"POINTS\": 681, \"SIZE\": 5.2, \"GOLDEN\": false}, {\"TYPE\": \"Golden\", \"POINTS\": 182, \"SIZE\": 2.6, \"GOLDEN\": false}, {\"TYPE\": \"Winged\", \"POINTS\": 480, \"SIZE\": 5.2, \"GOLDEN\": false}, {\"TYPE\": \"Royal\", \"POINTS\": 2194, \"SIZE\": 4.2, \"GOLDEN\": true}, {\"TYPE\": \"Winged\", \"POINTS\": 698, \"SIZE\": 5.2, \"GOLDEN\": false}]}")))
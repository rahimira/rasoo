import subprocess
import sys
import json
from datetime import datetime
from pytz import timezone
from random import choice

def is_installed(package):
    try:
        subprocess.run([sys.executable, "-m", "pip", "show", package], stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=True)
        return True
    except subprocess.CalledProcessError:
        return False

ORIGINAL = [":", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
FONTS = [
    [":", "𝟶", "𝟷", "𝟸", "𝟹", "𝟺", "𝟻", "𝟼", "𝟽", "𝟾", "𝟿"],
    [":", "𝟬", "𝟭", "𝟮", "𝟯", "𝟰", "𝟱", "𝟲", "𝟳", "𝟴", "𝟵"],
    [":", "０", "１", "２", "３", "４", "５", "６", "７", "８", "９"],
    [":", "₀", "₁", "₂", "₃", "₄", "₅", "₆", "₇", "₈", "₉"],
    [":", "𝟎", "𝟏", "𝟐", "𝟑", "𝟒", "𝟓", "𝟔", "𝟕", "𝟖", "𝟗"]
]

def create_time():
    current_time = datetime.now(timezone("Asia/Tehran")).strftime("%H:%M")
    font = choice(FONTS)
    return "".join(font[ORIGINAL.index(char)] if char in ORIGINAL else char for char in current_time)

def delete_permision(user):
    return getattr(user, 'privileges', None) and getattr(user.privileges, 'can_delete_messages', False)

def read_json(filename):
    try:
        with open(filename, "r", encoding="utf-8") as f:
            return json.load(f)
    except Exception:
        return {}

def write_json(filename, data):
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=6, ensure_ascii=False)
        
def read_blocked():
    try:
        with open("blocked.json", "r", encoding="utf-8") as f:
            return json.load(f)
    except Exception:
        return []

def write_blocked(blocked_list):
    with open("blocked.json", "w", encoding="utf-8") as f:
        json.dump(blocked_list, f, ensure_ascii=False)
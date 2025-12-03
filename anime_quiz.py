import random
from colorama import Fore, Style, init

init(autoreset=True)

characters = {
    "A": "Monkey D. Luffy - Adventurous, bold and free!",
    "B": "Satoru Gojo - Chill, stylish, effortlessly OP.",
    "C": "Levi Ackerman - Precise, disclipined, and lethal.",
    "D": "Tanjiro Kamado - Kind, selfless, and heart-driven."
}

questions = [
    {
        "q": f"{Fore.RED}You see danger ahead. What do you do?",
        "a": {
            "A": "Charge in bravely to protect everyone",
            "B": "Analyze the situation before moving",
            "C": "Stay calm and make a strategic plan",
            "D": "Joke around but prepare to fight if needed"
        }
    },
    {
        "q": f"{Fore.MAGENTA} What best describes your energy?",
        "a": {
            "A": "Bold, loud, and unstoppable",
            "B": "Chill, effortlessly powerful",
            "C": "Quiet, observant, and discliplined",
            "D": "Kind-hearted and empatheic"
        }
    },
    {
        "q": f"{Fore.CYAN} Your friends are arguing. Your role is:",
        "a": {
            "A": "The one who tries to make peace",
            "B": "The one who trolls but gives good advice",
            "C": "The silent mediator who fixes it behind the scenes",
            "D": "The one who says the real truth even if it's harsh"
        }
    },
    {
        "q": f"{Fore.YELLOW} What kind of fighter would you be?",
        "a": {
            "A": "Pure instincts + adaptability",
            "B": "Overpowered with style and confidence",
            "C": "Precise and lethal, no wasted movement",
            "D": "Technique + heart, every move has meaning"
        }
    },
    {
        "q": f"{Fore.GREEN} What motivates you most?",
        "a": {
            "A": "Adventure and freedom",
            "B": "Becoming the best in your field",
            "C": "Loyalty and protecting your circle",
            "D": "Saving others and standing up for what's right"
        }
    },
    {
        "q": f"{Fore.BLUE} If you were the main character, your flaw would be:",
        "a": {
            "A": "Too reckless",
            "B": "Too unserious at times",
            "C": "Too emotionally closed off",
            "D": "Too self-sacrificing"
        }
    }
]

def main():
    pass


if __name__ == "__main__":
    main()
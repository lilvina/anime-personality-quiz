from colorama import Fore, Style, init

init(autoreset=True)

moon = "\U0001F319"
flower = "\U0001F338"
bolt = "\U000026A1"
spark = "\U00002728"
fire = "\U0001F525"
wave = "\U0001F30A"
sword = "\U0001F5E1"
cool = "\U0001F60E"
heart = "\U0001F49A"

characters = {
    "A": f"Monkey D. Luffy {wave}{bolt} - Adventurous, bold and free!",
    "B": f"Satoru Gojo {cool}{moon} - Chill, stylish, effortlessly OP.",
    "C": f"Levi Ackerman {sword}{bolt} - Precise, disclipined, and lethal.",
    "D": f"Tanjiro Kamado {wave}{heart} - Kind, selfless, and heart-driven."
}

questions = [
    {
        "q": f"{Fore.RED}You see danger ahead. What do you do?",
        "a": {
            "A": f"Charge in bravely to protect everyone {bolt}",
            "B": "Analyze the situation before moving",
            "C": "Stay calm and make a strategic plan",
            "D": "Joke around but prepare to fight if needed"
        }
    },
    {
        "q": f"{Fore.MAGENTA} What best describes your energy?",
        "a": {
            "A": "Bold, loud, and unstoppable",
            "B": f"Chill, effortlessly powerful {cool}",
            "C": "Quiet, observant, and discliplined",
            "D": f"Kind-hearted and empatheic {heart}"
        }
    },
    {
        "q": f"{Fore.CYAN} Your friends are arguing. Your role is:",
        "a": {
            "A": "The one who tries to make peace",
            "B": f"The one who trolls but gives good advice {spark}",
            "C": f"The silent mediator who fixes it behind the scenes {moon}",
            "D": f"The one who says the real truth even if it's harsh {bolt}"
        }
    },
    {
        "q": f"{Fore.YELLOW} What kind of fighter would you be?",
        "a": {
            "A": "Pure instincts + adaptability",
            "B": f"Overpowered with style and confidence {cool}",
            "C": f"Precise and lethal, no wasted movement {sword}",
            "D": f"Technique + heart, every move has meaning {heart}"
        }
    },
    {
        "q": f"{Fore.GREEN} What motivates you most?",
        "a": {
            "A": f"Adventure and freedom {moon}",
            "B": "Becoming the best in your field",
            "C": "Loyalty and protecting your circle",
            "D": f"Saving others and standing up for what's right {heart}"
        }
    },
    {
        "q": f"{Fore.BLUE} If you were the main character, your flaw would be:",
        "a": {
            "A": "Too reckless",
            "B": "Too unserious at times",
            "C": "Too emotionally closed off",
            "D": f"Too self-sacrificing {heart}"
        }
    }
]

#function to ask questions
def ask_questions(question_obj):
    print("\n" + question_obj["q"])
    for key, val in question_obj["a"].items():
        print(f" {Fore.WHITE}{key}. {val}")

    #if true, it will output the answer, if you pick the wrong choice, you must pick again
    while True:
        choice = input(Fore.WHITE + Style.BRIGHT + f"Your answer {bolt} (A/B/C/D): ").upper()
        if choice in ["A", "B", "C", "D"]:
            return choice
        print(Fore.RED + "Invalid choice. Pick A, B, C, or D.")

#retrieve the results  
def get_result(answers):
    return max(set(answers), key=answers.count)


def main():
    print(f"{Fore.WHITE}{Style.BRIGHT} Welcome to the Anime Personality Quiz! {flower}")

    answers = []
    for question in questions:
        answers.append(ask_questions(question))

    result_key = get_result(answers)
    character = characters[result_key]

    print("\n" + f"{Fore.WHITE}{Style.BRIGHT} You are most like... ")
    print(f"{Fore.YELLOW}{Style.BRIGHT}{character}\n")

    print("\n" + Fore.CYAN + f"Power cinematic {fire}{wave}{spark}")


if __name__ == "__main__":
    main()
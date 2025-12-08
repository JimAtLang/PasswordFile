from faker import Faker
fake = Faker()
import random
import string

# Word lists for username generation
adjectives = [
    'swift', 'bright', 'cool', 'dark', 'silent', 'cosmic', 'electric',
    'crystal', 'shadow', 'mystic', 'golden', 'silver', 'crimson', 'azure',
    'phantom', 'neon', 'lunar', 'solar', 'frost', 'blaze'
]

nouns = [
    'wolf', 'dragon', 'phoenix', 'tiger', 'falcon', 'raven', 'panther',
    'viper', 'hawk', 'lion', 'eagle', 'bear', 'fox', 'owl', 'shark',
    'thunder', 'storm', 'flame', 'frost', 'shadow', 'ninja', 'knight',
    'warrior', 'hunter', 'ranger', 'mage', 'sage', 'blade', 'pixel'
]

verbs = [
    'runs', 'flies', 'jumps', 'dances', 'codes', 'plays', 'writes',
    'draws', 'builds', 'creates', 'explores', 'dreams', 'thinks'
]

common_names = [
    'alex', 'sam', 'jordan', 'taylor', 'casey', 'morgan', 'riley',
    'jamie', 'avery', 'quinn', 'charlie', 'drew', 'max', 'sage'
]


def adjective_noun():
    """Generate username like 'SilentWolf' or 'CoolDragon'"""
    adj = random.choice(adjectives)
    noun = random.choice(nouns)
    return f"{adj.capitalize()}{noun.capitalize()}"


def noun_number():
    """Generate username like 'Dragon42' or 'Phoenix99'"""
    noun = random.choice(nouns)
    num = random.randint(1, 999)
    return f"{noun.capitalize()}{num}"


def name_noun():
    """Generate username like 'AlexWolf' or 'SamDragon'"""
    name = random.choice(common_names)
    noun = random.choice(nouns)
    return f"{name.capitalize()}{noun.capitalize()}"


def adjective_noun_number():
    """Generate username like 'CoolWolf23' or 'DarkDragon88'"""
    adj = random.choice(adjectives)
    noun = random.choice(nouns)
    num = random.randint(1, 99)
    return f"{adj.capitalize()}{noun.capitalize()}{num}"


def name_verb_noun():
    """Generate username like 'alex_runs_fast' or 'sam_codes_python'"""
    name = random.choice(common_names)
    verb = random.choice(verbs)
    noun = random.choice(nouns)
    return f"{name}_{verb}_{noun}"


def underscore_style():
    """Generate username like 'silent_wolf' or 'cool_dragon_42'"""
    adj = random.choice(adjectives)
    noun = random.choice(nouns)
    if random.choice([True, False]):
        num = random.randint(1, 99)
        return f"{adj}_{noun}_{num}"
    return f"{adj}_{noun}"


def leet_speak():
    """Generate username with some leet speak like 'C00lWolf' or 'Sil3ntDragon'"""
    adj = random.choice(adjectives)
    noun = random.choice(nouns)
    username = f"{adj.capitalize()}{noun.capitalize()}"

    # Apply some leet speak transformations
    replacements = {'o': '0', 'e': '3', 'a': '4', 'i': '1', 's': '5'}
    if random.choice([True, False]):
        char = random.choice(list(replacements.keys()))
        username = username.replace(char, replacements[char])

    return username


def generate_username(style='random'):
    """
    Generate a random username based on the specified style.

    Styles:
    - 'random': randomly choose a style
    - 'adjective_noun': CoolDragon
    - 'noun_number': Phoenix42
    - 'name_noun': AlexWolf
    - 'adjective_noun_number': CoolWolf23
    - 'underscore': silent_wolf or cool_dragon_42
    - 'leet': C00lWolf
    """

    styles = {
        'adjective_noun': adjective_noun,
        'noun_number': noun_number,
        'name_noun': name_noun,
        'adjective_noun_number': adjective_noun_number,
        'underscore': underscore_style,
        'leet': leet_speak
    }

    if style == 'random':
        generator = random.choice(list(styles.values()))
    else:
        generator = styles.get(style, adjective_noun)

    return generator()


def generate_multiple(count=10, style='random'):
    """Generate multiple usernames"""
    return [generate_username(style) for _ in range(count)]


# # Example usage
# if __name__ == "__main__":
#     print("=== Random Username Generator ===\n")
#
#     print("10 Random Style Usernames:")
#     for username in generate_multiple(10, 'random'):
#         print(f"  {username}")
#
#     print("\n5 Adjective + Noun Usernames:")
#     for username in generate_multiple(5, 'adjective_noun'):
#         print(f"  {username}")
#
#     print("\n5 Underscore Style Usernames:")
#     for username in generate_multiple(5, 'underscore'):
#         print(f"  {username}")
#
#     print("\n5 Leet Speak Usernames:")
#     for username in generate_multiple(5, 'leet'):
#         print(f"  {username}")

def generate_password(min_length=8, max_length=12):
    length = random.randint(min_length, max_length)
    alphabet = string.ascii_letters + string.digits + "!@#$%^&*()<>"
    pw = "".join(random.sample(alphabet, length))
    return pw

authentication = {}

for i in range(1000):
    username = generate_username()
    authentication[username] = generate_password()

with open("passwords.txt", "w") as file:
    for username, password in authentication.items():
        file.write(f"{username}:{password}\n")

with open("userdata.txt", "w") as file:
    for username in authentication.keys():
        file.write(f"{username},{fake.first_name()},{fake.last_name()},{fake.email()}\n")
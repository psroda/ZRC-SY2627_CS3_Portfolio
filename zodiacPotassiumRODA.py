ZODIAC_SIGNS = {
    0: "Rat (鼠/Shǔ)",
    1: "Ox (牛/Niú)",
    2: "Tiger (虎/Hǔ)",
    3: "Rabbit (兔/Tù)",
    4: "Dragon (龙/ Lóng)",
    5: "Snake (蛇/Shé)",
    6: "Horse (马/Mǎ)",
    7: "Goat (羊/ Yáng)",
    8: "Monkey (猴/Hóu)",
    9: "Rooster (鸡/Jī)",
    10: "Dog (狗/Gǒu)",
    11: "Pig (豬/Zhū)"
}

birth_year_str = input("Enter your birth year: ")

if not birth_year_str.isdigit():
    print("Invalid Input, please enter a valid year number.")
else:
    birth_year = int(birth_year_str)

    if birth_year < 1900:
        print("Invalid Year, it should not be earlier than 1900")
    else:
        zodiac_index = (birth_year - 1900) % 12

        zodiac_sign = ZODIAC_SIGNS[zodiac_index]

        print(f"Your Chinese Zodiac Sign is: {zodiac_sign}")

<img width="311" height="29" alt="Screenshot 2026-08-24 142210" src="https://github.com/user-attachments/assets/25c922ae-bfed-4271-91f3-9c7da1db4466" />
<img width="323" height="79" alt="Screenshot 2026-08-24 142233" src="https://github.com/user-attachments/assets/0666ce0a-5f3a-4892-8094-de41c611f9ac" />
<img width="686" height="441" alt="Screenshot 2026-08-24 142134" src="https://github.com/user-attachments/assets/2e1857b8-5cf2-4261-aa65-c93beba990f0" />

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

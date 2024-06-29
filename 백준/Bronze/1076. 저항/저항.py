color_to_value = {
    "black": (0, 1),
    "brown": (1, 10),
    "red": (2, 100),
    "orange": (3, 1_000),
    "yellow": (4, 10_000),
    "green": (5, 100_000),
    "blue": (6, 1_000_000),
    "violet": (7, 10_000_000),
    "grey": (8, 100_000_000),
    "white": (9, 1_000_000_000)
}

color1 = input().strip()
color2 = input().strip()
color3 = input().strip()

value1 = color_to_value[color1][0]
value2 = color_to_value[color2][0]

multiplier = color_to_value[color3][1]

resistance = (value1 * 10 + value2) * multiplier

print(resistance)


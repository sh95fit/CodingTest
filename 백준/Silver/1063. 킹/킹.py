move_dict = {
    "R": (0, 1),
    "L": (0, -1),
    "B": (-1, 0),
    "T": (1, 0),
    "RT": (1, 1),
    "LT": (1, -1),
    "RB": (-1, 1),
    "LB": (-1, -1)
}

def pos_to_indices(pos):
    col = ord(pos[0]) - ord('A')
    row = int(pos[1]) - 1

    return row, col

def indices_to_pos(row, col):
    return chr(col + ord('A')) + str(row + 1)

def is_within_bounds(row, col):
    return 0 <= row < 8 and 0 <= col < 8

def move_king_and_stone(king_pos, stone_pos, moves):
    king_row, king_col = pos_to_indices(king_pos)
    stone_row, stone_col = pos_to_indices(stone_pos)   

    for move in moves:
        drow, dcol = move_dict[move]

        new_king_row = king_row + drow
        new_king_col = king_col + dcol

        if not is_within_bounds(new_king_row, new_king_col):
            continue

        if (new_king_row, new_king_col) == (stone_row, stone_col):
            new_stone_row = stone_row + drow
            new_stone_col = stone_col + dcol

            if not is_within_bounds(new_stone_row, new_stone_col):
                continue

            stone_row, stone_col = new_stone_row, new_stone_col

        king_row, king_col = new_king_row, new_king_col

    return indices_to_pos(king_row, king_col), indices_to_pos(stone_row, stone_col)

def main():
    import sys

    input = sys.stdin.read
    data = input().split()

    king_pos = data[0]
    stone_pos = data[1]
    n = int(data[2])
    moves = data[3:3+n]

    final_king_pos, final_stone_pos = move_king_and_stone(king_pos, stone_pos, moves)

    print(final_king_pos)
    print(final_stone_pos)

if __name__ == "__main__":
    main()


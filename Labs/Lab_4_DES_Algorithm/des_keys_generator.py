def permuted_choice_1(key):
    pc1_table = [57, 49, 41, 33, 25, 17, 9,
                 1, 58, 50, 42, 34, 26, 18,
                 10, 2, 59, 51, 43, 35, 27,
                 19, 11, 3, 60, 52, 44, 36,
                 63, 55, 47, 39, 31, 23, 15,
                 7, 62, 54, 46, 38, 30, 22,
                 14, 6, 61, 53, 45, 37, 29,
                 21, 13, 5, 28, 20, 12, 4]
    return [key[i - 1] for i in pc1_table]


def left_shift(key_half, shifts):
    return key_half[shifts:] + key_half[:shifts]


def permuted_choice_2(key):
    pc2_table = [14, 17, 11, 24, 1, 5,
                 3, 28, 15, 6, 21, 10,
                 23, 19, 12, 4, 26, 8,
                 16, 7, 27, 20, 13, 2,
                 41, 52, 31, 37, 47, 55,
                 30, 40, 51, 45, 33, 48,
                 44, 49, 39, 56, 34, 53,
                 46, 42, 50, 36, 29, 32]
    return [key[i - 1] for i in pc2_table]


def generate_round_keys(key):
    # Permuted Choice 1
    permuted_key = permuted_choice_1(key)
    left_half, right_half = permuted_key[:28], permuted_key[28:]

    # Shifts for each round
    shift_schedule = [1, 1, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 1]
    round_keys = []

    for shifts in shift_schedule:
        left_half = left_shift(left_half, shifts)
        right_half = left_shift(right_half, shifts)
        # Combine halves and permute
        combined_key = left_half + right_half
        round_key = permuted_choice_2(combined_key)
        round_keys.append(round_key)

    return round_keys


# Example usage
if __name__ == "__main__":
    # Example 64-bit key as binary list
    key = [0, 1, 0, 1, 0, 1, 0, 1] * 8
    round_keys = generate_round_keys(key)
    print("Generated Round Keys:")
    for i, rk in enumerate(round_keys, 1):
        print(f"K{i}: {rk}")

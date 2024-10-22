from utils import *

str = read_from_file("encrypted.txt").upper()


str = substitute_letters(str, 'V', 'e')
str = substitute_letters(str, 'W', 't')
str = substitute_letters(str, 'Q', 'h')
str = substitute_letters(str, 'T', 'a')
str = substitute_letters(str, 'O', 'd')
str = substitute_letters(str, 'N', 'o')
str = substitute_letters(str, 'G', 'n')
str = substitute_letters(str, 'P', 's')
str = substitute_letters(str, 'X', 'i')
str = substitute_letters(str, 'R', 'w')
str = substitute_letters(str, 'F', 'y')
str = substitute_letters(str, 'I', 'r')
str = substitute_letters(str, 'D', 'u')
str = substitute_letters(str, 'J', 'g')
str = substitute_letters(str, 'H', 'c')
str = substitute_letters(str, 'U', 'p')
str = substitute_letters(str, 'S', 'l')
str = substitute_letters(str, 'C', 'f')
str = substitute_letters(str, 'Z', 'm')
str = substitute_letters(str, 'A', 'b')
str = substitute_letters(str, 'K', 'v')
str = substitute_letters(str, 'E', 'j')
str = substitute_letters(str, 'L', 'k')
str = substitute_letters(str, 'M', 'z')
str = substitute_letters(str, 'Y', 'x')
str = substitute_letters(str, 'B', 'q')


frequency = find_frequency(str)
new_frequency = dict(sorted(frequency.items(), key=lambda x: x[1], reverse=True))
plot_frequency(new_frequency, label="Frequency of each letter in the text")
plot_frequency(english_language_letters_frequency, label=None)

write_to_file(str, "decrypted.txt")

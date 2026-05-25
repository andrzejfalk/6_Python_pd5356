# PYTHON_12

class InvalidDnaSequence(Exception):
    pass


def check_dna(sequence):
    for char in sequence:
        if char not in "ATCG":
            raise InvalidDnaSequence("Sequence can contain only A, T, C, G")


try:
    with open("sequence.txt", "r") as file:
        old_sequence = file.read()
        print(old_sequence)

except FileNotFoundError:
    print("File sequence.txt was not found")

new_sequence = input("Enter new DNA sequence: ").upper()

try:
    check_dna(new_sequence)

    with open("new_sequence.txt", "w") as file:
        file.write(new_sequence)

    print("Sequence saved to new_sequence.txt")

except InvalidDnaSequence as error:
    print("Error:", error)
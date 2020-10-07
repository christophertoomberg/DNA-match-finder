import csv

csv_path_large = "/home/christopher/Desktop/dna/databases/large.csv"
csv_path_small = "/home/christopher/Desktop/dna/databases/small.csv"
txt_path = "/home/christopher/Desktop/dna/sequences"


def find_longest_str_streak(str_part: str, sequence: str):
    # Here something is fishy
    streaks = []
    str_part_length = len(str_part)
    for i in range(len(sequence)):
        sub_seq = sequence[i:i + str_part_length]
        if sub_seq == str_part:
            streaks.append(1)
            for j in range(i + str_part_length, len(sequence), str_part_length):
                possible_match = sequence[j:j + str_part_length]
                if possible_match == str_part:
                    streaks[i] += 1
                else:
                    break
        else:
            streaks.append(0)
            continue
        return max(streaks)


def get_available_strs(csv_path):
    with open(csv_path) as csv_file:
        csv_reader = csv.reader(csv_file)
        for row in csv_reader:
            return row[1:]


def find_matches(t_path, csv_path):
    dna_sequence = ""
    available_strs = get_available_strs(csv_path)
    str_occurences = []

    # Open up the DNA sequence. There are 20 files.
    for i in range(1, 21):
        f = open(t_path + f"/{i}.txt", "r")
        dna_sequence = f.read()

        # Find how much does every str occur in sequence.
        for available_str in available_strs:
            str_occurences.append(find_longest_str_streak(available_str, dna_sequence))

        # Just repairing that something fishy
        for el in range(len(str_occurences)):
            if str_occurences[el] is None:
                str_occurences[el] = 0

        # Compare with every person
        with open(csv_path) as csv_file:
            csv_reader = csv.reader(csv_file)
            line_count = 0
            for row in csv_reader:

                # Skip the header
                if line_count == 0:
                    line_count += 1
                    continue

                # Do the rest
                if row[1:] == str_occurences:
                    print(f"{row[0]} matches the DNA sequence from file {i}.txt")


if __name__ == '__main__':
    find_matches(txt_path, csv_path_large)

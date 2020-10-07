import csv

csv_path_large = "/home/christopher/Desktop/dna/databases/large.csv"
csv_path_small = "/home/christopher/Desktop/dna/databases/small.csv"
txt_path = "/home/christopher/Desktop/dna/sequences"


def get_reoccurrences(partial_sequence, str_part):
    reoccurences = 0
    str_part_length = len(str_part)
    for i in range(0, len(partial_sequence), str_part_length):
        possible_match = partial_sequence[i: i + str_part_length]
        if possible_match == str_part:
            reoccurences += 1
        else:
            return reoccurences


def find_longest_str_streak(str_part: str, sequence: str):
    streaks = []
    str_part_length = len(str_part)
    for i in range(len(sequence)):
        sub_seq = sequence[i:i + str_part_length]
        if sub_seq == str_part:
            streaks.append(1)
            to_add_on = get_reoccurrences(sequence[i + str_part_length:], str_part)

            # This is weird..
            if to_add_on is None:
                to_add_on = 0
            streaks[i] += to_add_on
        else:
            streaks.append(0)
            continue
    return max(streaks)


def get_available_strs(csv_path):
    with open(csv_path) as csv_file:
        csv_reader = csv.reader(csv_file)
        for row in csv_reader:
            return row[1:]


def get_people(csv_path):
    people = []
    with open(csv_path) as csv_file:
        csv_reader = csv.reader(csv_file)
        line_count = 0
        for row in csv_reader:

            # Skip the header
            if line_count == 0:
                line_count += 1
                continue

            # Do the rest
            else:
                people.append(row)
    return people


def find_matches(t_path, csv_path):
    dna_sequence = ""
    available_strs = get_available_strs(csv_path)
    people = get_people(csv_path)

    # Open up the DNA sequence. There are 20 files.
    for i in range(1, 21):
        str_occurences = []

        f = open(t_path + f"/{i}.txt", "r")
        dna_sequence = f.read()

        # Find how much does every str occur in sequence.
        for available_str in available_strs:
            str_occurences.append(find_longest_str_streak(available_str, dna_sequence))

        # Compare with every person. Should be a separate function, since we don't need to read the contents of the
        # same file every iteration.
        for person in people:
            person_int_list = [int(p) for p in person[1:]]
            if person_int_list == str_occurences:
                print(f"{person[0]} matches the DNA sequence from file {i}.txt")


if __name__ == '__main__':
    # [4, 0, 1, 0, 1, 5, 1, 0] for the first txt file
    # test_seq = "AATCCTGGTTGGACATACCGTTTTCCACACAAATGCCCCAGACACTGTACGGAGACCCTCTAGTCTAGTCTAGTCTAGTCTAGTCTAGTCTAGTCTAGTCTAGTCTAGTCTAGTCTAGTCTAGTCTAGTTTTTTCTTTTTTTCTTTTTTTCTTTTTTTCTTTTTTTCTTTTTTTCTTTTTTTCTTTTTTTCTTTTTTTCTTTTTTTCTTTTTTTCTTTTTTTCTTTTTTTCTTTTTTTCTTTTTTTCTTTTTTTCTTTTTTTCTTTTTTTCTTTTTTTCTTTTTTTCTTTTTTTCTTTTTTTCTTTTTTTCTTTTTTTCTAAGAACCGGGGTTTTGGCTGATTCACCGAGTCAACCTAAGACACTAGTTAAACATGTTTGTCGATTATATCACCTTTCATATATTCCGAGCGACACTTTTCAATGCTATATGGTGCTTATTCCTGCTTACCATTTTCGGACCCAGGCCTCAACTTTTGCTTGTACGACATGAAAGGTGCAGCTCTACTTGGATAAGGTGTACTACCTAGCTTACTCGCACCGGACCATTAGCTATTACAGGGTTTGGATAGTTACGTGATGATCGAGGCAGACACCGTAAGACTCTTACGCGCCCGACGGTCCCCGTTAATGATGACAGTGACGAAAGGATTGAGAGGCGCGTCAGACCCCTGTTCCCATATTGTATGTTGTCGTTGGTACGGGCGCCTTACGGAGTAAGGTGTTAGGCAGGAATGGCCAAAGGTTGGTGAACCTGAATCATGGTTGACACGCAGCTCTCTACATTTATGGGCGTATTCCTATTCGCGACTACTACAACTCTTCGGCCGCCGGTAACCGTACGGTGGCTAGATGCCGCTCATACAAAGTATGCGAGCCGTATTCAGAGTATAATGACCTGAAGGAGTACATGAGGGTCATGGTCCGCAGGGACTCCCTGTCATATGCTGAGATGGAGCCATAATCCCTGCCAGCCGTGTGGACTCAGGCATTCCTGTATTAAGCACTCTAGCCCTCGTGAATGCTTGGAAGAGTCACCCAAGGAATCGATTATCACAGGTTGGGAGAGGATGTTTTTCAAGGCCCTGAAAATTTGAAGGGGCTATTGACTGCGGCGTTACAACCAAAGAGATGACGGAACCATTGCTTCCGTCATGCTGGTGTCCCTGTGCGACCCACCGTGTTTGCTCCAATAAGTGGAAGGGTAAATTGATTACTACCGGTTTCATAGGAAGTTCGAGGTGCACGGTTGAGTAGCATTAGAGCTTCGAGCCAGGTTACCATAGTTATCTTTATGGGGCACTCGCCCTGATGTTTACGCCAGGGTTTAGCTTTGTGATCCGTTAGGGGGTTACCTACGACGCAGCAATTAGCGGGTGTCGCAGGTGTGTAGTTTGTGGCACCAAGCCAGCGGGCTTTACTTAACCAACCCTGGGAAGATCACTTCATCCGAATATGAGATCGCCCAACGCTAATACGCCGAAATGGGAACTGAAGGTCTTAGACTAGCTCACGAACCGTATACCTTAAGTTCCCTAAGCGGACGAATTTTTACTAAGTAAGGATTGCAGGAATATGGAAATCATCCGTACGTGCTTTGACGACCCAAAAAGAGGATCAATGGTATCTACCCAAAGCGTTATTCCTAGTACCAGGAGCCTAAATCATTTATAAAAAAATGCAACCTTTACCGTGGAGCGAAGGAAACTCTACTTATCTATCTATCTATCTATCTATCTATCTATCTATCTATCTATCTATCTATCTATCTATCTATCTATCTATCTATCTATCTCTGTCTGTCTGTCTGTCTGTCTGTCTGTCTGTCTGTCTGTCTGTCTGTCTGTCTGTCTGTCTGTCTGTCTGTCTGTCTGTCTGTCTGTCTGTCTGTCTGGTGTCAACCGTAGCCTGGTAGATGGAGGATGGTCGACTGGCTCAGATCCACCCTTGTGGCGGCATAACAAAATGTTCACTGAATTGGGCGAAAAATTAGCGAGTGTCACTTGACAAGGACTGAATAGCAGCAACAACCGTCGAGATCGTTGTCCAGTCACGCGGACTGATGATCTTAGATATAACGCAGAACTCAATGGCTCCTCCTGTACTATGATAGGGCGATATAGCGAGCCGAAAACTCGGGCCGGATGAGCGCTCACTGCGGTCCCGCAGCGCTGTTACGACGCCACGTTACCCTTGATCCGTGGTTGGTAGTGTCGCGTGATGAATGCACGAGTTGGTACCGTTCTAAGATCGACTACACGTGGCTCGATTTTAGCAAGTGTGCGATACCTGAATAGTCTGTAACAGTCCGGCGACCCATGGAAGCCGTTTCGTCCCGTATGCCAAGGCCCCGTTTATCCCTCAGCATGGGAATGACGGCCACCAGTGGTCCGTGTTCGCGATCAGTCTCGGGGAGGTACACACCCTCACTGTAAACTGGCAAGGAGGTGATTTTGCCCAATCTGAGAGCCTAAAGTGGCAGTACAGGTTCCTCACACATAACGAGGTACTTGCCTAACTACGTCCTATGTAGACAGGATAAGAAAACGCAGAGCGCGACCGCCGTGCAGTAATGAGTACTAAGGTAACTGGCCGCTCATATGTTCAGTACTGTCACCGTGTTGGTTAGAAAGAAAGAAAGAAAGAAAGAAAGAAAGAAAGAAAGAAAGAAAGAAAGAAAGAAAGAAATCGACGCTAAGTCGGCTTCAGACTCTTGCGATGATTCCGATTCGGCCTTTTCCCTCAGTGCTTCTCAGCAGGCAACTTGCGAAAAGCATATCGCGCATTAGTACAACAGCAATTACTACACGACCAAAACGTCGTGGAGAGTCGCTGTACTGCAGCTCAAGGGTGGCCGACCATAGAACATTTAACGATATGCACGATCCGGTCAAATATCACAACAGAATTGTGTGCTAGTAGGGGAAAAGGGGAAGGCCCTTCCTTGGGATAGATAGATAGATAGATAGATAGATAGATAGATAGATAGATAGATAACCGACTCATTGCGGAATTTTCAGTTTTACAATGCGGTGACCACTAGCCAACGGCGTCATTGATAATGATACTAACTTCCTTGGGGCGACTCCGGTTTAAAAGTGGCCGGTACGCTTGTTCGACATCATGTGTAGCGTTATTAGGACTGAATTACCGGGCCCCGTTCCGAGATGTTCTTTTTCGGCCCCTGGCGCAGAGGCGCTTGAGCTGCATATACTGGAATATAAGAGGTCACTCGCGAGAACGGTCACGCTACCATGTCGGCAGGATGCAGGATCAGGAATAATGTGGTAGACCTGTGTTCAACGGTGATCTCGGTGTGGATCGGGTGAGCACCAGATCGACTAACTAAGGGATATGCAAGCAGATTCTTCGGACGCCTTTGCCGGTAACACATGGAACACGCCTATGCGCTCCATTACTGGGTGCCTTGTTGAGACGGATAGGTCGGGTTCAATGATTATTAAGGTTTATCAACGTATTACTGCTTGTAACGGCTTGTAAGTGCCAATTGTCATTCGACCCCGGCTGGTCTGACAAGGTTTGTACGCCGATTTGGCATGAGGGGACTAGAGTGGAATAGGATTGTGCACTAAGCTGCGGTCCCGCCTGCGTACCCGCGTATCAAGTGGCTCGGTGGCTGGTTGCGATTACTGAGCTCGTGCATTGCTATCAGTGCGTCCCCTGCAAGAACAGGTATCAAGTGTGGTTCCGTATTGCACGATTGACAATTTCATCGGGTATTCGCTCGTCGGCAAACATTGAAGGCTTCATAGGTTCACAACCGCGTTCCCTGTGATGCGGAATCGCGAGATCTGGATCATCCTTCTAAGACACTCAAAATGCAGACGTCGAGAGACGTATGCGTCCGCGGGAACTATGGCATCTGCCCTTAACATGTGAAGAGACTGCTTTAGCTCGATCTAACCGTAGGCCCTTCATGAAGAGAAGCCATTGTCGGGGGTAGTGACTTTTGGCCGTACGTGATTAAATAACACGGAGTCAAACTCGGAGCGTTCCGTCTCTGATATCGCCAACATCGCAAGCTCCCTACGTACCACCCTGGGTGAACACGACTTTAATGCTTTGAAAATATTGATGGAGACGGCACAAATTTCCGAAAACTCGAAACTTAGTAAATTTACACTGAAAAACCCGGGCGGACAAGTACAAGAGTCCGCGCTCGTAGTGCTCTGTTGAAGCGTTGACCTCTGTCGCTTAAAATCGTAAAGACTTTATACACGAATATTGAGTGAGAAAGAGTCCCCGATCTATCATTACAAATATTCCGTTCTACAATCTGAGGCCAGACAGTTTTGTTCCCTCTCCTTACCTAGTGCCATATCGAGGGACAGAAATTTGACACCTTGCAGTCACACGTTGTTTTGAGATATGCAAACCACGCCCAGTGTCGAGATCCCACATATCTTCATTATAAGCTCGACCACTTGAGACTGCAGCACGAAGGCAGATCAGATCAGATCAGATCAGATCAGATCAGATCAGATCAGATCAGATCAGATCAGATCAGATCAGATCAGATCAGATCAGATCAGATCAGATCAGAAATTCCAAGCAATGGCTTCAGCGCTCGGACGCCCCGCCCGTGCCCGGCGTGAACATATGGATGTATGAATTATTGCATGGTCTGTATCTTAATGCGCGCTTGGCAACACATGTGAGAACGGTCTCACGTGCGACTACGTATGATCTATGCAAATGTGCGGTGGCGCCCGGCCTTTTTAGGAGGTTCCTAGACCAGGAGCCTGTGTGGTAAGGGCCGGCAGACGTTTCCGGTACGCTCCGCCAAGAAGGTAACCATGCGGCCCGGTAATGTAACCAGGTCTCGAAAAAATTAGGCGAATCGAAAGGGTTCTATCGGACCGTTAACAATTTACGGTCATTCTAGTATGCATTCAAGGAACCGACTCTCGTCTCACATTTATGTCATCATTATGACTAACGCAAGCTGTTACAACGTGACTACTCACCTGGATCGTCATCACGCGCGATGTGCATGAACTCGCAAAAACGAACCTAATCGAACGGTTATCGGTGACATTTGATTTTGAGTCTGCGGCACGTAAAAGCTCTGGGATGCAGCTCCTATATCAGCCTAGGGGTCGGGCTCTCTGGTTCTGCTCGCTAGAATGAATGAATGAATGAATGAATGAATGAATGAATGAATGAATGAATGAATGAATGAATGAATGAATGAATGAATGAATGAATGAATGAATGAATGAATGAATGAATGAATGAATGAATGAATGAATGAATGAATGAATGAATGCAGTCCCGTGAGTGAGTAGTATACGCGATCTTGTGTGTCTAAGTTATTGCCACACACGAATGACCAAATACGAGATCTAGACTCGTGTATATGAGACAGGTTGCACAATCAGCCTTTATTCTGAGACAGTGGTGCTGGGGATGGCTTGAGATACATACGCACACAAGCCCAGGGGGATTAATTGCTGCGCAGATAGCCCGCCCAAAGTTGTCCCAGTGACCTTAGAAGGACCCTGTACCTGGCGTTGGGTAAGACACGTCACCCGTCGTAGCCGTGTATAGCCGAGCGTCCTGCAAAAGCGTATCTTTTTGATGAGCGAAATCGCGTCCAAAGACTTCGCTCAATTCAGAAGGCTCGAATTGCCGATCGTCGCAGGGCTGCATTAGGCACGCCAGTTCTTCTAGGTCCCGGGCCGAGAGTGTTCGGCGGTAACTGCCTTTTAGGGGCCGCACACCTCGGCTGCGGCCGGGCGGAAGGCGCTTACTTCTGGATGCGGCTTCAGACGGCTGTAATATGTCTCGGAATACCGCTCAGCATACGAGGAGTCTCCGCTTTCGACAGCCTGGGGCCACGTCGTGTTGAA"
    # test_str = "AATG"
    # find_longest_str_streak(test_str, test_seq)
    find_matches(txt_path, csv_path_large)

import re
import csv

csv_path_large = "/home/christopher/Desktop/dna/databases/large.csv"
csv_path_small = "/home/christopher/Desktop/dna/databases/small.csv"
txt_path = "/home/christopher/Desktop/dna/sequences"


# Read the people data from CSV file and map it to a dict.
def read_dna_db(path) -> dict:
    people = {}
    with open(path) as csv_file:
        csv_reader = csv.reader(csv_file)
        line_count = 0
        strs = []
        for row in csv_reader:

            # Skip header
            if line_count == 0:
                line_count += 1
                strs = row
                continue

            # Build the dictionary -> 'name' : 'str_name:count'
            person_strs = ""
            for i in range(1, len(strs)):
                if i == len(strs) - 1:
                    person_strs += f"{strs[i]}:{row[i]}"
                else:
                    person_strs += f"{strs[i]}:{row[i]} "
            people[row[0]] = person_strs

    print(people)
    return people


# Read a DNA sequence from a .txt file -> 'filename' : 'sequence'
def read_dna_sequence(path, file_index) -> str:
    f = open(path + f"/{file_index}.txt", "r")
    return f.read()


def get_all_strs_for_person(person_data: str):
    strs = []
    datas = person_data.split(" ")
    for data in datas:
        strs.append(data.split(":")[0])
    return strs


def count_occurences(sequence, p_str):
    pass


def find_matches(people):
    # For every .txt file we loop through all the persons to find the match.
    # There are 20 files.
    available_strs = []
    for name, data in people.items():
        available_strs = get_all_strs_for_person(data)
        break
    for i in range(1, 21):
        sequence = read_dna_sequence(txt_path, i)

    pass


def main():
    people = read_dna_db(csv_path_large)
    find_matches(people)


if __name__ == '__main__':
    main()


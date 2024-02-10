import csv


def fix_extra_commas(input_file, output_file):
    with open('Aviewingactivity.csv', 'r', encoding='utf-8', newline='') as infile, open('1Aviewingactivity.csv', 'w', encoding='utf-8', newline='') as outfile:
        reader = csv.reader(infile)
        writer = csv.writer(outfile)

        for row in reader:
            fixed_row = [column.replace(',,', ',') for column in row]
            writer.writerow(fixed_row)

    print(f"Extra commas fixed. Output written to {output_file}")


# Replace 'input.csv' with the name of your input file and 'output.csv' with the desired output file name
fix_extra_commas('Aviewingactivity.csv', '1Aviewingactivity.csv')

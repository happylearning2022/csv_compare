file1_path = 'file1.txt'
file2_path = 'file2.txt'

with open(file1_path, 'r') as file1, open(file2_path, 'r') as file2:
    lines_file1 = file1.readlines()
    lines_file2 = file2.readlines()

    if len(lines_file1) != len(lines_file2):
        print("The files have different numbers of lines. Cannot compare.")
    else:
        mismatches = []
        for line_num, (line1, line2) in enumerate(zip(lines_file1, lines_file2), start=1):
            fields1 = line1.strip().split('|')
            fields2 = line2.strip().split('|')

            if len(fields1) != len(fields2):
                mismatches.append(f"Line {line_num}: Number of fields differ")
            else:
                for col_num, (field1, field2) in enumerate(zip(fields1, fields2), start=1):
                    if field1 != field2:
                        mismatches.append(f"Line {line_num}, Column {col_num}: '{field1}' != '{field2}'")

        if mismatches:
            print("Mismatches found:")
            for mismatch in mismatches:
                print(mismatch)
        else:
            print("No mismatches found. Files are identical.")

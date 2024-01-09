import csv

def compare_csv_files(file1, file2):
    with open(file1, 'r') as csv_file1, open(file2, 'r') as csv_file2:
        reader1 = csv.reader(csv_file1)
        reader2 = csv.reader(csv_file2)
        
        # Assuming both CSV files have the same number of rows and columns
        for row1, row2 in zip(reader1, reader2):
            for col1, col2 in zip(row1, row2):
                if col1 != col2:
                    print(f"Difference found: {col1} (File 1) - {col2} (File 2)")
            # Check for differences in row length
            if len(row1) != len(row2):
                print("Row length differs between files.")
            # You can add more detailed comparison logic here
            
# Example usage:
file1_path = 'file1.csv'
file2_path = 'file2.csv'
compare_csv_files(file1_path, file2_path)

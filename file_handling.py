
import csv

input_f = r'C:\Users\HP\OneDrive\Desktop\WEEK 1\DAY 1\file.csv'

output_f = r'C:\Users\HP\OneDrive\Desktop\WEEK 1\DAY 1\output.csv'

ro = csv.reader(input_f, delimiter = ',') # reader object which return iterable rows of csv file
print(ro)

try:
    with open(input_f, mode="r") as f:
        ro = csv.reader(f, delimiter=",")
        output_data=[]
        
        
        print("File content after removed spaces:")
        
        for row in ro:
            output_row = [col.strip() for col in row] # for removal of spaces
            output_data.append(output_row)
            print(output_row)  # Print each row using reader object
            
    with open(output_f, mode="w", newline="") as file:
        writer = csv.writer(file)
        writer.writerows(output_data)

    print("Cleaned data saved successfully")
    
    new_data = [
        ["RAM", "30", "JAIPUR"],
        ["RAJ", "28", "UDAIPUR"]
    ]

    with open(output_f, mode="a", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerows(new_data)

    print(f"New data appended successfully to '{output_f}'.")
 



except FileNotFoundError:
    print(f"The file {f} was not found.")

except PermissionError:
    print("Permission denied")

except csv.Error:
    print("Invalid CSV format.")

except Exception as e:
    print(f" An unexpected error occurred: {e}")

finally:
    print("CSV operation completed")
    


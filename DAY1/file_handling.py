
import csv
import re

input_f = 'file.csv'

output_f = 'output.csv'

ro = csv.reader(input_f, delimiter = ',') 
print(ro)

try:
    with open(input_f, mode="r") as f:
        ro = csv.reader(f, delimiter=",")
        output_data=[]
        
        
        print("File content after removed spaces:")
        
        for row in ro:
            output_row = [re.sub(r'\s+', '',col).strip() for col in row ]       #[col.strip() for col in row]
            output_data.append(output_row)
            print(output_row)  
            
    with open(output_f, mode="w") as file:
        writer = csv.writer(file)
        writer.writerows(output_data)

    print("Cleaned data saved successfully")
    
    new_data = [
        ["RAM", "30", "JAIPUR"],
        ["RAJ", "28", "UDAIPUR"]
    ]

    with open(output_f, mode="a", newline="") as file:
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
    


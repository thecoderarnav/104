import csv
with open ("HW.csv", newline='')as f:
    reader = csv.reader(f)
    file_data = list (reader)
    
file_data.pop (0)
new_data = []    
for i in range (len(file_data)):
    n_number = file_data[i][1]
    new_data.append(float(n_number))

n = len(new_data)
total = 0
for x in new_data:
    total+=x

Mean = total/n
print("Mean Is:"+ str(Mean))
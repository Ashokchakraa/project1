'''
import csv


# field names
fields = ['Name', 'Branch', 'Year', 'CGPA']
	
# data rows of csv file
rows = [ ['Nikhil', 'COE', '2', '9.0'],
		['Sanchit', 'COE', '2', '9.1'],
		['Aditya', 'IT', '2', '9.3'],
		['Sagar', 'SE', '1', '9.5'],
		['Prateek', 'MCE', '3', '7.8'],
		['Sahil', 'EP', '2', '9.1']]

with open('GFG', 'w') as f:
	
	# using csv.writer method from CSV package
write = csv.writer(f)
	
write.writerow(fields)
write.writerows(rows)

'''


import pandas as pd

# initialise data dictionary.
data_dict = {'CustomerID': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
			
			'Gender': ["Male", "Female", "Female", "Male",
						"Male", "Female", "Male", "Male",
						"Female", "Male"],
			
			'Age': [20, 21, 19, 18, 25, 26, 32, 41, 20, 19],
			
			'Annual Income(k$)': [10, 20, 30, 10, 25, 60, 70,
								15, 21, 22],
			
			'Spending Score': [30, 50, 48, 84, 90, 65, 32, 46,
								12, 56]}

# Create DataFrame
data = pd.DataFrame(data_dict)

# Write to CSV file
data.to_csv("Customers.csv")

# Print the output.
print(data)




import pandas as pd

# read DataFrame
data = pd.read_csv("Customers.csv")

# no of csv files with row size
k = 2
size = 5

for i in range(k):
	df = data[size*i:size*(i+1)]
	df.to_csv(f'Customers_{i+1}.csv', index=False)

df_1 = pd.read_csv("Customers_1.csv")
print(df_1)

df_2 = pd.read_csv("Customers_2.csv")
print(df_2)

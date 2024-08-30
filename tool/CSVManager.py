"""
	CSVManager: search,update,add,remove lines to a csv file in python
	Author: Mostafa Zia Sistani (mostafas.dev@gmail.com)
"""
import csv
class CSVManager:
	def __init__(self, filename):
		self.filename = filename

	def search(self, search_text):
		# Guard clause to check the length of search_text  
		if len(search_text) <= 2:
			raise ValueError("search_text must be greater than 2 characters.")  
		search_text=search_text.lower() # to lower case
		found=0
		result=[]
		with open(self.filename, mode='r', newline='\n') as file:
			reader = csv.reader(file)
			rows = list(reader)
			for index, row in enumerate(rows):
				for cells in row: # here we search text in all cells of each rows
					if search_text in cells.lower():
						found=1
				if found == 1:
					result.append([index+1,row]) # Return line number (1-based) and the row
				found = 0
			#show result
			for entry in result:
				line_number = entry[0]
				details = ','.join(entry[1])
				print(f"Line {line_number}: {details}")
			result=[]
		return None, None

	def update(self, line_number, new_data):
		with open(self.filename, mode='r', newline='\n') as file:
			reader = csv.reader(file)
			rows = list(reader)

		if 0 < line_number <= len(rows):
			rows[line_number - 1] = new_data  # Update the row

			with open(self.filename, mode='w', newline='\n') as file:
				writer = csv.writer(file)
				writer.writerows(rows)
			return True
		return False

	def remove(self, line_number):
		with open(self.filename, mode='r', newline='\n') as file:
			reader = csv.reader(file)
			rows = list(reader)

		if 0 < line_number <= len(rows):
			rows.pop(line_number - 1)  # Remove the row

			with open(self.filename, mode='w', newline='\n') as file:
				writer = csv.writer(file)
				writer.writerows(rows)
			return True
		return False

	def add(self, name, mime_type, extension, description):
		with open(self.filename, mode='a', newline='\n') as file:
			writer = csv.writer(file)
			writer.writerow([name, mime_type, extension, description])
		return True

if __name__ == "__main__":
	csv_manager = CSVManager('sample.csv')

	# Add a new row
	#csv_manager.add('Example Name', 'application/example', '.ex', 'This is an example.')

	# Search for a row
	line_number, row = csv_manager.search('E')
	print(f'Found at line {line_number}: {row}')

	# Update a row
	# if line_number:
	# csv_manager.update(line_number, ['Updated Name', 'application/updated', '.ex', 'Updated description.'])

	# Remove a row
	# if line_number:
	#csv_manager.remove(line_number)

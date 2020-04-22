import csv

class Readfile():
	def __init__(self, filename):
		with open (filename, 'r') as f_input:
			csv_input = csv.reader(f_input)
			self.details = list(csv_input)
	
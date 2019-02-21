import csv

class CSV2TabPlugin:
	def input(self, filename):
		self.myfile = filename


	def run(self):
		self.input_csvfile = csv.reader(open(self.myfile, 'r'))


	def output(self, filename):
		out_tabfile = csv.writer(open(filename, 'w'), delimiter = "\t")
		out_tabfile.writerows(self.input_csvfile)
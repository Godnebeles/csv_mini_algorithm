from itertools import chain
from dateutil.parser import parse
import copy


class Worker:
	name: str
	date: str
	hours: float

	def __init__(self, name, date, hours):
		self.name = name
		self.date = date
		self.hours = hours


def get_workers_from_csv(csv_text: str):
	workers = []
	dates = []
	for line in csv_text[1:]:
		name, date, hours = line.split(",")
		isFound = False
		temp_date = str(parse(date).strftime('%Y-%m-%d'))
		if not any(x.lower() == temp_date.lower() for x in dates):		
			dates.append(str(temp_date))
		for j in range(0, len(workers)):
			if name.lower() == workers[j].name.lower():
				workers[j].date.append(date)
				workers[j].hours.append(float(hours))  
				isFound = True
				break  	     	
		if isFound == False:
			workers.append(
			Worker(name, [date], [float(hours)])
			)
					
	return [workers, dates]


def write_workers_in_csv(workers, dates, file):
	temp_string_dates = ",".join([str(i) for i in dates])
	file.write("Name / Date," + temp_string_dates +'\n')
	for worker in workers:
		temp_string_hours = ",".join([str(i) for i in worker.hours])
		file.write(worker.name + "," + temp_string_hours + '\n')


text_from_file = open("./acme_worksheet.csv", 'r', encoding="utf-8").readlines()
workers = get_workers_from_csv(text_from_file)
workers[0].sort(key=lambda x: x.name)


drop_file = open("./workers.csv", 'w', encoding="utf-8")
write_workers_in_csv(workers[0], workers[1], drop_file)
drop_file.close()

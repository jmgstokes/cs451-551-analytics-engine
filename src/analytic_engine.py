#Stokes, Jeff
#Assignment 3 - CS451, Software Engineering

#-------------------#
# Read in JSON file #
#-------------------#

import json

class dataset():

	def load_json(self,filename):
		with open(filename, 'r') as f:
			data = json.load(f)

		return data

#--------------------------#
# Find average final grade #
#--------------------------#

	def grade_avg(self,data):
		total = 0
		grades = 0
		for i in data:

			if i[3] == 'A': total += 4
			elif i[3] == 'B': total += 3
			elif i[3] == 'C': total += 2
			elif i[3] == 'D': total += 1
			grades += 1

		avg = total//grades

		if avg == 4: return 'A'
		elif avg == 3: return 'B'
		elif avg == 2: return 'C'
		elif avg == 1: return 'D'
		else: return 'F'

#--------------------------------------------#
# Average grade change from midterm to final #
#--------------------------------------------#

	def grade_change(self, data):
		total_mid, total_final, mid_grades, final_grades = 0,0,0,0
		for i in data:
			if i[2] == 'A': total_mid += 4
			elif i[2] == 'B': total_mid += 3
			elif i[2] == 'C': total_mid += 2
			elif i[2] == 'D': total_mid += 1


			if i[3] == 'A': total_final += 4
			elif i[3] == 'B': total_final += 3
			elif i[3] == 'C': total_final += 2
			elif i[3] == 'D': total_final += 1
			mid_grades += 1
			final_grades += 1

		mid_avg = total_mid//mid_grades
		final_avg = total_final//final_grades

		diff = abs(final_avg - mid_avg)
		# print(total_final,total_mid)
		# print('Grades changed on average by:',diff,'points from midterm to final.')
		return diff

#------------------------#
# Count each final grade #
#------------------------#
	def grade_count(self,data):
		num_A, num_B, num_C, num_D, num_F = 0,0,0,0,0
		for i in data:

			if i[3] == 'A': num_A += 1
			elif i[3] == 'B': num_B += 1
			elif i[3] == 'C': num_C += 1
			elif i[3] == 'D': num_D += 1
			else: num_F += 1
		d = dict()
		d['A'], d['B'], d['C'] ,d['D'], d['F'] = num_A, num_B, num_C, num_D, num_F
		# print('Final Grades: \nA:',num_A,'B:',num_B,'C:',num_C,'D:',num_D,'F:',num_F)
		return d


#--------------------------------#
# Count male and female students #
#--------------------------------#

	def count_genders(self, data):
		m_count = 0
		f_count = 0
		for i in data:
			if i[1] == 'M':
				m_count += 1
			else:
				f_count += 1
		# print ()
		# print (m_count,'male students and', f_count, 'female students')
		d = dict()
		d['Male'], d['Female'] = m_count, f_count
		return d




if __name__ == '__main__':
	grade_data = dataset.load_json('/Desktop/cs451-551-analytics-engine/data/grade-data.json')
	genders = grade_data.count_genders(grade_data)
	avg_grade = grade_data.grade_avg(grade_data)
	num_of_grades = grade_data.grade_count(grade_data)
	avg_grade_change = grade_data.grade_change(grade_data)
	print(genders)
	print(avg_grade)
	print(num_of_grades)
	print(avg_grade_change)

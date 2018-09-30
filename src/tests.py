import unittest

from analytic_engine import dataset

class TestWrapper(unittest.TestCase):
	def test_read_data(self):
		d = dataset
		data = d.load_json('/Desktop/cs451-551-analytics-engine/data/grade-data.json')
		self.assertEqual(size(data), 89)

	def test_count_male(self):
		d = dataset
		data = d.load_json('/Desktop/cs451-551-analytics-engine/data/grade-data.json')
		d.count_genders(data)
		self.assertEqual(M, 72)

	def test_count_female(self):
		d = dataset
		data = d.load_json('/Desktop/cs451-551-analytics-engine/data/grade-data.json')
		d.count_genders(data)
		self.assertEqual(F, 17)

	def test_grade_count(self):
		d = dataset
		data = d.load_json('/Desktop/cs451-551-analytics-engine/data/grade-data.json')
		grades = d.grade_count(data)
		self.assertEqual(grades, {'A':43, 'B':25, 'C':13, 'D':2, 'F': 6})

	def test_avg_grade(self):
		d = dataset
		data = d.load_json('/Desktop/cs451-551-analytics-engine/data/grade-data.json')
		avg = d.grade_avg(data)
		self.assertEqual(avg, "B")

	def test_avg_change(self):
		d = dataset
		data = d.load_json('/Desktop/cs451-551-analytics-engine/data/grade-data.json')
		chng = d.grade_change(data)	
		self.assertEqual(chng, 2)

if __name__ == '__main__':
	unittest.main()
import os
import csv
import json

path = "/home/weltom/Documents/projects/practice /4/"
output = "/home/weltom/Documents/projects/practice /4/output"
file = "students.csv"

class FileManager():
	def __init__(self,file):
		self.file = file

	def check_files(self):
		if not os.path.exists(self.file):
			print(file, "not found")
			return False
		print("File found: ", self.file)

	def create_output_folder(self, folder='output'):
		if not os.path.exists(output):
			os.makedir(folder)
			print(f"Output folder created: {folder}/")
		else:
			print(f"Output folder already exists: {folder}/")


def load_data(filename):
    try:
        print("Loading data...")
        with open(filename, 'r', encoding='utf-8') as f:
            r = csv.DictReader(f)
            students = list(r)
        print(f"Data loaded successfully: {len(students)} students")
        return students
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found. Please check the filename.")
        return None
    except Exception as e:
        print(f"Error: An unexpected error occurred — {e}")
        return None

load_data(file)


def preview_data(students, n):
	print(f"First {n} rows")
	print("-"*30)
	for s in students[:n]:
		print(f"{s['student_id']} | {s['age']} | {s['gender']} | {s['country']} | {s['GPA']}")
	print("-"*30)

preview_data(load_data(file), 5)


def get_top_students(students, n=10):
    top = []
    sorted_students = sorted(students, key=lambda x: float(x['final_exam_score']), reverse=True)
    for s in sorted_students[:n]:
        try:
            float(s['final_exam_score'])
            float(s['GPA'])
            top.append(s)
        except ValueError:
            print(f"Warning: could not convert value for student {s['student_id']} — skipping row.")
            continue
    return top

students = load_data("students.csv")

load_data("wrong_file.csv")

get_top_students(load_data(file), 10)


print("-"*30)
print("Lambda / Map / Filter")
print("-"*30)
top_scorers = list(filter(lambda s: float(s['final_exam_score']) > 95,load_data(file)))
print(f"final_exam_score > 95  : {len(top_scorers)}")

gpa_values = list(map(lambda s: float(s['GPA']), load_data(file)))
print(f"GPA values (first 5)   : {gpa_values[:5]}")

good_assignments = list(filter(lambda s: float(s['assignment_score']) > 90,load_data(file)))
print(f"assignment_score > 90  : {len(good_assignments)}")
print("-"*30)


top10 = get_top_students(students, 10)

x = {
	"analysis": "Top 10 Students by Exam Score",
	"total_students": len(file),
	"top": [
		{
		"rank": i+1,
		"student_id": top10[i]['student_id'],
		"country": top10[i]['country'],
		"major" : top10[i]['major'],
		"final_exam_score" : top10[i]['final_exam_score'],
		"GPA" : top10[i]['GPA']
		}
		for i in range(len(top10))
	]
}

with open("output/x.json", "w", encoding='utf-8') as f:
	json.dump(x, f, indent=4) 


 
print("\n" + "=" * 30)
print("ANALYSIS RESULT")
print("=" * 30)
print(f"Analysis : Top 10 Students by Exam Score")
print(f"Total students : {len(students)}")
print("Top 10 saved to output/result.json")
print("=" * 30)
print("Result saved to output/result.json")
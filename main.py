import os
import csv
import json

path = "/home/weltom/Documents/projects/practice /4/"
output = "/home/weltom/Documents/projects/practice /4/output"
file = "students.csv"


def check_files():
	if not os.path.exists(file):
		print(file, "not found")
		return False
	print("File found: ", file)

	if not os.path.exists(output):
		print("Output folder dont created")
		return False
	print("Output folder exist")
	print("Output folder: ", output)

check_files()

#task2
with open(file, 'r', encoding='utf-8') as f:
	r = csv.DictReader(f)
	students = list(r)

print("\n" + f"Total students: {len(students)}")
print("First 5 rows")
print("-"*30)
for s in students[:5]:
	print(f"{s['student_id']} | {s['age']} | {s['gender']} | {s['country']} GPA: {s['GPA']}")
print("-"*30)

#task3
sorted_students = sorted(students, key=lambda x: float(x['final_exam_score']), reverse=True)
top10 = sorted_students[:10]

print("\n" + "-" * 30)
print("Top 10 Students by Exam Score")
print("-" * 30)
for i in range(len(top10)):
    s = top10[i]
    print(f"{i+1}. {s['student_id']} | {s['country']} | {s['major']} | Score: {float(s['final_exam_score'])} | GPA: {float(s['GPA'])}")
print("-" * 30)
#task4

x = {
	"analysis": "Top 10 Students by Exam Score",
	"total_students": len(students),
	"top10": [
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
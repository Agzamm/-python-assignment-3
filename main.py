import os
import csv
import json


class FileManager:
    def __init__(self, filename):
        self.filename = filename

    def check_file(self):
        print("Checking file...")
        if not os.path.exists(self.filename):
            print(f"File not found: {self.filename}")
            return False
        print(f"File found: {self.filename}")
        return True

    def create_output_folder(self, folder='output'):
        print("Checking output folder...")
        if not os.path.exists(folder):
            os.makedirs(folder)
            print(f"Output folder created: {folder}")
        else:
            print(f"Output folder already exists: {folder}")


class DataLoader:
    def __init__(self, filename):
        self.filename = filename
        self.students = []

    def load(self):
        try:
            print("Loading data...")
            with open(self.filename, 'r', encoding='utf-8') as f:
                r = csv.DictReader(f)
                self.students = list(r)
            print(f"Data loaded successfully: {len(self.students)} students")
            return self.students
        except FileNotFoundError:
            print(f"Error: File '{self.filename}' not found. Please check the filename.")
            return []
        except Exception as e:
            print(f"Error: {e}")
            return []

    def preview(self, n=5):
        print(f"First {n} rows:")
        print("-" * 30)
        for s in self.students[:n]:
            print(f"{s['student_id']} | {s['age']} | {s['gender']} | {s['country']} | GPA: {s['GPA']}")
        print("-" * 30)


class DataAnalyser:
    def __init__(self, students):
        self.students = students
        self.result = {}

    def analyse(self):
        try:
            sorted_students = sorted(
                self.students,
                key=lambda x: float(x['final_exam_score']),
                reverse=True
            )
        except ValueError as e:
            print(f"Warning: could not convert value — {e}")
            sorted_students = []

        top10 = sorted_students[:10]

        self.result = {
            "top_10_students": [
                {
                    "rank": i + 1,
                    "student_id": s['student_id'],
                    "country": s['country'],
                    "major": s['major'],
                    "final_exam_score": float(s['final_exam_score']),
                    "gpa": float(s['GPA'])
                }
                for i, s in enumerate(top10)
            ]
        }
        return self.result

    def print_results(self):
        print("-" * 30)
        print("Top 10 Students by Exam Score")
        print("-" * 30)
        for entry in self.result["top_10_students"]:
            print(
                f"{entry['rank']}. {entry['student_id']} | {entry['country']} | "
                f"{entry['major']} | Score: {entry['final_exam_score']} | GPA: {entry['gpa']}"
            )
        print("-" * 30)


class ResultSaver:
    def __init__(self, result, output_path):
        self.result = result
        self.output_path = output_path

    def save_json(self):
        try:
            with open(self.output_path, 'w', encoding='utf-8') as f:
                json.dump(self.result, f, indent=4)
            print(f"Result saved to {self.output_path}")
        except Exception as e:
            print(f"Error saving file: {e}")


fm = FileManager('students.csv')
if not fm.check_file():
    print('Stopping program.')
    exit()
fm.create_output_folder()

dl = DataLoader('students.csv')
dl.load()
dl.preview()

print("-" * 30)
print("Lambda / Map / Filter")
print("-" * 30)

top_scorers = list(filter(lambda s: float(s['final_exam_score']) > 95, dl.students))
print(f"final_exam_score > 95  : {len(top_scorers)}")

gpa_values = list(map(lambda s: float(s['GPA']), dl.students))
print(f"GPA values (first 5)   : {gpa_values[:5]}")

good_assignments = list(filter(lambda s: float(s['assignment_score']) > 90, dl.students))
print(f"assignment_score > 90  : {len(good_assignments)}")
print("-" * 30)

DataLoader("wrong_file.csv").load()

analyser = DataAnalyser(dl.students)
analyser.analyse()
analyser.print_results()

saver = ResultSaver(analyser.result, 'output/result.json')
saver.save_json()
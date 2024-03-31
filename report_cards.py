import os
import json
from pypdf import PdfReader

max_grade = 9

folder = 'report_cards/'
pdf_files = [i for i in os.listdir(folder) if '.pdf' in i]


def main():
    print(pdf_files)
    for i in pdf_files:
        full_name = i.replace('.pdf', '')
        reader = PdfReader(folder+i)
        grades = {}
        subjects = ['Art', 'Computing', 'Drama', 'English', 'Humanities', 'Mathematics', 'Music', 'Physical Education', 'Science']

        grade_pages = reader.pages[1:]
        for grade_page in grade_pages:
            current_grade = grade_page.extract_text().split('\n')
            for index, value in enumerate(current_grade):
                for subject in subjects:
                    if subject in value:
                        subjects.remove(subject)
                        try:
                            grade_score = int(current_grade[index+1]) / max_grade
                            grades[subject] = grade_score
                        except ValueError:
                            pass

        with open(folder+full_name+'.json', 'w') as f:
            json.dump(grades, f, indent=4)
        print(full_name)


if __name__ == "__main__":
    main()

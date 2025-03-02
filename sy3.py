student_grades=[]
for i in range(5):
    while True:
        try:
            score=float(input(f"请输入第{i+1}个学生的成绩："))
            student_grades.append(score)
            break
        except ValueError:
            print("输出错误，请输入有效的数字成绩！")
print(f"最高分{max(student_grades)}")
print(f"最低分{min(student_grades)}")
print(f"平均分{sum(student_grades)/len(student_grades)}")

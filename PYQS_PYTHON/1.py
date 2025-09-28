student_records= {
    "StudentID": [101, 102, 103, 104, 105],
    "Name": ["Alice", "Bob", "Charlie", "David", "Eva"],
    "Subject": ["Math", "Science", "Math", "English", "Science"],
    "Marks": [95, 88, 70, 92, 85]
}
#1
marks=95+88+70+92+85
percentage=(marks/500)*100
print("the average marks is : ",percentage)
#2
sub_marks={"maths":99,"python":100}
avg=(sum(sub_marks.values()))/len(sub_marks)
print("the average of 2 sub is :",avg)
#3
student_data="Name:kannah,class:cse,sec-g"
with open("student.txt","w") as f:
    f.write(student_data)
with open("student.txt","r") as f:
       print(f.read()) 
#4
import numpy as np
m=np.array([99,44,78,83,40])
print("mean: ",np.mean(m))
print("sort :",np.sort(m)) #[::-1] REVERSE
#5
import pandas as pd
data = pd.DataFrame({
    'StudentID': [1,2,3],
    'Name': ['A', 'B', 'C'],
    'Subject': ['Math', 'Science', 'Math'],
    'Marks': [95, 88, 70]
})
print("groupby subject: ",data.groupby("Subject")['Marks'].mean())
print("above 80:\n",data[data["Marks"]>80])


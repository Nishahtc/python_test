
studentdata={1:4000,2:4000,3:15000,4:30000,5:10000,6:4000}
m=max(studentdata ,key=studentdata.get)
print(m)
# Print the student ID with the maximum salary
print(f"Maximum Student ID: {m}")

# Get the salary of the student with the maximum ID
max_salary = studentdata[m]

# Print the maximum salary
print(f"Maximum Salary: {max_salary}")

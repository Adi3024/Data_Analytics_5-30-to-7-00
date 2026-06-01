import pandas as pd

employee = {
    'name': ['brijesh', 'het', 'krish'],
    'course_name': ['DA', 'Data_science', 'DA'],
    'age': [25, 24, 24]
}

print(type(employee))

df = pd.DataFrame(employee)
print(df)

# w.r.t to create employee data using pandas

# banking management system
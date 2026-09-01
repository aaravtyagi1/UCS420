import pandas as pd
import numpy as np

data = {
    "Tid": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    "Refund": ["Yes", "No", "No", "Yes", "No", "No", "Yes", "No", "No", "No"],
    "Marital_Status": [
        "Single", "Married", "Single", "Married", "Divorced",
        "Married", "Divorced", "Single", "Married", "Single"
    ],
    "Taxable_Income": [
        "125K", "100K", "70K", "120K", "95K",
        "60K", "220K", "85K", "75K", "90K"
    ],
    "Cheat": ["No", "No", "No", "No", "Yes", "No", "No", "Yes", "No", "Yes"]
}

df = pd.DataFrame(data)
df

print(df.loc[[0, 4, 7, 8]])

print(df.iloc[3:8])

print(df.iloc[4:9,2:5])

print(df.iloc[:,1:4])

path = '/content/Iris.csv'
iris_df = pd.read_csv("Iris.csv")

print("First five rows of Iris dataset:")
print(iris_df.head())

#Q5

iris_deleted_df = iris_df.drop(index=4).drop(columns=iris_df.columns[3])

iris_deleted_df

#Q6

employee_data = {
    "Employee_ID": [101, 102, 103, 104, 105],
    "Name": ["Alice", "Bob", "Charlie", "Diana", "Edward"],
    "Department": ["HR", "IT", "IT", "Marketing", "Sales"],
    "Age": [29, 34, 41, 28, 38],
    "Salary": [50000, 70000, 65000, 55000, 60000],
    "Years_of_Experience": [4, 8, 10, 3, 12],
    "Joining_Date": [
        "2020-03-15",
        "2017-07-19",
        "2013-06-01",
        "2021-02-10",
        "2010-11-25"
    ],
    "Gender": ["Female", "Male", "Male", "Female", "Male"],
    "Bonus": [5000, 7000, 6000, 4500, 5000],
    "Rating": [4.5, 4.0, 3.8, 4.7, 3.5]
}
employees_df = pd.DataFrame(employee_data)
employees_df["Joining_Date"] = pd.to_datetime(employees_df["Joining_Date"])

employees_df.to_csv("employees.csv", index=False)
print(employees_df.shape)
## (5, 10)
print(employees_df.info())

print(employees_df.describe())

print(employees_df.head()) #first 5

print(employees_df.tail(3))

avg_salary = employees_df["Salary"].mean()
total_bonus = employees_df["Bonus"].sum()
youngest_age = employees_df["Age"].min()
highest_rating = employees_df["Rating"].max()

print("Average Salary:", avg_salary)
print("Total Bonus:", total_bonus)
print("Youngest Employee Age:", youngest_age)
print("Highest Performance Rating:", highest_rating)

sorted_salary_df = employees_df.sort_values(by="Salary", ascending=False)

print(sorted_salary_df)

def performance_category(rating):
    if rating >= 4.5:
        return "Excellent"
    elif rating >= 4.0:
        return "Good"
    else:
        return "Average"

employees_df["Performance_Category"] = employees_df["Rating"].apply(
    performance_category
)

print(employees_df[["Name", "Rating", "Performance_Category"]])

print("Missing values in each column:")
print(employees_df.isnull().sum())

employees_df.rename(columns={"Employee_ID": "ID"}, inplace=True)

print(employees_df.head())

more_than_5_years = employees_df[
    employees_df["Years_of_Experience"] > 5
]

print("Employees with more than 5 years of experience:")
print(more_than_5_years)

it_employees = employees_df[
    employees_df["Department"] == "IT"
]

print("Employees in IT department:")
print(it_employees)

employees_df["Tax"] = employees_df["Salary"] * 0.10

print(employees_df[["ID", "Name", "Salary", "Tax"]])

employees_df.to_csv("modified_employees.csv", index=False)

print("Modified employee dataset saved successfully.")
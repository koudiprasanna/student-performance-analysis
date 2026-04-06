import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
data = pd.read_csv("students.csv")

# Show first data
print("Dataset:\n", data)

# Calculate average marks
data['Average'] = data[['Maths', 'Science', 'English']].mean(axis=1)

print("\nAverage Marks:\n", data[['Name', 'Average']])

# Top student
top_student = data.loc[data['Average'].idxmax()]
print("\nTop Student:\n", top_student)

# Plot average marks
plt.bar(data['Name'], data['Average'])
plt.title("Student Average Marks")
plt.xlabel("Students")
plt.ylabel("Average Marks")
plt.xticks(rotation=45)
plt.show()
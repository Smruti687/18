import pandas as pd
import matplotlib.pyplot as plt

# dataset with Result already included
data = {
    "Name": ["A","B","C","D","E","F","G","H"],
    "Marks": [85, 78, 90, 66, 88, 72, 95, 60],
    "Hours": [5, 4, 6, 3, 5, 4, 7, 2],
    "Result": ["Pass","Pass","Pass","Fail","Pass","Pass","Pass","Fail"]
}

df = pd.DataFrame(data)

print(df)

# 1. Bar Chart
df.plot(x="Name", y="Marks", kind="bar")
plt.title("Marks of Students")
plt.show()

# 2. Line Chart
df.plot(x="Name", y="Marks")
plt.title("Marks Trend")
plt.show()

# 3. Pie Chart (Pass vs Fail)
df["Result"].value_counts().plot(kind="pie")
plt.title("Pass vs Fail")
plt.show()

# 4. Histogram
df["Marks"].plot(kind="hist")
plt.title("Marks Distribution")
plt.show()

# 5. Scatter Plot
df.plot(x="Hours", y="Marks", kind="scatter")
plt.title("Hours vs Marks")
plt.show()

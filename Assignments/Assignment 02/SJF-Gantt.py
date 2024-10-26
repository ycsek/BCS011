'''
Author: Yuchen Shi
Date: 18-10-2024 23:56:27
Last Editors: Jason
Contact Last Editors: D23090120503@cityu.edu.mo
LastEditTime: 19-10-2024 01:15:02
'''
import pandas as pd
import matplotlib.pyplot as plt

# Sample data
data = {
    'Task': ['P2', 'P4', 'P3', 'P5', 'P1'],
    'Start': [0, 1, 2, 4, 9],
    'Finish': [1, 2, 4, 9, 19]
}

# Assign colors to tasks
colors = {
    'P1': 'blue',
    'P2': 'green',
    'P3': 'red',
    'P4': 'purple',
    'P5': 'orange'
}

# Create DataFrame
df = pd.DataFrame(data)

# Create figure and axis
fig, ax = plt.subplots()

# Plot Gantt chart with colors
for i, task in df.iterrows():
    ax.barh(task['Task'], task['Finish'] - task['Start'],
            left=task['Start'], color=colors[task['Task']])
    # Increase the distance between x-axis ticks
    ax.xaxis.set_major_locator(plt.MultipleLocator(1))

# Set labels
ax.set_xlabel('Time')
ax.set_ylabel('Process')
ax.set_title('SJF-Gantt Chart')

# Show plot
plt.show()

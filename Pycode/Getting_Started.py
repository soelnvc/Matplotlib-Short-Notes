#Getting Started with Matplotlib: A Simple Line Graph Example

import matplotlib.pyplot as plt
import numpy as np

# Generate sample data
x=np.arange(2000,2050)
y1=np.random.randint(100,200,size=50)
y2=np.random.randint(200,300,size=50)
y3=np.random.randint(1,20,size=50)

# Define a consistent style for all lines, You can customize this dictionary to create a unique look for your graph.
linedefault={
    'color': '#2C3E50',       # Deep Slate/Midnight blue
    'linewidth': 2.0,         # Thick enough to look intentional, not spindly
    'linestyle': '-',         # Solid line
    'marker': 'o',            # Round markers
    'markersize': 6,          # Subtle markers
    'markerfacecolor': 'white', # Hollow look
    'markeredgewidth': 2,     # Defined border around markers
    'alpha': 0.9,             # Slight transparency to catch the grid
    'antialiased': True       # Ensures smooth edges)
}

# Create the line graph with the defined style. '**linedefault' unpacks the dictionary to apply the style to each line.
plt.plot(x,y1,**linedefault)
plt.plot(x,y2,**linedefault)
plt.plot(x,y3,**linedefault)

# Add grid for better readability
plt.grid(True, which='both', linestyle='--', linewidth=0.5, alpha=0.7) # alpha adds a subtle touch to the grid, making it visible without overpowering the data lines

#Coustumize the ticks to match the overall aesthetic. You can adjust the font size and color to ensure they complement the rest of the graph.
plt.xticks(fontsize=10, color='#34495E') # Darker shade for x-axis ticks
plt.yticks(fontsize=10, color='#34495E') # Darker shade for y-axis ticks

# Add labels and title to the graph
plt.xlabel('X-axis', fontsize=12, fontweight='bold', color='#34495E') # Darker shade for labels
plt.ylabel('Y-axis', fontsize=12, fontweight='bold', color='#34495E') # Darker shade for labels

# Add a title with a complementary color and a slightly larger font size to make it stand out.
plt.title('Line Graph', fontsize=14, fontweight='bold', color='#2C3E50')

#show the graph
plt.show()
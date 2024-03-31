import report_cards
report_cards.main()
from analyze import df
import seaborn as sns
import networkx as nx
from matplotlib import pyplot as plt
import pandas as pd

# Create heatmap of subjects
corr_matrix = df.pivot(index='Subject1', columns='Subject2', values='Correlation')

plt.figure(figsize=(10, 7.5))
sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', fmt=".2f", vmin=-1, vmax=1)
plt.title('Correlation Heatmap of Subjects')
plt.xlabel('Subject 2')
plt.ylabel('Subject 1')
plt.show()

# Create network visualizer
G = nx.DiGraph()
subjects = pd.unique(df[['Subject1', 'Subject2']].values.ravel('K'))
G.add_nodes_from(subjects)

for index, row in df.iterrows():
    G.add_edge(row['Subject1'], row['Subject2'], weight=row['Correlation'])

plt.figure(figsize=(10, 7.5))
pos = nx.spring_layout(G)
nx.draw(G, pos, with_labels=True, node_size=2000, node_color='lightblue', font_size=10, font_weight='bold', arrows=True)
labels = nx.get_edge_attributes(G, 'weight')
nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
plt.title('Network Visualization of Subject Correlation')
plt.show()

import matplotlib.pyplot as plt
import networkx as nx

# Test Example - Define Nodes and Edges
nodes = {
    1: {"id": 1, "name": "node 1", "func": "product", "type": "<(DefaultNode) Static typed default node>"},
    2: {"id": 2, "name": "node 2", "func": "product", "type": "<(DefaultNode) Static typed default node>"},
    3: {"id": 3, "name": "node 3", "func": "product", "type": "<(DefaultNode) Static typed default node>"},
    4: {"id": 4, "name": "node 4", "func": "product", "type": "<(DefaultNode) Static typed default node>"},
}

edges = {
    (1,2): {"id": 1, "name": "edge 12", "weight": 3.27, "type": "<(DefaultEdge) Static typed default edge>"},
    (2,1): {"id": 2, "name": "edge 21", "weight": 1.38, "type": "<(DefaultEdge) Static typed default edge>"},
    (1,3): {"id": 3, "name": "edge 13", "weight": 5.13, "type": "<(DefaultEdge) Static typed default edge>"}, 
    (3,4): {"id": 4, "name": "edge 34", "weight": 9.49, "type": "<(DefaultEdge) Static typed default edge>"},
}

# Set up graph

G = nx.DiGraph()

for node in nodes:
    G.add_node(node, attr=nodes[node])
G.add_edges_from(edges)

idx_to_node_dict = {}
for idx, node in enumerate(G.nodes):
    idx_to_node_dict[idx] = node

# Plot

fig, ax = plt.subplots()
pos = nx.spring_layout(G)
nodes = nx.draw_networkx_nodes(G, pos=pos, ax=ax)
nx.draw_networkx_edges(G, pos=pos, ax=ax)

annot = ax.annotate("", xy=(0,0), xytext=(20,20),textcoords="offset points",
bbox=dict(boxstyle="round", fc="w"),
arrowprops=dict(arrowstyle="->"))
annot.set_visible(False)

def update_annot(ind):
    # node = ind["ind"][0]
    node_idx = ind["ind"][0]
    node = idx_to_node_dict[node_idx]
    xy = pos[node]
    annot.xy = xy
    node_attr = G.nodes[node]["attr"]
    text = '\n'.join(f'{k}: {v}' for k, v in node_attr.items())
    annot.set_text(text)

def hover(event):
    vis = annot.get_visible()
    if event.inaxes == ax:
        cont, ind = nodes.contains(event)
        if cont:
            update_annot(ind)
            annot.set_visible(True)
            fig.canvas.draw_idle()
        else:
            if vis:
                annot.set_visible(False)
                fig.canvas.draw_idle()

fig.canvas.mpl_connect("motion_notify_event", hover)

# Add edge labels
edge_labels = {(u, v): f"{edges[(u, v)]['name']}({edges[(u, v)]['weight']})" for u, v in G.edges()}
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)

# Add node labels
node_labels = {node: f"{G.nodes[node]['attr']['name']}\n{G.nodes[node]['attr']['func']}" for node in G.nodes()}
nx.draw_networkx_labels(G, pos, labels=node_labels)

plt.show()

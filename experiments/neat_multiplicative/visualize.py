import warnings
import networkx as nx
import graphviz
import matplotlib.pyplot as plt
import numpy as np
import os


def plot_stats(statistics, ylog=False, view=False, filename='avg_fitness.svg'):
    """ Plots the population's average and best fitness. """
    if plt is None:
        warnings.warn("This display is not available due to a missing optional dependency (matplotlib)")
        return

    generation = range(len(statistics.most_fit_genomes))
    best_fitness = [c.fitness for c in statistics.most_fit_genomes]
    avg_fitness = np.array(statistics.get_fitness_mean())
    stdev_fitness = np.array(statistics.get_fitness_stdev())

    plt.plot(generation, avg_fitness, 'b-', label="average")
    plt.plot(generation, avg_fitness - stdev_fitness, 'g-.', label="-1 sd")
    plt.plot(generation, avg_fitness + stdev_fitness, 'g-.', label="+1 sd")
    plt.plot(generation, best_fitness, 'r-', label="best")

    plt.title("Population's average and best fitness")
    plt.xlabel("Generations")
    plt.ylabel("Fitness")
    plt.grid()
    plt.legend(loc="best")
    if ylog:
        plt.gca().set_yscale('symlog')

    plt.savefig(filename)
    if view:
        plt.show()

    plt.close()


def plot_spikes(spikes, view=False, filename=None, title=None):
    """ Plots the trains for a single spiking neuron. """
    t_values = [t for t, I, v, u, f in spikes]
    v_values = [v for t, I, v, u, f in spikes]
    u_values = [u for t, I, v, u, f in spikes]
    I_values = [I for t, I, v, u, f in spikes]
    f_values = [f for t, I, v, u, f in spikes]

    fig = plt.figure()
    plt.subplot(4, 1, 1)
    plt.ylabel("Potential (mv)")
    plt.xlabel("Time (in ms)")
    plt.grid()
    plt.plot(t_values, v_values, "g-")

    if title is None:
        plt.title("Izhikevich's spiking neuron model")
    else:
        plt.title("Izhikevich's spiking neuron model ({0!s})".format(title))

    plt.subplot(4, 1, 2)
    plt.ylabel("Fired")
    plt.xlabel("Time (in ms)")
    plt.grid()
    plt.plot(t_values, f_values, "r-")

    plt.subplot(4, 1, 3)
    plt.ylabel("Recovery (u)")
    plt.xlabel("Time (in ms)")
    plt.grid()
    plt.plot(t_values, u_values, "r-")

    plt.subplot(4, 1, 4)
    plt.ylabel("Current (I)")
    plt.xlabel("Time (in ms)")
    plt.grid()
    plt.plot(t_values, I_values, "r-o")

    if filename is not None:
        plt.savefig(filename)

    if view:
        plt.show()
        plt.close()
        fig = None

    return fig


def plot_species(statistics, view=False, filename='speciation.svg'):
    """ Visualizes speciation throughout evolution. """
    if plt is None:
        warnings.warn("This display is not available due to a missing optional dependency (matplotlib)")
        return

    species_sizes = statistics.get_species_sizes()
    num_generations = len(species_sizes)
    curves = np.array(species_sizes).T

    fig, ax = plt.subplots()
    ax.stackplot(range(num_generations), *curves)

    plt.title("Speciation")
    plt.ylabel("Size per Species")
    plt.xlabel("Generations")

    plt.savefig(filename)

    if view:
        plt.show()

    plt.close()


def draw_net(config, genome, view=False, filename=None, node_names=None, show_disabled=True, prune_unused=False,
             node_colors=None, fmt='png'):
    """ Receives a genome and draws a neural network with arbitrary topology. """
    # Attributes for network nodes.
    if graphviz is None:
        warnings.warn("This display is not available due to a missing optional dependency (graphviz)")
        return

    # If requested, use a copy of the genome which omits all components that won't affect the output.
    if prune_unused:
        genome = genome.get_pruned_copy(config.genome_config)

    if node_names is None:
        node_names = {}

    assert type(node_names) is dict

    if node_colors is None:
        node_colors = {}

    assert type(node_colors) is dict

    """

    node_attrs = {
        'shape': 'circle',
        'fontsize': '9',
        'height': '0.2',
        'width': '0.2'}

    # dot = graphviz.Digraph(format=fmt, node_attr=node_attrs)
    dot = nx.DiGraph()

    inputs = set()
    for k in config.genome_config.input_keys:
        inputs.add(k)
        name = node_names.get(k, str(k))
        input_attrs = {'style': 'filled', 'shape': 'box', 'fillcolor': node_colors.get(k, 'lightgray')}
        dot.add_node(name, _attributes=input_attrs)

    outputs = set()
    for k in config.genome_config.output_keys:
        outputs.add(k)
        name = node_names.get(k, str(k))
        node_attrs = {"key": genome.nodes[k].key, "bias": genome.nodes[k].bias, "response": genome.nodes[k].response, "activation": genome.nodes[k].activation, "aggregation": genome.nodes[k].aggregation} # , "type": type(genome.nodes[k])
        node_labels = ''.join([str(y)+'\n' for x,y in node_attrs.items()])
        dot.add_node(name + "\n" + node_labels, _attributes=node_attrs)

    used_nodes = set(genome.nodes.keys())
    for n in used_nodes:
        if n in inputs or n in outputs:
            continue

        # attrs = {'style': 'filled',
        #          'fillcolor': node_colors.get(n, 'white')}
        # dot.add_node(str(n), _attributes=attrs)

        node_attrs = {"key": genome.nodes[n].key, "bias": genome.nodes[n].bias, "response": genome.nodes[n].response, "activation": genome.nodes[n].activation, "aggregation": genome.nodes[n].aggregation} # , "type": type(genome.nodes[n])
        node_labels = ''.join([str(y)+'\n' for x,y in node_attrs.items()])
        dot.add_node(name + "\n" + node_labels, _attributes=node_attrs)

    for cg in genome.connections.values():
        if cg.enabled or show_disabled:
            # if cg.input not in used_nodes or cg.output not in used_nodes:
            #    continue
            input, output = cg.key
            a = node_names.get(input, str(input))
            b = node_names.get(output, str(output))
            # style = 'solid' if cg.enabled else 'dotted'
            # color = 'green' if cg.weight > 0 else 'red'
            # width = str(0.1 + abs(cg.weight / 5.0))
            connection_attrs = {"key": cg.key, "weight": cg.weight, "enabled": cg.enabled} # , "type": type(cg)
            # dot.add_edge((a, b), *connection_attrs) # , _attributes={'style': style, 'color': color, 'penwidth': width}
            
            # Get nodes starting with a, b
            # Get the first element that starts with s
            a = a if next((x for x in list(dot.nodes) if x.startswith(a)), None) is None else next((x for x in list(dot.nodes) if x.startswith(a)), None)
            b = b if next((x for x in list(dot.nodes) if x.startswith(b)), None) is None else next((x for x in list(dot.nodes) if x.startswith(b)), None)

            dot.add_edges_from([(a,b, connection_attrs)])

    # dot.render(filename, view=view)
            
    # Plot the graph
    G = dot
    fig, ax = plt.subplots(figsize=(8, 6))
    pos = nx.spring_layout(G)  # Positions nodes using Fruchterman-Reingold force-directed algorithm
    nx.draw(G, pos, with_labels=True, node_size=3000, node_color='skyblue', font_size=10, font_weight='bold')
    edge_labels = {(u, v): (''.join([str(x)+": "+str(y)+'\n' for x,y in d.items()])) for (u, v, d) in G.edges(data=True)}

    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_color='red')
    plt.title('NEAT Network Visualization')
    plt.show()

    return dot

    """

    nodes = {}
    edges = {}

    inputs = set()
    for k in config.genome_config.input_keys:
        inputs.add(k)
        name = node_names.get(k, str(k))
        nodes[str(name)] = name
    
    outputs = set()
    for k in config.genome_config.output_keys:
        outputs.add(k)
        name = node_names.get(k, str(k))
        node_attrs = {"key": genome.nodes[k].key, "bias": genome.nodes[k].bias, "response": genome.nodes[k].response, "activation": genome.nodes[k].activation, "aggregation": genome.nodes[k].aggregation} # , "type": type(genome.nodes[k])
        nodes[str(name)] = node_attrs

    used_nodes = set(genome.nodes.keys())
    for n in used_nodes:
        if n in inputs or n in outputs:
            continue

        node_attrs = {"key": genome.nodes[n].key, "bias": genome.nodes[n].bias, "response": genome.nodes[n].response, "activation": genome.nodes[n].activation, "aggregation": genome.nodes[n].aggregation} # , "type": type(genome.nodes[n])
        # node_labels = ''.join([str(y)+'\n' for x,y in node_attrs.items()])
        nodes[str(n)] = node_attrs

    print("nodes: ", nodes)

    G = nx.DiGraph()

    for node in nodes:
        G.add_node(node, attr=nodes[node])


    for cg in genome.connections.values():
        if cg.enabled or show_disabled:
            input, output = cg.key
            a = node_names.get(input, str(input))
            b = node_names.get(output, str(output))
            connection_attrs = {"key": cg.key, "weight": cg.weight, "enabled": cg.enabled} # , "type": type(cg)
            
            a = a if next((x for x in list(G.nodes) if x.startswith(a)), None) is None else next((x for x in list(G.nodes) if x.startswith(a)), None)
            b = b if next((x for x in list(G.nodes) if x.startswith(b)), None) is None else next((x for x in list(G.nodes) if x.startswith(b)), None)

            edges[(a,b)] = connection_attrs
            # dot.add_edges_from([(a,b, connection_attrs)])

    G.add_edges_from(edges)
    print("edges: ", edges)

    idx_to_node_dict = {}
    for idx, node in enumerate(G.nodes):
        idx_to_node_dict[idx] = node

    # Plot

    fig, ax = plt.subplots(figsize=(12,12))
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
        try:
            node_attr = G.nodes[node]["attr"]
            text = '\n'.join(f'{k}: {v}' for k, v in node_attr.items())
            annot.set_text(text)
        except:
            # hovered over an input node :: there is no dictionary of items, just a name value for key attr
            node_attr = G.nodes[node]["attr"]
            text = node_attr
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
    edge_labels = {(u, v): f"{edges[(u, v)]['key']}({edges[(u, v)]['weight']})" for u, v in G.edges()}
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)

    # Add node labels
        
    def node_to_data(node):
        try:
            s = f"{G.nodes[node]['attr']['key']}\n{G.nodes[node]['attr']['activation']}\n{G.nodes[node]['attr']['aggregation']}\n{G.nodes[node]['attr']['response']}\n{G.nodes[node]['attr']['bias']}"
        except:
            s = f"{G.nodes[node]['attr']}"
        return s

    node_labels = {node: node_to_data(node) for node in G.nodes()}
    nx.draw_networkx_labels(G, pos, labels=node_labels)
    
    file_dir = os.path.dirname(os.path.realpath(__file__))
    path = os.path.join(file_dir, "data", "computational_graph")
    
    plt.title("Genetic Algorithm (Neuro-Evolution of Augmented Topologies (NEAT)) Learned Computational Graph")
    plt.savefig(path)
    plt.show()

    return G
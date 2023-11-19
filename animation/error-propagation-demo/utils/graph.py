import networkx as nx
import random
from matplotlib.offsetbox import OffsetImage, AnnotationBbox


def init_graph():
    """
    Create a graph
    :return: The networkx graph
    """
    # Create several smaller graphs (no particular reason for these numbers: 4 networks of 12 nodes each)
    graphs = [nx.random_geometric_graph(15, 0.4,2) for _ in range(2)]

    # Combine them into one graph
    G = nx.disjoint_union_all(graphs)

    # Initialize nodes
    for node in G.nodes():
        G.nodes[node]['status'] = 'smiley'  # smiley, affected, zombie
        G.nodes[node]['infected_steps'] = 0  # Count of steps since being infected
        G.nodes[node]['immutable'] = True if random.random() < 0.1 else False

    # Apply a breaking change to a random node in one of the graphs
    start_node = random.choice(list(graphs[random.randint(0, len(graphs) - 1)].nodes()))
    G.nodes[start_node]['status'] = 'affected'
    return G


def propagate_change(G):
    """
    Propagate the change in the graph
    :param G: The networkx graph
    :return: void
    """
    new_infections = []
    for node in G.nodes():
        if G.nodes[node]['status'] == 'affected' and not G.nodes[node]['immutable']:
            G.nodes[node]['infected_steps'] += 1
            if G.nodes[node]['infected_steps'] > 1:
                G.nodes[node]['status'] = 'zombie'
            for neighbor in G.neighbors(node):
                if G.nodes[neighbor]['status'] == 'smiley' and random.random() < 0.5:
                    new_infections.append(neighbor)
    for node in new_infections:
        G.nodes[node]['status'] = 'affected'

def update(num, G, ax, pos, smiley_face, affected_face, zombie_face):
    ax.clear()
    propagate_change(G)

    ax.set_title('What it should have been a normal working day at Bikeleasing...')

    for node in G.nodes():
        status = G.nodes[node]['status']
        image = smiley_face if status == 'smiley' \
            else affected_face if status == 'affected' \
            else zombie_face
        im = OffsetImage(image, zoom=0.1)
        im.image.axes = ax

        ab = AnnotationBbox(im,
                            pos[node],
                            xybox=(0, 0),
                            xycoords='data',
                            boxcoords="offset points",
                            frameon=False)
        ax.add_artist(ab)

    nx.draw_networkx_edges(G, pos, ax=ax)

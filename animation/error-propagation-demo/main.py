import matplotlib.pyplot as plt
import networkx as nx
from PIL import Image
from utils import resize_image, init_graph, update
from utils.animation import create_animation, save_animation

def run():
    # Resize downloaded icons
    resize_image('./icons/smiley.png', './icons/smiley_resized.png')
    resize_image('./icons/affected.png', './icons/affected_resized.png')
    resize_image('./icons/zombie.png', './icons/zombie_resized.png')

    # Load your resized custom icons
    smiley_face = Image.open('./icons/smiley_resized.png')
    affected_face = Image.open('./icons/affected_resized.png')
    zombie_face = Image.open('./icons/zombie_resized.png')

    # Initialize the graph and the initial states
    G = init_graph()

    # Setup visualization of the graph
    pos = nx.get_node_attributes(G, 'pos')
    fig, ax = plt.subplots(figsize=(10, 8))

    ani = create_animation(fig, update, G, ax, pos, smiley_face, affected_face, zombie_face)
    #save_animation(ani, 'error-propagation.gif', 'gif')
    save_animation(ani, 'error-propagation.mp4', 'video')


if __name__ == '__main__':
    run()
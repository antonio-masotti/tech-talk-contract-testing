from matplotlib.animation import FuncAnimation


def create_animation(fig, update_func, G, ax, pos, smiley_face, sad_face, zombie_face):
    return FuncAnimation(fig, update_func, fargs=(G, ax, pos, smiley_face, sad_face, zombie_face), frames=25, interval=1000, repeat=True)

def save_animation(ani, filename, type='gif',fps=1):
    """
    Save the animation as a gif or mp4
    :param ani: the matplotlib animation
    :param filename: the filename to save to
    :param type: 'gif' or 'video'
    :param fps: frames per second
    :return: void
    """
    if type == 'gif':
        ani.save(filename, writer='imagemagick', fps=fps)
    elif type == 'video':
        ani.save(filename, writer='ffmpeg', fps=fps)
    else:
        raise ValueError('Unknown type: {}'.format(type))
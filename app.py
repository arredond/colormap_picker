import cmasher as cmr
import streamlit as st
import matplotlib.pyplot as plt

from matplotlib.colors import ListedColormap

THUMBNAIL_WIDTH = 750

st.set_page_config(
    page_title="Colormap Picker", page_icon="🎨"
)

st.title('Colormap Picker')

def show_colors(color_list):
    """Simple helper to plot colors for a color name or list of colors"""
    data = [list(range(len(color_list)))]
    cmap = ListedColormap(color_list)

    fig, ax = plt.subplots()
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)

    ax.imshow(data, cmap=cmap)
    return fig
    # plt.show()


# colormap = st.text_input('Select a colormap')
colormap = st.selectbox('Select a colormap', cmr.get_cmap_list())
num_colors = st.slider('Number of colors', 0, 20, 9)
cmap_range = st.slider('Number of colors', 0.0, 1.0, (0.1, 0.9))
if colormap:
    color_list = cmr.take_cmap_colors(f'cmr.{colormap}', num_colors, cmap_range=cmap_range, return_fmt='hex')
    st.pyplot(show_colors(color_list))
    st.code(color_list)

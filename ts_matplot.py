import numpy as np
import matplotlib.pyplot as plt

from matplotlib.collections import PatchCollection
from matplotlib.patches import Circle, Polygon, Wedge

from matplotlib.widgets import Button, Slider

import matplotlib.cbook as cbook
import matplotlib.image as image

from matplotlib import transforms
'''
#with cbook.get_sample_data('logo2.png') as file:
#    im = image.imread(file)

# plt.figure(figsize=(10,6))
im1 = image.imread("image.jpg")
im2 = image.imread("png.png")

# The parametrized function to be plotted
def f(t, amplitude, frequency):
    return amplitude * np.sin(2 * np.pi * frequency * t)
t = np.linspace(0, 1, 1000)
# Define initial parameters
init_amplitude = 5
init_frequency = 3
# Create the figure and the line that we will manipulate

fig, ax = plt.subplots(figsize=(12,8))
line, = ax.plot(t, f(t, init_amplitude, init_frequency), lw=2)
ax.set_xlabel('Time [s]')
# adjust the main plot to make room for the sliders

fig.subplots_adjust(left=0.25, bottom=0.25)

# Make a horizontal slider to control the frequency.
axfreq = fig.add_axes([0.25, 0.1, 0.65, 0.03])
freq_slider = Slider(
    ax=axfreq,
    label='Frequency [Hz]',
    valmin=0.1,
    valmax=30,
    valinit=init_frequency,
)

# Make a vertically oriented slider to control the amplitude
axamp = fig.add_axes([0.1, 0.25, 0.0425, 0.63])
amp_slider = Slider(
    ax=axamp,
    label="A1",
    valmin=0,
    valmax=10,
    valinit=init_amplitude,
    orientation="vertical"
)

axamp2 = fig.add_axes([0.15, 0.25, 0.0425, 0.63])
amp_slider2 = Slider(
    ax=axamp2,
    label="A2",
    valmin=0,
    valmax=10,
    valinit=init_amplitude,
    orientation="vertical"
)

# The function to be called anytime a slider's value changes
def update(val):
    ax.clear()

    line.set_ydata(f(t, amp_slider.val, freq_slider.val))
    fig.canvas.draw_idle()
    ax.imshow(im1)
    tr = transforms.Affine2D().rotate_deg(amp_slider.val * 10)
    tr2 = transforms.ScaledTranslation(3.5, 0, fig.dpi_scale_trans)
    ax.imshow(im2, transform=tr + tr2 + ax.transData )

ax.imshow(im1)
tr = transforms.Affine2D().rotate_deg(amp_slider.val * 10)
tr2 = transforms.ScaledTranslation(3.5,0,fig.dpi_scale_trans)
ax.imshow(im2, transform=tr + tr2 + ax.transData)


# register the update function with each slider
freq_slider.on_changed(update)
amp_slider.on_changed(update)

# Create a `matplotlib.widgets.Button` to reset the sliders to initial values.
resetax = fig.add_axes([0.8, 0.025, 0.1, 0.04])
button = Button(resetax, 'Reset', hovercolor='0.975')
def reset(event):
    freq_slider.reset()
    amp_slider.reset()
button.on_clicked(reset)


#fig.figimage(im2, 25, 25, zorder=3, alpha=.9)
'''
# ref :
# https://matplotlib.org/stable/gallery/shapes_and_collections/patch_collection.html#sphx-glr-gallery-shapes-and-collections-patch-collection-py
plt.rcParams["figure.figsize"] = [12.0, 8.0]
#plt.rcParams["figure.autolayout"] = True

fig, ax = plt.subplots()
resolution = 50  # the number of vertices
N = 3
x = np.random.rand(N)
y = np.random.rand(N)
radii = 0.1*np.random.rand(N)
patches = []

for x1, y1, r in zip(x, y, radii):
    circle = Circle((x1, y1), r)
    patches.append(circle)

x = np.random.rand(N)
y = np.random.rand(N)
radii = 0.1*np.random.rand(N)
theta1 = 360.0*np.random.rand(N)
theta2 = 360.0*np.random.rand(N)

for x1, y1, r, t1, t2 in zip(x, y, radii, theta1, theta2):
    wedge = Wedge((x1, y1), r, t1, t2)
    patches.append(wedge)

# Some limiting conditions on Wedge
patches += [
    Wedge((.3, .7), .1, 0, 360),             # Full circle
    #Wedge((.7, .8), .2, 0, 360, width=0.05),  # Full ring
    #Wedge((.8, .3), .2, 0, 45),              # Full sector
    #Wedge((.8, .3), .2, 45, 90, width=0.10),  # Ring sector
]

for i in range(N):
    polygon = Polygon(np.random.rand(N, 2), closed=True)
    patches.append(polygon)

colors = 100 * np.random.rand(len(patches))
p = PatchCollection(patches, alpha=0.4)
p.set_array(colors)
ax.add_collection(p)
fig.colorbar(p, ax=ax)


plt.show()
# draw02.py
# 此版本
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.transforms as transforms
from matplotlib.patches import Circle, Polygon, Ellipse
from matplotlib.widgets import Button, Slider
import matplotlib.image as image

im1 = image.imread("ts_bk0.jpg")

rot = transforms.Affine2D().rotate_deg(90)

plt.rcParams["figure.figsize"] = [15, 8]
plt.rcParams["figure.autolayout"] = False
#plt.figure()
iCx, iCy = 0, 0
TS_Scale = 1.0
TS_Angle = 180
init_Dt = 3000      # Tons
init_Freq = 3000    # Hz
Dt = init_Dt  # 750,1500,2900,5600
Freq = init_Freq  # Hz

fig, ax = plt.subplots(figsize=(15,8))


fig.subplots_adjust(left=0.35, bottom=0.2)
# left, bottom, width, height

axfreq = fig.add_axes([0.05, 0.83, 0.2, 0.06])
freq_slider = Slider(
    ax=axfreq,
    label='Hz',
    valmin = 100,
    valmax = 10000,
    valinit = Freq,
)

axdt = fig.add_axes([0.05, 0.73, 0.2, 0.06])
dt_slider = Slider(
    ax=axdt,
    label='Ton',
    valmin = 600,
    valmax = 5600,
    valinit = Dt,
)

axrt = fig.add_axes([0.05, 0.63, 0.2, 0.06])
rt_slider = Slider(
    ax=axrt,
    label='Degree',
    valmin = 0,
    valmax = 360,
    valinit = TS_Angle,
)

ax.set_xlim([-200,200])
ax.set_ylim([-200,200])

# dt : tons
# rt : rotate angle
def ts_generate(dt):
    N = 90
    MinF2 = np.min([2000, Freq])/1000
    r0 = 11 * np.exp((-90) / 10) - 3 * np.exp(0) + 11 * np.log(dt) + 9 * np.log(MinF2) - 25
    ts_shape = [[iCx + np.cos(0) * r0, iCy + np.sin(0) * r0]]
    # rt_diff = rt * np.pi / 180.0
    for ix in range(N):
        theta0 = ix * np.pi / 180.0

        r0 = 11 * np.exp((ix - 90) / 10) - 3 * np.exp(-ix / 10) + 11 * np.log(dt) + 9 * np.log(MinF2) - 25
        r0 = r0 * TS_Scale
        ts_shape.append([iCx + np.cos(theta0) * r0, iCy + np.sin(theta0) * r0])
    for ix in range(N, 2*N):
        ts_shape.append([-ts_shape[2*N-ix][0],ts_shape[2*N-ix][1]])

    ts_shape.append([ts_shape[0][0],ts_shape[0][1]])
    return ts_shape
def update(val):
    # fig.clear()
    tr2 = transforms.ScaledTranslation(-2.2, -1.8, fig.dpi_scale_trans)
    # do not imshow here, impact on performance
    #ax.imshow(im1,transform=tr2+ax.transData)
    Freq = freq_slider.val
    Dt = dt_slider.val
    TS_Angle = rt_slider.val
    global Polygon0
    # Polygon0.remove()
    for p in ax.patches:
        p.set_visible(False)
        p.remove()
        print ('remove')
    ts_s = np.array( ts_generate(Dt))
    Polygon0 = Polygon( ts_s, fill=None, linewidth=5, color='blue', transform=transforms.Affine2D().rotate_deg(TS_Angle)+ ax.transData)
    #polygon = Polygon( ts_s, fill=True, linewidth=5, transform= ax.transData)
    ax.add_patch(Polygon0)


def reset(event):
    freq_slider.reset()
    dt_slider.reset()
    rt_slider.reset()

resetax = fig.add_axes([0.8, 0.025, 0.1, 0.04])
button = Button(resetax, 'Reset', hovercolor='0.975')
button.on_clicked(reset)

#plt.cla()
tr2 = transforms.ScaledTranslation(-2.2, -1.8, fig.dpi_scale_trans)
ax.imshow(im1, transform=tr2+ax.transData)
Polygon0 = Polygon( np.array( ts_generate(Dt)), fill=None, linewidth=5, color='orange', transform=transforms.Affine2D().rotate_deg(TS_Angle)+ ax.transData)

ax.text(0.05, 0.95, 'TS', transform=ax.transAxes,
            fontsize=16, fontweight='bold', va='top')


# fig2, ax2 = plt.subplots(figsize=(12,8))

xs, ys = zip(*ts_generate(750))
plt.plot(xs,ys, color='red',linewidth=5, transform=transforms.Affine2D().rotate_deg(TS_Angle)+ ax.transData)


'''
#ax.plot(xdata, ydata, "o")
trans = (fig.dpi_scale_trans +
         transforms.ScaledTranslation(-1, -1, ax.transData))
trans2 = transforms.Affine2D().rotate_deg(45)
circle = Ellipse((0, 0), 2, 4, angle=0,
                          fill=None,linewidth=5, transform=trans2+ ax.transData)
'''
#ax.add_patch(circle)
#ts_s = np.array([[0, 0], [30, 70], [60,60], [80,10]])
ts_s = np.array( ts_generate(Dt))

Polygon0 = Polygon( ts_s, fill=None, linewidth=5, color='blue', transform=transforms.Affine2D().rotate_deg(TS_Angle)+ ax.transData)
#polygon = Polygon( ts_s, fill=True, linewidth=5, transform= ax.transData)
ax.add_patch(Polygon0)


freq_slider.on_changed(update)
dt_slider.on_changed(update)
rt_slider.on_changed(update)
plt.show()


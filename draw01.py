# draw01.py
# 此版本作到初步繪製 TS 圖形, 先留存一份, 複製到 draw02.py 繼續開發
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.transforms as transforms
from matplotlib.patches import Circle, Polygon, Ellipse

rot = transforms.Affine2D().rotate_deg(90)

plt.rcParams["figure.figsize"] = [8, 8]
plt.rcParams["figure.autolayout"] = True
#plt.figure()
iCx, iCy = 0, 0
TS_Scale = 1.0
TS_Angle = 45

fig, ax = plt.subplots(figsize=(8,8))
ax.set_xlim([-200,200])
ax.set_ylim([-200,200])
N = 90

Dt = 5600  # 750,1500,2900,5600
Freq = 10  # kHz
MinF2 = np.min([2, Freq])
# dt : tons
# rt : rotate angle
def ts_generate(dt):
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

xs, ys = zip(*ts_generate(Dt))

plt.plot(xs,ys, color='green',linewidth=5)
plt.plot(xs,ys, color='green',linewidth=5,transform=rot)

ax.text(0.05, 0.95, 'TS', transform=ax.transAxes,
            fontsize=16, fontweight='bold', va='top')
#

# fig2, ax2 = plt.subplots(figsize=(12,8))

Dt = 750  # 750,1500,2900,5600

xs, ys = zip(*ts_generate(Dt))
plt.plot(xs,ys, color='black',linewidth=5, transform=transforms.Affine2D().rotate_deg(TS_Angle)+ ax.transData)


#ax.plot(xdata, ydata, "o")
trans = (fig.dpi_scale_trans +
         transforms.ScaledTranslation(0.2, 0.5, ax.transData))
trans2 = transforms.Affine2D().rotate_deg(45)
circle = Ellipse((0, 0), 2, 4, angle=0,
                          fill=None,linewidth=5, transform=trans2+ ax.transData)
#ax.add_patch(circle)
#ts_s = np.array([[0, 0], [30, 70], [60,60], [80,10]])
ts_s = np.array( ts_generate(3000))
polygon = Polygon( ts_s, fill=None, linewidth=5, color='orange', transform=transforms.Affine2D().rotate_deg(TS_Angle)+ ax.transData)
#polygon = Polygon( ts_s, fill=True, linewidth=5, transform= ax.transData)
ax.add_patch(polygon)


plt.show()


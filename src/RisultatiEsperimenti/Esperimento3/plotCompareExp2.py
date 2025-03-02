import matplotlib.pyplot as plt
import matplotlib as mpl

mpl.rcParams['axes.linewidth'] = 0
mpl.rcParams['ytick.left'] = False
mpl.rcParams['xtick.bottom'] = False

folders = ["C1", "C2", "C3", "C4", "C5", "C6"]
folders2 = ["/4. aligned_origin_data", "/5. results", "/5. results", "/4. aligned_origin_data"]
files = ["/Exp2.png", "/Exp2ape.png", "/Exp2rpe.png", "/Exp2error.png"]

fig = plt.figure(figsize=(4,6)) # Notice the equal aspect ratio
ax = [fig.add_subplot(6,4,i+1) for i in range(24)]

r = 0
c = 0
for a in ax:
    a.set_xticklabels([])
    a.set_yticklabels([])
    #a.set_aspect('equal')
    im = plt.imread(folders[r] + folders2[c] + files[c])
    a.imshow(im)
    if c == 0:
        a.set_title("Case " + str(r+1), fontsize=8)
    c = c+1
    if c == 4:
        c = 0
        r = r+1

fig.subplots_adjust(wspace=0, hspace=0)

plt.savefig('ConfrontoExp2.png', dpi=2000)
plt.show()
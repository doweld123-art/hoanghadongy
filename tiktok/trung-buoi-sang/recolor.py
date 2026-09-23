# Đổi phông nền kem của ảnh gốc sang xanh nước biển
import numpy as np
from PIL import Image
from collections import deque

im = np.asarray(Image.open("goc.png").convert("RGB")).astype(float)
h, w, _ = im.shape
mx, mn = im.max(2), im.min(2)
bright = mx > 200
lowsat = (mx - mn) < 30
LIST_TOP = 244
STEP = 9
cand = bright & lowsat
cand[LIST_TOP:] = False

# flood fill từ viền ảnh và vùng trống phía trên, để không ăn vào các ô trắng của danh sách
seen = np.zeros((h, w), bool)
q = deque()
for x in range(w):
    for y in (0, 1, 2):
        if cand[y, x]: q.append((y, x)); seen[y, x] = True
for y in range(h):
    for x in (0, w - 1):
        if cand[y, x] and not seen[y, x]: q.append((y, x)); seen[y, x] = True
while q:
    y, x = q.popleft()
    for dy, dx in ((1, 0), (-1, 0), (0, 1), (0, -1)):
        ny, nx = y + dy, x + dx
        if 0 <= ny < h and 0 <= nx < w and cand[ny, nx] and not seen[ny, nx]:
            # dừng ở mép ô danh sách (ô trắng tinh, viền cam)
            if abs(im[ny, nx] - im[y, x]).sum() > STEP: continue
            seen[ny, nx] = True; q.append((ny, nx))
# khăn trải dưới đĩa trứng giữ màu gốc: chỉ tô phần nền bên phải đĩa ở dải dưới
yy, xx = np.mgrid[0:h, 0:w]
seen &= yy < 190
Image.fromarray((seen * 255).astype(np.uint8)).save("mask.png")

# Tô xanh nước biển (giữ nguyên vân sáng tối của nền cũ), viền mềm để không răng cưa
from PIL import ImageFilter
m = Image.fromarray((seen * 255).astype(np.uint8)).filter(ImageFilter.MaxFilter(3)).filter(ImageFilter.GaussianBlur(0.8))
a = np.asarray(m).astype(float) / 255
# chuyển mềm từ nền xanh sang ảnh khăn phía dưới bên trái
k = np.clip((xx - 235) / 60, 0, 1)
a *= np.clip((160 + 30 * k - yy) / (32 + 13 * k), 0, 1)
a = a[..., None]
top, bot = np.array([178, 226, 248.]), np.array([30, 136, 208.])
t = np.clip(np.arange(h) / LIST_TOP, 0, 1)[:, None, None]
blue = top * (1 - t) + bot * t
shade = np.clip(im.mean(2, keepdims=True) / 241.0, 0.6, 1.05)
out = im * (1 - a) + np.clip(blue * shade, 0, 255) * a
Image.fromarray(out.astype(np.uint8)).save("nen-xanh.png")

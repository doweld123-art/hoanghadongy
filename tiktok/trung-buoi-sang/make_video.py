# Dựng video TikTok 1080x1920 từ ảnh nen-xanh.png
import subprocess
import numpy as np
import imageio_ffmpeg
from PIL import Image, ImageDraw, ImageFilter, ImageFont

W, H, FPS = 1080, 1920, 30
HANDLE = "@ha666222"
FONT = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"

src = Image.open("nen-xanh.png").convert("RGB").crop((0, 0, 321, 571))  # bỏ dải trắng lỗi ở mép phải
S = W / src.width
base = src.resize((W, round(src.height * S)), Image.LANCZOS).filter(ImageFilter.UnsharpMask(2, 80, 2))
base = base.crop((0, 0, W, H)) if base.height >= H else base

# Ranh giới 9 dòng trong ảnh gốc (toạ độ y)
edges = [243 + i * 35.25 for i in range(10)]
rows = [(edges[i] * S, edges[i + 1] * S) for i in range(9)]

INTRO, PER_ROW, OUTRO = 2.5, 1.2, 3.5
DUR = INTRO + PER_ROW * 9 + OUTRO


def font(size):
    return ImageFont.truetype(FONT, size)


def ease(t):
    t = min(max(t, 0), 1)
    return t * t * (3 - 2 * t)


def zoom(img, scale, cy):
    """Phóng to quanh tâm ngang giữa ảnh, tâm dọc cy."""
    w, h = W / scale, H / scale
    top = min(max(cy - h / 2, 0), H - h)
    left = (W - w) / 2
    return img.resize((W, H), Image.LANCZOS, box=(left, top, left + w, top + h))


def pill(draw, xy, text, size, fill, color):
    f = font(size)
    l, t, r, b = draw.textbbox((0, 0), text, font=f)
    x, y = xy
    pad = size * 0.55
    draw.rounded_rectangle((x - (r - l) / 2 - pad, y - pad * 0.6, x + (r - l) / 2 + pad, y + (b - t) + pad * 0.9),
                           radius=size, fill=fill)
    draw.text((x - (r - l) / 2 - l, y - t), text, font=f, fill=color)


def frame(t):
    if t < INTRO:
        # mở đầu: phóng to vào tiêu đề rồi lùi ra toàn cảnh
        k = ease(t / INTRO)
        return zoom(base, 1.2 - 0.2 * k, 330 + (H / 2 - 330) * k)

    i = int((t - INTRO) // PER_ROW)
    if i < 9:
        img = base.copy()
        lt = (t - INTRO - i * PER_ROW) / PER_ROW
        y0, y1 = rows[i]
        # làm tối phần danh sách, riêng dòng đang nói sáng lên và nhô ra
        dim = Image.new("RGBA", (W, H), (0, 0, 0, 0))
        d = ImageDraw.Draw(dim)
        d.rectangle((0, rows[0][0] - 6, W, H), fill=(0, 20, 45, 120))
        img = Image.alpha_composite(img.convert("RGBA"), dim)
        pop = 1 + 0.08 * ease(lt / 0.25)
        row = base.crop((0, int(y0), W, int(y1)))
        row = row.resize((int(W * pop), int(row.height * pop)), Image.LANCZOS)
        rx, ry = (W - row.width) // 2, int((y0 + y1) / 2 - row.height / 2)
        glow = Image.new("RGBA", (W, H), (0, 0, 0, 0))
        ImageDraw.Draw(glow).rounded_rectangle((rx - 6, ry - 6, rx + row.width + 6, ry + row.height + 6),
                                               radius=28, fill=(80, 190, 255, 255))
        img = Image.alpha_composite(img, glow.filter(ImageFilter.GaussianBlur(14)))
        img.paste(row, (rx, ry))
        return img.convert("RGB")

    # kết: làm mờ nền, kêu gọi lưu & theo dõi
    k = ease((t - INTRO - PER_ROW * 9) / 0.5)
    img = base.filter(ImageFilter.GaussianBlur(12 * k)).convert("RGBA")
    ov = Image.new("RGBA", (W, H), (8, 60, 110, int(150 * k)))
    img = Image.alpha_composite(img, ov)
    if k > 0.5:
        d = ImageDraw.Draw(img)
        pill(d, (W / 2, 720), "Lưu lại để dùng dần nhé!", 64, (255, 255, 255, 240), (20, 80, 140))
        pill(d, (W / 2, 900), f"Theo dõi {HANDLE}", 72, (242, 115, 0, 255), (255, 255, 255))
        f = font(34)
        note = "Thông tin tham khảo, không thay thế tư vấn của bác sĩ"
        l, tt, r, b = d.textbbox((0, 0), note, font=f)
        d.text(((W - (r - l)) / 2, 1120), note, font=f, fill=(230, 240, 250))
    return img.convert("RGB")


ff = imageio_ffmpeg.get_ffmpeg_exe()
cmd = [ff, "-y", "-f", "rawvideo", "-pix_fmt", "rgb24", "-s", f"{W}x{H}", "-r", str(FPS), "-i", "-",
       "-f", "lavfi", "-i", "anullsrc=r=44100:cl=stereo",
       "-c:v", "libx264", "-preset", "slow", "-crf", "18", "-pix_fmt", "yuv420p", "-profile:v", "high",
       "-c:a", "aac", "-b:a", "128k", "-shortest", "-movflags", "+faststart", "video-tiktok.mp4"]
p = subprocess.Popen(cmd, stdin=subprocess.PIPE, stderr=subprocess.DEVNULL)
for n in range(int(DUR * FPS)):
    p.stdin.write(np.asarray(frame(n / FPS)).tobytes())
p.stdin.close()
p.wait()
for t in (0.1, 5.3, DUR - 0.5):
    frame(t).save(f"xem-truoc-{t:.1f}s.jpg", quality=85)
print("done", DUR, "s")

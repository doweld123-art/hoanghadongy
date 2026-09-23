# Hoàng Hà Đông Y – bộ công cụ traffic TikTok

- `index.html` – landing page (link bio) tối ưu cho điện thoại: nút Zalo / gọi / Messenger / chỉ đường, form để lại số, gắn TikTok Pixel và ghi nhận UTM + `ttclid`.
- `assets/config.js` – **sửa file này**: số điện thoại, Zalo, Messenger, bản đồ, link TikTok, TikTok Pixel ID, URL nhận lead.
- `docs/tiktok-traffic-plan.md` – kế hoạch nội dung 30 ngày, hook mẫu, hashtag, quảng cáo, chỉ số và lưu ý tuân thủ.

## Chạy thử

```bash
python3 -m http.server 8000
# mở http://localhost:8000/?utm_source=tiktok
```

## Đưa lên mạng

Trang là HTML tĩnh, đăng miễn phí được bằng GitHub Pages (Settings → Pages → chọn nhánh), Netlify hoặc Vercel. Sau đó dán link vào bio TikTok kèm UTM:

```
https://<domain>/?utm_source=tiktok&utm_medium=bio&utm_campaign=organic
```

## Sự kiện Pixel

| Sự kiện | Khi nào |
|---|---|
| `PageView` | Mở trang |
| `Contact` | Bấm Zalo / gọi / Messenger / chỉ đường |
| `SubmitForm` | Gửi form thành công |

Nếu chưa cấu hình `leadEndpoint`, lead chỉ được lưu tạm trong trình duyệt của người gửi, nên cần cấu hình (ví dụ Google Apps Script ghi vào Google Sheet) trước khi chạy thật.

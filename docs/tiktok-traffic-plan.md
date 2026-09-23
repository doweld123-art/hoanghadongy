# Kế hoạch xây traffic TikTok – Hoàng Hà Đông Y

Mục tiêu: kéo người xem từ TikTok về landing page (`index.html`) và chuyển thành khách nhắn Zalo, gọi điện hoặc để lại số.

## 1. Thiết lập kênh (tuần 0)

- [ ] Chuyển sang **Tài khoản doanh nghiệp** (Business Account), danh mục *Sức khỏe & Sắc đẹp*.
- [ ] Tên hiển thị: `Hoàng Hà Đông Y`. Handle ngắn, dễ nhớ.
- [ ] Bio 3 dòng: đang làm gì, cho ai, và CTA. Ví dụ:
  > Đông y gia truyền – chăm sóc xương khớp, tiêu hóa, giấc ngủ
  > Tư vấn miễn phí 👇
- [ ] Gắn link bio là landing page, có UTM:
  `https://<domain>/?utm_source=tiktok&utm_medium=bio&utm_campaign=organic`
- [ ] Tạo TikTok Pixel trong Ads Manager, dán ID vào `assets/config.js`.
- [ ] Ảnh đại diện: logo hoặc ảnh thầy thuốc mặc áo blouse, nền sáng.

## 2. Trụ cột nội dung (content pillars)

| Trụ cột | Tỷ lệ | Mục đích | Ví dụ |
|---|---|---|---|
| Kiến thức nhanh | 40% | Viral, lên đề xuất | "3 thói quen buổi sáng làm dạ dày yếu đi" |
| Hậu trường nhà thuốc | 25% | Tạo niềm tin | Sắc thuốc, phơi dược liệu, bốc thuốc |
| Hỏi đáp / trả lời bình luận | 20% | Tương tác | Dùng tính năng *Trả lời bằng video* |
| Câu chuyện thầy thuốc / gia truyền | 10% | Thương hiệu | Nghề truyền mấy đời, vì sao theo nghề |
| CTA / ưu đãi | 5% | Chuyển đổi | "Nhắn Zalo để được bắt mạch miễn phí" |

## 3. Công thức 1 video (15–45 giây)

1. **Hook 0–2s**: câu hỏi hoặc câu gây tò mò, có chữ to trên màn hình.
2. **Nội dung 3–30s**: 1 ý duy nhất, nói nhanh, cắt cảnh 2–3 giây một lần.
3. **CTA cuối**: "Lưu lại kẻo quên", "Bình luận *KHỚP* để mình gửi thêm", "Link tư vấn ở bio".

Mẫu hook:
- "Đừng uống nước ấm buổi sáng nếu bạn chưa biết điều này…"
- "Đau lưng mỗi sáng thức dậy? Có thể do…"
- "Ông bà mình ngày xưa làm gì để ngủ ngon?"
- "Bình luận hỏi: *Mất ngủ nên uống gì?* – mình trả lời nhé."
- "3 loại lá quanh nhà mà ít ai biết công dụng."

## 4. Lịch đăng 30 ngày

- Tần suất: **1–2 video/ngày**, tối thiểu 5 ngày/tuần.
- Khung giờ gợi ý (giờ VN): **11h30–12h30**, **19h30–21h30**. Sau 2 tuần, đối chiếu *Analytics > Người theo dõi* để chỉnh giờ.
- Live 1–2 buổi/tuần (20h–21h) để hỏi đáp; ghim bình luận có link Zalo.

| Tuần | Trọng tâm | Việc chính |
|---|---|---|
| 1 | Thử nghiệm | 10 video, 5 chủ đề khác nhau, xem chủ đề nào giữ chân tốt |
| 2 | Nhân bản | Làm thêm 3–5 video theo chủ đề thắng ở tuần 1 |
| 3 | Tương tác | Series nhiều phần ("Phần 1/3"), trả lời bình luận bằng video, bắt đầu Live |
| 4 | Chuyển đổi | Đẩy CTA về Zalo/landing, chạy thử quảng cáo (mục 6) |

## 5. Hashtag

Dùng 3–5 hashtag: 1–2 rộng + 2–3 ngách.
- Rộng: `#suckhoe` `#meohay` `#xuhuong`
- Ngách: `#dongy` `#yhoccotruyen` `#thuocnam` `#xuongkhop` `#matngu` `#tieuhoa`
- Thương hiệu: `#hoanghadongy`

## 6. Quảng cáo (khi đã có 5–10 video tốt)

- **Spark Ads**: chọn video organic có tỷ lệ xem hết cao để boost, giữ tương tác trên video gốc.
- Mục tiêu chiến dịch: *Lượt truy cập trang web* → sau khi Pixel có dữ liệu thì chuyển sang *Chuyển đổi* (sự kiện `SubmitForm` / `Contact`).
- Ngân sách thử: 200–300k/ngày/nhóm quảng cáo, chạy 3–5 ngày rồi tắt nhóm kém.
- Nhắm mục tiêu: 30–60 tuổi, bán kính quanh phòng khám (nếu khách chủ yếu đến trực tiếp).
- Link quảng cáo có UTM: `?utm_source=tiktok&utm_medium=paid&utm_campaign=<ten_chien_dich>`

## 7. Chỉ số theo dõi hằng tuần

| Chỉ số | Ngưỡng tốt | Nếu thấp |
|---|---|---|
| Tỷ lệ xem hết (completion) | > 30% | Rút ngắn video, hook mạnh hơn |
| Thời gian xem trung bình | > 50% độ dài | Cắt bớt đoạn mở đầu |
| Lượt chia sẻ + lưu / lượt xem | > 1% | Nội dung hữu ích hơn, dạng "lưu lại" |
| Lượt xem hồ sơ → click link bio | > 5% | Sửa bio, nhắc "link ở bio" trong video |
| Click → lead (landing page) | > 10% | Rút gọn form, đẩy nút Zalo lên đầu |

## 8. Lưu ý tuân thủ (rất quan trọng với ngành y dược)

TikTok và luật Việt Nam siết chặt nội dung y tế. Vi phạm có thể bị bóp tương tác, gỡ video hoặc khóa kênh.

- **Không** khẳng định chữa khỏi bệnh ("khỏi hẳn", "dứt điểm 100%", "thay thế thuốc tây").
- **Không** dùng ảnh trước/sau, không đưa lời chứng thực kiểu "uống 1 tuần hết đau".
- **Không** nêu tên bệnh nặng (ung thư, tiểu đường…) kèm sản phẩm.
- Quảng cáo trả phí về dịch vụ khám chữa bệnh / thuốc cần giấy phép và nội dung được xác nhận theo Luật Quảng cáo; kiểm tra chính sách quảng cáo y tế của TikTok trước khi chạy.
- Luôn kèm câu: *"Thông tin tham khảo, hãy thăm khám để được tư vấn phù hợp."*
- Ưu tiên nội dung **giáo dục, lối sống, hậu trường** thay vì bán sản phẩm trực tiếp.

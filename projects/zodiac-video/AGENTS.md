# Điểm vào workflow video Zodiac

Đây là entrypoint riêng cho workflow video StoryGraph của Zodiac Controversy Factory. Không dùng entrypoint hoặc rule viết Series/Carousel cho tác vụ video.

## Thứ tự đọc bắt buộc

1. Đọc toàn bộ `rules/video-direction.md` trước khi biên tập, đạo diễn hoặc review story video.
2. Dùng Writer Context do ứng dụng xuất làm nguồn runtime cho idea, claim/evidence, asset allowlist, directing options, StoryGraph schema và response template.
3. Nếu thiếu rule, evidence, allowlist hoặc contract cần thiết, dừng và báo rõ phần thiếu; không tự điền bằng trí nhớ.

## Phạm vi

- Mỗi lần chỉ làm video cho một idea đã chọn; có thể là một cung trong Series hoặc một idea độc lập.
- Không nhận Carousel hoặc cả batch Series.
- Rule trong thư mục này chỉ áp dụng cho workflow video.

## Đồng bộ asset cho agent kết nối GitHub

- Asset runtime được phép dùng vẫn do `allowed_assets` trong Writer Context quyết định; repo này chỉ chứa bản SVG để agent kết nối GitHub có thể xem và chọn đúng asset.
- Đồng bộ nguyên file SVG được catalog app duyệt từ `assets/video/<art-direction-id>/` sang `projects/zodiac-video/assets/<art-direction-id>/`, giữ nguyên tên file và nội dung. Không thêm asset chỉ có trong repo này vào StoryGraph.
- Mỗi lần thêm, thay thế hoặc gỡ asset video ở app, cập nhật bản mirror tương ứng trong repo này cùng task và push thay đổi lên GitHub trước khi coi asset mới là khả dụng cho agent kết nối repo.
- Dùng `agent_asset_path` trong Writer Context để mở SVG mirror. Nếu field đó chưa có, tra theo `src` trong `allowed_assets` và giữ phần đường dẫn sau `assets/video/` dưới `projects/zodiac-video/assets/`.
- Khi chọn, chỉ trả ID nằm trong `allowed_assets`; mirror hoặc manifest cũ không được phép vượt qua catalog/fingerprint runtime.

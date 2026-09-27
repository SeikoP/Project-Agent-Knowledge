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

## Writer Context v3

- Khi `video_story_writer_context.version` là `3`, hợp đồng output runtime duy nhất là `response_template.video_story_draft`; trả đúng một root `video_story_draft` với `version`, `idea_id`, hai fingerprint và `story`.
- Chỉ viết các trường trong `story_draft_schema`: spine, beats, sequences/shots/reveals, continuity objects, asset needs và narration. App dựng StoryGraph đầy đủ sau khi validate; không gửi lại claim/evidence, premise, asset `src`, renderer, canvas, layout, audio, subtitle hoặc metadata.
- Trong rule đạo diễn cũ, các đường dẫn bắt đầu `graph.` mô tả vị trí ngữ nghĩa trong StoryGraph; với context v3 hãy ánh xạ chúng theo `story_draft_schema` và trả `story.*`, không tạo thêm trường `graph`.
- Chọn asset bằng ID từ `allowed_assets`. Với nhu cầu mới, dùng `status="open"` và `resolved_asset_id=null`; không tự đổi trạng thái asset need đã được app/người dùng xác nhận.
- Nếu context có `current_story_status="fresh"`, biên tập toàn bộ `current_story`; nếu trạng thái khác, không dùng StoryGraph cũ làm nguồn.
- Giữ trình tự preview nội dung/đạo diễn trong cuộc trò chuyện → chờ người dùng duyệt → mới trả JSON. Output v2 chỉ dùng khi ứng dụng đưa Writer Context v2 cũ.

Các tag `pack:*` chỉ nhóm asset theo chức năng, không phải nguồn xác định visual direction.


## Art direction and production asset contract

Production direction hiện hành là Storybook Expressive Chibi v1. Nguồn visual chuẩn duy nhất là [design/storybook-expressive-chibi-v1.md](design/storybook-expressive-chibi-v1.md); mọi con số dùng cho validation lấy từ [design/tokens.storybook-expressive-chibi.v1.json](design/tokens.storybook-expressive-chibi.v1.json). Contract metadata nằm tại [design/asset-metadata.v1.schema.json](design/asset-metadata.v1.schema.json). Rule đạo diễn video phải tuân theo nguồn chuẩn này.

Các direction `chibi-object-theater` và `chibi-human-story` chỉ là legacy/historical, không dùng làm visual source-of-truth hoặc trộn vào catalog Storybook Expressive Chibi v1. SVG trong `design/references/` chỉ để đối chiếu, không phải runtime asset.

Semantic category không tự suy ra runtime role. Đọc `runtime_compatibility` tường minh; effects và overlays không có mapping mặc định trong engine hiện tại. Chỉ expose khi mapping trực tiếp được hỗ trợ hoặc adapter đã đăng ký. `allowed_assets` trong Writer Context vẫn là authority duy nhất cho agent chọn asset.

Chỉ mirror asset production được catalog app duyệt vào `projects/zodiac-video/assets/storybook-expressive-chibi/`. Mỗi lần cập nhật phải đồng bộ nguyên file được duyệt, metadata/direction version và catalog fingerprint; không thêm asset riêng từ repo Knowledge vào allowlist runtime.

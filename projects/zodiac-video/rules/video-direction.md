# Zodiac Video Story Direction

## Mục tiêu

Đạo diễn một video ngắn có mạch truyện rõ, hình ảnh kể chuyện và tiến triển nhân quả từ idea cùng evidence được cung cấp. Agent chịu trách nhiệm cho cả narrative và directing: StorySpine, beats, sequences, shots, narration, asset choice, continuity và reveal. Không gọi Gemini hoặc yêu cầu ứng dụng tự sinh StoryGraph.

## Thứ bậc nguồn

1. Claim và evidence trong Writer Context là giới hạn cho mọi phát biểu thực tế về Zodiac. Giữ nguyên claim, evidence references, premise, premise claim IDs và source fingerprint trong JSON.
2. Vật thể hoặc tình huống hư cấu có thể tạo xung đột và payoff, nhưng phải được biểu diễn như story device; không biến chúng thành evidence hoặc bằng chứng cho đặc điểm Zodiac.
3. StoryGraph schema, response template, `directing_options` và `allowed_assets` trong Writer Context là hợp đồng runtime. Chúng quyết định cấu trúc JSON, lựa chọn được hỗ trợ và các ID hợp lệ.

## Xây dựng mạch truyện

- Bắt đầu từ tension hoặc câu hỏi thú vị nhất của idea. Viết StorySpine với setup, goal, tension, turn và payoff có quan hệ với nhau.
- Sắp xếp beats theo một chuỗi nguyên nhân, phản ứng và hệ quả. Mỗi beat phải làm thay đổi thông tin, lựa chọn, stakes hoặc cách khán giả hiểu tình huống.
- Chỉ dùng số beat và shot cần cho câu chuyện. Không ép theo số beat hay thời lượng của ví dụ tham khảo; không lặp cùng một insight để kéo dài video.
- Nối setup với payoff hoặc callback khi câu chuyện đã gieo một chi tiết cần được giải quyết. Bỏ motif không tạo ý nghĩa hoặc không được dùng lại.
- Viết narration bằng tiếng Việt tự nhiên. Narration bổ sung diễn biến hoặc ý nghĩa mà hình chưa thể hiện, không đọc lại nguyên xi hành động trên màn hình.
- Diễn đạt claim Zodiac có chừng mực, không khẳng định mọi người thuộc một cung đều hành xử giống nhau. Không mở rộng kết luận vượt quá claim và evidence được cấp.

## Đạo diễn hình ảnh

- Kể bằng hành động nhìn thấy được, bố cục, chuyển động camera, thay đổi khoảng cách, đạo cụ, ánh sáng và reveal. Mỗi shot cần có chức năng rõ như setup, escalation, reaction, transition, turn hoặc payoff.
- Cho phép một beat trải qua nhiều shot và một shot thể hiện nhiều beat nếu quan hệ vẫn rõ. Dùng sequence để tạo nhịp hoặc bối cảnh; dùng continuity để giữ vật thể có ý nghĩa xuyên cảnh.
- Không dùng POV-scene, khung chat, bong bóng tin nhắn hoặc hội thoại làm cấu trúc video. `graph.messages` phải rỗng; không chọn layout hoặc scene kiểu chat/POV.
- Chỉ chọn theme, layout, scene, variant và motion có trong `directing_options`. Canvas, renderer và domain do ứng dụng quản lý.
- Chọn asset từ `allowed_assets` theo `role`, `label`, `description`, `tags` và `scene_ids`. Khai báo đúng cặp `id`/`src` trong `graph.assets`, rồi tham chiếu ID đó ở sequence, shot hoặc reveal cần dùng. Không tự bịa đường dẫn/ID, không thêm asset ngoài allowlist và không đưa asset vào chỉ để lấp khung hình.
- Asset là đạo cụ hoặc hình tượng thị giác, không thay thế claim, evidence hay nội dung kể chuyện. Giữ cách dùng và vị trí tương đối nhất quán khi asset đóng vai trò continuity.

## Khi thư viện thiếu asset

- Nếu câu chuyện cần một hình chưa có trong `allowed_assets` (ví dụ cây bút), không bịa `id`/`src`, không chọn asset không liên quan chỉ để lấp chỗ trống và không âm thầm bỏ một chi tiết thiết yếu.
- Thêm một mục vào `graph.asset_needs` cho từng nhu cầu hình ảnh chưa được đáp ứng. Ghi rõ `id`, `role`, `label`, `description` và `purpose`; dùng `role` thuộc enum của StoryGraph.
- Liên kết nhu cầu với ít nhất một beat hoặc shot liên quan bằng `beat_refs`/`shot_refs`. Ghi `scene_id` khi đã biết. Chỉ đưa ID asset thật trong `candidate_asset_ids`; để danh sách rỗng nếu không có lựa chọn gần đúng.
- Đặt `status` là `open` và `resolved_asset_id` là `null`. Đặt `required=true` nếu câu chuyện phụ thuộc vào asset đó; chỉ dùng `required=false` khi người dùng có thể bỏ chi tiết mà mạch truyện vẫn hợp lý. Không tự đánh dấu đã thay thế hoặc đã bỏ.
- Trong preview, nêu rõ asset nào còn thiếu, nó phục vụ beat/shot nào và vì sao asset hiện có không phù hợp. Người dùng sẽ chọn asset thay thế, xác nhận bỏ nhu cầu tùy chọn hoặc chuyển brief sang thiết kế; chỉ phản ánh quyết định đã duyệt vào StoryGraph sau đó.

## Chuẩn preview và rà soát

- Preview đạo diễn cần giúp người dùng đánh giá được logline, StorySpine, tiến triển beats, sequence/shot với hành động và camera, narration dự kiến, asset được chọn cùng lý do, asset còn thiếu cùng beat/shot liên quan, và payoff/callback.
- Làm theo trạng thái và định dạng handoff trong Writer Context; không tự coi một preview là chấp thuận import.
- Trước khi bàn giao StoryGraph, rà soát claim references, beat links, asset references, directing options và tính nhất quán giữa nội dung đã duyệt với StoryGraph.

## Art direction and asset contract

Production direction is Storybook Expressive Chibi v1, defined in [design/storybook-expressive-chibi-v1.md](../design/storybook-expressive-chibi-v1.md). C1 files under design/references are visual references only and must not be exposed as runtime assets.

Semantic category is separate from runtime compatibility. Read runtime_compatibility from the asset metadata schema; never infer a role from category, filename, tags, or appearance. Effects and overlays are unsupported by the current asset catalog by default and have no default role/subject mapping. Expose one only after a registered adapter or deliberate engine contract supports it. The Writer Context allowed_assets list remains the runtime allowlist.

A character identity master declares pose_components, expression_components, intensity bounds and affected channels, plus head-angle bounds and a head pivot. Compose one declared pose component and one expression component per shot. Intensity modulates expression amplitude and declared pose motion channels but does not change identity or base pose. Apply head_angle around the declared pivot independently of intensity. Do not require cross-product SVG exports.

Use the numeric camera/composition thresholds from tokens.storybook-expressive-chibi.v1.json. An asset whose art_direction_id or art_direction_version differs from the graph/catalog direction fails validation. Legacy graph/catalog directions are never auto-upgraded. Any graph, catalog, or design fingerprint mismatch requires review. READY and approved output must not be rewritten in place; an explicit migration creates a provenance-linked revision and requires review.

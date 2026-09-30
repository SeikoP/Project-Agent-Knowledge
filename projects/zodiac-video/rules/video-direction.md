# Zodiac Video Story Direction

## Mục tiêu

Đạo diễn một video ngắn có mạch truyện rõ, hình ảnh kể chuyện và tiến triển nhân quả từ idea cùng evidence được cung cấp. Agent xây dựng `StoryOutline`, `ScenePlan[]` rồi `VisualScene[]`; ứng dụng kiểm tra draft và dựng StoryGraph đầy đủ. Không gọi Gemini hoặc yêu cầu ứng dụng tự sinh nội dung thay cho draft đã được duyệt.

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

- Làm theo đúng thứ tự `StoryOutline → ScenePlan[] → VisualScene[]`. Mỗi ScenePlan có đúng một VisualScene với `scene_plan_id` tương ứng. Scene N+1 phải có lý do hình ảnh bắt nguồn từ diễn biến trước.
- VisualScene mô tả environment/stage, actor, acting intent, interaction, gaze/focus, story object và state, camera purpose/profile, composition intent, treatment intent, typography role. Nó không chứa tọa độ, scale, transform, SVG component ID, reveal part hay renderer implementation.
- Chọn environment và asset ID chỉ từ `asset_catalog.scenes` và `allowed_assets`. Ghi `background_asset_id`, `set_dressing_asset_ids`, character master `asset_id`, và continuity object ID; không tự viết `src` hoặc đường dẫn.
- Chọn một character master ổn định cho mỗi actor. Dùng pose/expression nằm trong `supported_poses`/`supported_expressions`; mô tả acting cụ thể, chọn `gaze_target_id`, interaction và focus tới actor/object đang hiện.
- Story object dùng `continuity_id` đã khai báo trong `continuity_objects`; giữ nguyên asset identity. Khi đổi state, relation hoặc actor anchor, đặt `transition_from` đúng state trước và nêu `transition_reason`. Không tạo ID mới để giả vờ vật thể mới xuất hiện.
- `sequence_id` giữ nguyên khi tiếp tục cùng bối cảnh và background; đổi ID khi câu chuyện chuyển sang environment/background khác. Tọa độ và lớp dựng sẽ do ứng dụng suy ra từ composition intent.
- Camera, composition, treatment hay chữ thay đổi riêng lẻ không phải visual progression. Phải có thay đổi acting/gaze/interaction/object state hoặc stage mà câu chuyện yêu cầu.
- Không dùng POV-scene, khung chat, bong bóng tin nhắn hoặc hội thoại làm cấu trúc video. Writer Context v5 không có trường messages; không tự thêm trường đó.
- Chỉ đạo dựa trên `allowed_assets` và các enum trong `visual_contract`/`directing_options`. Không yêu cầu writer chọn thời lượng, reveal timing, chuyển động part hoặc tọa độ.
- Asset là đạo cụ hoặc hình tượng thị giác, không thay thế claim, evidence hay nội dung kể chuyện. Vật thể giữ state và vị trí tương đối nhất quán khi đóng vai continuity.

## Art direction và typography

- Production art direction là `storybook-expressive-chibi@1`. Catalog và `allowed_assets` là authority; giữ identity người chibi, silhouette, expression và shape language theo direction này. Không chuyển sang direction khác trong cùng graph.
- Đạo cụ và phong cảnh luôn vô tri: không gắn mặt, tay, chân, biểu cảm hoặc vai diễn cho ly, thẻ giấy, đồ ăn, bàn ghế hay vật dụng. Chọn asset semantic đúng mục đích và scene compatibility.
- Nhân vật là nhân vật hư cấu cho tình huống; không khẳng định họ đại diện mọi người thuộc cung đó. Biểu cảm và lựa chọn cần thể hiện cá tính qua hành động cụ thể, không qua ký hiệu cung hay lời giảng giải.
- Dùng `typography_role` để chỉ định `none`, `narration`, `emphasis` hoặc `verdict`; nội dung narration phải tham chiếu ID đã khai báo. Không thêm caption riêng ngoài nội dung đã duyệt.
- Dùng treatment intent `normal`, `bold_comic`, `paper_layer`, `dramatic` hoặc `editorial_verdict` nếu nó phục vụ nhịp đó. Đây là chỉ thị semantic, không phải yêu cầu tự tạo CSS/asset mới.
- Khi trình bày preview, giải thích ngắn acting, interaction, gaze/focus, object continuity, camera/composition và vai trò chữ. Giữ `ScenePlan → VisualScene → allowed_assets` nhất quán; không thêm lời thoại, audio hoặc nội dung ngoài claim/evidence.

## Kể chuyện từ nét tính cách

- Lấy idea/evidence đã chọn làm điểm xuất phát, rồi dựng một tình huống hư cấu khiến nét tính cách hoặc đặc trưng của cung tạo ra hành động, lựa chọn và hệ quả nhìn thấy được. Không kể nguồn gốc cung, không tóm tắt ý nghĩa cung, không biến video thành bài giải thích claim.
- Mỗi câu chuyện cần có mong muốn cụ thể, trở ngại do cách hành xử tạo ra, leo thang có nguyên nhân, khoảnh khắc nhận ra hoặc lựa chọn làm đổi hướng, và payoff gọi lại một chi tiết đã gieo. Không lặp cùng một ý bằng caption khác.
- Dùng source claim và evidence để giới hạn điều được kết luận. Để nhân vật/tình huống hư cấu nằm ở `story_device`; chỉ nối takeaway với claim bằng ngôn ngữ có điều kiện như “có thể”, không khái quát cho mọi người thuộc cung đó.
- Ưu tiên kể bằng biểu cảm, cử chỉ, thay đổi khoảng cách, đạo cụ và nhịp dừng. Caption phải làm câu chuyện tiến lên; không đọc lại nội dung nguồn hoặc kể thay hành động đang thấy.

## Khi thư viện thiếu asset

- Nếu câu chuyện cần một hình chưa có trong `allowed_assets` (ví dụ cây bút), không bịa `id`/`src`, không chọn asset không liên quan chỉ để lấp chỗ trống và không âm thầm bỏ một chi tiết thiết yếu.
- Thêm một mục vào `story.asset_needs` cho từng nhu cầu hình ảnh chưa được đáp ứng. Ghi rõ `id`, `role`, `label`, `description` và `purpose`; dùng `role` thuộc schema do Writer Context cung cấp.
- Liên kết nhu cầu với ít nhất một beat hoặc VisualScene liên quan bằng `beat_refs`/`shot_refs`; dùng `VisualScene.id` trong `shot_refs`. Ghi `scene_id` khi đã biết. Chỉ đưa ID asset thật trong `candidate_asset_ids`; để danh sách rỗng nếu không có lựa chọn gần đúng.
- Đặt `status` là `open` và `resolved_asset_id` là `null`. Đặt `required=true` nếu câu chuyện phụ thuộc vào asset đó; chỉ dùng `required=false` khi người dùng có thể bỏ chi tiết mà mạch truyện vẫn hợp lý. Không tự đánh dấu đã thay thế hoặc đã bỏ.
- Trong preview, nêu rõ asset nào còn thiếu, nó phục vụ beat/shot nào và vì sao asset hiện có không phù hợp. Người dùng sẽ chọn asset thay thế, xác nhận bỏ nhu cầu tùy chọn hoặc chuyển brief sang thiết kế; chỉ phản ánh quyết định đã duyệt vào StoryGraph sau đó.

## Chuẩn preview và rà soát

- Preview đạo diễn cần giúp người dùng đánh giá được StoryOutline, causal ScenePlan, VisualScene theo thứ tự, character acting/identity, object continuity, camera/composition, narration role, asset được chọn, asset còn thiếu và payoff/callback.
- Làm theo trạng thái và định dạng handoff trong Writer Context; không tự coi một preview là chấp thuận import.
- Trả đúng envelope trong `response_template` của Writer Context. Với context v5, trả một root `video_story_draft` gồm `version`, `idea_id`, hai fingerprint và `story`; không gửi StoryGraph đã dựng.
- Trước khi bàn giao, rà soát claim references, causal state, mapping một-một ScenePlan/VisualScene, asset references, directing options, fingerprint và tính nhất quán với nội dung đã duyệt.

## Art direction and asset contract

Production direction is Storybook Expressive Chibi v1, defined in [design/storybook-expressive-chibi-v1.md](../design/storybook-expressive-chibi-v1.md). C1 files under design/references are visual references only and must not be exposed as runtime assets.

Semantic category is separate from runtime compatibility. Read runtime_compatibility from the asset metadata schema; never infer a role from category, filename, tags, or appearance. Effects and overlays are unsupported by the current asset catalog by default and have no default role/subject mapping. Expose one only after a registered adapter or deliberate engine contract supports it. The Writer Context allowed_assets list remains the runtime allowlist.

A character identity master declares pose_components, expression_components, intensity bounds and affected channels, plus head-angle bounds and a head pivot. Compose one declared pose component and one expression component per shot. Intensity modulates expression amplitude and declared pose motion channels but does not change identity or base pose. Apply head_angle around the declared pivot independently of intensity. Do not require cross-product SVG exports.

Use the numeric camera/composition thresholds from tokens.storybook-expressive-chibi.v1.json. An asset whose art_direction_id or art_direction_version differs from the graph/catalog direction fails validation. Legacy graph/catalog directions are never auto-upgraded. Any missing, unverifiable, or different graph, catalog, or design fingerprint requires review. READY and approved output must not be rewritten in place; an explicit migration creates a provenance-linked revision and requires review.

# Điểm vào dự án Zodiac

Thư mục này chứa hướng dẫn riêng cho thiết kế nội dung của Zodiac Controversy Factory.

## Nguồn rule duy nhất

Đọc toàn bộ `rules/content-design.md` trước khi viết hoặc review nội dung Zodiac. Đây là **nguồn rule biên tập duy nhất**.

Writer Context chỉ mang dữ liệu/evidence/contract của package. Không coi `VIRAL_OVERLAY`, `EDITORIAL_DESIGN`, prompt export, bản Google Drive hoặc trí nhớ của agent là một bộ rule thứ hai.

## Authority của dữ liệu package

- `KNOWLEDGE_CONTEXT`: biên claim/fact của package.
- `EDITORIAL_DESIGN`: beat và điểm biên tập đã chọn trong biên claim đó.
- `VIRAL_OVERLAY` hoặc `VIRAL_FOCUS`: anchor riêng của package để tối ưu cách nói; không phải rule và không phải nguồn fact.
- `OUTPUT_CONTRACT` / `SLIDE_OPTIONS`: cấu trúc kỹ thuật.

`RAW_IDEA` là provenance. Khi có `EDITORIAL_DESIGN.planning.shared_question`, dùng shared question đã validate làm câu hỏi viết.

## Output protocol

Nếu Writer Context yêu cầu preview, tạo preview trước và dừng chờ duyệt. Chỉ sau khi được duyệt rõ ràng mới xuất JSON đúng `response_contract.exact_package_ids`.

## Compatibility

Concept cũ chỉ nên dùng sau khi regenerate Writer Context bằng pipeline hiện tại. Không dùng Writer Context cũ làm authority nếu schema mới đã tồn tại.

## Khi thiếu nguồn

Nếu không đọc được `rules/content-design.md` hoặc thiếu context/evidence bắt buộc của package, dừng và báo rõ phần thiếu.

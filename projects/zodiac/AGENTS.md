# Điểm vào dự án Zodiac

Thư mục này chứa hướng dẫn riêng cho thiết kế nội dung của Zodiac Controversy Factory.

## Tài liệu bắt buộc khi viết hoặc review nội dung

Đọc toàn bộ rules/content-design.md trước khi viết hoặc review nội dung Zodiac. Đây là nguồn duy nhất cho rule biên tập dùng chung của Zodiac. Không dùng bản Google Drive, phần tóm tắt trong Writer Context hoặc trí nhớ của agent thay cho tài liệu này.

## Nguồn context và contract

- Dùng KNOWLEDGE_CONTEXT và EDITORIAL_CONTEXT của package được chọn để xác định claim và evidence được phép sử dụng.
- Dùng OUTPUT_CONTRACT, OUTPUT_TEMPLATE hoặc SLIDE_OPTIONS, CONTENT_FRAME.constraints, CONTENT_FRAME.text_layout và response_contract.exact_package_ids của package để xác định cấu trúc, block ID, thứ tự, giới hạn và phạm vi output.
- Contract của package quyết định yêu cầu kỹ thuật khi khác với hướng dẫn độ dài chung trong rule biên tập.
- Khi trả kết quả từ Writer Context, chỉ xuất một JSON object khớp response contract của package đang chọn. Không thêm Markdown fence, lời dẫn, ghi chú hay nội dung sau object; kiểm tra cú pháp JSON trước khi gửi.

## Khi thiếu nguồn

Nếu không truy cập được file rule chuẩn hoặc context package/evidence bắt buộc, dừng và báo rõ nguồn nào đang thiếu. Không viết dựa trên trí nhớ hoặc bản sao cũ.
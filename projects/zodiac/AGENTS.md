# Điểm vào dự án Zodiac

Thư mục này chứa hướng dẫn riêng cho thiết kế nội dung của Zodiac Controversy Factory.

## Tài liệu bắt buộc khi viết hoặc review nội dung

Đọc toàn bộ `rules/content-design.md` trước khi viết hoặc review nội dung Zodiac. Đây là nguồn duy nhất cho rule biên tập dùng chung của Zodiac. Không dùng bản Google Drive, phần tóm tắt trong Writer Context hoặc trí nhớ của agent thay cho tài liệu này.

## Nguồn context và contract

Khi Writer Context đã có schema mới, dùng các lớp theo thứ tự quyền hạn sau:

1. `KNOWLEDGE_CONTEXT`: quyết định điều gì được phép claim.
2. `EDITORIAL_DESIGN`: quyết định điểm nào đáng nói, beat nào được chọn và progression nào cần giữ.
3. `VIRAL_OVERLAY` nếu có: chỉ tối ưu attention, recognition, shareability, headline direction và nhịp diễn đạt. Đây là soft guidance, không phải nguồn fact và không được override hai lớp trên.
4. `OUTPUT_CONTRACT`, `OUTPUT_TEMPLATE` và `SLIDE_OPTIONS`: quyết định schema, block ID, thứ tự, giới hạn renderer và số slide.

`RAW_IDEA` là provenance/original intent. Khi package có `EDITORIAL_DESIGN.planning.shared_question`, dùng shared question đã được evidence validate làm câu hỏi chung của batch; không ép wording hẹp hoặc không được hỗ trợ trong RAW IDEA lên từng subject.

Contract của package quyết định yêu cầu kỹ thuật khi khác với hướng dẫn độ dài chung trong rule biên tập. Contract không được nới evidence boundary hoặc tạo thêm claim.

Khi trả kết quả từ Writer Context, tạo preview trước nếu context yêu cầu approval flow. Chỉ sau khi được duyệt rõ ràng mới xuất JSON theo `response_contract.exact_package_ids`. JSON cuối không thêm Markdown fence, lời dẫn, ghi chú hay nội dung sau object; kiểm tra cú pháp trước khi gửi.

## Compatibility

Concept/package cũ có thể được dùng lại nếu pipeline hiện tại regenerate được `KNOWLEDGE_CONTEXT`, `EDITORIAL_DESIGN` và output contract từ evidence hiện tại. Không dùng Writer Context cũ như authority khi schema mới đã tồn tại.

## Khi thiếu nguồn

Nếu không truy cập được file rule chuẩn hoặc context package/evidence bắt buộc, dừng và báo rõ nguồn nào đang thiếu. Không viết dựa trên trí nhớ hoặc bản sao cũ.

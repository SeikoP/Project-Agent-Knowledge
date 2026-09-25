# Project Agent Knowledge

Kho hướng dẫn cho agent, được tổ chức theo nhiều dự án. Mỗi dự án có entrypoint riêng để agent chỉ đọc và áp dụng đúng ngữ cảnh.

## Cách agent bắt đầu

1. Đọc AGENTS.md ở root.
2. Xác định dự án theo yêu cầu hiện tại và repository code đang làm việc.
3. Đọc projects/<project-id>/AGENTS.md tương ứng và làm theo thứ tự đọc trong đó.
4. Chỉ áp dụng tài liệu của dự án đang làm. Nếu chưa xác định được dự án, hỏi trước khi dùng rule riêng.

## Dự án hiện có

- Zodiac: projects/zodiac/AGENTS.md, hướng dẫn viết và review nội dung cùng rule biên tập.

## Thêm dự án

Tạo projects/<project-id>/AGENTS.md làm entrypoint cho dự án mới, sau đó thêm các tài liệu cần thiết trong thư mục của dự án đó. Chỉ đặt hướng dẫn ở root khi nó áp dụng cho mọi dự án. Không sao chép rule từ dự án này sang dự án khác.

## Nguồn và quyền sở hữu

Repo này là nguồn chuẩn cho hướng dẫn agent và docs được lưu ở đây. Contract runtime, schema và dữ liệu nghiệp vụ vẫn thuộc repository hoặc hệ thống sở hữu chúng; tài liệu trong repo này trỏ tới các nguồn đó thay vì tạo bản sao.
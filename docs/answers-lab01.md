**Vì sao dùng git mv?** 
Dùng git mv để di chuyển file dưới sự quản lý của Git. Nó tương đương với việc di chuyển file rồi cập nhật staging, giúp thao tác rõ ràng trong lịch sử thay đổi.

**release/lab01 có phải baseline?**
Có thể xem là baseline của Lab 01, nhưng theo cách bài lab này tổ chức thì đây chưa phải là một baseline được đánh dấu chính xác bằng tag.

**Vì sao không commit thẳng master dù làm một mình?**
Không commit trực tiếp lên master vì master nên đại diện cho trạng thái đã được tích hợp và ổn định. Dù làm một mình, việc phát triển trên nhánh riêng và merge qua Pull Request vẫn tạo một điểm kiểm soát để xem lại thay đổi, kiểm thử và giữ lịch sử thay đổi rõ ràng. Số approval có thể là 0, nhưng quy trình PR vẫn được duy trì để thực hành đúng Change Control trong SCM.
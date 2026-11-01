Vì sao phải đồng bộ master trước khi PR? 
để branch làm việc dựa trên phiên bản mới nhất, phát hiện conflict sớm và kiểm tra khả năng tích hợp.

Khi nào không được rebase? feature/* khác topic/* ra sao?
Không rebase: khi branch là branch dùng chung/public hoặc có người khác đang dựa vào lịch sử của nó, đặc biệt là master và release/*, vì rebase viết lại lịch sử.

feature/* vs topic/*: Git không phân biệt kỹ thuật; đây là quy ước. feature/* dành cho chức năng sản phẩm, còn topic/* dành cho công việc theo chủ đề như tài liệu, cấu hình hoặc thiết kế.
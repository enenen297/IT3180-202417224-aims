# Changelog

All notable changes to this project are documented in this file.
The format is based on [Keep a Changelog](https://keepachangelog.com/).

## [Unreleased]

## [1.1.0]-1/11/2026
### Added
- Cart.sort_by_title(), Cart.sort_by_cost()
- search_by_category()

## [1.0.1] - 2026-11-xx
### Fixed
- `search_by_title` bỏ khoảng trắng thừa ở từ khóa (#<1>)

## [1.0.0] - 2026-11-01
### Added
- `Cart.print_cart()` để in nội dung giỏ hàng
- `search_by_title()` để tìm đĩa theo tiêu đề
- `total_cost_with_discount()` để tính tổng tiền sau giảm giá (có kiểm tra phần trăm hợp lệ)
- Pull request template (`.github/pull_request_template.md`)
- Use case diagram (`docs/use-case.md`)

### Changed
- Chuyển mã nguồn vào package `aims`
- Thông báo khi thêm đĩa dùng tiếng Việt và hiển thị tên đĩa

### Fixed
- Giỏ hàng nhận đĩa thứ 21 dù giới hạn là 20 (#7)
- Tính giảm giá trả về sai giá trị
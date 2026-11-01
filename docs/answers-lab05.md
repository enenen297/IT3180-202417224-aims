

## 1. Ưu, nhược điểm của upstream first so với release first

**Hai cách làm:**
- **Upstream first**: sửa lỗi ở `master` trước, rồi cherry-pick xuống các nhánh `release/*`.
- **Release first** (cách học phần đang dùng): tạo `hotfix/*` từ `release/*`, sửa và phát hành bản vá, rồi cherry-pick về `master` và các release khác.

| | Ưu điểm | Nhược điểm |
|---|---|---|
| **Upstream first** | Bản sửa chắc chắn có ở master, nên không thể "quên" đưa về và lỗi không tái xuất hiện ở bản sau. Lỗi được sửa trên mã mới nhất, có đủ test và CI của master. Có một nguồn sự thật duy nhất. | Phải chờ sửa và merge ở master (qua PR, review, CI) rồi mới vá được release, nên chậm khi sự cố khẩn cấp. Master đã đi xa so với bản cũ nên cherry-pick xuống dễ xung đột. Mã sửa ở master có thể phụ thuộc tính năng mới mà bản release không có. |
| **Release first** | Vá nhanh, đúng với mã đang chạy ở người dùng, kiểm thử trực tiếp trên đúng phiên bản bị lỗi, ít rủi ro kéo theo thay đổi không liên quan. Phù hợp khi phải bảo trì nhiều bản song song. | Dễ quên đưa bản sửa về master và các release khác, khiến lỗi quay lại ở bản sau. Phải lan truyền thủ công nên cần kiểm toán (Phần F). Bản sửa có thể được viết theo cách khác nhau ở mỗi dòng nếu không dùng `cherry-pick -x`. |

**Kết luận:** upstream first an toàn hơn về tính nhất quán, release first nhanh hơn khi khẩn cấp. Dù chọn cách nào đều cần `cherry-pick -x` để truy vết và kiểm toán để chắc bản sửa có ở mọi dòng bị ảnh hưởng.

## 2. Nếu quên lan truyền bản sửa sang `release/lab05`, lệnh nào ở Phần F phát hiện?

Có ba lệnh phát hiện được:

1. **Vòng lặp kiểm tra hành vi** (phát hiện rõ nhất): ở `v1.1.0` (hoặc `release/lab05`) sẽ in `0` thay vì `1`, vì từ khóa `'  lion '` vẫn không tìm ra đĩa.

   ```
   v1.0.1  1
   v1.1.0  0   <- thiếu bản sửa
   master  1
   ```

2. **`git log --all --oneline --grep "cherry picked from commit <FIX_SHA>"`**: kỳ vọng 2 commit cherry-pick (master và `release/lab05`). Nếu quên thì chỉ ra 1, thiếu bản của `release/lab05`.

3. **`git cherry -v origin/release/lab05 origin/release/lab04`** (hoặc đối chiếu master): commit `fix: trim whitespace in search_by_title keyword` sẽ hiện dấu `+`, nghĩa là nhánh `release/lab05` chưa có bản tương đương. Khi đã lan truyền đúng thì nó hiện dấu `-`.

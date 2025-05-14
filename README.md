# Hệ Thống Phân Tích Cảm Xúc Ẩm Thực

## Giới thiệu hệ thống

Hệ thống Phân Tích Cảm Xúc Ẩm Thực là một ứng dụng web cho phép người dùng đánh giá cảm xúc của mình về các món ăn Việt Nam thông qua nhận xét tự do. Hệ thống sử dụng xử lý ngôn ngữ tự nhiên để phân tích cảm xúc (tích cực, trung tính, tiêu cực) từ nội dung đánh giá, lưu trữ kết quả và cung cấp giao diện thống kê, quản lý đánh giá cho quản trị viên.

## Ứng dụng của hệ thống

- Thu thập và phân tích cảm xúc khách hàng về các món ăn.
- Quản lý, thống kê, và trực quan hóa dữ liệu cảm xúc theo từng món ăn.
- Hỗ trợ nhà hàng, quán ăn, hoặc các nhà nghiên cứu ẩm thực hiểu rõ hơn về cảm nhận thực tế của khách hàng, từ đó đưa ra kế hoạch kinh doanh hoặc thay đổi công thức các món ăn sao cho phù hợp.


## Tên sinh viên

- Nguyễn Trường Vương - 22642961 - Lớp: DHKHDL18A
- Lê Hữu Trọng - 22652671 - Lớp: DHKHDL18A

## Yêu cầu công cụ

- Docker & Docker Compose
- Tài khoản Google để đăng nhập (qua Firebase)
- File cấu hình `.env` (chứa thông tin kết nối MongoDB)

## Hướng dẫn cài đặt và chạy hệ thống

### 1. Clone source code

```sh
git clone https://github.com/your-username/ten-repo.git
cd ten-repo
```

### 2. Cấu hình môi trường

- Đảm bảo file `.env` đã có thông tin kết nối Mongo Atlas, ví dụ:
  ```
  MONGO_URI=mongodb+srv://<user>:<password>@<cluster>.mongodb.net/?retryWrites=true&w=majority
  ```

### 3. Chạy hệ thống

- Sử dụng Docker Compose:

  ```sh
  docker-compose up --build
  ```

- Hoặc trên Windows, chạy file:

  ```sh
  run.bat  
  ```

lệnh : .\run.bat (trong terminal)
### 4. Truy cập giao diện

- Trang người dùng: http://localhost:5000
- Quản lý đánh giá (admin): http://localhost:5000/admin
- Thống kê cảm xúc: http://localhost:5000/stats

- Hoặc có thể truy cập giao diện trực tiếp trên web
### 5. Đăng nhập

- Đăng nhập bằng Google để gửi đánh giá hoặc truy cập trang quản trị.
- Chỉ tài khoản trong danh sách ADMIN_EMAILS mới truy cập được trang admin.

### 6. Dừng hệ thống

- Nhấn `Ctrl+C` trong terminal hoặc dùng lệnh:

  ```sh
  docker-compose down
  ```

---


### 5. Ghi chú

- MongoDB sẽ tự động khởi tạo và lưu dữ liệu trong volume docker.
- Nếu muốn thay đổi kết nối MongoDB, sửa file `.env`.
- Để dừng hệ thống: nhấn `Ctrl+C` trong terminal hoặc dùng `docker-compose down`.

---
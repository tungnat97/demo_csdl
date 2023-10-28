# demo_csdl

## Cài đặt môi trường
- Python 3
- Django: `python3 -m pip install django`

## Cài đặt ứng dụng
- Sửa lại config db trong `demo_csdl/settings.py -> DATABASES`
- Clone project về, cd vào project
- Chạy `python3 manage.py makemigrations employee`, `python3 manage.py migrate` để init database
- Chạy `python3 manage.py createsuperuser` để khởi tạo super user
- Chạy script init trigger trong `scripts/trigger.sql` để khởi tạo các trigger`

## Chạy ứng dụng
- Chạy `python3 manage.py runserver`. Server chạy ở port mặc định là 8000
- Vào `localhost:8000/admin` để quản lý CRUD các bảng. Tài khoản đăng nhập là superuser vừa tạo
- Vào `localhost:8000/calculate` để thực hiện các yêu cầu khác. Từ trên xuống dưới:
  - Tính lương nhân viên
  - Tính lương giảng viên
  - Liệt kê danh sách điểm của sinh viên trong 1 chương trình đào tạo
  - Liệt kê danh sách sinh viên chưa hoàn thành chương trình đào tạo
![image](https://github.com/tungnat97/demo_csdl/assets/30834737/bd5dadd1-a735-4382-aff0-a99cbb508097)

## Sơ lược về ứng dụng
- Định nghĩa bảng trong file `employee/models.py`
- Base CRUD cơ bản
- Sử dụng 2 trigger để check số lượng môn học trong 1 chương trình đào tạo, và check trùng tên trong cùng 1 chương trình đào tạo
- Các hàm SQL thực hiện các yêu cầu ngoài CRUD được định nghĩa trong `employee/views.py`

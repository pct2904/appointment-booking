class Patient:
    def __init__(self, patient_id, full_name, phone, email, password_hash):
        self.patient_id = patient_id       # Mã định danh bệnh nhân
        self.full_name = full_name         # Họ và tên
        self.phone = phone                 # Số điện thoại (dùng làm khóa chính logic để kiểm tra trùng)
        self.email = email                 # Thư điện tử
        self.password_hash = password_hash # Mật khẩu đã được mã hóa (bảo mật)
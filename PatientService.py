class PatientService:
    def __init__(self):
        # Khởi tạo kho chứa dữ liệu
        self.patient_repository = PatientRepository()

    def register_patient(self, full_name, phone, email, password):
        # BƯỚC 1: Validate dữ liệu đầu vào (Kiểm tra rỗng)
        if not full_name or not full_name.strip() or not phone or not phone.strip() or not password:
            raise ValueError("Vui lòng nhập đầy đủ thông tin bắt buộc!")
        
        # BƯỚC 2: Kiểm tra độ dài mật khẩu tối thiểu (ít nhất 6 ký tự)
        if len(password) < 6:
            raise ValueError("Mật khẩu phải có ít nhất 6 ký tự!")
        
        # BƯỚC 3: Kiểm tra xem số điện thoại đã được đăng ký trước đó chưa
        existing_patient = self.patient_repository.find_by_phone(phone)
        if existing_patient is not None:
            raise RuntimeError("Số điện thoại này đã được đăng ký tài khoản!")

        # BƯỚC 4: Giả lập mã hóa mật khẩu và tạo đối tượng mới
        password_hash = "hashed_" + password
        new_patient = Patient(
            patient_id="ID_" + phone,
            full_name=full_name,
            phone=phone,
            email=email,
            password_hash=password_hash
        )
        
        # BƯỚC 5: Lưu vào kho dữ liệu
        self.patient_repository.save(new_patient)

        return "Đăng ký tài khoản thành công!"
    
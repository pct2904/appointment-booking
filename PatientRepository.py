class PatientRepository:
    def __init__(self):
        # Dùng một danh sách (List) trong Python để giả lập cơ sở dữ liệu RAM
        self.database = []

    def find_by_phone(self, phone):
        # Duyệt qua từng bệnh nhân trong database giả lập để tìm xem số điện thoại đã tồn tại chưa
        for patient in self.database:
            if patient.phone == phone:
                return patient  # Trả về đối tượng nếu tìm thấy
        return None             # Không tìm thấy thì trả về None

    def save(self, patient):
        # Thêm bệnh nhân mới vào danh sách (giống lệnh INSERT INTO trong SQL)
        self.database.append(patient)
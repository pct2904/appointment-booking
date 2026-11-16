class NotificationRepository:
    def __init__(self, db_connection=None):
        self.db = db_connection  # Giả lập kết nối CSDL (SQLite/MySQL)
        
    def get_upcoming_appointments(self):
        # Giả lập lấy danh sách các lịch khám sắp diễn ra từ CSDL
        # Trong thực tế, bạn sẽ viết câu lệnh SQL: SELECT * FROM Appointments WHERE time > NOW()
        return [
            # Giả sử có một lịch khám vào 15 tiếng nữa
            # Appointment(id=1, patient_name="Nguyen Van A", appointment_time=...)
        ]
        
    def save_notification(self, notification):
        # Lưu thông báo vào bảng Notification
        # INSERT INTO Notification (appointment_id, status, send_time) VALUES (...)
        print(f"[DB LOG] Đã lưu thông báo cho lịch khám {notification.appointment_id} - Trạng thái: {notification.status}")
        return True
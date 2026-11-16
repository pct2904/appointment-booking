from datetime import datetime

class ReminderService:
    def __init__(self, repository):
        self.repository = repository

    def calculate_reminder_status(self, hours_until_appointment):
        """
        Logic tính toán xem có nên gửi thông báo không.
        Trả về:
        0: Không gửi (đã quá giờ hoặc sát giờ <= 1h)
        1: Gửi thông báo nhắc lịch bình thường (1h < time <= 24h)
        2: Gửi thông báo nhắc lịch sớm để chuẩn bị (24h < time <= 48h)
        """
        if hours_until_appointment <= 1:
            return 0
        if hours_until_appointment <= 24:
            return 1
        if hours_until_appointment <= 48:
            return 2
        return 0

    def trigger_auto_reminders(self):
        """
        Hàm cronjob chạy ngầm: Quét các lịch khám và gửi thông báo
        """
        appointments = self.repository.get_upcoming_appointments()
        now = datetime.now()
        
        for appt in appointments:
            # Tính toán thời gian còn lại (tính bằng giờ)
            time_diff = appt.appointment_time - now
            hours_until = time_diff.total_seconds() / 3600
            
            # Kiểm tra trạng thái dựa vào logic nghiệp vụ
            status = self.calculate_reminder_status(hours_until)
            
            if status == 1:
                self.send_sms(appt.patient_name, "Lịch khám của bạn sẽ diễn ra trong 24h tới. Vui lòng đến đúng giờ!")
                self._log_notification(appt.id, 'SENT')
            elif status == 2:
                self.send_email(appt.patient_name, "Nhắc lịch sớm: Bạn có một lịch khám trong 2 ngày tới.")
                self._log_notification(appt.id, 'SENT')

    def send_sms(self, patient_name, message):
        # Tích hợp API gửi SMS (VD: Twilio, SpeedSMS)
        print(f"[SMS] Gửi tới {patient_name}: {message}")

    def send_email(self, patient_name, message):
        # Tích hợp API gửi Email
        print(f"[EMAIL] Gửi tới {patient_name}: {message}")

    def _log_notification(self, appt_id, status):
        from models import Notification
        new_noti = Notification(notification_id=None, appointment_id=appt_id, status=status)
        self.repository.save_notification(new_noti)
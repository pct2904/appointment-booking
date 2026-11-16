from datetime import datetime

class Appointment:
    def __init__(self, appointment_id, patient_name, appointment_time):
        self.id = appointment_id
        self.patient_name = patient_name
        self.appointment_time = appointment_time  # datetime object

class Notification:
    def __init__(self, notification_id, appointment_id, status, send_time=None):
        self.id = notification_id
        self.appointment_id = appointment_id
        self.status = status  # 'PENDING', 'SENT', 'FAILED'
        self.send_time = send_time or datetime.now()
        
    def to_dict(self):
        return {
            "id": self.id,
            "appointment_id": self.appointment_id,
            "status": self.status,
            "send_time": self.send_time.strftime("%Y-%m-%d %H:%M:%S")
        }
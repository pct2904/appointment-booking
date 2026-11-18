import unittest
class AppointmentManager:
    def cancel_appointment(
        self, hours_before: int, reason: str, slot_status: str = "Đã đặt"
    ) -> dict:
        if not reason or not reason.strip():
            return {
                "success": False,
                "appointment_status": "Sắp tới",
                "slot_status": slot_status,
            }
        if hours_before < 24:
            return {
                "success": False,
                "appointment_status": "Sắp tới",
                "slot_status": slot_status,
            }
        return {
            "success": True,
            "appointment_status": "Đã hủy",
            "slot_status": "Còn trống",
        }



# ==========================================
class TestAppointmentManager(unittest.TestCase):

    def testCancelSuccess(self):
        """Test Case 1: Hủy lịch hợp lệ (trước >= 24h và có nhập lý do) -> Hủy thành công & giải phóng slot."""
        # 1. Arrange
        manager = AppointmentManager()
        hours_before = 36
        reason = "Có việc đột xuất"
        expected = {
            "success": True,
            "appointment_status": "Đã hủy",
            "slot_status": "Còn trống",
        }

        # 2. Act
        actual = manager.cancel_appointment(hours_before, reason)

        # 3. Assert
        self.assertEqual(expected, actual)

    def testCancelTooLateOrNoReason(self):
        """Test Case 2: Hủy lịch không hợp lệ (sát giờ hẹn < 24h) -> Từ chối hủy & giữ nguyên slot."""
        # 1. Arrange
        manager = AppointmentManager()
        hours_before = 12
        reason = "Có việc đột xuất"
        expected = {
            "success": False,
            "appointment_status": "Sắp tới",
            "slot_status": "Đã đặt",
        }

        # 2. Act
        actual = manager.cancel_appointment(hours_before, reason)

        # 3. Assert
        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main(verbosity=2)
public class FineCalculator {
    public double calculate(int daysOverdue) {
        if (daysOverdue <= 0) return 0;
        double fine = daysOverdue * 5000;
        if (daysOverdue > 10) {
            fine = fine * 1.2;
        }
        return fine;
    }
}
import static org.junit.Assert.assertEquals;
import org.junit.Test;

public class FineCalculatorTest {

    @Test
    public void testNoFine() {
        FineCalculator calc = new FineCalculator();
        int days = 0;
        double expected = 0;
        double actual = calc.calculate(days);
        assertEquals(expected, actual, 0.01);
    }

    @Test
    public void testNormalFine() {
        FineCalculator calc = new FineCalculator();
        int days = 5;
        double expected = 25000;
        double actual = calc.calculate(days);
        assertEquals(expected, actual, 0.01);
    }

    @Test
    public void testHeavyFine() {
        FineCalculator calc = new FineCalculator();
        int days = 11;
        double expected = (11 * 5000) * 1.2;
        double actual = calc.calculate(days);
        assertEquals(expected, actual, 0.01);
    }
}
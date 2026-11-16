public class Customer {
    private int id;
    private String name;
    private String phone;
    private String email;
    private int points;

    // Constructor
    public Customer(int id, String name, String phone, String email, int points) {
        this.id = id;
        this.name = name;
        this.phone = phone;
        this.email = email;
        this.points = points;
    }

    // Getters and Setters
    public int getId() { return id; }
    public String getName() { return name; }
    public String getPhone() { return phone; }
    public String getEmail() { return email; }
    public int getPoints() { return points; }
    
    public void setPoints(int points) { 
        this.points = points; 
    }
}
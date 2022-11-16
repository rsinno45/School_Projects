class FC {

    public static double convert(double f) {
        return (f - 32) * 5 / 9;
    }

    public static void main(String[] args) {
        for (int i = -30; i <= 110; i = i + 20) {
            System.out.println(i + " F == " + convert(i) + " C");
        }

    }
}
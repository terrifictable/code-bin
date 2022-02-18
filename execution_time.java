public class execution_time {
    public static void main(String[] args) throws InterruptedException {
        long start = System.nanoTime();
        // ------------------ PROGRAM ----------------
        Thread.sleep(3000);
        // -------------------------------------------
        System.out.println((System.nanoTime() - start) / 1000000 + "ms");
    }
}

import java.io.*;
import java.math.BigInteger;
import java.util.StringTokenizer;

public class Main {

    private static void run(Reader fs, PrintWriter out) throws IOException {
        int n = fs.nextInt();

        BigInteger fact = BigInteger.ONE;
        for(int i = n; i > 0; i--) {
            fact = fact.multiply(BigInteger.valueOf(i));
        }
        out.println(fact);
    }

    public static void main(String[] args) throws IOException {
        Reader in = new Reader(new InputStreamReader(System.in));
        PrintWriter out = new PrintWriter(new OutputStreamWriter(System.out));

        int t = in.nextInt();
        for (int i = 0; i < t; i++) {
            run(in, out);
        }

        out.flush();
        in.close();
        out.close();
    }

    static class Reader {
        BufferedReader reader;
        StringTokenizer st;

        Reader(InputStreamReader stream) {
            reader = new BufferedReader(stream, 32768);
            st = null;
        }

        void close() throws IOException {
            reader.close();
        }

        String next() {
            while (st == null || !st.hasMoreTokens()) {
                try {
                    st = new StringTokenizer(reader.readLine());
                } catch (IOException e) {
                    throw new RuntimeException(e);
                }
            }
            return st.nextToken();
        }

        int nextInt() {
            return Integer.parseInt(next());
        }

        String nextLine() throws IOException {
            return reader.readLine();
        }

        long nextLong() {
            return Long.parseLong(next());
        }

        double nextDouble() {
            return Double.parseDouble(next());
        }

    }
}
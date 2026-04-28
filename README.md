🧮 Euclidean Algorithm (Step‑by‑Step)
Definition:  
The Euclidean Algorithm is used to compute the Greatest Common Divisor (GCD) of two integers 
𝑎
 and 
𝑏
.
It works by repeatedly dividing and taking remainders until the remainder becomes 0.

Steps:

Divide the larger number by the smaller number.

Replace the larger number with the smaller number, and the smaller number with the remainder.

Repeat until the remainder = 0.

The last non‑zero remainder is the GCD.

📖 Example: GCD(2740, 1760)
2740
÷
1760
=
1
, remainder = 980 → GCD(1760, 980)

1760
÷
980
=
1
, remainder = 780 → GCD(980, 780)

980
÷
780
=
1
, remainder = 200 → GCD(780, 200)

780
÷
200
=
3
, remainder = 180 → GCD(200, 180)

200
÷
180
=
1
, remainder = 20 → GCD(180, 20)

180
÷
20
=
9
, remainder = 0 → Stop

✅ GCD(2740, 1760) = 20

🎓 Mnemonic (Quick Recall)
👉 “Divide → Remainder → Repeat → Stop at 0”


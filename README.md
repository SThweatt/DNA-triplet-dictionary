# DNA-triplet-dictionary

## Simple Conversion Dictionary

### What it does:
1. Maps each DNA triplet base (A, T, C, G) to a number (Base-4 mapping) using a defined key:
   - **A = 0**
   - **T = 1**
   - **C = 2**
   - **G = 3**

### Example:
   - **TAC** → T = 1, A = 0, C = 2 → Base-4 number = 102  
   - **TAC = 102**

---

## Because I know you love doing math, I've included a manual version of the same concept.

### Manual Calculation of ASCII Decimal Using TAC = 102:
To convert the **Base-4 number** (102) to **decimal**, use the formula:
(First-Digit x 4^2) + (Second-Digit x 4^1) + (Third-Digit x 4^0)
1 x 16 + 0 x 4 + 2 x 1 = 18
18 is the decimal equivalent of TAC 

---

### To Verify Base-4 Value of TAC Using Integer Division:
Start with **18 / 4 = quotient:remainder**
Next, take the quotient of **18 / 4** and divide it by 4.  
Repeat this process (quotient / 4) until you no longer have a whole number. We stop here because **integer division** only gives us the whole number portion of the result.

- **18 / 4 = 4** Remainder **2**
- **4 / 4 = 1** Remainder **0**
- **1 / 4 = 0** Remainder **1** (STOP! because quotient is now 0)

Now, you should have:
- **18 / 4 = 4** Remainder **2**
- **4 / 4 = 1** Remainder **0**
- **1 / 4 = 0** Remainder **1**

Read the remainders from bottom to top:  
**102** (Base-4 representation)

So, **18 in decimal** is now **102 in Base-4**
**TAC = 18 = 102**

---

## You're not done yet!

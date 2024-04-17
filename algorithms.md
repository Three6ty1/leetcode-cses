# Algorithms (Miscellaneous)

### String to Integer (atoi)
- DFA, Deterministic Finite Automation
-   State machine that is determined by the constraints of the string
- We keep track of the value, position (i), sign and **state** of the machine
    - State == 0
        - If we see whitespace, we continue
        - If we see a sign, we change state to 1
        - If we see a digit, we change state to 2
        - Otherwise, we return 0 (can't read digits)
    - State == 1 (Saw a +/- previously)
        - If we see a digit, we change state to 2 and calculate the value
        - Otherwise, the sign is useless and we return 0
    - State == 2 (Saw a digit previously)
        - If we see a digit, we preserve the second state and continue calculating the values
        - Otherwise, we break out since we've reached the end of the number
    - Otherwise
        - We return 0 as we didn't read an numerical character
- We can add the next digit onto value by doing value = value * 10 + the digit (as it shifts all numbers up)
- We then account for overflows and check if the value is more than 32bit min and max
    - max between value and (2 ** 31) - 1
    - min between value and - 2 ** 31

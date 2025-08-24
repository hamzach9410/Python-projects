# 📧 Python Email Validation Script

This project is a **Python-based email validator** that checks whether a given email address is valid or not using basic conditions. It helps beginners understand string handling, logical operators, and input validation in Python.

---

## 🔍 What This Script Does

When a user enters their email, the script checks for several rules to decide whether the email is valid. If the email breaks any rule, it shows a specific error message with a number to help identify the issue.

---

## ✅ Validation Rules

1. **Length Check:**  
   Email must be at least 6 characters long.

2. **Starting Character:**  
   The first character must be an English letter (a-z or A-Z).

3. **@ Symbol Check:**

   - Must contain exactly **one `@` symbol**.

4. **Dot (.) Check:**

   - Email must end with a dot in the **3rd or 4th position from the end**  
     (for example: `.com`, `.net`, `.org`, etc.).

5. **Character Validity Check:**

   - Only allows:
     - Letters (a-z, A-Z)
     - Numbers (0–9)
     - Underscores `_`
     - Dots `.`
     - At-symbol `@`
   - Disallows:
     - Whitespaces
     - Uppercase letters
     - Special characters like `!`, `#`, `%`, etc.

6. **Error Reporting:**  
   The script prints error messages like:
   - `Wrong Email - 1` → Too short
   - `Wrong Email - 2` → First character is not a letter
   - `Wrong Email - 3` → Invalid `@` usage
   - `Wrong Email - 4` → Missing proper dot placement
   - `Wrong Email - 5` → Other character issues

---

## 🛠 Technologies Used

- Python 3.x
- Core string functions
- Conditional logic
- Loops and input handling

---

## 💡 Why I Made This

This project helped me practice:

- String indexing and slicing
- Input validation
- Working with conditions (`if`, `elif`, `else`)
- Logical operators and loops

It's a great starter project for anyone learning how to **validate user input in Python**.

---

## 🧪 Example Output

```text
Enter your email:
> ali.hamza@gmail.com
✅ Email is valid!

> rumi@gmail.com
Wrong Email - 5

> @hamza.com
Wrong Email - 2
```

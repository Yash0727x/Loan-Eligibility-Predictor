# Loan-Eligibility-Predictor
This Python script determines a user's loan eligibility based on three key financial criteria: credit score, annual income, and Debt-to-Income (DTI) ratio. It takes user input, calculates the DTI, applies predefined rules (e.g., Min Score: 650, Max DTI: 35%), and provides a final decision with specific rejection reasons if applicable.

FEATURES

  * Rule-Based Logic: Uses predefined, hardcoded financial standards to make a clear decision.
  *  Input Handling:  Securely collects user data (Credit Score, Income, Debt) using a `try...except` block to prevent crashes from non-numeric input.
  *  DTI Calculation:  Automatically calculates the crucial Debt-to-Income Ratio.
  *  Detailed Feedback:  If rejected, the script lists all the specific reasons why the applicant did not qualify.

HOW TO RUN THE CODE

  *  Python:  You must have Python installed (version 3.x recommended).

 * Execution

1.   Save the Code:  Save the provided script as a file named `loan_checker.py`.

2.   Open Terminal/Command Prompt:  Navigate to the directory where you saved the file.

3.   Run:  Execute the script using the Python interpreter:

    ```bash
    python loan_checker.py
    ```

4.   Follow Prompts:  The program will then ask you to enter the required financial data.

-----

CODE ANALYSIS AND KEY LOGICSN

The script's core functionality relies on a set of static variables (the bank's rules) and sequential `if` statements.

1. The Financial Rules (Constants)

These variables set the standard the user must meet. They are placed at the top of the script for easy modification.

 `MIN_CREDIT_SCORE`:  650   Must be greater than or equal to this value. 
 `MIN_INCOME` :   $40,000   Must be greater than or equal to this value. 
 `MAX_DTI_RATIO` :   0.35 (35%)   Must be less than or equal to this value. 

 2. Debt-to-Income (DTI) Calculation

This section handles a critical financial calculation. The DTI ratio is calculated as:

$$
\text{DTI Ratio} = \frac{\text{Total Monthly Debt Payments}}{\text{Annual Income} / 12}
$$The code includes a safeguard (`if monthly_income > 0`) to prevent a  ZeroDivisionError  if the user inputs an annual income of zero.

3. Conditional Eligibility Check

* The variable  `is_eligible`  starts as `True`.
* The  `reasons_for_rejection`  list starts empty.
* The script runs through  three independent `if` statements . If *any* of the rules are broken:
 1.  `is_eligible` is immediately set to  `False` .
 2.  The specific reason is appended to the `reasons_for_rejection` list.
* This ensures that the user receives  all  points of rejection, not just the first one found.

4. Output

The final decision is based solely on the final state of the `is_eligible` boolean flag. If it's `False`, the script iterates through the collected reasons and prints them clearly.


FUTERE IMPROVEMENTS

*  Modularize Input:  Create a function to handle input collection and validation, making the main script cleaner.
*  Accept Loan Amount:  Add an input for the requested loan amount and incorporate it into the calculation logic (e.g., rejecting if `Loan_Amount > 5 * Annual_Income`).
*  Model Integration:  Convert the project from rule-based logic to a simple  Machine Learning  classifier (like Logistic Regression) trained on historical loan data to make predictions based on probability, rather than strict thresholds.
$$

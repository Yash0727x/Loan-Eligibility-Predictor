# The minimum credit score required for loan approval
MIN_CREDIT_SCORE = 650

# The minimum annual income required (in USD)
MIN_INCOME = 40000

# The maximum allowed Debt-to-Income (DTI) ratio (e.g., 0.40 means 40%)
MAX_DTI_RATIO = 0.35 


# Get User Input (The user's Data) 

print(" ### Loan Eligibility Check ###  ")

try:
    # Get Credit Score input
    credit_score = int(input("Enter your Credit Score : "))
    
    # Get Annual Income input
    annual_income = float(input("Enter your Annual Income (in dollar): $"))
    
    # Get Monthly Debt Payments input
    total_monthly_debt = float(input("Enter your Total Monthly Debt Payments (in dollar): $"))
    
    # Get Monthly Income (calculate)
    monthly_income = annual_income / 12

except ValueError:
    print("\nERROR: Please enter valid numbers for all inputs.")
    # Exit the script if input fails
    exit()


# Calculate DTI Ratio (A key financial health measure)

# DTI is the percentage of your monthly income that goes toward debt.
if monthly_income > 0:
    dti_ratio = total_monthly_debt / monthly_income
else:
    dti_ratio = 0.8 # Set high to guarantee rejection
    print("\nWarning: Monthly income is zero or negative. DTI set to 100%.")


# Check Eligibility 

is_eligible = True # Assume they are eligible unless a rule breaks
reasons_for_rejection = []

# Rule 1: Check Credit Score
if credit_score < MIN_CREDIT_SCORE:
    is_eligible = False
    reasons_for_rejection.append(
        f"Credit Score ({credit_score}) is below the minimum required ({MIN_CREDIT_SCORE})."
    )

# Rule 2: Check Annual Income
if annual_income < MIN_INCOME:
    is_eligible = False
    reasons_for_rejection.append(
        f"Annual Income (${annual_income:,.2f}) is below the minimum required (${MIN_INCOME:,.2f})."
    )

# Rule 3: Check Debt-to-Income Ratio
if dti_ratio > MAX_DTI_RATIO:
    is_eligible = False
    reasons_for_rejection.append(
        f"DTI Ratio ({dti_ratio:.2f} or {dti_ratio*100:.0f}%) is above the maximum allowed ({MAX_DTI_RATIO*100:.0f}%)."
    )


# Display the Final Result 

print("\n" + "="*40)
print("             FINAL DECISION")
print("="*40)

if is_eligible:
    print(" CONGRATULATIONS! You are **ELIGIBLE** for the loan.")
    print("\nBased on the current rules, you meet all requirements.")
else:
    print(" SORRY. You are **NOT ELIGIBLE** for the loan.")
    print("\nReasons for Ineligibility:")
    for reason in reasons_for_rejection:
        print(f"- {reason}")

print("="*40)
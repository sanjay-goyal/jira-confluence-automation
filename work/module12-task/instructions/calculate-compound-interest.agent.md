# Calculate Compound Interest

- Use this instruction when a task requires calculating compound interest for a principal amount, annual interest rate, compounding frequency, and investment duration.
- Use the script at `./tools/compound_interest.py` to compute the final amount and interest earned.
- Invoke the script with four command-line arguments in this order:
  + `principal`
  + `annual_rate_percent`
  + `compounds_per_year`
  + `years`
- Example command:
  + `python ./tools/compound_interest.py 1000 5 12 10`
- Supported behavior:
  + The script calculates the final amount using the compound interest formula: $A = P \times (1 + r/n)^{nt}$
  + It prints the final amount and the interest earned as currency values rounded to two decimal places.
  + It validates input and exits with an error if values are invalid.
- Presentation rules:
  + Report the final amount and interest earned as plain numeric values with two decimal places.
  + Keep the output concise and easy to read.
  + If an invalid input is provided, explain the issue briefly and show the expected usage format.
- Constraints:
  + Do not guess values or estimate missing inputs.
  + Do not use tables or long narratives.
  + Use the exact command format shown above when running the script.
  + Keep the output focused on calculation results and validation feedback only.

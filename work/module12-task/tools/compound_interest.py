import sys


def calculate_compound_interest(principal, annual_rate, compounds_per_year, years):
    amount = principal * (1 + annual_rate / compounds_per_year) ** (compounds_per_year * years)
    interest_earned = amount - principal
    return amount, interest_earned


def main():
    if len(sys.argv) != 5:
        print("Usage: python compound_interest.py <principal> <annual_rate> <compounds_per_year> <years>")
        sys.exit(1)

    try:
        principal = float(sys.argv[1])
        annual_rate = float(sys.argv[2]) / 100.0
        compounds_per_year = int(sys.argv[3])
        years = float(sys.argv[4])

        if principal < 0 or annual_rate < 0 or compounds_per_year <= 0 or years < 0:
            raise ValueError("Inputs must be non-negative and compounds_per_year must be greater than 0.")

        amount, interest_earned = calculate_compound_interest(
            principal, annual_rate, compounds_per_year, years
        )

        print(f"Final amount: {amount:.2f}")
        print(f"Interest earned: {interest_earned:.2f}")
    except ValueError as exc:
        print(f"Error: {exc}")
        sys.exit(1)
    except Exception as exc:
        print(f"Error: {exc}")
        sys.exit(1)


if __name__ == "__main__":
    main()

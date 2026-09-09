# Polynomial Addition using Linked Lists
# Tax Formula Example

# STEP 1: Create a Node
class Node:
    def __init__(self, coeff, exp):
        self.coeff = coeff
        self.exp = exp
        self.next = None


# STEP 2: Insert a term in descending order of exponent
def insert_term(head, coeff, exp):
    new_node = Node(coeff, exp)

    # If list is empty or new exponent is greater
    if head is None or exp > head.exp:
        new_node.next = head
        return new_node

    # If exponent already exists, add coefficients
    if exp == head.exp:
        head.coeff += coeff
        return head

    current = head

    while current.next is not None and current.next.exp > exp:
        current = current.next

    # Same exponent found
    if current.next is not None and current.next.exp == exp:
        current.next.coeff += coeff
    else:
        new_node.next = current.next
        current.next = new_node

    return head


# STEP 3: Create a polynomial
def create_polynomial():
    head = None

    n = int(input("Enter number of terms: "))

    for i in range(n):
        coeff = int(input(f"Enter coefficient for term {i + 1}: "))
        exp = int(input(f"Enter exponent for term {i + 1}: "))

        head = insert_term(head, coeff, exp)

    return head


# STEP 4: Add two polynomials
def add_polynomials(p1, p2):
    result = None

    while p1 is not None and p2 is not None:

        # Same exponent
        if p1.exp == p2.exp:
            coeff = p1.coeff + p2.coeff

            if coeff != 0:
                result = insert_term(result, coeff, p1.exp)

            p1 = p1.next
            p2 = p2.next

        # p1 has larger exponent
        elif p1.exp > p2.exp:
            result = insert_term(result, p1.coeff, p1.exp)
            p1 = p1.next

        # p2 has larger exponent
        else:
            result = insert_term(result, p2.coeff, p2.exp)
            p2 = p2.next

    # Add remaining terms
    while p1 is not None:
        result = insert_term(result, p1.coeff, p1.exp)
        p1 = p1.next

    while p2 is not None:
        result = insert_term(result, p2.coeff, p2.exp)
        p2 = p2.next

    return result


# STEP 5: Display polynomial
def display_polynomial(head):
    if head is None:
        print("0")
        return

    current = head
    first = True

    while current is not None:

        coeff = current.coeff
        exp = current.exp

        if coeff != 0:

            # Sign
            if not first:
                if coeff > 0:
                    print(" + ", end="")
                else:
                    print(" - ", end="")
                    coeff = abs(coeff)
            elif coeff < 0:
                print("-", end="")
                coeff = abs(coeff)

            # Display coefficient and exponent
            if exp == 0:
                print(coeff, end="")

            elif exp == 1:
                if coeff == 1:
                    print("x", end="")
                else:
                    print(f"{coeff}x", end="")

            else:
                if coeff == 1:
                    print(f"x^{exp}", end="")
                else:
                    print(f"{coeff}x^{exp}", end="")

            first = False

        current = current.next

    print()


# STEP 6: Evaluate polynomial
def evaluate_polynomial(head, x):
    total = 0
    current = head

    while current is not None:
        total += current.coeff * (x ** current.exp)
        current = current.next

    return total


# STEP 7: Main Program
def main():

    print("====================================")
    print("      POLYNOMIAL TAX CALCULATOR")
    print("====================================")

    # First polynomial
    print("\nEnter First Tax Formula")
    p1 = create_polynomial()

    # Second polynomial
    print("\nEnter Second Tax Formula")
    p2 = create_polynomial()

    # Display first polynomial
    print("\nTax Formula 1:")
    display_polynomial(p1)

    # Display second polynomial
    print("Tax Formula 2:")
    display_polynomial(p2)

    # Add polynomials
    result = add_polynomials(p1, p2)

    print("\nCombined Tax Formula:")
    display_polynomial(result)

    # Evaluate
    x = float(input("\nEnter income value: "))

    tax = evaluate_polynomial(result, x)

    print(f"Tax Amount for income = {x:g}: {tax:g}")


# Start program
if __name__ == "__main__":
    main()

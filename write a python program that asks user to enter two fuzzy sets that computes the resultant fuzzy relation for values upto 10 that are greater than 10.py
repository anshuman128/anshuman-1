import numpy as np

def get_fuzzy_set(name):
    fuzzy_set = {}
    for i in range(1, 11):
        membership_value = float(input(f"Enter the membership value for {i} in {name}: "))
        fuzzy_set[i] = membership_value
    return fuzzy_set

def fuzzy_relation(set_a, set_b):
    relation = {}
    for x in set_a:
        if x > 6:
            relation[x] = min(set_a[x], set_b[x])
    return relation

def main():
    print("Enter the membership values for Fuzzy Set A (values between 0 and 1):")
    fuzzy_set_a = get_fuzzy_set("Set A")

    print("\nEnter the membership values for Fuzzy Set B (values between 0 and 1):")
    fuzzy_set_b = get_fuzzy_set("Set B")

    result_relation = fuzzy_relation(fuzzy_set_a, fuzzy_set_b)

    print("\nThe resultant fuzzy relation for elements greater than 6 is:")
    for x, val in result_relation.items():
        print(f"({x}, {val})")

if __name__ == "__main__":
    main()
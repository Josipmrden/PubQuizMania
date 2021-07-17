from fuzzywuzzy import fuzz


if __name__ == "__main__":
    a1 = "Srbija"
    a2 = "U Srbiji"
    print(f"a: {fuzz.ratio(a1, a2)}")

    b1 = "I don't wanna be"
    b2 = "I don't want to be"
    print(f"b {fuzz.ratio(b1, b2)}")

    c1 = "Hrvatska"
    c2 = "Srbija i Crna Gora"
    print(f"c {fuzz.ratio(c1, c2)}")

    d1 = "Pakistan"
    d2 = "Tadžikistan"
    print(f"d {fuzz.ratio(d1, d2)}")

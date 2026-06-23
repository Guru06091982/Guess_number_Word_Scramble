# total amount to be formed
amount = 10

# counter tp count the number of ways
count = 0

# Loop through possible numbers of ₹10 coins
for ten in range(amount // 10 + 1):

    # Loop through possible numbers of ₹5 coins
    for five in range(amount // 5 + 1):

        # Loop through possible numbers of ₹2 coins
        for two in range(amount // 2 + 1):

            # Loop through possible numbers of ₹1 coins
            for one in range(amount + 1):

                # Check if the combination sums to ₹10
                if (ten * 10) + (five * 5) + (two * 2) + (one * 1) == amount:

                    count += 1

                    print(f"Way {count}: "
                          f"₹10 coins = {ten}, "
                          f"₹5 coins = {five}, "
                          f"₹2 coins = {two}, "
                          f"₹1 coins = {one}")

                    # Print total number of ways
                    print("\nTotal number of ways:", count)
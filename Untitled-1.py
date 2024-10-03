attempts = 0
max_attempts = 3

while attempts < max_attempts:
    try:
        age = int(input("How old are you? "))  

        if age >= 18 and age < 100:
            print("You're 18! (or older)")
            break

        elif age >= 100 or age <= 1:
            print("Please enter a valid age.")
            attempts += 1

        else:
            print("You're not 18 years old.")
            attempts += 1

    except ValueError:
        print("Please enter a valid number.")
        attempts += 1

if attempts == max_attempts:
    print("Maximum attempts reached. Exiting.")

def is_prime(n):

    if n < 2:
        return False  
    for i in range(2, n):  
        if n % i == 0:  
            return False
    return True  

def prime_sum(start, end):
    total = 0
    for number in range(start, end + 1): 
        if is_prime(number):  
            total += number  
    return total  


def length_converter(value, unit):
    
    if unit == 'm' or unit == 'M':
        return round(value * 3.28084, 2)  
    elif unit == 'f' or unit == 'F':
        return round(value / 3.28084, 2)  
    else:
        return "Invalid unit" 

def consonant_counter(text):

    vowels = "aeiouAEIOU" 
    consonants = 0 
    for char in text:
        if char.isalpha() and char not in vowels:  
            consonants += 1 
    return consonants

def min_max_finder(numbers):
    smallest = numbers[0] 
    largest = numbers[0]
    for num in numbers:
        if num < smallest:  
            smallest = num
        if num > largest:  
            largest = num
    return smallest, largest  

def is_palindrome(text):
    cleaned_text = "".join(text.split()).lower()  
    return cleaned_text == cleaned_text[::-1]  

def word_counter(file_path):
    target_words = ["the", "was", "and"]  
    word_count = {word: 0 for word in target_words} 
    
    try:
        with open(file_path, 'r') as file: 
            for line in file:  
                words = line.lower().split()  
                for word in words:
                    if word in target_words:  
                        word_count[word] += 1  
        return word_count  
    except FileNotFoundError:  
        return "Error: File not found."


def main():
    while True:  
        print("\nSelect a function (1-6):")  
        print("1. Calculate the sum of prime numbers")
        print("2. Convert length units")
        print("3. Count consonants in a string")
        print("4. Find min and max numbers")
        print("5. Check if a string is a palindrome")
        print("6. Count words in a file")
        print("7. Exit")

        choice = input("Enter your choice: ") 
        
        if choice == '1':
            start = int(input("Enter the start number: "))
            end = int(input("Enter the end number: "))
            print("Sum of primes:", prime_sum(start, end))
        elif choice == '2':
            value = float(input("Enter the value: "))
            unit = input("Enter the unit (m or f): ")
            print("Converted value:", length_converter(value, unit))
        elif choice == '3':
            text = input("Enter a string: ")
            print("Number of consonants:", consonant_counter(text))
        elif choice == '4':
            numbers = list(map(int, input("Enter numbers separated by space: ").split()))
            min_num, max_num = min_max_finder(numbers)
            print(f"Smallest: {min_num}, Largest: {max_num}")
        elif choice == '5':
            text = input("Enter a string: ")
            if is_palindrome(text):
                print("Yes, it's a palindrome!")
            else:
                print("No, it's not a palindrome.")
        elif choice == '6':
            file_path = input("Enter the file path: ")
            print("Word count:", word_counter(file_path))
        elif choice == '7':
            print("Exiting...")
            break  
        else:
            print("Invalid choice, please select a valid option.")  


if __name__ == "__main__":
    main()

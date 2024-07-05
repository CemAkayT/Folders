#!/Library/Frameworks/Python.framework/Versions/3.12/bin/python3


def generate_frequency_array(numbers):
    # Initialize a dictionary to store frequencies
    frequency_dict = {}

    # Count the occurrences of each number
    for num in numbers:
        if num in frequency_dict:
            frequency_dict[num] += 1
        else:
            frequency_dict[num] = 1

    # Generate the frequency array
    frequency_array = [0] * 100  # Initialize the frequency array with zeros
    for num, frequency in frequency_dict.items():
        frequency_array[num] = frequency

    return frequency_array

# Input list of integers
numbers = [63, 25, 73, 1, 98, 73, 56, 84, 86, 57, 16, 83, 8, 25, 81, 56, 9, 53, 98, 67, 99, 12, 83, 89, 80, 91, 39, 86, 76, 85, 74, 39, 25, 90, 59, 10, 94, 32, 44, 3, 89, 30, 27, 79, 46, 96, 27, 32, 18, 21, 92, 69, 81, 40, 40, 34, 68, 78, 24, 87, 42, 69, 23, 41, 78, 22, 6, 90, 99, 89, 50, 30, 20, 1, 43, 3, 70, 95, 33, 46, 44, 9, 69, 48, 33, 60, 65, 16, 82, 67, 61, 32, 21, 79, 75, 75, 13, 87, 70, 33]

# Generate the frequency array
frequency_array = generate_frequency_array(numbers)

# Print the frequency array
print(f'Freq arr:\n', *frequency_array)




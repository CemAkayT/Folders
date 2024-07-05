#!/Library/Frameworks/Python.framework/Versions/3.12/bin/python3

def flippingBits(n: int) -> int:
    return ~n & 0xFFFFFFFF

# Example usage:
original_integer = 0 
flipped_integer = flippingBits(original_integer)

print("Original integer:", original_integer)
print("Flipped integer:", flipped_integer)
def octal_to_binary(octal_str):   
    octal_to_binary_map = {
        '0': '000', '1': '001', '2': '010', '3': '011',
        '4': '100', '5': '101', '6': '110', '7': '111'
    }
  
    binary_str = ''.join(octal_to_binary_map[digit] for digit in octal_str)
 
    return binary_str.lstrip('0') or '0'

def main():
    import sys

    input = sys.stdin.read().strip()

    print(octal_to_binary(input))

if __name__ == "__main__":
    main()


if __name__ == "__main__":
    x, y, z = input("Enter an arithmetic expression (x y z): ").split()
    x, z = int(x), int(z)  
    
    if y == '+':
        result = x + z
    elif y == '-':
        result = x - z
    elif y == '*':
        result = x * z
    elif y == '/':
        result = x / z
    else:
        print("Error: Invalid operator")
        exit()
    
    print(f"{result:.1f}")
    
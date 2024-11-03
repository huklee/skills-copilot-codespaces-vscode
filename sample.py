def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)
    
def sum_list(lst):
    if len(lst) == 0:
        return 0
    else:
        return lst[0] + sum_list(lst[1:])

def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

def reverse_string(s):
    if len(s) == 0:
        return ''
    else:
        return s[-1] + reverse_string(s[:-1])
    
def is_palindrome(s):
    if len(s) == 0 or len(s) == 1:
        return True
    else:
        return s[0] == s[-1] and is_palindrome(s[1:-1])
    
def test_factorial():
    try:
        assert factorial(0) == 1
        assert factorial(1) == 1
        assert factorial(5) == 120
        assert factorial(10) == 3628800
        print("test_factorial passed")
    except AssertionError:
        print("test_factorial failed")

def test_sum_list():
    try:
        assert sum_list([]) == 0
        assert sum_list([1]) == 1
        assert sum_list([1, 2, 3, 4, 5]) == 15
        assert sum_list([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 55
        print("test_sum_list passed")
    except AssertionError:
        print("test_sum_list failed")

def test_fibonacci():
    try:
        assert fibonacci(0) == 0
        assert fibonacci(1) == 1
        assert fibonacci(2) == 1
        assert fibonacci(3) == 2
        assert fibonacci(4) == 3
        assert fibonacci(5) == 5
        assert fibonacci(6) == 8
        assert fibonacci(7) == 13
        assert fibonacci(8) == 21
        assert fibonacci(9) == 34
        assert fibonacci(10) == 55
        print("test_fibonacci passed")
    except AssertionError:
        print("test_fibonacci failed")
    
def test_reverse_string():
    try:
        assert reverse_string('') == ''
        assert reverse_string('a') == 'a'
        assert reverse_string('abc') == 'cba'
        assert reverse_string('hello') == 'olleh'
        assert reverse_string('world') == 'dlrow'
        print("test_reverse_string passed")
    except AssertionError:
        print("test_reverse_string failed")
def main():
    import sys
    if len(sys.argv) != 2:
        print('Usage: python sample.py <number>')
        sys.exit(1)
    
    # run tests
    test_factorial()
    test_sum_list()
    test_fibonacci()
    test_reverse_string()
    
    # read the input file that consists of lines of numbers
    print(f"Running tests with input file: {sys.argv[1]}")
    with open(sys.argv[1], 'r') as f:
        for line in f:
            n = int(line.strip())
            print(f"=== Processing number: {n} Result: {fibonacci(n)}")
          
if __name__ == '__main__':
    main()
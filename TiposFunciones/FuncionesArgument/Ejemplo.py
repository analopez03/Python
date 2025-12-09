def my_function(geeting, *name):
    for n in name:
        print(f"{geeting} {n}")
        
my_function("Hello", "Alice", "Bob", "Charlie")
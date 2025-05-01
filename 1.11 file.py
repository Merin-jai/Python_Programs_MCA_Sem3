with open("f1.txt") as f1: 
    with open("f2.txt", "w") as f2: 
        for line in f1: 
            f2.write(line) 
            print("Success") 
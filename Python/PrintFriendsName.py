def print_friends_names(*names):
    
    reversed_names = list(names[::-1])

    
    if len(reversed_names) > 1:
        reversed_names[-1] = "and " + reversed_names[-1]

    
    output = ", ".join(reversed_names)

    print("Hi", output)



if __name__ == "__main__":
    print_friends_names("Mahesh", "Suresh", "Devesh")

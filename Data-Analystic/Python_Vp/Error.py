# x = 0
# while True:

#     try:
#         x = int(input("Enter a number: "))
#         break
#     except ValueError:
#         print(" It`s a not valid number !")
#         x += 1
#     except KeyboardInterrupt:
#         print(" ")
#         break
#     finally:
#         print(" \n\nAttempted Input {} \n\n".format(x))


def create_groups(items, n):
    try:
        size = len(items) // n
    except ZeroDivisionError:
        print("WARNING: Returning empty list. Please use a nonzero number.")
        return []
    else:
        groups = []
        for i in range(0, len(items), size):
            groups.append(items[i:i + size])
        return groups
    finally:
        print("{} groups returned.".format(n))

print("Creating 6 groups...")
for group in create_groups(range(32), 6):
    print(list(group))

print("\nCreating 0 groups...")
for group in create_groups(range(32), 0):
    print(list(group))



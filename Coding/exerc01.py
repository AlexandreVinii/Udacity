
manifest = [("banana", 10),("Ariana Serafim", 61),
            ("cheese", 28), ("Machine", 210), ("amoeba", 300)]

weight = 0
items = []
for cargo_name, cargo_weight in manifest:
    print("current Weight :  {}".format(weight))
    if weight >= 100:
        print("Breaking now !")
        break

    else:
        print("adding {} ({})".format(cargo_name, cargo_weight))
        items.append(cargo_name)
        weight += cargo_weight

print("\nFinal Weight: {}".format(weight))
print("Final Items: {}".format(items))

print("\nMETHOD 2")
weight = 0
items = []
for cargo_name, cargo_weight in manifest:
    print("current weight: {}".format(weight))
    print("current cargo_weight: {}".format(cargo_weight))
    if weight >= 100:
        print("  breaking from the loop now!")
        break
    elif weight + cargo_weight > 100:
        print("  skipping {} ({})".format(cargo_name, cargo_weight))
        continue
    else:
        print("  adding {} ({})".format(cargo_name, cargo_weight))
        items.append(cargo_name)
        weight += cargo_weight

print("\nFinal Weight: {}".format(weight))
print("Final Items: {}".format(items))
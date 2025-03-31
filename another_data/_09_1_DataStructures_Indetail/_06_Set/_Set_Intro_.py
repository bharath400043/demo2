# Ceate
days = set(["Mon", "Tue", "Wed", "Thu", "Fri", "Sat"])
print("set of days:", days)
months = {"Jan", "Feb", "Mar"}
print("set of months:", months)

# Retrive
for d in days:
    print(d)

# Update
days.add("Sun")
print("set of days after update:", days)

# Delete
days.discard("Sun")
print("set of days after delete:", days)

# Union
days1 = {"mon", "Tue", "Wed"}
days2 = {"Wed", "Thu", "Fri", "Sat", "Sun"}
alldays = days1 | days2
print("Union all days: ", alldays)

# Interseection
days1 = {"mon", "Tue", "Wed"}
days2 = {"Wed", "Thu", "Fri", "Sat", "Sun"}
alldays = days1 & days2
print("Intersection all days: ", alldays)

# Difference
days1 = {"mon", "Tue", "Wed"}
days2 = {"Wed", "Thu", "Fri", "Sat", "Sun"}
alldays = days1 - days2
print("Diff all days days1 - days2: ", alldays)
print("Diff all days days2 - days1: ", days2 - days1)

# Compare
days1 = {"mon", "Tue", "Wed"}
days2 = {"Wed", "Thu", "Fri", "Sat", "Sun"}
subset = days1 <= days2
superset = days1 >= days2
print("subset: ", subset)
print("superset: ", superset)

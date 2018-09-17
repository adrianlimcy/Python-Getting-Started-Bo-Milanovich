student_names=["James", "Katarina", "Jessica", "Mark", "Bort", "Frank Grimes", "Max Power"]

for name in student_names:
    if name == "Mark":
        print(f"Found him! {name}")
        break
    print(f"Currently testing {name}")

for name in student_names:
    if name == "Bort":
        continue
        print(f"Found him! {name}")
    print(f"Currently testing {name}")

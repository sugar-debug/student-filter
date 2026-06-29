import csv

def main():
    print("Choices are:\n1.Filter by age>25\n2.Filter by grade")
    try:
        choice=int(input("Enter choice number:")) 
        if choice==1:
            age_criteria("students.csv")
        elif choice==2:
            grade_criteria("students.csv")
        else:
            print("Invalid choice")
    except ValueError:
        print("Invalid choice.")

def age_criteria(filename):
    try:
        with open(filename,"r") as f:
            reader=csv.reader(f)
            next(reader)
            print(f"\n{'Name':<12} {'Age':<6} {'City':<14} {'Grade'}")
            print("-"*40)
            count=0
            for row in reader:
                try:
                    if int(row[1])>25:
                        print(f"{row[0]:<12} {row[1]:<6} {row[2]:<14} {row[3]}")
                        count+=1
                except ValueError:
                    print("Invalid Row.")
            print(f"{count} rows matched.")
    except FileNotFoundError:
         print("File does not exist.")


def grade_criteria(filename):
    user=input("Enter Grade:")
    with open(filename,"r") as f:
        reader=csv.reader(f)        
        next(reader)
        print(f"\n{'Name':<12} {'Age':<6} {'City':<14} {'Grade'}")
        print("-"*40)
        count=0
        for row in reader:
            try:
                if row[3].strip().upper()==user.strip().upper():
                    print(f"{row[0]:<12} {row[1]:<6} {row[2]:<14} {row[3]}")
                    count+=1            
            except IndexError:
                print("Skipping invalid row.")
        print(f"{count} rows matched.")

main()

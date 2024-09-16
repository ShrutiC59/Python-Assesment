import json

sat_results =[]

def get_pass_fail(sat_score):
    return "Pass" if sat_score > 30 else "Fail"

def insert_data():
    name = input("Enter Name: ")
    address = input("Enter Address: ")
    city = input("Enter city: ")
    country = input("Enter country: ")
    pincode = input("Enter Pincode: ")
    sat_score = float(input("Enter SAT score: "))
    passed = get_pass_fail(sat_score)

    for record in sat_results:
        if record['Name'] == name:
            print("Error: name must be unique")
            return

    sat_results.append({
        'Name': name,
        'Address': address,
        'City': city,
        'Country': country,
        'Pincode': pincode,
        'SAT Score': sat_score,
        'Passed': passed
    })

    print("Record inserted successfully!")


def view_data():
    print(json.dumps(sat_results, indent=4))

def get_rank():
    name = input("Enter Name: ")
    sorted_results = sorted(sat_results, key=lambda x:x['SAT Score'], reverse =True)

    for index, record in enumerate(sorted_results, start=1):
        if record['Name'] == name:
            print(f"Rank of {name} is {index}")
            return
    print(f"No record found for {name}")

def update_score():
    name = input("Enter Name to update SAT score: ")

    for record in sat_results:
        if record['Name'] == name:
            new_score = float(input("Enter new SAT Score: "))
            record['SAT Score'] = new_score
            record['Passed'] = get_pass_fail(new_score)
            print(f"Score updated for {name}")
            return
    print(f"No record found for {name}")

def delete_record():
    name = input("Enter Name to delete: ")

    for record in sat_results:
        if record['Name'] == name:
            sat_results.remove(record)
            print(f"Record for {name} deleted")
            return
    print(f"No record found for {name}")

def calculate_average():
    if not sat_results:
        print("No records to calculate average")
        return
    avg_score = sum(record['SAT Score'] for record in sat_results )/ len(sat_results)
    print(f"Average SAT Score : {avg_score:.2f}")

def filter_by_status():
    status = input("Enter status to filter by (Pass/Fail): ")
    filtered_result = [record for record in sat_results if record['Passed']==status]
    if filtered_result:
        print(json.dumps(filtered_result, indent=4))
    else:
        print(f"No records are found with status {status}")

def save_to_json_file():
    with open('sat_result_json', 'w') as file:
        json.dump(sat_results, file, indent=4)
    print("Data saved to sat_results.json")


def main_menu():
    while True:
        print("\nSAT ResulT Management")
        print("1. Insert Data")
        print("2. View all data")
        print("3. Get rank")
        print("4. Update score")
        print("5. Delete one record")
        print("6. Calculate Average SAT Score")
        print("7. Filter records by Pass/Fail Status")
        print("8. Put the inserted data in json format in a file")
        print("9. Exit")
        choice = input('Select an option: ')
        if   choice =="1":
            insert_data()
        elif choice =="2":
            view_data()
        elif choice =="3":
            get_rank()
        elif choice =="4":
            update_score()
        elif choice =="5":
            delete_record()
        elif choice =="6":
            calculate_average()
        elif choice =="7":
            filter_by_status()
        elif choice =="8":
            save_to_json_file()
        elif choice=="8":
            print("Exiting program")
            break
        else:
            print("Invalid choice ")

if __name__ == "__main__":
    main_menu()


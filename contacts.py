import json

def load_contacts():
    try:
        with open("contacts.json") as f:
            return json.load(f)
    except FileNotFoundError:
        return []
    
def save_contacts(contacts):
    with open("contacts.json", "w") as f:
        json.dump(contacts, f, indent=2)

def add_contact(name, phone):
    contacts = load_contacts()
    contacts.append({"name": name, "phone": phone})
    save_contacts(contacts)
    print(f"{name} added!")

def show_contacts():
    contacts = load_contacts()
    if not contacts:
        print("No contacts yet.")
        return
    for c in contacts:
        print(f"Name: {c['name']} | phone: {c['phone']}")

add_contact("Gad", "0716969917")
add_contact("Kelvin", "0704407933")
show_contacts()
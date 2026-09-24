tickets = []

def add_ticket():
    """Add a new incident ticket to the list."""
    incident_id = input("Enter Incident ID: ").strip()
    bot = input("Enter Bot Name: ").strip()
    description = input("Enter Short Description: ").strip()

    for ticket in tickets:
        if ticket["id"] == incident_id:
            print(f"Ticket with Incident ID '{incident_id}' already exists.\n")
            return

    ticket = {"id": incident_id, "bot": bot, "description": description}
    tickets.append(ticket)
    print(f"Ticket '{incident_id}' added successfully.\n")


def display_tickets():
    """Display all active incident tickets."""
    if not tickets:
        print("No active incident tickets.\n")
        return

    print("\n" + "-" * 70)
    print(f"{'Incident ID':<15}{'Bot':<20}{'Short Description'}")
    print("-" * 70)
    for ticket in tickets:
        print(f"{ticket['id']:<15}{ticket['bot']:<20}{ticket['description']}")
    print("-" * 70 + "\n")


def search_ticket():
    """Search for a ticket using its Incident ID."""
    incident_id = input("Enter Incident ID to search: ").strip()

    for ticket in tickets:
        if ticket["id"] == incident_id:
            print("\nTicket Found:")
            print(f"Incident ID : {ticket['id']}")
            print(f"Bot         : {ticket['bot']}")
            print(f"Description : {ticket['description']}\n")
            return

    print(f"No ticket found with Incident ID '{incident_id}'.\n")


def remove_ticket():
    """Remove a resolved incident ticket using its Incident ID."""
    incident_id = input("Enter Incident ID to remove: ").strip()

    for ticket in tickets:
        if ticket["id"] == incident_id:
            tickets.remove(ticket)
            print(f"Ticket '{incident_id}' removed successfully.\n")
            return

    print(f"No ticket found with Incident ID '{incident_id}'.\n")


def count_tickets():
    """Display the total number of active incident tickets."""
    print(f"Total active incident tickets: {len(tickets)}\n")


def load_sample_data():
    """Preload the 10 sample incident tickets given in the lab exercise."""
    sample_data = [
        ("INC1392939", "BOT-Inventory", "Failed to generate the daily report"),
        ("INC1392940", "BOT-Email", "Failed to send the scheduled notification"),
        ("INC1392941", "BOT-DataSync", "Encountered an error during data transfer"),
        ("INC1392942", "BOT-Invoice", "Failed to process an invoice"),
        ("INC1392943", "BOT-Report", "Failed to generate the weekly report"),
        ("INC1392944", "BOT-FileTransfer", "Failed to upload the required file"),
        ("INC1392945", "BOT-DataEntry", "Encountered an error while entering records"),
        ("INC1392946", "BOT-Backup", "Failed to complete the scheduled backup"),
        ("INC1392947", "BOT-Validation", "Failed to validate the submitted records"),
        ("INC1392948", "BOT-Notification", "Failed to send the system alert"),
    ]
    for incident_id, bot, description in sample_data:
        tickets.append({"id": incident_id, "bot": bot, "description": description})
    print(f"{len(sample_data)} sample incident tickets loaded.\n")


def show_menu():
    print("=" * 50)
    print(" IT AUTOMATION INCIDENT TICKET MANAGER")
    print("=" * 50)
    print("1. Add a new incident ticket")
    print("2. Display all active incident tickets")
    print("3. Search for an incident ticket")
    print("4. Remove a resolved incident ticket")
    print("5. Display total number of active tickets")
    print("6. Load sample data (10 test tickets)")
    print("7. Exit")
    print("=" * 50)


def main():
    while True:
        show_menu()
        choice = input("Enter your choice (1-7): ").strip()
        print()

        if choice == "1":
            add_ticket()
        elif choice == "2":
            display_tickets()
        elif choice == "3":
            search_ticket()
        elif choice == "4":
            remove_ticket()
        elif choice == "5":
            count_tickets()
        elif choice == "6":
            load_sample_data()
        elif choice == "7":
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 7.\n")


if __name__ == "__main__":
    main()

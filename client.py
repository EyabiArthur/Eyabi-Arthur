"""
client.py
Community Watch Neighborhood – Client Application

Description:
    This client allows a user to connect to the Community Watch Network
    and perform actions such as:
    - Sending a suspicious activity report
    - Viewing alerts
    - Viewing members
    - Registering a new member

    It communicates with the VirtualNetwork and StorageNodes
    to simulate a distributed community watch system.
"""

from storage_virtual_network import VirtualNetwork
from storage_virtual_node import StorageNode


class CommunityWatchClient:
    def __init__(self):
        # Connect to network
        print("Connecting to Community Watch Network...\n")
        self.network = VirtualNetwork("Client Side Network")

        # Create client-side nodes
        self.client_node = StorageNode("Client Node")
        self.network.add_node(self.client_node)

        print("Client connected successfully.\n")

    # -----------------------------------------------------
    # CLIENT FUNCTIONS
    # -----------------------------------------------------

    def send_alert(self, message):
        """
        Send alert message to the network.
        """
        print("Sending alert to network...")
        self.network.broadcast(f"New Alert: {message}")
        print("Alert broadcasted.\n")

    def fetch_alerts(self):
        """
        Retrieve alerts stored in the network.
        """
        print("Fetching community alerts...\n")
        data = []
        for node in self.network.nodes:
            node_data = node.get_all_data()
            if node_data:
                data.extend(node_data)

        return data

    def register_member(self, name, phone):
        """
        Register a new member into the network.
        """
        member_info = f"{name} - {phone}"
        self.network.broadcast(f"New Member: {member_info}")
        print("Member information broadcasted.\n")

    # -----------------------------------------------------
    # MENU INTERFACE
    # -----------------------------------------------------

    def run(self):
        while True:
            print("====== COMMUNITY WATCH CLIENT ======")
            print("1. Send suspicious activity alert")
            print("2. View alerts")
            print("3. Register new member")
            print("4. Exit")
            choice = input("Enter your choice: ")

            if choice == "1":
                message = input("Describe the suspicious activity: ")
                self.send_alert(message)

            elif choice == "2":
                alerts = self.fetch_alerts()
                print("\n--- ALERTS RECEIVED FROM NETWORK ---")
                if not alerts:
                    print("No alerts found.\n")
                else:
                    for idx, alert in enumerate(alerts, 1):
                        print(f"{idx}. {alert}")
                print()

            elif choice == "3":
                name = input("Enter member name: ")
                phone = input("Enter phone number: ")
                self.register_member(name, phone)

            elif choice == "4":
                print("Disconnecting client. Goodbye!")
                break

            else:
                print("Invalid choice. Try again.\n")


# -----------------------------------------------------
# ENTRY POINT
# -----------------------------------------------------
if __name__ == "__main__":
    client = CommunityWatchClient()
    client.run()

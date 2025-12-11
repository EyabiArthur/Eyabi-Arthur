"""
cloud.py
Cloud Simulation Layer for Community Watch Neighborhood System

DESCRIPTION:
    This module simulates a cloud-style distributed environment
    made of Virtual Storage Nodes and a Virtual Storage Network.
    It acts as the CLOUD CONTROLLER: managing nodes, 
    replicating data, broadcasting alerts, and monitoring capacity.

Used by:
    - main.py
    - client.py
    - storage_virtual_network.py
    - storage_virtual_node.py
"""


from storage_virtual_node import StorageNode
from storage_virtual_network import VirtualNetwork


class CloudController:
    """
    Top-level controller that manages the entire cloud environment.
    """

    def __init__(self, cloud_name="CommunityWatchCloud"):
        self.cloud_name = cloud_name
        self.network = VirtualNetwork(f"{cloud_name}-Network")
        self.nodes = []

        print(f"Cloud Controller '{self.cloud_name}' initialized.\n")

    # ======================================================
    # CLOUD NODE MANAGEMENT
    # ======================================================

    def add_node(self, name):
        """
        Creates and attaches a new virtual storage node.
        """
        node = StorageNode(name)
        self.nodes.append(node)
        self.network.add_node(node)

        print(f"[CLOUD] Node '{name}' added to cloud and network.\n")
        return node

    def list_nodes(self):
        """
        Returns a list of all nodes in the cloud.
        """
        return [node.name for node in self.nodes]

    # ======================================================
    # DATA OPERATIONS
    # ======================================================

    def store_global_data(self, data):
        """
        Stores the given data across all nodes 
        (acts like replication in distributed systems).
        """
        print("[CLOUD] Replicating data to all nodes...")
        for node in self.nodes:
            node.store_data(data)

        print("[CLOUD] Replication complete.\n")

    def broadcast_alert(self, alert):
        """
        Sends an alert to ALL nodes and the virtual network.
        """
        print("[CLOUD] Broadcasting community alert...")
        self.network.broadcast(f"ALERT: {alert}")
        print("[CLOUD] Alert broadcast complete.\n")

    def collect_all_data(self):
        """
        Collects all data stored across the cloud and returns a combined list.
        """
        print("[CLOUD] Collecting data from all nodes...")
        all_data = []

        for node in self.nodes:
            ndata = node.get_all_data()
            if ndata:
                all_data.extend(ndata)

        return all_data

    # ======================================================
    # CLOUD STATUS
    # ======================================================

    def cloud_status(self):
        """
        Displays cloud-wide node and data status.
        """
        print("======== CLOUD STATUS ========")
        print(f"Cloud Name: {self.cloud_name}")
        print(f"Network: {self.network.network_name}")
        print(f"Total Nodes: {len(self.nodes)}")

        for node in self.nodes:
            print(f" - Node: {node.name} | Items stored: {len(node.storage)}")

        print("================================\n")


# ======================================================
# TEST CLOUD (if run alone)
# ======================================================
if __name__ == "__main__":
    cloud = CloudController()

    # Create nodes
    cloud.add_node("AdminNode")
    cloud.add_node("AlertNode")
    cloud.add_node("MembersNode")

    # Store sample data
    cloud.store_global_data("Test replication message.")

    # Broadcast alert
    cloud.broadcast_alert("Suspicious movement detected near Zone 3.")

    # Display all data
    print("\nCollected Data from Cloud:")
    print(cloud.collect_all_data())

    # Cloud status
    cloud.cloud_status()

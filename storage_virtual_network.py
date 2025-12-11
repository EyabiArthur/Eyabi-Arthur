"""
storage_virtual_network.py
-----------------------------------
Virtual Network Layer for the Community Watch Cloud System.

DESCRIPTION:
    Represents a virtual network that connects storage nodes.
    Supports:
        - Adding nodes
        - Broadcasting messages to all nodes
        - Network-level monitoring

Works seamlessly with:
    - StorageNode
    - CloudController
    - Client & Main applications
"""


class VirtualNetwork:
    def __init__(self, network_name="Virtual-Network"):
        self.network_name = network_name
        self.nodes = []     # List of StorageNode instances

        print(f"[Network Created] {self.network_name}")

    # ====================================================
    # NETWORK NODE MANAGEMENT
    # ====================================================

    def add_node(self, node):
        """
        Add a StorageNode to the network.
        """
        self.nodes.append(node)
        print(f"[Network] Node '{node.name}' added to {self.network_name}")

    def remove_node(self, node):
        """
        Remove a node from the network.
        """
        if node in self.nodes:
            self.nodes.remove(node)
            print(f"[Network] Node '{node.name}' removed.")
        else:
            print(f"[Network] Node '{node.name}' not found.")

    # ====================================================
    # NETWORK COMMUNICATION
    # ====================================================

    def broadcast(self, message):
        """
        Broadcasts a message to ALL nodes in the network.
        Message is stored on each node.
        """
        print(f"[Broadcast] Sending message to all nodes: {message}")
        for node in self.nodes:
            node.store_data(message)
        print(f"[Broadcast Completed]\n")

    # ====================================================
    # NETWORK STATUS
    # ====================================================

    def list_nodes(self):
        """
        Returns a list of node names in the network.
        """
        return [node.name for node in self.nodes]

    def network_status(self):
        """
        Prints a summary of the network.
        """
        print("======== NETWORK STATUS ========")
        print(f"Network Name: {self.network_name}")
        print(f"Total Nodes: {len(self.nodes)}")
        for node in self.nodes:
            print(f" - Node: {node.name} | Items stored: {len(node.storage)}")
        print("================================\n")

    def __repr__(self):
        return f"<VirtualNetwork {self.network_name}: {len(self.nodes)} nodes>"

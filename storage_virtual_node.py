"""
storage_virtual_node.py
-----------------------------------
A Virtual Storage Node for the Community Watch Cloud System.

DESCRIPTION:
    Represents a cloud storage node that stores data items.
    Each node has:
        - A name
        - Local storage (list)
        - Basic methods to store, retrieve, and clear data
    Works with VirtualNetwork and CloudController.
"""


class StorageNode:
    def __init__(self, name):
        self.name = name
        self.storage = []      # Local data store
        print(f"[Node Created] {self.name}")

    # ====================================================
    # DATA OPERATIONS
    # ====================================================

    def store_data(self, data):
        """
        Store a piece of data on this node.
        """
        self.storage.append(data)
        print(f"[{self.name}] Data stored: {data}")

    def get_all_data(self):
        """
        Returns a copy of all stored data.
        """
        return list(self.storage)

    def clear_data(self):
        """
        Clears all data from the node.
        """
        self.storage = []
        print(f"[{self.name}] Storage cleared.")

    # ====================================================
    # NODE STATUS
    # ====================================================

    def __repr__(self):
        return f"<StorageNode {self.name}: {len(self.storage)} items>"

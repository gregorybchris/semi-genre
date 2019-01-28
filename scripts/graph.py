import json
import numpy as np


class Graph:
    def __init__(self):
        self._nodes = dict()

    def add_node(self, node_key, node_data):
        if node_key in self._nodes:
            raise KeyError(f"Key {node_key} already exists")
        self._nodes[node_key] = Node(node_key, node_data)

    def has_node(self, node_key):
        return node_key in self._nodes

    def add_link(self, source_key, target_key, value=1):
        self._check_key(source_key)
        self._check_key(target_key)
        if source_key == target_key:
            raise ValueError(f"Self links not allowed, key={target_key}")

        source_node = self._nodes[source_key]
        if target_key in source_node.neighbors:
            source_node.neighbors[target_key] += value
        else:
            source_node.neighbors[target_key] = value

    def add_complete_links(self, node_keys):
        self._check_duplicates(node_keys)
        for node_key in node_keys:
            self._check_key(node_key)

        for key_a in node_keys:
            for key_b in node_keys:
                if key_a != key_b:
                    self.add_link(key_a, key_b)

    def _check_duplicates(self, node_keys):
        seen = set()
        for node_key in node_keys:
            if node_key in seen:
                raise ValueError(f"Self links not allowed, key={node_key}")
            else:
                seen.add(node_key)

    def _check_key(self, node_key):
        if node_key not in self._nodes:
            raise KeyError(f"Key {node_key} not found")

    def to_json(self, min_weight=1):
        nodes = [node.to_dict() for node in self._nodes.values()]
        links = []
        for node_key, node in self._nodes.items():
            for neighbor_key, value in node.neighbors.items():
                if value >= min_weight:
                    link = {
                        'source': node_key,
                        'target': neighbor_key,
                        'value': value
                    }
                    links.append(link)
        out = {
            'nodes': nodes,
            'links': links
        }
        return json.dumps(out)


class Node():
    def __init__(self, node_key, node_data):
        self.key = node_key
        self.data = node_data
        self.neighbors = dict()

    def to_dict(self):
        return {
            'id': self.key,
            'data': self.data
        }

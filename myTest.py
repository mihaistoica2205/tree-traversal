import unittest
from tree import Tree

class TestTree(unittest.TestCase):

    def setUp(self):
        self.tree = Tree()
        self.tree.add(3)
        self.tree.add(4)
        self.tree.add(0)
        self.tree.add(8)
        self.tree.add(2)

    def test_find_existing_node(self):
        node = self.tree._find(3, self.tree.root)
        self.assertEqual(node.data, 3)

    def test_find_nonexisting_node(self):
        node = self.tree._find(1, self.tree.root)
        self.assertIsNone(node)
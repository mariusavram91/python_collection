#!/usr/bin/python3

import unittest


class Node:
    def __init__(self, number):
        self.number = number
        self.left = None
        self.right = None


def count_nodes_in_longest_unique_path(tree):
    return len(find_longest_unique_path(tree, [], 0, []))


def find_all_paths(tree):
    if tree is None:
        return []

    if tree.left is None and tree.right is None:
        return [tree.number]

    left_subtree = find_all_paths(tree.left)
    right_subtree = find_all_paths(tree.right)
    full_subtree = left_subtree + right_subtree

    list1 = []
    for leaf in full_subtree:
        list1.append([2].extend([tree.number, leaf]))

    print(list1)
    return list1


def find_longest_unique_path(node, paths, pathLength=0, path=None):
    if node is None:
        return []

    if path is None:
        path = []

    if node.number not in path:
        if len(path) > pathLength:
            path[pathLength] = node.number
            del path[pathLength+1:]
        else:
            path.append(node.number)

        pathLength += 1

    if node.left is None and node.right is None:
        paths.append(path)
        return

    find_longest_unique_path(node.left, paths, pathLength, path)
    find_longest_unique_path(node.right, paths, pathLength, path)

    return path


class BinaryTreeTest(unittest.TestCase):
    def setUp(self):
        pass

    def test_node_1(self):
        tree = Node(4)
        tree.left = Node(5)
        tree.left.left = Node(4)
        tree.left.left.left = Node(5)
        tree.right = Node(6)
        tree.right.left = Node(1)
        tree.right.right = Node(6)

        paths = []
        self.assertEqual(find_longest_unique_path(tree, paths), [4, 6, 1])
        self.assertEqual(count_nodes_in_longest_unique_path(tree), 3)

    def test_node_2(self):
        tree = Node(4)
        tree.left = Node(4)
        tree.right = Node(6)

        self.assertEqual(find_longest_unique_path(tree, []), [4, 6])
        self.assertEqual(count_nodes_in_longest_unique_path(tree), 2)

    def test_node_3(self):
        tree = Node(4)
        tree.left = Node(4)
        tree.left.left = Node(9)
        tree.right = Node(6)

        self.assertEqual(find_longest_unique_path(tree, []), [4, 6])
        self.assertEqual(count_nodes_in_longest_unique_path(tree), 2)

    def test_node_4(self):
        tree = Node(2)
        tree.left = Node(5)
        tree.left.left = Node(1)
        tree.left.left.left = Node(8)
        tree.right = Node(7)

        print(find_all_paths(tree))
        self.assertEqual(find_longest_unique_path(tree, []), [2, 5, 1, 8])
        self.assertEqual(count_nodes_in_longest_unique_path(tree), 4)

    def test_node_5(self):
        tree = Node(2)
        tree.left = Node(6)
        tree.right = Node(1)
        tree.right.left = Node(3)
        tree.right.right = Node(6)

        self.assertEqual(find_longest_unique_path(tree, []), [2, 1, 6])
        self.assertEqual(count_nodes_in_longest_unique_path(tree), 3)

    def test_node_6(self):
        tree = Node(2)
        tree.left = Node(6)
        tree.right = Node(1)
        tree.right.left = Node(3)
        tree.right.left.left = Node(8)
        tree.right.right = Node(6)

        print(find_all_paths(tree))
        self.assertEqual(find_longest_unique_path(tree, []), [2, 1, 3, 8])
        self.assertEqual(count_nodes_in_longest_unique_path(tree), 4)

    def test_node_7(self):
        tree = Node(2)
        tree.left = Node(6)
        tree.right = Node(1)
        tree.right.left = Node(3)
        tree.right.right = Node(6)
        tree.right.right.left = Node(7)

        self.assertEqual(find_longest_unique_path(tree, []), [2, 1, 6, 7])
        self.assertEqual(count_nodes_in_longest_unique_path(tree), 4)

    def test_node_8(self):
        tree = Node(4)
        tree.left = Node(6)
        tree.right = Node(4)

        self.assertEqual(find_longest_unique_path(tree, []), [4, 6])
        self.assertEqual(count_nodes_in_longest_unique_path(tree), 2)

if __name__ == '__main__':
    unittest.main()

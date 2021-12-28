# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from AVLBinarySearchTree import AVLBinarySearchTree
from AVLTreeNode import AVLTreeNode

def main():
    my_tree = AVLBinarySearchTree()
    my_tree["a"] = "a"
    my_tree["q"] = "quick"
    my_tree["b"] = "brown"
    my_tree["f"] = "fox"
    my_tree["j"] = "jumps"
    my_tree["o"] = "over"
    my_tree["t"] = "the"
    my_tree["l"] = "lazy"
    my_tree["d"] = "dog"

    print(my_tree["q"])
    print(my_tree["l"])
    print("There are {} items in this tree".format(len(my_tree)))
    my_tree.delete("a")
    print("There are {} items in this tree".format(len(my_tree)))

    for node in my_tree:
        print(my_tree[node], end=" ")
    print()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()





# See PyCharm help at https://www.jetbrains.com/help/pycharm/

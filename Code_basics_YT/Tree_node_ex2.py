class TreeNode:
    def __init__(self, name) -> None:
        self.parent = None
        self.children = []
        self.data = name

    def add_child(self, child):
        child.parent = self
        self.children.append(child)

    def get_level(self):
        parent_count = 0

        p = self.parent
        while p:
            parent_count += 1
            p = p.parent
        return parent_count

    def print_tree(self, level):
        if self.get_level() >= level:
            return
        spaces = " " * self.get_level() * 10
        prefix = spaces + "\__" if self.parent else ""
        print(prefix + self.data)

        if self.children:
            for child in self.children:
                child.print_tree(level)


def country_tree():
    # India
    india = TreeNode("India")

    gujarut = TreeNode("Gujarut")
    karnataka = TreeNode("Karnataka")
    india.add_child(gujarut)
    india.add_child(karnataka)
    # Gujarut
    gujarut.add_child(TreeNode("Ahmedabad"))
    gujarut.add_child(TreeNode("Baroda"))

    # Karnataka
    karnataka.add_child(TreeNode("Bangluru"))
    karnataka.add_child(TreeNode("Mysore"))

    # India
    usa = TreeNode("USA")

    nj = TreeNode("New Jersey")
    cali = TreeNode("Cali")
    usa.add_child(nj)
    usa.add_child(cali)
    # New jersey
    nj.add_child(TreeNode("Princeton"))
    nj.add_child(TreeNode("Trenton"))

    # California
    cali.add_child(TreeNode("San Fran"))
    cali.add_child(TreeNode("Mountain View"))
    cali.add_child(TreeNode("Palo Alto"))

    # California
    globalworld = TreeNode("Global")
    globalworld.add_child(usa)
    globalworld.add_child(india)

    return globalworld


if __name__ == "__main__":
    # root = TreeNode("Electronics")
    # root.print_tree()

    # TV = TreeNode("Television")
    # TV.add_child(TreeNode("Sony"))
    # TV.add_child(TreeNode("LG"))
    # TV.add_child(TreeNode("TCL"))

    # Mobile = TreeNode("Mobile")
    # Mobile.add_child(TreeNode("Samsung Galaxy"))
    # Mobile.add_child(TreeNode("Iphone"))
    # Mobile.add_child(TreeNode("Pixel"))

    # root.add_child(TV)
    # root.add_child(Mobile)

    # root.print_tree()

    root_node = country_tree()
    root_node.print_tree(3)
    root_node.print_tree(1)

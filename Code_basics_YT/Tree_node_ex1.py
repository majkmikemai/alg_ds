class TreeNode:
    def __init__(self, name, designation) -> None:
        self.parent = None
        self.children = []
        self.data = name
        self.role = designation

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

    def print_tree(self, designation1):
        spaces = " " * self.get_level() * 10
        prefix = spaces + "\__" if self.parent else ""

        if designation1 == "name":
            print(prefix + self.data)
        elif designation1 == "designation":
            print(prefix + self.role)
        elif designation1 == "both":
            print(prefix + self.data + " (" + self.role + ")")

        if self.children:
            for child in self.children:
                child.print_tree(designation1)


def build_management_tree():
    # CTO Hierarchy
    infra_head = TreeNode("Vishwa", "Infrastructure Head")
    infra_head.add_child(TreeNode("Dhaval", "Cloud Manager"))
    infra_head.add_child(TreeNode("Abhijit", "App Manager"))

    cto = TreeNode("Chinmay", "CTO")
    cto.add_child(infra_head)
    cto.add_child(TreeNode("Aamir", "Application Head"))

    # HR hierarchy
    hr_head = TreeNode("Gels", "HR Head")

    hr_head.add_child(TreeNode("Peter", "Recruitment Manager"))
    hr_head.add_child(TreeNode("Waqas", "Policy Manager"))

    ceo = TreeNode("Nilupul", "CEO")
    ceo.add_child(cto)
    ceo.add_child(hr_head)

    return ceo


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

    root_node = build_management_tree()
    root_node.print_tree("name")  # prints only name hierarchy
    root_node.print_tree("designation")  # prints only designation hierarchy
    root_node.print_tree("both")  # prints both (name and designation) hierarchy

"""6.009 Lab 7 -- Faster Gift Delivery."""


from graph import Graph

# NO ADDITIONAL IMPORTS ALLOWED!


class FastGraph(Graph):
    """Faster implementation of `Graph`.

    Has extra optimizations for star and clique patterns.
    """

    def __init__(self):
        pass

    def query(self, pattern):
        raise NotImplementedError("not implemented")

    def add_node(self, name, label=''):
        raise NotImplementedError("not implemented")

    def remove_node(self, name):
        raise NotImplementedError("not implemented")

    def add_edge(self, start, end):
        raise NotImplementedError("not implemented")

    def remove_edge(self, start, end):
        raise NotImplementedError("not implemented")


if __name__ == '__main__':
    pass

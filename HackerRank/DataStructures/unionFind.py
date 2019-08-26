class UnionFind:
    def __init__(self):
        self.components = {}
        self.sizes = {}

    def _find(self, u):
        while self.components[u]:
            u = self.components[u]
        return u

    def find(self, u):
        if u not in self.components:
            self.components[u] = None
            self.sizes[u] = 1

        if not self.components[u]:
            return u

        v = self._find(u)
        self.components[u] = v
        return v

    def getSizeComponent(self, u):
        return self.sizes[self.find(u)]

    def union(self, u, v):
        pointerU = self.find(u)
        pointerV = self.find(v)
        componentUSize = self.sizes[pointerU]
        componentVSize = self.sizes[pointerV]
        if componentUSize > componentVSize:
            self.components[pointerV] = pointerU
            newComponentPointer = pointerU
        else:
            self.components[pointerU] = pointerV
            newComponentPointer = pointerV

        self.sizes[newComponentPointer] = componentUSize + componentVSize
        return self.sizes[newComponentPointer]

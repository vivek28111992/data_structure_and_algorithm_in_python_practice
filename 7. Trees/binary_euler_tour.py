# Binary Euler Tour
# A Binary Euler Tour base class providing a specialized tour for binary tree.

from eulerTour import EulerTour

class BinaryEulerTour(EulerTour):
    """Abstract base class for performing Euler tour of a binary tree.

    This version includes an additional _hook_invisit that is called after the tour of the left subtree (if any), yet before the tour of the right subtree (if any).

    Note: Right child is always assigned index 1 in path, even if no left subling.
    """

    def _tour(self, p, d, path):
        results = [None, None]                   # will update with results od recursions
        self._hook._previsit(p, d, path)        # "pre visit" for p
        if self._tree.left(p) is not None:      # consider left child
            path.append(0)
            results[0] = self._tour(self._tree.left(p), d+1, path)
            path.pop()
        self._hook_invisit(p, d, path)          # "in visit" for p
        if self._tree.right(p) is not None:     # consider right child
            path.append(1)
            results[1] = self._tour(self._tree.right(p), d+1, path)
            path.pop()
        answer = self._hook_postvisit(p, d, path, results)
        return answer

    def _hook_invisit(self, p, d, path): pass

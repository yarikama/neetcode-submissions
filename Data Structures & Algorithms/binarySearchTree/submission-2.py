from typing import Optional

class TreeNode:
    def __init__(
        self, 
        key: int,
        val: int,
        left: Optional['TreeNode'] = None,
        right: Optional['TreeNode'] = None,
    ) -> 'TreeNode':
        self.key = key
        self.val = val
        self.left = left
        self.right = right

    def __str__(self) -> str:
        return f"Key: {self.key}, Value: {self.val}"

class TreeMap:
    def __init__(
        self,
        root: Optional[TreeNode] = None,
    ) -> "TreeMap":
        self.root = root

    def _is_empty(self) -> bool:
        if self.root is None:
            return True
        return False

    def _insert(
        self,
        current: Optional[TreeNode],
        node_to_insert: TreeNode,
    ) -> TreeNode:
        if current is None:
            return node_to_insert

        if current.key > node_to_insert.key:
            current.left = self._insert(
                current=current.left,
                node_to_insert=node_to_insert
            )

        if current.key < node_to_insert.key:
            current.right = self._insert(
                current=current.right,
                node_to_insert=node_to_insert
            )

        return current


    def insert(
        self, 
        key: int, 
        val: int
    ) -> None:
        node_to_insert = TreeNode(
            key=key,
            val=val,
        )

        if self._is_empty():
            self.root = node_to_insert
            return

        self._insert(
            current=self.root,
            node_to_insert=node_to_insert,
        )

    def get(self, key: int) -> int:
        current = self.root

        while current is not None:
            if current.key == key:
                return current.val
            elif current.key > key:
                current = current.left
            elif current.key < key:
                current = current.right

        if current is None:
            return -1

    def getMin(
        self, 
        root: Optional[TreeNode] = None,
        return_node: bool = False,
    ) -> int:
        if self._is_empty():
            return -1

        current = root or self.root
        while current and current.left:
            current = current.left

        if return_node:
            return current

        return current.val

    def getMax(
        self, 
        root: Optional[TreeNode] = None,
        return_node: bool = False,
    ) -> int:
        if self._is_empty():
            return -1

        current = root or self.root
        while current and current.right:
            current = current.right

        if return_node:
            return current

        return current.val


    def _remove(
        self,
        root: Optional[TreeNode],
        key: int,
    ) -> Optional[TreeNode]:
        if root is None:
            return

        if key > root.key:
            root.right = self._remove(
                root=root.right,
                key=key,
            )        
        elif key < root.key:
            root.left = self._remove(
                root=root.left,
                key=key,
            )

        else:
            if root.left is None:
                if self.root == root:
                    self.root = root.right
                return root.right

            elif root.right is None:
                if self.root == root:
                    self.root = root.left
                return root.left

            else:
                min_node: TreeNode = self.getMin(
                    root=root.right,
                    return_node=True,
                )
                root.val = min_node.val
                root.key = min_node.key
                root.right = self._remove(
                    root=root.right,
                    key=key
                )


    def remove(self, key: int) -> None:
        self._remove(
            root=self.root,
            key=key,
        )


    def getInorderKeys(self) -> List[int]:
        keys = []

        def dfs(cur_node: Optional[TreeNode]) -> None:
            if cur_node is None:
                return

            dfs(cur_node.left)
            keys.append(cur_node.key)
            dfs(cur_node.right)

        dfs(self.root)

        return keys















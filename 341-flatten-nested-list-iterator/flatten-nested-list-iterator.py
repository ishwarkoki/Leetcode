# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger:
#    def isInteger(self) -> bool:
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        """
#
#    def getInteger(self) -> int:
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        """
#
#    def getList(self) -> [NestedInteger]:
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        """

class NestedIterator:
  def __init__(self, nestedList: List[NestedInteger]):
    self.stack: List[NestedInteger] = []
    self.addInteger(nestedList)

  def next(self) -> int:
    return self.stack.pop().getInteger()

  def hasNext(self) -> bool:
    while self.stack and not self.stack[-1].isInteger():
      self.addInteger(self.stack.pop().getList())
    return self.stack

  # addInteger([1, [4, [6]]]) . stack = [[4, [6]], 1]
  # addInteger([4, [6]]) . stack = [[6], 4]
  # addInteger([6]) . stack = [6]
  def addInteger(self, nestedList: List[NestedInteger]) -> None:
    for n in reversed(nestedList):
      self.stack.append(n)

         

# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())
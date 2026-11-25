class UndoExecutive:

    def __init__(self):
        self._sofar = []

    def perform(self,cmd,*args):
        _sofar.push((cmd,args))
        getattr(self,"do_%s" % cmd)(*args)
  
    def undo(self):
        while self._sofar:
            cmd,args = self._sofar.pop()
            getattr(self,"undo_%s" % cmd)(*args)


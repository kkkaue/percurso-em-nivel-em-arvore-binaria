

# inserir na fila
# remover da fila
# observar o topo da fila
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class Fila:
    def __init__(self):
        self.first = None
        self.last = None
        self._size = 0
        
    def push(self,elem):
        # insere um elemento na fila
        node = Node(elem)
        if self.last is None:
            self.last = node
        else:
            self.last.next = node
            self.last = node
        if self.first is None:
            self.first = node

        self._size = self._size + 1

    def pop(self):
        # remove o elemento do topo da fila
        if self._size > 0:
            elem = self.first.data
            self.first = self.first.next
            self._size = self._size - 1
            return elem 
        else:
            raise IndexError("The Queue is empty")
        
    def peek(self):
        # retorna o topo sem remover
        if self._size > 0:
            elem = self.first.data
            return elem 
        else:
            raise IndexError("The Queue is empty")

    def __len__(self):
        """Retorna o tamanho da fila"""
        return self._size
        
    def __repr__(self):
        if self._size > 0:
            r = ""
            pointer = self.first
            while(pointer):
                r = r + str(pointer.data) + " "
                pointer = pointer.next
            return r
        else:
            return "Empty Queue"
    def __str__(self):
        return self.__repr__()

if __name__ == '__main__':
    fila = Fila()
    print(len(fila))
    fila.push(1)
    fila.push(2)
    fila.push("python")
    fila.push(True)
    fila.push(1.2)

    print(fila)
    print(len(fila))
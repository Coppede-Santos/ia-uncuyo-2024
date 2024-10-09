

class Board:
    def __init__(self, long):
        self.long = long
        self.dominio = [list(range(long)) for _ in range(long)]
        self.solution = [None for _ in range(long)]

    def check(self,row,column):
        for i in range(row):
            if self.solution[i] == column or abs(column - self.solution[i]) == abs(row - i): return False

        return True

    def finished(self):
        return all(elemento is not None for elemento in self.solution)

    def choose_index(self):
        low_index = None
        low_amount = float("inf")

        for index, element in enumerate(self.dominio):
            if isinstance(element, list) and len(element) < low_amount:
                low_amount = len(element)
                low_index = index

        return low_index

    def print_solution(self):
        for i in range(self.long):
            linea = ['.'] * self.long
            if self.solution[i] is not None:
                linea[self.solution[i]] = 'Q'  # Usar 'Q' para representar la posición de la reina

                # Unir la fila como un string y mostrarla
            print(' '.join(linea))


def foward_checking(board, row, value):

    aux = 1
    for i in range(row+1, board.long):
        if value in board.dominio[i]:
            board.dominio[i].remove(value)

        back_diagonal = value - aux
        foward_diagonal = value + aux

        if back_diagonal > 0:
            if back_diagonal in board.dominio[i]:
                board.dominio[i].remove(back_diagonal)
        if foward_diagonal > board.long:
            if foward_diagonal in board.dominio[i]:
                board.dominio[i].remove(foward_diagonal)
        aux +=1
    return board


def ac_3 (board):
    if board.finished():
        return True

    index = board.choose_index()

    for i in board.dominio[index]:

        if board.check(index,i):

            possible_values = [set(subset) for subset in board.dominio]


            foward_checking(board,index, i)

            board.solution[index] = i

            condition = ac_3(board)

            if condition: return True

            board.dominio=possible_values

    return False



board = Board(8)
ac_3(board)
board.print_solution()

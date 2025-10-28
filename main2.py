def get_player_input(board, current_player):
    """Получает и проверяет ввод игрока"""
    while True:
        try:
            position = int(input(f"Игрок {current_player}, выбери позицию (1-9): "))
            if 1 <= position <= 9:
                if board[position-1] == " ":
                    return position - 1
                else:
                    print("Эта клетка уже занята! Выбери другую.")
            else:
                print("Введи число от 1 до 9!")
        except ValueError:
            print("Нужно ввести число!")
def display_board(board):
    """Отображает игровое поле"""
    print(f"\n {board[0]} | {board[1]} | {board[2]} ")
    print("-----------")
    print(f" {board[3]} | {board[4]} | {board[5]} ")
    print("-----------")
    print(f" {board[6]} | {board[7]} | {board[8]} \n")
def display_rules():
    """Показывает правила игры"""
    print("\n=== ПРАВИЛА ИГРЫ ===")
    print("Игровое поле пронумеровано так:")
    print(" 1 | 2 | 3 ")
    print("-----------")
    print(" 4 | 5 | 6 ")
    print("-----------")
    print(" 7 | 8 | 9 ")
    print("\nИгроки по очереди ставят X и O на свободные клетки")
    print("Первый, собравший 3 в ряд (по горизонтали, вертикали или диагонали) - побеждает!\n")
def main():
    """Основная функция игры"""
    print("🎮 Добро пожаловать в крестики-нолики! 🎮")
    display_rules()
    while True:
        # Инициализация игры
        board = [" "] * 9
        current_player = "X"
        game_over = False
        
        while not game_over:
            display_board(board)
            
            # Ход игрока
            position = get_player_input(board, current_player)
            board[position] = current_player


if __name__ == "__main__":
    main()
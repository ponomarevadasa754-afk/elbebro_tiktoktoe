def check_winner(board):
    """Проверяет есть ли победитель"""
    # Выигрышные комбинации
    winning_combinations = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # горизонтали
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # вертикали
        [0, 4, 8], [2, 4, 6]              # диагонали
    ]
    
    for combo in winning_combinations:
        if board[combo[0]] == board[combo[1]] == board[combo[2]] != " ":
            return board[combo[0]]
    return None

def check_draw(board):
    """Проверяет ничью"""
    return " " not in board
def restart_game():
    """Спрашивает хочет ли игрок сыграть ещё"""
    while True:
        choice = input("Хочешь сыграть ещё раз? (y/n): ").lower()
        if choice in ['y', 'н']:  # н - для русской раскладки
            return True
        elif choice in ['n', 'т']:  # т - для русской раскладки
            return False
        else:
            print("Введи 'y' (да) или 'n' (нет)")
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
            winner = check_winner(board)
            if winner:
                display_board(board)
                print(f"🎉 Поздравляю! Игрок {winner} победил! 🎉")
                game_over = True
            # Проверка ничьи
            elif check_draw(board):
                display_board(board)
                print("🤝 Ничья! Победила дружба! 🤝")
                game_over = True
            else:
                # Смена игрока
                current_player = "O" if current_player == "X" else "X"
        
        # Предложение сыграть ещё
        if not restart_game():
            print("Спасибо за игру! До встречи! 👋")
            break
        else:
            print("\n" + "="*40)
            print("НАЧИНАЕМ НОВУЮ ИГРУ!")
            print("="*40)



if __name__ == "__main__":
    main()
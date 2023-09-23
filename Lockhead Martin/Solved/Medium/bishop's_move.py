def bishop_move(a, b, c, d):


    """If the starting and ending squares are on the same diagonal, it is possible for the bishop to reach the ending square in multiple moves. This is because the bishop can move diagonally in any direction, and each move will change the row and column values of the bishop's position by the same amount. So, if the difference in the row and column values between the starting and ending squares are equal, the bishop can reach the ending square by making a series of diagonal moves.

On the other hand, if the starting and ending squares are not on the same diagonal, it is not possible for the bishop to reach the ending square by making diagonal moves only. Therefore, in this case, the function returns "NO"."""


    
    return "YES" if abs(a - c) % 2 == abs(b - d) % 2 else "NO"  # Bishop can reach ending square in multiple moves if both row and column differences are even or odd
for t in range(int(input())):
    board_r, board_c = (input()).split(",")
    start_r, start_c = (input()).split(",")
    end_r, end_c = input().split(",")
    if int(start_r) > int(board_r) or int(start_c) > int(board_c) or int(end_r) > int(board_r)  or int(end_c) > int(board_c):
        print("No")
    elif (bishop_move(int(start_r), int(start_c), int(end_r), int(end_c))) == "YES":
        print("Yes")
    else:
        print("No")
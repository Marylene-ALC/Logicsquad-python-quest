#!/usr/bin/python3
gold_piece=27
friend_num=4

pieces_for_each = gold_piece // friend_num
num_left= gold_piece % friend_num

print(f"The number shared is : {pieces_for_each} and the left are {num_left}")

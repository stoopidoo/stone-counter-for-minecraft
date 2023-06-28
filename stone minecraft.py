# ce truc m'as pris 40 minutes m'ai benef
import math
stone = int(input("Stone ="))
stone_slab = int(input("Stone slab ="))
stone_bricks = int(input("Stone bricks ="))
chiseled_stone_bricks = int(input("Chiseled Stone Bricks ="))
stone_brick_slab = int(input("Stone bricks slab ="))
stone_brick_stairs = int(input("Stone brick stairs ="))

total_stone_slab = math.ceil((stone_slab/6))*3
total_chiseled_stone_bricks = chiseled_stone_bricks*2
total_stone_brick_stairs = math.ceil(stone_brick_stairs/4)*6
total_stone_brick_slab = math.ceil((stone_brick_slab+total_chiseled_stone_bricks)/6)*3
total_stone_bricks = math.ceil(((stone_bricks+total_stone_brick_slab+total_stone_brick_stairs)/4))*4
total = total_stone_slab + total_stone_bricks + stone

print (total)
print (math.ceil(total/64))
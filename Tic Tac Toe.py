# TicTacToe in Minecraft Pi
# Mission Custom
# Create a working game in Minecraft Pi
# Developed by Braedon Mitchell

#Connect to Minecraft
from mcpi.minecraft import Minecraft
mc = Minecraft.create()
import random
import time

pos = mc.player.getPos()
White = 155
Black = 49
x = pos.x
y = pos.y
z = pos.z

# Define Create the Board
def create_board():
    mc.setBlocks(x+2,y-1,z+2,x-2,y-1,z-2,White)
    mc.setBlocks(x+1,y-1,z+2,x+1,y-1,z-2,Black)
    mc.setBlocks(x-1,y-1,z+2,x-1,y-1,z-2,Black)
    mc.setBlocks(x-2,y-1,z-1,x+2,y-1,z-1,Black)
    mc.setBlocks(x-2,y-1,z+1,x+2,y-1,z+1,Black)
    mc.postToChat("It is your turn, right-click the square you want")


         
# Check for win
def check_win():
    if slot1 == 103 and slot2 == 103 and slot3 == 103 or \
        slot4 == 103 and slot5 == 103 and slot6 == 103 or \
        slot7 == 103 and slot8 == 103 and slot9 == 103 or \
        slot1 == 103 and slot4 == 103 and slot7 == 103 or \
        slot2 == 103 and slot4 == 103 and slot8 == 103 or \
        slot3 == 103 and slot6 == 103 and slot9 == 103 or \
        slot1 == 103 and slot5 == 103 and slot9 == 103 or \
        slot3 == 103 and slot5 == 103 and slot7 == 103:
         mc.postToChat("YOU WIN!!")
         time.sleep(1)
         create_board()
         
# Create the first Board       
create_board()

#Player Input
while True:
    blocks_hit = mc.events.pollBlockHits()
    for block in blocks_hit:
        position = block.pos
        mc.setBlock(position,103)
        # Read gameboard
        slot1 = mc.getBlock(x+2,y-1,z+2)
        slot2 = mc.getBlock(x,y-1,z+2)
        slot3 = mc.getBlock(x-2,y-1,z+2)
        slot4 = mc.getBlock(x+2,y-1,z)
        slot5 = mc.getBlock(x,y-1,z)
        slot6 = mc.getBlock(x-2,y-1,z)
        slot7 = mc.getBlock(x+2,y-1,z-2)
        slot8 = mc.getBlock(x,y-1,z-2)
        slot9 = mc.getBlock(x-2,y-1,z-2)
        check_win()
        
        

            
            
       
        
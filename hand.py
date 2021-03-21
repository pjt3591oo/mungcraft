from ursina import *
from voxel import set_block_id, block_id

is_init = False

player_hand = None

def set_player_hand(n: int):
  player_hand.texture = set_block_id(n)

if not is_init: 
  is_init = True
  ORIGIN_POS = Vec2(0.6, -0.6)
  BLOCK_MAKE_POS = Vec2(0.4, -0.5)

  player_hand = player_hand or Entity(
    parent=camera.ui,
    model='cube',
    texture=set_block_id(block_id),
    scale=0.5,
    position=ORIGIN_POS,
    rotation=Vec3(-10.0, -10.0, -10.0)
  )

from ursina import *
from time import time
blocks = [
  'brick',
  'white_cube'
]

block_id = 0

def set_block_id(n: int):
  global block_id
  block_id = n
  return blocks[block_id]

class Voxel(Button):
  def __init__(self, position=(0,0,0), texture='brick'):
    super().__init__(
      parent=scene,
      position=position,
      model='cube',
      origin_y=0.5,
      texture=texture,
      color=color.color(0,0, random.uniform(0.9, 1.0)),
      scale=1.0
    )

  # 키보드 & 마우스 이벤트
  def input(self, key):
    if self.hovered:
      if key == 'left mouse down':
        Voxel(position=self.position + mouse.normal, texture=blocks[block_id])
      elif key == 'right mouse down':
        destroy(self)

  # tick당 호출
  # def update(self):
  #   print('Voxel update')
from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController
from voxel import Voxel

app = Ursina()

window.fps_counter.enable = False
window.exit_button.visible = False

if __name__ == "__main__":
  from sky import *
  from hand import *

  # tick당 호출
  def update():
    pass

  # 키보드 & 마우스 이벤트
  def input(key):
    if key.isdigit():
      block_id = int(key)
      
      block_id == 1 or block_id == 0 and set_player_hand(block_id)

    if held_keys['left mouse'] or held_keys['right mouse']:
      player_hand.position = BLOCK_MAKE_POS

    else:
      player_hand.position = ORIGIN_POS

  for z in range(20):
    for x in range(20):
      voxel = Voxel(position=(x, 0, z))

  player = FirstPersonController()



  app.run()

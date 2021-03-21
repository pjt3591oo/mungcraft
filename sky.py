from ursina import *

sky = Entity(
  parent=scene,
  model='sphere',
  texture=load_texture('assets/sky.jpeg'),
  scale=500,
  double_sided=True
)

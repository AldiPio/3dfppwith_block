from ursina import *
from ursina.prefabs.first_person_controller \
  import FirstPersonController
from random import uniform


app = Ursina()

ground = Entity(model= 'plane',
                texture= 'grass',
                collider= 'mesh',
                scale= (100,1, 100))

player = FirstPersonController(
  collider='box'
)
player.cursor.visible = False

# myBox = Entity(model= 'cube',
#                color= color.black,
#                collider= 'box',
#                position= (15, 0.5, 5))
# myBall = Entity(model= 'sphere',
#                 color= color.red,
#                 collider= 'sphere',
#                 position= (5, 0.5, 10))

sky = Sky()
lvl = 1

# buat box
blocks = []
directions = []
window.fullscreen = True
for i in range(10):
  r = uniform(-1,1)
  block = Entity(
    position=(r, 1+i , 2+i*3),
    model='cube',
    texture='white_cube',
    color=color.azure,
    scale=(2, 0.5, 2),
    collider='box',
  )
# moving box    
  blocks.append(block)
  if r < 0:
    directions.append(1)
  else:
    directions.append(-1)
    
# goal = Entity(
#   color=color.gold,
#   model='cube',
#   texture='white_cube',
#   position=(0,10,36),
#   scale=(10,1,10),
#   collider='box'
# )
# pillar = Entity(
#   color=color.green,
#   model='cube',
#   position=(0,20,36),
#   scale=(1,50,1)
# )

# jump = Audio(
#   'Assets\jump.mp3',
#   loop = False,
#   autoplay = False
# )

# walk = Audio(
#   'Assets\walk.mp3',
#   loop = False,
#   autoplay = False
# )

def update():
  global lvl
  i = 0
  for block in blocks:
    block.x -= directions[i] * time.dt
    if abs(block.x) > 5:
      directions[i] *= -1
    if block.intersects().hit:
      player.x -= directions[i]*time.dt
    i = i + 1

  walking = held_keys['a'] or \
          held_keys['d'] or \
          held_keys['w'] or \
          held_keys['s']
  
#   if walking and player.grounded:
#     if not walk.playing:
#       walk.play()
#   else:
#     if walk.playing:
#       walk.stop()

def input(key):
  if key == 'q':
    quit()
#   if key == 'space':
#     if not jump.playing:
#       jump.play()
app.run()
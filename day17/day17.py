target_area_x = [i for i in range(60, 95)]
target_area_y = [i for i in range(-136, -171)]

initial_pos = (0, 0)
highest_y = 0

def simulate(x_vel, y_vel, target_x_min, target_x_max, target_y_min, target_y_max):
  x = 0
  y = 0
  max_y = 0
  while True:
    x += x_vel
    y += y_vel
    max_y = max(max_y, y)
    x_vel = max(x_vel-1, 0)
    y_vel -= 1
    if target_x_min <= x <= target_x_max and target_y_min <= y <= target_y_max:
      return True
    if y_vel < 0 and y < target_y_min:
      return False

target_x_min, target_x_max = 60, 94 
target_y_min, target_y_max =  -171, -136

works_count = 0
for x in range(100):
  for y in range(target_y_min, 250):
        if simulate(x,y, target_x_min, target_x_max, target_y_min, target_y_max ):
            works_count += 1
print(works_count)
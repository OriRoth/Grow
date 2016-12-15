from random import choice

initial_water = 100
initial_light = 100
initial_age = 0

light_drop = lambda *x: choice(range(10))
rain_drop = lambda *x: choice(range(10))
ground_waters_bottom = lambda *x: choice(range(20))
light_diffusion = lambda r: int(r / 2)
rain_diffusion = lambda r: int(r / 2)
ground_waters_diffusion = lambda r: int(r / 2)

leaf_price = 20, 20
branch_price = 10, 10
root_price = 20, 20
fruit_price = 100, 100

rounds = 50

no_near_vertical_branches = True

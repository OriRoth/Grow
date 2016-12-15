from random import choice

initial_water = 1000
initial_light = 1000
initial_age = 0

light_drop = lambda *x: choice(range(100))
rain_drop = lambda *x: choice(range(100))
ground_waters_bottom = lambda *x: choice(range(200))
light_diffusion = lambda r: int(r / 2)
rain_diffusion = lambda r: int(r / 2)
ground_waters_diffusion = lambda r: int(r / 2)

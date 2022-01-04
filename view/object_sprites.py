import random
from PIL import Image

from model.util import load_image
from parameters import CELL_SIZE
import view.level
import pygame


class BaseObjectSprite(pygame.sprite.Sprite):
    def __init__(self, image, image1, image2, image3, image4, image5, image6, image7, image8,
                 x, y, *group):
        super().__init__(group)
        self.image = image
        self.light_images = [image1, image2, image3, image4, image5, image6, image7, image8]
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.dung_x = self.rect.x // CELL_SIZE
        self.dung_y = self.rect.y // CELL_SIZE
        self.light = 0

    def set_light(self, light):
        self.light = light
        self.image = self.light_images[self.light]


class Wall1(BaseObjectSprite):
    image = load_image('64x64_wall_1.png')
    image_0 = load_image('64x64_wall_1.png')
    image_1 = load_image('64x64_1_wall_1.png')
    image_2 = load_image('64x64_2_wall_1.png')
    image_3 = load_image('64x64_3_wall_1.png')
    image_4 = load_image('64x64_4_wall_1.png')
    image_5 = load_image('64x64_5_wall_1.png')
    image_6 = load_image('64x64_6_wall_1.png')
    image_7 = load_image('64x64_7_wall_1.png')
    image_8 = load_image('64x64_8_wall_1.png')

    def __init__(self, x, y, *group):
        super().__init__(Wall1.image, Wall1.image_1, Wall1.image_2, Wall1.image_3,
                         Wall1.image_4, Wall1.image_5, Wall1.image_6, Wall1.image_7,
                         Wall1.image_8, x, y, *group)


class Wall2(BaseObjectSprite):
    image = load_image('64x64_wall_2.png')
    image_0 = load_image('64x64_wall_2.png')
    image_1 = load_image('64x64_1_wall_2.png')
    image_2 = load_image('64x64_2_wall_2.png')
    image_3 = load_image('64x64_3_wall_2.png')
    image_4 = load_image('64x64_4_wall_2.png')
    image_5 = load_image('64x64_5_wall_2.png')
    image_6 = load_image('64x64_6_wall_2.png')
    image_7 = load_image('64x64_7_wall_2.png')
    image_8 = load_image('64x64_8_wall_2.png')

    def __init__(self, x, y, *group):
        super().__init__(Wall2.image, Wall2.image_1, Wall2.image_2, Wall2.image_3,
                         Wall2.image_4, Wall2.image_5, Wall2.image_6, Wall2.image_7,
                         Wall2.image_8, x, y, *group)


class Wall3(BaseObjectSprite):
    image = load_image('64x64_wall_3.png')
    image_0 = load_image('64x64_wall_3.png')
    image_1 = load_image('64x64_1_wall_3.png')
    image_2 = load_image('64x64_2_wall_3.png')
    image_3 = load_image('64x64_3_wall_3.png')
    image_4 = load_image('64x64_4_wall_3.png')
    image_5 = load_image('64x64_5_wall_3.png')
    image_6 = load_image('64x64_6_wall_3.png')
    image_7 = load_image('64x64_7_wall_3.png')
    image_8 = load_image('64x64_8_wall_3.png')

    def __init__(self, x, y, *group):
        super().__init__(Wall3.image, Wall3.image_1, Wall3.image_2, Wall3.image_3,
                         Wall3.image_4, Wall3.image_5, Wall3.image_6, Wall3.image_7,
                         Wall3.image_8, x, y, *group)


# TODO поменять спрайты
class UnbreakableWall(BaseObjectSprite):
    image = load_image('64x64_wall_3.png')
    image_0 = load_image('64x64_wall_3.png')
    image_1 = load_image('64x64_1_wall_3.png')
    image_2 = load_image('64x64_2_wall_3.png')
    image_3 = load_image('64x64_3_wall_3.png')
    image_4 = load_image('64x64_4_wall_3.png')
    image_5 = load_image('64x64_5_wall_3.png')
    image_6 = load_image('64x64_6_wall_3.png')
    image_7 = load_image('64x64_7_wall_3.png')
    image_8 = load_image('64x64_8_wall_3.png')

    def __init__(self, x, y, *group):
        super().__init__(Wall3.image, Wall3.image_1, Wall3.image_2, Wall3.image_3,
                         Wall3.image_4, Wall3.image_5, Wall3.image_6, Wall3.image_7,
                         Wall3.image_8, x, y, *group)


class Floor1(BaseObjectSprite):
    image = load_image('64x64_floor_1.png')
    image_0 = load_image('64x64_floor_1.png')
    image_1 = load_image('64x64_1_floor_1.png')
    image_2 = load_image('64x64_2_floor_1.png')
    image_3 = load_image('64x64_3_floor_1.png')
    image_4 = load_image('64x64_4_floor_1.png')
    image_5 = load_image('64x64_5_floor_1.png')
    image_6 = load_image('64x64_6_floor_1.png')
    image_7 = load_image('64x64_7_floor_1.png')
    image_8 = load_image('64x64_8_floor_1.png')

    def __init__(self, x, y, *group):
        super().__init__(Floor1.image, Floor1.image_1, Floor1.image_2, Floor1.image_3,
                         Floor1.image_4, Floor1.image_5, Floor1.image_6, Floor1.image_7,
                         Floor1.image_8, x, y, *group)


class Floor2(BaseObjectSprite):
    image = load_image('64x64_floor_2.png')
    image_0 = load_image('64x64_floor_2.png')
    image_1 = load_image('64x64_1_floor_2.png')
    image_2 = load_image('64x64_2_floor_2.png')
    image_3 = load_image('64x64_3_floor_2.png')
    image_4 = load_image('64x64_4_floor_2.png')
    image_5 = load_image('64x64_5_floor_2.png')
    image_6 = load_image('64x64_6_floor_2.png')
    image_7 = load_image('64x64_7_floor_2.png')
    image_8 = load_image('64x64_8_floor_2.png')

    def __init__(self, x, y, *group):
        super().__init__(Floor2.image, Floor2.image_1, Floor2.image_2, Floor2.image_3,
                         Floor2.image_4, Floor2.image_5, Floor2.image_6, Floor2.image_7,
                         Floor2.image_8, x, y, *group)


class Floor3(BaseObjectSprite):
    image = load_image('64x64_floor_3.png')
    image_0 = load_image('64x64_floor_3.png')
    image_1 = load_image('64x64_1_floor_3.png')
    image_2 = load_image('64x64_2_floor_3.png')
    image_3 = load_image('64x64_3_floor_3.png')
    image_4 = load_image('64x64_4_floor_3.png')
    image_5 = load_image('64x64_5_floor_3.png')
    image_6 = load_image('64x64_6_floor_3.png')
    image_7 = load_image('64x64_7_floor_3.png')
    image_8 = load_image('64x64_8_floor_3.png')

    def __init__(self, x, y, *group):
        super().__init__(Floor3.image, Floor3.image_1, Floor3.image_2, Floor3.image_3,
                         Floor3.image_4, Floor3.image_5, Floor3.image_6, Floor3.image_7,
                         Floor3.image_8, x, y, *group)


class Chest(BaseObjectSprite):
    closed_chest_image = load_image('64x64_chest.png')
    opened_chest_image = load_image('64x64_opened_chest.png')

    def __init__(self, x, y, *group):
        super().__init__(Chest.closed_chest_image, x, y, *group)

    def update(self, event):
        level = view.level.LevelManager.get_current_level()
        if event is not None:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_o:
                if (self.dung_x, self.dung_y) == level.character.get_dung_coords() or \
                        (self.dung_x, self.dung_y) == level.character.get_d_dung_coords():
                    self.open_chest()

    def open_chest(self):
        self.image = Chest.opened_chest_image



# TODO
# Ловушка
class Trap(BaseObjectSprite):
    closed_chest_image = None

    def __init__(self, x, y, *group):
        super().__init__(Chest.opened_chest_image, x, y, *group)

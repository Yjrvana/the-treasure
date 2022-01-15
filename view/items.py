from model.util import load_image, seconds_to_milliseconds
from model.value_manager import ValueManager

size = 48

RANDOM_ITEMS_LIST = {
    'tea': 0.25,
    'hot_tea': 0.15,
    'dream_catcher': 0.03,
    'bag': 0.15,
    'old_clock': 0.02,
    'hearing_potion': 0.10,
    'speed_potion': 0.10,
    'music_box': 0.05,
    'snow_ball': 0.05,
    'invisibility_potion': 0.10,
}

images = {
    'tea': load_image('48x48_tea.png'),
    'hot_tea': load_image('48x48_hot_tea.png'),
    'oil': load_image('48x48_oil.png'),
    'bag': load_image('48x48_bag.png'),
    'old_clock': load_image('48x48_old_clock.png'),
    'hearing_potion': load_image('48x48_hearing_potion.png'),
    'speed_potion': load_image('48x48_speed_potion.png'),
    'music_box': load_image('48x48_music_box.png'),
    'snow_ball': load_image('48x48_snow_ball.png'),
    'invisibility_potion': load_image('48x48_invisibility_potion.png'),
}


class Item:
    @staticmethod
    def use(item_name):
        if item_name is None:
            return
        if item_name == 'tea':
            Item.tea()
        elif item_name == 'hearing_potion':
            Item.hearing_potion()
        elif item_name == 'speed_potion':
            Item.speed_potion()
        elif item_name == 'oil':
            Item.oil()

    @staticmethod
    def tea():
        ValueManager.update_speed(1, for_time=seconds_to_milliseconds(60))
        ValueManager.update_health(5)

    @staticmethod
    def hot_tea():
        ValueManager.update_speed(1, for_time=seconds_to_milliseconds(60))
        ValueManager.update_health(5)

    @staticmethod
    def hearing_potion():
        ValueManager.update_hearing(3, for_time=seconds_to_milliseconds(120))

    @staticmethod
    def speed_potion():
        ValueManager.update_speed(3, for_time=seconds_to_milliseconds(120))

    @staticmethod
    def oil():
        ValueManager.update_light(2)


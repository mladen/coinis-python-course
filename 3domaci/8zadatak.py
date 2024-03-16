class Player:
    def __init__(self, x, y, width, height, health):
        self._x = x
        self._y = y
        self._width = width
        self._height = height
        self._health = health

    def get_x(self):
        return self._x

    def set_x(self, x):
        self._x = x

    def get_y(self):
        return self._y

    def set_y(self, y):
        self._y = y

    def get_width(self):
        return self._width

    def set_width(self, width):
        self._width = width

    def get_height(self):
        return self._height

    def set_height(self, height):
        self._height = height

    def get_health(self):
        return self._health

    def set_health(self, health):
        if 0 <= health <= 100:
            self._health = health
        else:
            raise ValueError("Health mora biti izmedju 0 i 100.")


class Enemy:
    def __init__(self, x, y, width, height, damage):
        self._x = x
        self._y = y
        self._width = width
        self._height = height
        self._damage = damage

    def get_x(self):
        return self._x

    def set_x(self, x):
        self._x = x

    def get_y(self):
        return self._y

    def set_y(self, y):
        self._y = y

    def get_width(self):
        return self._width

    def set_width(self, width):
        self._width = width

    def get_height(self):
        return self._height

    def set_height(self, height):
        self._height = height

    def get_damage(self):
        return self._damage

    def set_damage(self, damage):
        if 0 <= damage <= 100:
            self._damage = damage
        else:
            raise ValueError("Damage mora biti izmedju 0 i 100.")


def check_collision(player, enemy):
    player_left = player.get_x()
    player_right = player_left + player.get_width()
    player_top = player.get_y()
    player_bottom = player_top + player.get_height()

    enemy_left = enemy.get_x()
    enemy_right = enemy_left + enemy.get_width()
    enemy_top = enemy.get_y()
    enemy_bottom = enemy_top + enemy.get_height()

    if (
        player_right < enemy_left
        or player_left > enemy_right
        or player_bottom < enemy_top
        or player_top > enemy_bottom
    ):
        return False
    else:
        return True

    # TODO: ChatGPT: Ovo je isto kao i kod iznad, samo je drugaciji nacin pisanja??? Da li je ovo tacno?
    # if (
    #     player_right >= enemy_left
    #     and player_left <= enemy_right
    #     and player_bottom >= enemy_top
    #     and player_top <= enemy_bottom
    # ):
    #     return True
    # return False


def decrease_health(player, enemy):
    if check_collision(player, enemy):
        player.set_health(player.get_health() - enemy.get_damage())


# Kreiranje objekata player i enemy
player = Player(0, 0, 50, 50, 100)
enemy1 = Enemy(45, 45, 30, 30, 20)
enemy2 = Enemy(200, 200, 30, 30, 30)

print("Player health before collision:", player.get_health())

# Provjera kolizije i smanjenje zdravlja ako je detektovana kolizija
decrease_health(player, enemy1)
decrease_health(player, enemy2)

print("Player health after collision:", player.get_health())

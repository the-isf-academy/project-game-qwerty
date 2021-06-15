# game.py
# Authors:
# Alastair, Lucian
# This file should run your game.
#
# You can (and should) create other files and modules to import them
# here as needed.

from quest.game import QuestGame
from quest.map import TiledMap
from quest.sprite import Background, Wall, NPC, QuestSprite, Player
from quest.helpers import scale, resolve_resource_path
from quest.strategy import RandomWalk
import arcade
import os
from pathlib import Path
import time


class Maze(QuestGame):
    """A very simple subclass of :py:class:`QuestGame`.

    To run this example::

        $ python -m quest.examples.island

    :py:class:`IslandAdventure` shows off the basic features of the Quest
    framework, loading a map and letting the player explore it.
    After you play it, check out the sorce code by clicking on "source" in the
    blue bar just above.
    """

    player_sprite_image = ("images/DungeonTiles/frames/knight_m_idle_anim_f1.png")
    screen_width = 300
    screen_height = 300
    left_viewport_margin = 150
    right_viewport_margin = 150
    bottom_viewport_margin = 150
    top_viewport_margin = 150
    player_initial_x = 340
    player_initial_y = 250
    player_speed = 3
    health = 100


    def reduce_health(self):
        self.health = self.health - 10
        if self.health <= 0:
            pass

    def setup_maps(self):
        """Sets up the map.

        Uses a :py:class:`TiledMap` to load the map from a ``.tmx`` file,
        created using :doc:`Tiled <tiled:manual/introduction>`.
        """
        super().setup_maps()
        sprite_classes = {
            "walls": Wall,
            "play": Background,
            "exit": Background,
        }
        island_map = TiledMap(("images/qwerty_game_1.tmx"), sprite_classes)
        self.add_map(island_map)


    def setup_walls(self):
        """Assigns sprites to `self.wall_list`. These sprites will function as walls, blocking
        the player from passing through them.
        """
        self.wall_list = self.get_current_map().get_layer_by_name("walls").sprite_list

    def instructions(self):
        print(" ")
        print("W,A,S,D to move, SPACE to attack")


    def setup_npcs(self):
        npc_data = []
        for i in range(1):
            npc_data.append([mob, "images/DungeonTiles/frames/big_demon_idle_anim_f3.png", 0.8, 430, 140])
        self.npc_list = arcade.SpriteList()
        for sprite_class, image, scale, x, y in npc_data:
            sprite = sprite_class(image, scale)
            sprite.center_x = x
            sprite.center_y = y
            self.npc_list.append(sprite)
        walk = RandomWalk(0.03)
        mob.strategy = walk

class mob(NPC):
    repel_distance = 30

    def on_collision(self, sprite, game):
        if isinstance(sprite, Player):
            self.repel(sprite)
            game.reduce_health()
            print(game.health)

    def repel(self, sprite):
        "Backs the sprite away from self"
        away = (self.center_x - sprite.center_x, self.center_y - sprite.center_y)
        away_x, away_y = scale(away, self.repel_distance)
        sprite.center_x = sprite.center_x - away_x
        sprite.center_y = sprite.center_y - away_y
        sprite.stop()

if __name__ == '__main__':
    game = Maze()
    game.instructions()
    game.run()

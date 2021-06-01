# game.py
# Authors:
# Alastair, Lucian
# This file should run your game.
#
# You can (and should) create other files and modules to import them
# here as needed.

from quest.game import QuestGame
from quest.map import TiledMap
from quest.sprite import Background, Wall
from quest.helpers import resolve_resource_path
import arcade
import os
from pathlib import Path

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
    screen_width = 500
    screen_height = 500
    left_viewport_margin = 96
    right_viewport_margin = 96
    bottom_viewport_margin = 96
    top_viewport_margin = 96
    player_initial_x = 300
    player_initial_y = 300
    player_speed = 6

    def setup_maps(self):
        """Sets up the map.

        Uses a :py:class:`TiledMap` to load the map from a ``.tmx`` file,
        created using :doc:`Tiled <tiled:manual/introduction>`.
        """
        super().setup_maps()
        sprite_classes = {
            "walls": Wall,
            "play": Background,
        }
        island_map = TiledMap(("images/qwerty_game_1.tmx"), sprite_classes)
        self.add_map(island_map)


    def setup_walls(self):
        """Assigns sprites to `self.wall_list`. These sprites will function as walls, blocking
        the player from passing through them.
        """
        self.wall_list = self.get_current_map().get_layer_by_name("walls").sprite_list


if __name__ == '__main__':
    game = Maze()
    game.run()

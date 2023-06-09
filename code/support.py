from csv import reader
from os import walk
import pygame.image


def import_csv_layout(path):
    terrain_map = []
    with open(path) as level_map:
        layout = reader(level_map, delimiter=',')
        for row in layout:
            terrain_map.append(list(row))
        return terrain_map

# Function returns png files tuple from directory
def import_folder(path):
    surface_list = []
    for _, __, img_files in walk(path):
        for img in img_files:
            fullpath = path + '/' + img
            img_surf = pygame.image.load(fullpath).convert_alpha()
            surface_list.append(img_surf)

    return surface_list

def import_folder(path):
    surface_list = []
    for _, __, img_files in walk(path):
        for img in img_files:
            fullpath = path + '/' + img
            img_surf = pygame.image.load(fullpath).convert_alpha()
            surface_list.append(img_surf)

    return surface_list

import pygame
import json

class Spritesheet:
    def __init__(self, filename):
        self.filename = filename
        self.sprite_sheet = pygame.image.load(filename).convert()#loads image

        self.size = self.sprite_sheet.get_rect().size; #handles all the scaling. actually redundant since all sprites are scaled at 1:1
        self.size = [self.size[0], self.size[1]]
        self.size[0] *= 1;
        self.size[1] *= 1
        self.size[0], self.size[1] = int(self.size[0]), int(self.size[1])
        self.sprite_sheet = pygame.transform.scale(self.sprite_sheet, self.size)

        self.meta_data = self.filename.replace("png", "json")#replaces the png to json
        with open(self.meta_data) as f: #loads the json
            self.data = json.load(f)


    def get_sprite(self, x, y, width, height):
        sprite = pygame.Surface((width,height))
        sprite.set_colorkey((0, 0, 0))
        sprite.blit(self.sprite_sheet,(0,0),(x,y,width,height))
        return sprite

    def parse_sprite(self,name,sprite):
        """loads in the specific image in the given frame
        """
        sprite = sprite[name]["frame"]
        x,y,width, height = sprite["x"], sprite["y"], sprite["w"],sprite["h"]
        image = self.get_sprite(x,y,width,height)
        return image

    def load_sprite_json(self):
        sprite = self.data["frames"]
        return sprite

    def create_sprite_array(self):
        """
        basically loads the spritejson, then parses each of the images in the spritesheet, then creates an array of them

        returns: the sprite array
        """
        sprite = self.load_sprite_json() #loads the json with all the sprites
        sprite_array,loop_count = [], 0 #creates an array
        for frames in sprite:
            loop_count+=1
            frame = self.parse_sprite(f"{loop_count}.png", sprite)
            sprite_array.append(frame)
        return sprite_array

    """make another function that loads the json index sprite called in parse_sprite()
    then use that to read the number of indexes in there and parse that many sprites"""
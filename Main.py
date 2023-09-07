#Main.py

from direct.showbase.ShowBase import ShowBase
from World import WorldGenerator, TILE_SIZE
from Camera import CameraSettings
from Character import Character
from panda3d.core import Point3
from direct.interval.LerpInterval import LerpPosInterval
class MyApp(ShowBase):
    def __init__(self):
        ShowBase.__init__(self)

        self.disableMouse()

        world = WorldGenerator(self.render)
        world.generate_world()
        self.world = WorldGenerator(self.render)

        self.character = Character(self.render, self.loader)
        char_position = self.character.get_position()
        self.setup_mouse_input()

        self.camera_settings = CameraSettings(self.camera)
        self.camera_settings.set_initial_position(char_position)
        self.camera_settings.setup_text()
        base.taskMgr.add(self.camera_settings.update_text, "updateTextTask")

    def basic_mouse_click(self):
        print("Basic mouse click detected!")

    def setup_mouse_input(self):
        self.accept("mouse1", self.handle_mouse_click)

    def handle_mouse_click(self):
        pos3d = Point3()
        if base.mouseWatcherNode.hasMouse():
            # Get the mouse position
            mpos = base.mouseWatcherNode.getMouse()
            print(f"Mouse Position in window: {mpos}")

            # Convert this into 3D world coordinates
            nearPoint = Point3()
            farPoint = Point3()
            base.camLens.extrude(mpos, nearPoint, farPoint)
            print(f"Near Point: {nearPoint}, Far Point: {farPoint}")
            base.camLens.extrude(mpos, nearPoint, farPoint)

            # Calculate the intersection with the XY plane (z=0)
            if farPoint.getZ() != nearPoint.getZ():
                t = -nearPoint.getZ() / (farPoint.getZ() - nearPoint.getZ())
                pos3d.setX(nearPoint.getX() + t * (farPoint.getX() - nearPoint.getX()))
                pos3d.setY(nearPoint.getY() + t * (farPoint.getY() - nearPoint.getY()))
                pos3d.setZ(0)

            # Determine the tile coordinates
            tile_x = int(pos3d.getX() // TILE_SIZE)
            tile_y = int(pos3d.getY() // TILE_SIZE)

            print(f"Calculated Tile: ({tile_x}, {tile_y})")

            # Convert tile coordinates back to world coordinates
            target_pos = Point3(tile_x * TILE_SIZE + TILE_SIZE / 2, tile_y * TILE_SIZE + TILE_SIZE / 2, 0)

            # Ensure the character only moves to valid tiles
            rows, columns = 30, 30  # These values should match your grid size
            if 0 <= tile_x < self.world.rows and 0 <= tile_y < self.world.columns:
                print(f"Clicked on tile: {tile_x}, {tile_y}")
                move_duration = 1.0  # Adjust this value for faster/slower movement
                character_node_path = self.character.get_node_path()
                move_interval = LerpPosInterval(character_node_path, move_duration, target_pos)
                move_interval.start()
            else:
                print(f"Clicked outside the grid.")

app = MyApp()
app.run()
#Camera.py
from direct.gui.OnscreenText import OnscreenText
class CameraSettings:
    def __init__(self, camera):
        self.camera = camera

    def setup_text(self):
        self.positionText = OnscreenText(text='', pos=(-0.95, 0.9), scale=0.05, fg=(1, 1, 1, 1))

    def update_text(self, task):
        pos = self.camera.getPos()
        hpr = self.camera.getHpr()
        self.positionText.setText(
            f"Pos: {pos[0]:.2f}, {pos[1]:.2f}, {pos[2]:.2f} | HPR: {hpr[0]:.2f}, {hpr[1]:.2f}, {hpr[2]:.2f}")
        return task.cont  # Continue the task indefinitely

    def set_initial_position(self, character_position):
        x, y, z = character_position
        self.camera.setPos(x, y - 150, z - 50)
        self.camera.lookAt(x, y, z)

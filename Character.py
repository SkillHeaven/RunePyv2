#Character.py

from panda3d.core import CollisionSphere, CollisionNode

class Character:
    def __init__(self, render, loader):
        self.render = render
        self.loader = loader
        self.head = None  # Declare an instance variable for the head
        self.generate_character()
        self.setup_collision()

    def setup_collision(self):
        cs = CollisionSphere(0, 0, 0, 1)  # Adjust this to fit your character size
        cnode = CollisionNode('character')
        cnode.addSolid(cs)
        cnodepath = self.head.attachNewNode(cnode)
        cnodepath.show()  # You can comment this out later. It just helps in visualizing the collision sphere.

    def generate_character(self):
        # Head
        self.head = self.loader.loadModel('smiley')  # Assign head model to the instance variable
        self.head.reparentTo(self.render)
        self.head.setScale(2)
        self.head.setPos(0, 0, 1)

    def move_to(self, point):
        self.head.setPos(point)

    def get_position(self):
        if self.head:
            return self.head.getPos()
        return None

    def get_node_path(self):
        return self.head
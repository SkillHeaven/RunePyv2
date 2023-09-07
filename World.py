#world.py

from panda3d.core import Geom, GeomVertexData, GeomVertexFormat, GeomVertexWriter
from panda3d.core import GeomTriangles, GeomNode, NodePath, CardMaker
TILE_SIZE=5


class WorldGenerator:
    def __init__(self, render, rows=30, columns=30):
        self.render = render
        self.rows = rows  # Set rows as an instance variable
        self.columns = columns  # Set columns as an instance variable
        self.tile_root = NodePath("TileRoot")
        self.tile_root.reparentTo(self.render)

        @property
        def rows(self):
            return self.rows

        @property
        def columns(self):
            return self.columns

    def generate_world(self):
        card = CardMaker("tile")
        color1 = (1, 0, 0, 1)  # Red
        color2 = (0, 1, 0, 1)  # Green

        for i in range(self.rows):  # Use self.rows here
            for j in range(self.columns):  # Use self.columns here
                card.setFrame(i * TILE_SIZE, (i + 1) * TILE_SIZE, j * TILE_SIZE, (j + 1) * TILE_SIZE)
                tile_node = self.tile_root.attachNewNode(card.generate())

                # Determine the tile color based on a checker pattern
                if (i + j) % 2 == 0:
                    tile_node.setColor(*color1)
                else:
                    tile_node.setColor(*color2)

    def add_tile(self, x, y, vertex, normal, color, texcoord):
        size = TILE_SIZE
        vertex.addData3(x * size, y * size, 0)
        vertex.addData3((x + 1) * size, y * size, 0)
        vertex.addData3((x + 1) * size, (y + 1) * size, 0)
        vertex.addData3(x * size, (y + 1) * size, 0)

        for _ in range(4):
            normal.addData3(0, 0, 1)  # Upwards
            color.addData4f(1, 1, 1, 1)
            texcoord.addData2f(x, y)

    def add_tile_indices(self, x, y, geom):
        index = (x + y * 10) * 4
        tri1 = GeomTriangles(Geom.UHDynamic)
        tri1.addVertices(index, index + 1, index + 2)
        tri1.closePrimitive()

        tri2 = GeomTriangles(Geom.UHDynamic)
        tri2.addVertices(index, index + 2, index + 3)
        tri2.closePrimitive()

        geom.addPrimitive(tri1)
        geom.addPrimitive(tri2)
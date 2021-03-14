from org.bukkit import Location

from circle import createCircle, createCandleLayer


def renderTuples (welt, material, tuples):
    for tuple in tuples:
            l = Location (welt, tuple[0], tuple[1], tuple[2])
            block = welt.getBlockAt(l)
            block.setType(material)

class HappyBirthdayPlugin(PythonPlugin):
    def onEnable(self):
        self.getLogger().info("Instantiates HappyBirthday plugin")

    def onCommand(self, sender, command, label, args):
        welt = sender.getWorld()
        position = sender.getLocation()
        self.getLogger().info("Happy Birthday")
        position = Location(welt, position.getX() + 12, position.getY(), position.getZ())
        # self.getLogger().info("!!!!!!!!!!!! Failed to convert param:" + args[0])
        # self.getLogger().info("!!!!!!!!!!!! Ignored to build Tower")

        material = bukkit.Material.COBBLESTONE
        self.getLogger().info("material")
        
        blocks = [(position.getX()+2, position.getY()+2, position.getZ()+2)]
        self.getLogger().info("blocks")

        renderTuples(
            welt, 
            bukkit.Material.COBBLESTONE,
            createCircle(position, 10)
        )
        for i in [1,2,3,4,5,6]:
            center = Location(welt, position.getX(), position.getY() + i, position.getZ())
            self.getLogger().info("height" + str(center.getY()))
            renderTuples(
                welt, 
                bukkit.Material.LIGHT_BLUE_WOOL,
                createCircle(center, 9)
            )

        for i in [1,3,5]:
            center = Location(welt, position.getX(), position.getY() + i, position.getZ())
            self.getLogger().info("height" + str(center.getY()))
            renderTuples(
                welt, 
                bukkit.Material.SAND,
                createCircle(center, 8)
            )

        for i in [7,8,9]:
            candlesCenter = Location(welt, position.getX(), position.getY() + i, position.getZ())
            renderTuples(
                welt,
                bukkit.Material.WHITE_WOOL,
                createCandleLayer(candlesCenter)
            )

        fireCenter = Location(welt, position.getX(), position.getY() + 10, position.getZ())
        renderTuples(
            welt,
            bukkit.Material.CAMPFIRE,
            createCandleLayer(fireCenter)
        )

        return True
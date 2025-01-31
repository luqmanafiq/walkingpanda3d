from math import pi, sin, cos

from direct.showbase.ShowBase import ShowBase
from direct.task import Task
from direct.actor.Actor import Actor
from direct.interval.IntervalGlobal import Sequence
from panda3d.core import Point3


class WalkingPanda(ShowBase):
    def __init__(self, no_rotate=False, scale=1, playsound=False, moonwalk=False, spin=False):
        ShowBase.__init__(self)

        #playsound
        playsound = self.loader.loadSfx("walking_panda/sound/Defending-the-Princess-Haunted_v002.mp3")
        playsound.play()

        if playsound:
            self.loader.loadSfx("walking_panda/sound/Defending-the-Princess-Haunted_v002.mp3")

        # Load the environment model.
        self.scene = self.loader.loadModel("models/environment")
        # Reparent the model to render.
        self.scene.reparentTo(self.render)
        # Apply scale and position transforms on the model.
        self.scene.setScale(0.25, 0.25, 0.25)

        self.scene.setPos(-8, 42, 0)

        # Add the spinCameraTask procedure to the task manager.
        if no_rotate:
            self.taskMgr.add(self.spinCameraTask, "SpinCameraTask")
        else:
            self.taskMgr.add(self.DspinCameraTask, "SpinCameraTask")


        # Load and transform the panda actor.
        self.pandaActor = Actor("models/panda-model",
                                {"walk": "models/panda-walk4"})

        if scale:
            self.pandaActor.setScale(0.005, 0.005, 0.005)

        self.pandaActor.reparentTo(self.render)
        # Loop its animation.
        self.pandaActor.loop("walk")


        # Create the four lerp intervals needed for the panda to
        # walk back and forth.
        # It can spin 10 times at the end and 2 times at the start
        if spin:
            self.pandaActor.hprInterval
        posInterval1 = self.pandaActor.posInterval(13,
                                                   Point3(0, -10, 0),
                                                   startPos=Point3(0, 10, 0))
        posInterval2 = self.pandaActor.posInterval(13,
                                                   Point3(0, 10, 0),
                                                   startPos=Point3(0, -10, 0))
        hprInterval1 = self.pandaActor.hprInterval(3,
                                                   Point3(3600, 0, 0),
                                                   startHpr=Point3(0, 0, 0))
        hprInterval2 = self.pandaActor.hprInterval(3,
                                                   Point3(0, 0, 0),
                                                   startHpr=Point3(360, 0, 0))

        # Create and play the sequence that coordinates the intervals.
        #Panda moonwalk at every return. It will walk straight first then moonwalk because He is cool :)
        if moonwalk:
            self.pandaPace

        self.pandaPace = Sequence(posInterval1, hprInterval1,
                                  posInterval2, hprInterval2,
                                  name="pandaPace")
        self.pandaPace.loop()


    # Define a procedure to move the camera.
    def spinCameraTask(self, task):
        angleDegrees = task.time * 6.0
        angleRadians = angleDegrees * (pi / 180.0)
        self.camera.setPos(20 * sin(angleRadians), -20.0 * cos(angleRadians), 3)
        self.camera.setHpr(angleDegrees, 0, 0)
        return task.cont

    def DspinCameraTask(self, task):
        angleDegrees = task.time * 0.0
        angleRadians = angleDegrees * (pi / 180.0)
        self.camera.setPos(20 * sin(angleRadians), -20.0 * cos(angleRadians), 3)
        self.camera.setHpr(angleDegrees, 0, 0)
        return task.cont


walking = WalkingPanda()
walking.run()
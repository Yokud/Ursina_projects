from ursina import Entity, Vec3, time, color, Mesh
import math


def magnitude(vec):
    return math.hypot(vec[0], vec[1])


def limit(vec, lim):
    vecmag = magnitude(vec)
    vec1 = vec * lim / vecmag if vecmag > lim else vec
    return vec1


class Boid(Entity):
    def __init__(self, maxspeed=2, maxforce=0.1, sep=2, align=1, position=Vec3(0, 0, 0), **kwargs):
        super().__init__()
        self.position = position
        verts = ((0, 0, 0), (1, 0, 0), (.5, 1, 0))
        tris = (1, 2, 0)
        self.model = Mesh(vertices=verts, triangles=tris)
        self.color = color.red
        self.collider = 'box'
        self.origin = Vec3(0.5, 0.5, 0)
        self.maxspeed = maxspeed
        self.maxforce = maxforce
        self.desiredSep = sep
        self.desiredAl = align
        self.velocity = Vec3(0, 0, 0)
        self.acceleration = Vec3(0, 0, 0)

    def checkedges(self, display):
        pass

    def applyforce(self, force=1):
        self.acceleration += force

    def update(self):
        self.velocity += self.acceleration
        velmag = magnitude(self.velocity)
        self.velocity = limit(self.velocity, self.maxspeed)
        self.position += self.velocity * time.dt
        self.acceleration = Vec3(0, 0, 0)

    def seek(self, target):
        desired = Vec3(target[0], target[1], 0) - self.position
        mag = magnitude(desired)
        desired *= self.maxspeed / mag
        steer = desired - self.velocity
        steermag = magnitude(steer)
        steer = limit(steer, self.maxforce)
        if mag > 2:
            self.applyforce(steer)
        else:
            self.applyforce(-steer)

    def separate(self, boids):
        sum = Vec3(0, 0, 0)
        count = 0
        for boid in boids:
            d = magnitude(self.position - boid.position)
            if d > 0 and d < self.desiredSep:
                current = self.position - boid.position
                sum += current / magnitude(current)
                count += 1

        if count > 0:
            sum *= self.maxspeed / count
            sum -= self.velocity
            sum = limit(sum, self.maxforce * 3)
            self.applyforce(sum)


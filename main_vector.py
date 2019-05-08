from playLA.Vector import Vector

if __name__ == '__main__':
    vec = Vector([5, 2])
    print(vec)
    print(len(vec))
    print("Vec[0]={}, Vec[1]={}".format(vec[0], vec[1]))

    vec2 = Vector([3, 1])
    print("{} + {} = {}".format(vec, vec2, vec + vec2))
    print("{} - {} = {}".format(vec, vec2, vec - vec2))
    print("{} * {} = {}".format(vec2, 3, vec2 * 3))
    print("{} * {} = {}".format(3, vec2, 3 * vec2))
    print("+{} = {}".format(vec, +vec))
    print("-{} = {}".format(vec, -vec))

    zero2 = Vector.zero(2)
    print(zero2)

    print("norm({}) = {}".format(vec, vec.norm()))

    print("normalize {} is {}".format(vec, vec.normalize()))
    print(vec.normalize().norm())

    print(vec.dot(vec2))

import numpy as np

if __name__ == '__main__':
    print(np.__version__)
    print(np.zeros(5))
    print(np.ones(5))
    print(np.full(5, 100))

    vec = np.array([1, 2, 3])
    print(vec)
    print(vec.size)
    print(len(vec))
    print(type(vec))

    vec2 = np.array([4, 5, 6])
    print("{} + {} = {}".format(vec, vec2, vec + vec2))
    print("{} - {} = {}".format(vec, vec2, vec - vec2))
    print("{} * {} = {}".format(3, vec2, 3 * vec2))
    print("{} * {} = {}".format(vec2, 3, vec2 * 3))
    print("{} * {} = {}".format(vec, vec2, vec * vec2))
    print("{}.dot({}) = {}".format(vec, vec2, vec.dot(vec2)))

    print(np.linalg.norm(vec))
    print(vec / np.linalg.norm(vec))
    print(np.linalg.norm(vec / np.linalg.norm(vec)))

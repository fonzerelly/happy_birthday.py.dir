import unittest

from tower import createTowerAt, createLayerAt, createStep

from Position import Position

exact = lambda fst: lambda snd: fst[0] == snd[0] and fst[1] == snd[1] and fst[2] == snd[2]
ignoreHeight = lambda fst: lambda snd: fst[0] == snd[0] and fst[2] == snd[2]
curriedFilter = lambda predicate: lambda l: list(filter(predicate, l))
findExactlyIn = lambda tpl: lambda lst: len(curriedFilter(exact(tpl))(lst)) == 1
excludes = lambda tpl: lambda lst: len(curriedFilter(exact(tpl))(lst)) == 0

class TestCircleAt(unittest.TestCase):
    def test_should_create_tiny_circle (self):
        p = Position()
        result = createCircle(p,2)
        self.assertEqual(len(result), 5)




if __name__ == '__main__':
    unittest.main() 
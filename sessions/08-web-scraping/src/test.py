import unittest
from rubiks_cube import Cube



class TestRotate(unittest.TestCase):
	def setUp(self):
		self.cube = Cube([
			[['O', 'G'], ['W', 'Y']],
			[['B', 'G'], ['G', 'R']],
			[['R', 'Y'], ['W', 'O']],
			[['R', 'B'], ['W', 'O']],
			[['B', 'R'], ['G', 'Y']],
			[['O', 'W'], ['B', 'Y']]
		])
	
	def test_L(self):
		cube = Cube(self.cube)
		rotate = Cube([
			[['R', 'G'], ['W', 'Y']],
			[['O', 'G'], ['W', 'R']],
			[['B', 'Y'], ['G', 'O']],
			[['R', 'B'], ['W', 'O']],
			[['G', 'B'], ['Y', 'R']],
			[['O', 'W'], ['B', 'Y']]
		])
		cube.left_rotate()
		self.assertEqual(cube, rotate)
	
	def test_L_prime(self):
		cube = Cube(self.cube)
		rotate = Cube([
			[['B', 'G'], ['G', 'Y']],
			[['R', 'G'], ['W', 'R']],
			[['R', 'Y'], ['W', 'O']],
			[['O', 'B'], ['W', 'O']],
			[['R', 'Y'], ['B', 'G']],
			[['O', 'W'], ['B', 'Y']]
		])
		cube.left_rotate(True)
		self.assertEqual(cube, rotate)
	
	def test_R(self):
		cube = Cube(self.cube)
		rotate = Cube([
			[['O', 'G'], ['W', 'R']],
			[['B', 'Y'], ['G', 'O']],
			[['R', 'B'], ['W', 'O']],
			[['R', 'G'], ['W', 'Y']],
			[['B', 'R'], ['G', 'Y']],
			[['B', 'O'], ['Y', 'W']]
		])
		cube.right_rotate()
		self.assertEqual(cube, rotate)
	
	def test_R_prime(self):
		cube = Cube(self.cube)
		rotate = Cube([
			[['O', 'B'], ['W', 'O']],
			[['B', 'G'], ['G', 'Y']],
			[['R', 'G'], ['W', 'R']],
			[['R', 'Y'], ['W', 'O']],
			[['B', 'R'], ['G', 'Y']],
			[['W', 'Y'], ['O', 'B']]
		])
		cube.right_rotate(True)
		self.assertEqual(cube, rotate)
	
	def test_U(self):
		cube = Cube(self.cube)
		rotate = Cube([
			[['W', 'O'], ['Y', 'G']],
			[['O', 'W'], ['G', 'R']],
			[['R', 'Y'], ['W', 'O']],
			[['R', 'B'], ['R', 'B']],
			[['B', 'G'], ['G', 'Y']],
			[['O', 'W'], ['B', 'Y']]
		])
		cube.up_rotate()
		self.assertEqual(cube, rotate)
	
	def test_U_prime(self):
		cube = Cube(self.cube)
		rotate = Cube([
			[['G', 'Y'], ['O', 'W']],
			[['B', 'R'], ['G', 'R']],
			[['R', 'Y'], ['W', 'O']],
			[['R', 'B'], ['W', 'O']],
			[['O', 'W'], ['G', 'Y']],
			[['B', 'G'], ['B', 'Y']]
		])
		cube.up_rotate(True)
		self.assertEqual(cube, rotate)
	
	def test_D(self):
		cube = Cube(self.cube)
		rotate = Cube([
			[['O', 'G'], ['W', 'Y']],
			[['B', 'G'], ['G', 'Y']],
			[['W', 'R'], ['O', 'Y']],
			[['Y', 'B'], ['W', 'O']],
			[['B', 'R'], ['B', 'R']],
			[['O', 'W'], ['G', 'R']]
		])
		cube.down_rotate()
		self.assertEqual(cube, rotate)
	
	def test_D_prime(self):
		cube = Cube(self.cube)
		rotate = Cube([
			[['O', 'G'], ['W', 'Y']],
			[['B', 'G'], ['B', 'Y']],
			[['Y', 'O'], ['R', 'W']],
			[['Y', 'G'], ['W', 'O']],
			[['B', 'R'], ['G', 'R']],
			[['O', 'W'], ['B', 'R']]
		])
		cube.down_rotate(True)
		self.assertEqual(cube, rotate)
	
	def test_F(self):
		cube = Cube(self.cube)
		rotate = Cube([
			[['O', 'G'], ['Y', 'R']],
			[['G', 'B'], ['R', 'G']],
			[['B', 'O'], ['W', 'O']],
			[['R', 'B'], ['W', 'O']],
			[['B', 'R'], ['G', 'Y']],
			[['W', 'W'], ['Y', 'Y']]
		])
		cube.front_rotate()
		self.assertEqual(cube, rotate)
	
	def test_F_prime(self):
		cube = Cube(self.cube)
		rotate = Cube([
			[['O', 'G'], ['O', 'B']],
			[['G', 'R'], ['B', 'G']],
			[['R', 'Y'], ['W', 'O']],
			[['R', 'B'], ['W', 'O']],
			[['B', 'Y'], ['G', 'W']],
			[['Y', 'W'], ['R', 'Y']]
		])
		cube.front_rotate(True)
		self.assertEqual(cube, rotate)
	
	def test_B(self):
		cube = Cube(self.cube)
		rotate = Cube([
			[['W', 'Y'], ['W', 'Y']],
			[['B', 'G'], ['G', 'R']],
			[['R', 'Y'], ['B', 'G']],
			[['W', 'R'], ['O', 'B']],
			[['G', 'R'], ['O', 'Y']],
			[['O', 'O'], ['B', 'W']]
		])
		cube.back_rotate()
		self.assertEqual(cube, rotate)
	
	def test_B_prime(self):
		cube = Cube(self.cube)
		rotate = Cube([
			[['G', 'B'], ['W', 'Y']],
			[['B', 'G'], ['G', 'R']],
			[['R', 'Y'], ['Y', 'W']],
			[['B', 'O'], ['R', 'W']],
			[['W', 'R'], ['O', 'Y']],
			[['O', 'O'], ['B', 'G']]
		])
		cube.back_rotate(True)
		self.assertEqual(cube, rotate)



if __name__ == '__main__':
	unittest.main()
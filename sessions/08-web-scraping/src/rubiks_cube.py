import itertools
import numpy as np
from copy import deepcopy
from collections import deque



class Cube:
	def __init__(self, cube):
		if isinstance(cube, Cube):
			self.cube = deepcopy(cube.cube)
		else:
			self.cube = np.array(cube)
	
	def __str__(self):
		s = ""
		faces = ['Up', 'Front', 'Down', 'Back', 'Left', 'Right']
		for i in range(len(faces)):
			s += f'{faces[i]} Face:\n'
			for row in self.cube[i]:
				s += ' '.join(row) + '\n'
			s += '\n'
		return s
	
	def __repr__(self):
		return self.__str__()
	
	def __eq__(self, other):
		""" Overrides the default implementation """
		if not isinstance(other, Cube):
			return False
		return np.array_equal(self.cube, other.cube)
	
	def is_solved(self):
		""" Returns if the cube is in a solved state """
		for face in self.cube:
			row = list(itertools.chain.from_iterable(face))
			if row.count(row[0]) != len(row):
				return False
		return True

	def rotate_90(self, face, neg=False):
		""" Performs a (+/-)90° rotation on the face and returns it """
		face = np.transpose(face)
		if neg:
			face = np.flipud(face)
		else:
			face = np.fliplr(face)
		return face

	def rotate_180(self, face):
		""" Performs a 180° rotation on the face and returns it """
		face = np.fliplr(face)
		face = np.flipud(face)
		return face

	def left(self, face, pos):
		""" Assigns the left side of the face to cube face at pos """
		for i in range(len(face)):
			self.cube[pos][i][0] = face[i][0]

	def right(self, face, pos):
		""" Assigns the right side of the face to cube face at pos """
		for i in range(len(face)):
			self.cube[pos][i][1] = face[i][1]

	def up(self, face, pos):
		""" Assigns the up side of the face to cube face at pos """
		self.cube[pos][0] = face[0]

	def down(self, face, pos):
		""" Assigns the down side of the face to cube face at pos """
		self.cube[pos][1] = face[1]

	def left_rotate(self, prime=False):
		""" Performs a L / L' rotation on the cube """
		pos = [0, 3, 2, 1]
		if prime:
			pos.reverse()
		temp = deepcopy(self.cube[pos[0]])
		for i in range(len(pos) - 1):
			self.left(self.cube[pos[i + 1]], pos[i])
		self.left(temp, pos[-1])
		self.cube[4] = self.rotate_90(self.cube[4], prime)

	def right_rotate(self, prime=False):
		""" Performs a R / R' rotation on the cube """
		pos = [0, 1, 2, 3]
		if prime:
			pos.reverse()
		temp = deepcopy(self.cube[pos[0]])
		for i in range(len(pos) - 1):
			self.right(self.cube[pos[i + 1]], pos[i])
		self.right(temp, pos[-1])
		self.cube[5] = self.rotate_90(self.cube[5], prime)

	def up_rotate(self, prime=False):
		""" Performs a U / U' rotation on the cube """
		pos = [1, 5, 3, 4]
		if prime:
			pos.reverse()
		temp = deepcopy(self.cube[pos[0]])
		self.cube[3] = self.rotate_180(self.cube[3])
		for i in range(len(pos) - 1):
			self.up(self.cube[pos[i + 1]], pos[i])
		self.up(temp, pos[-1])
		self.cube[3] = self.rotate_180(self.cube[3])
		self.cube[0] = self.rotate_90(self.cube[0], prime)

	def down_rotate(self, prime=False):
		""" Performs a D / D' rotation on the cube """
		pos = [1, 4, 3, 5]
		if prime:
			pos.reverse()
		temp = deepcopy(self.cube[pos[0]])
		self.cube[3] = self.rotate_180(self.cube[3])
		for i in range(len(pos) - 1):
			self.down(self.cube[pos[i + 1]], pos[i])
		self.down(temp, pos[-1])
		self.cube[3] = self.rotate_180(self.cube[3])
		self.cube[2] = self.rotate_90(self.cube[2], prime)

	def front_rotate(self, prime=False):
		""" Performs a F / F' rotation on the cube """
		pos = [0, 4, 2, 5]
		if prime:
			pos[1:] = pos[1:][::-1]
		self.cube[2] = self.rotate_180(self.cube[2])
		self.cube[4] = self.rotate_90(self.cube[4])
		self.cube[5] = self.rotate_90(self.cube[5], True)
		temp = deepcopy(self.cube[pos[0]])
		for i in range(len(pos) - 1):
			self.down(self.cube[pos[i + 1]], pos[i])
		self.down(temp, pos[-1])
		self.cube[2] = self.rotate_180(self.cube[2])
		self.cube[4] = self.rotate_90(self.cube[4], True)
		self.cube[5] = self.rotate_90(self.cube[5])
		self.cube[1] = self.rotate_90(self.cube[1], prime)
	
	def back_rotate(self, prime=False):
		""" Performs a B / B' rotation on the cube """
		pos = [0, 5, 2, 4]
		if prime:
			pos[1:] = pos[1:][::-1]
		self.cube[2] = self.rotate_180(self.cube[2])
		self.cube[4] = self.rotate_90(self.cube[4])
		self.cube[5] = self.rotate_90(self.cube[5], True)
		temp = deepcopy(self.cube[pos[0]])
		for i in range(len(pos) - 1):
			self.up(self.cube[pos[i + 1]], pos[i])
		self.up(temp, pos[-1])
		self.cube[2] = self.rotate_180(self.cube[2])
		self.cube[4] = self.rotate_90(self.cube[4], True)
		self.cube[5] = self.rotate_90(self.cube[5])
		self.cube[3] = self.rotate_90(self.cube[3], prime)
	
	def left_rotated(self, prime=False):
		cube = Cube(self.cube)
		cube.left_rotate(prime)
		return cube
	
	def right_rotated(self, prime=False):
		cube = Cube(self.cube)
		cube.right_rotate(prime)
		return cube
	
	def up_rotated(self, prime=False):
		cube = Cube(self.cube)
		cube.up_rotate(prime)
		return cube
	
	def down_rotated(self, prime=False):
		cube = Cube(self.cube)
		cube.down_rotate(prime)
		return cube
	
	def front_rotated(self, prime=False):
		cube = Cube(self.cube)
		cube.front_rotate(prime)
		return cube
	
	def back_rotated(self, prime=False):
		cube = Cube(self.cube)
		cube.back_rotate(prime)
		return cube



def get_cubes(cube):
	cubes = []
	moves = ["L", "L'", "L2", "R", "R'", "R2", "U", "U'", "U2", "D", "D'", "D2", "F", "F'", "F2", "B", "B'", "B2"]
	cubes.append(cube.left_rotated().cube)
	cubes.append(cube.left_rotated(True).cube)
	cubes.append(cube.left_rotated().left_rotated().cube)
	cubes.append(cube.right_rotated().cube)
	cubes.append(cube.right_rotated(True).cube)
	cubes.append(cube.right_rotated().right_rotated().cube)
	cubes.append(cube.up_rotated().cube)
	cubes.append(cube.up_rotated(True).cube)
	cubes.append(cube.up_rotated().up_rotated().cube)
	cubes.append(cube.down_rotated().cube)
	cubes.append(cube.down_rotated(True).cube)
	cubes.append(cube.down_rotated().down_rotated().cube)
	cubes.append(cube.front_rotated().cube)
	cubes.append(cube.front_rotated(True).cube)
	cubes.append(cube.front_rotated().front_rotated().cube)
	cubes.append(cube.back_rotated().cube)
	cubes.append(cube.back_rotated(True).cube)
	cubes.append(cube.back_rotated().back_rotated().cube)
	return moves, cubes



def shortest_path(start):
	"""
	Finds the shortest path in solving a 2×2×2 rubik's cube from start state to solved state

	Arguments:
		start {np.array} -- start state of the cube
	"""
	i = 1
	tree = {}
	seen = set()
	dtype = start.dtype
	shape = start.shape
	d = deque([(None, start.tobytes())])
	level = {(None, start.tobytes()): 1}

	while d:
		# Get element in front
		mc = d.pop()
		cube = np.frombuffer(mc[1], dtype=dtype).reshape(*shape)
		if i % 1000 == 0:
			print(f'{i}) Deque: {len(d)}, Seen: {len(seen)}, Level: {level[mc]}')

		moves, cubes = get_cubes(Cube(cube))

		# Update structures with new cubes
		for j in range(len(moves)):
			b = cubes[j].tobytes()
			mc_j = (moves[j], b)
			if b not in seen:
				tree[mc_j] = mc
				level[mc_j] = level[mc] + 1
				seen.add(b)
				d.appendleft(mc_j)

		# Check if cube is solved
		if Cube(cube).is_solved():
			break
		i += 1

	# Get path from start to solved
	path = []
	while mc in tree:
		path.append(mc[0])
		mc = tree[mc]
	print(' \u2192 '.join(reversed(path)))
	print(f'Length: {len(path) - 1}')



if __name__ == '__main__':
	start = np.array([
		[['O', 'G'], ['W', 'Y']],
		[['B', 'G'], ['G', 'R']],
		[['R', 'Y'], ['W', 'O']],
		[['R', 'B'], ['W', 'O']],
		[['B', 'R'], ['G', 'Y']],
		[['O', 'W'], ['B', 'Y']]
	])
	solved = np.array([
		[['O', 'O'], ['O', 'O']],
		[['R', 'R'], ['R', 'R']],
		[['Y', 'Y'], ['Y', 'Y']],
		[['B', 'B'], ['B', 'B']],
		[['G', 'G'], ['G', 'G']],
		[['W', 'W'], ['W', 'W']]
	])
	shortest_path(start)
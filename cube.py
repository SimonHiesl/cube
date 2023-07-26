class RubiksCube:
    def __init__(self):
        # Initialize the cube with default colors
        self.cube = [['W']*9, ['G']*9, ['R']*9, ['B']*9, ['O']*9, ['Y']*9]

    def turn_front_clockwise(self):
        # Rotate front face clockwise
        temp = self.cube[0][:]  # Copy front face stickers
        self.cube[0][0] = temp[6]
        self.cube[0][1] = temp[3]
        self.cube[0][2] = temp[0]
        self.cube[0][3] = temp[7]
        self.cube[0][5] = temp[1]
        self.cube[0][6] = temp[8]
        self.cube[0][7] = temp[5]
        self.cube[0][8] = temp[2]

        # Rotate side face stickers
        self.cube[1][6], self.cube[2][0], self.cube[3][2], self.cube[4][8] = self.cube[4][8], self.cube[1][6], self.cube[2][0], self.cube[3][2]
        self.cube[1][7], self.cube[2][3], self.cube[3][1], self.cube[4][5] = self.cube[4][5], self.cube[1][7], self.cube[2][3], self.cube[3][1]
        self.cube[1][8], self.cube[2][6], self.cube[3][0], self.cube[4][2] = self.cube[4][2], self.cube[1][8], self.cube[2][6], self.cube[3][0]

    # Implement other turn methods for different faces

    def print_cube(self):
        # Print the current state of the cube
        for face in self.cube:
            for sticker in face:
                print(sticker, end=' ')
            print()

# Example usage
cube = RubiksCube()
cube.print_cube()
cube.turn_front_clockwise()
cube.print_cube()

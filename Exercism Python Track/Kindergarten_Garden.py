"""
Instructions:

Given a diagram, determine which plants each child in the kindergarten class is responsible for.
The kindergarten class is learning about growing plants. The teacher thought it would be a good idea to give them actual seeds, plant them in actual dirt, and grow actual plants.
They've chosen to grow grass, clover, radishes, and violets.
To this end, the children have put little cups along the window sills, and planted one type of plant in each cup, choosing randomly from the available types of seeds.
[window][window][window]
........................ # each dot represents a cup
........................
There are 12 children in the class:
Alice, Bob, Charlie, David,
Eve, Fred, Ginny, Harriet,
Ileana, Joseph, Kincaid, and Larry.
Each child gets 4 cups, two on each row. Their teacher assigns cups to the children alphabetically by their names.
The following diagram represents Alice's plants:
[window][window][window]
VR......................
RG......................
In the first row, nearest the windows, she has a violet and a radish. In the second row she has a radish and some grass.
Your program will be given the plants from left-to-right starting with the row nearest the windows.
From this, it should be able to determine which plants belong to each student.
"""

class Garden(object):
    list_students = ['Alice', 'Bob', 'Charlie', 'David',
                     'Eve', 'Fred', 'Ginny', 'Harriet',
                     'Ileana', 'Joseph', 'Kincaid', 'Larry']

    def __init__(self, diagram, students=list_students):
        self.diagram = diagram.split("\n")
        self.students = sorted(students)

    def plants(self, student):
        plants_dict = {"G": "Grass", "R": "Radishes", "C": "Clover", "V": "Violets"}
        i = self.students.index(student)
        plants = []
        plant_code = self.diagram[0][2 * i:2 * i + 2] + self.diagram[1][2 * i:2 * i + 2]
        for j in plant_code:
            plants.append(plants_dict[j])
        return plants

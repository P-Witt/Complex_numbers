import numpy as np
import matplotlib.pyplot as plt


# currently missing equality multiplication and division

class complex_number:
    def __init__(self, a, b, type="standard"):
        self.z = [a, b]
        self.type = type

    def convert_to_polar(self, change=True):
        """"
        converts a nonzero complex number into its coordinate form

        if zero is given as an argument nothing will be changed
        if change is True values will be changed in place
        given a complex number in polar form will trigger a warning message but continue the process
        """
        if self.type == "polar":
            print("Warning: You are converting a complex number in polar form to polar form")
        theta = np.arctan2(self.z[1], self.z[0])
        r = np.sqrt(self.z[0] * self.z[0] + self.z[1] * self.z[1])
        if change:
            if self.z == [0, 0]:
                self.type = "polar"
                print("Warning: you are trying to convert 0 to polar form this is not well defined")
                pass
            # maybe write the function yourself
            self.z = [r, theta]
            self.type = "polar"
        else:
            if self.z == [0, 0]:
                return complex_number(0, 0, type="polar")
            return complex_number(r, theta, type="polar")

    def convert_to_standard(self, change=True):
        """"
        converts a complex number from polar form to standard form
        if change is True values will be changed in place otherwise they will be returned
        """
        if self.type == "standard":
            print("Warning: You are converting a complex number in standard form to standard form")
        a = self.z[0] * np.cos(self.z[1])
        b = self.z[0] * np.sin(self.z[1])
        if change:
            self.z = [a, b]
            self.type = "standard"
        else:
            return complex_number(a, b, "standard")

    def copy(self):
        return complex_number(self.z[0], self.z[1], type=self.type)

    def __add__(self, other):
        """"
        This function will add to complex parameters
        if the type of these parameters is different they will be converted to match the same
        the type returned will be of the first input
        """
        if self.state == "standard":
            if other.state == "standard":
                return complex_number(self.z[0]+other.z[0], self.z[1]+other.z[1], type="standard")
            if other.state == "polar":
                temp = other.copy()
                temp.convert_to_standard()
                return complex_number(self.z[0]+temp.z[0],self.z[1]+temp.z[1], type= "standard")

    def get_conjugate(self):
        if self.type == "standard":
            return [self.z[0], -self.z[1]]
        else:
            a = self.z[0]
            b = self.z[1]
            temp = complex_number(a, b, type="polar")
            temp.convert_to_standard()
            temp.conjugate()
            return temp.convert_to_polar()

    def conjugate(self):
        if self.type == "standard":
            [self.z[0], -self.z[1]]
        else:
            """"
            some what unreasonable in computation but the shortest implementation coming to mind right now
            """
            a = self.z[0]
            b = self.z[1]
            temp = complex_number(a, b, type="polar")
            temp.convert_to_standard()
            temp.conjugate()
            temp.convert_to_polar()
            self.z = temp.z

    def invert(self):
        return

    def __repr__(self):
        """"
        print method for complex numbers
        """
        return str(self.z) + " in " + self.type + " form"


test = complex_number(1, -2)
test.convert_to_polar()
test.convert_to_standard()
print(test.get_conjugate())

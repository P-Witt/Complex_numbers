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
        # maybe write the function yourself
        r = np.sqrt(self.z[0] * self.z[0] + self.z[1] * self.z[1])
        if change:
            if self.z == [0, 0]:
                self.type = "polar"
                print("Warning: you are trying to convert 0 to polar form this is not well defined")
                pass
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

    def __eq__(self, other):
        """"
        **Warning**
        due to the fact that converting between polar and standard form produces numerical error
        the function cuts of after 14 decimal point and may return "false" statements
        """
        if self.type == other.type:
            re = other.z[0] - 10 ** (-15) < self.z[0] < other.z[0] + 10 ** (-15)
            im = other.z[1] - 10 ** (-15) < self.z[1] < other.z[1] + 10 ** (-15)
            return re and im
        if self.type == "polar":
            temp = self.copy()
            temp.convert_to_standard()
            re = temp.z[0] - 10 ** (-15) < other.z[0] < temp.z[0] + 10 ** (-15)
            print(re)
            im = temp.z[1] - 10 ** (-15) < other.z[1] < temp.z[1] + 10 ** (-15)
            return re and im
        if other.type == "polar":
            temp = other.copy()
            temp.convert_to_standard()
            re = temp.z[0] - 10 ** (-15) < self.z[0] < temp.z[0] + 10 ** (-15)
            im = temp.z[1] - 10 ** (-15) < self.z[1] < temp.z[1] + 10 ** (-15)
            return re and im

    def __add__(self, other):
        """"
        This function will add to complex parameters
        if the type of these parameters is different they will be converted to match the same
        the type returned will be of the first input
        """
        if self.type == "standard":
            if other.type == "standard":
                return complex_number(self.z[0] + other.z[0], self.z[1] + other.z[1], type="standard")
            if other.type == "polar":
                temp = other.copy()
                temp.convert_to_standard()
                return complex_number(self.z[0] + temp.z[0], self.z[1] + temp.z[1], type="standard")
        if self.type == "polar":
            if other.type == "standard":
                temp = self.copy()
                temp.convert_to_standard
                temp = complex_number(self.z[0] + temp.z[0], self.z[1] + temp.z[1], type="standard")
                return temp.convert_to_polar()
            if other.type == "polar":
                temp1 = self.copy()
                temp2 = other.copy()
                temp1.convert_to_standard()
                temp2.convert_to_standard()
                temp = complex_number(temp1.z[0] + temp2.z[0], temp1.z[1] + temp2.z[1], type="standard")
                temp.convert_to_polar()
                return temp

    def __mul__(self, other):
        if self.type == other.type == "standard":
            re = self.z[0] * other.z[0] - self.z[1] * other.z[1]
            im = self.z[0] * other.z[1] + self.z[1] * other.z[0]
            temp = complex_number(re, im, type="standard")
            return temp
        if self.type == other.type == "polar":
            r = self.z[0]*other.z[0]
            theta = self.z[1] + other.z[1]
            temp = complex_number(r, theta, type= "polar")
            return temp
        if self.type == "standard" and other.type == "polar":
            temp = other.convert_to_standard(change = False)
            re = self.z[0] * temp.z[0] - self.z[1] * temp.z[1]
            im = self.z[0] * temp.z[1] + self.z[1] * temp.z[0]
            temp = complex_number(re, im, type="standard")
            return temp
        if self.type == "polar" and other.type == "standard":
            temp = other.convert_to_polar(change = False)
            r = self.z[0] * temp.z[0]
            theta = self.z[1] + temp.z[1]
            temp = complex_number(r, theta, type="polar")
            return temp

    def __abs__(self):
        return np.sqrt(self.z[0]**2 + self.z[1]**2)

    def invert(self):
        if self.type == "standard":
            re = self.z[0]/(abs(self)**2)
            im = -self.z[1]/(abs(self)**2)
            temp = complex_number(re, im, type="standard")
            return temp
        if self.type == "polar":
            r = 1/self.z[0]
            theta = -self.z[1]
            temp = complex_number(r, theta, type="polar")
            return temp

    def __truediv__(self, other):
        return self*(other.invert())

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

    def __repr__(self):
        """"
        print method for complex numbers
        """
        if self.type == "polar":
            return str(self.z[0]) + "*exp(" + str(self.z[1]) + "*i)"
        if self.type == "standard":
            return str(self.z[0]) + " + " + str(self.z[1]) + "*i"

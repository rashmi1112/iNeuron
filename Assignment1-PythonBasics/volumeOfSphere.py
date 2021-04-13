class print_volume:
    def print_volume(self, radius):
        pi = 3.14
        volume = (4 / 3) * pi * (radius**3)
        print('Volume of the sphere is: ' + '{:.2f}'.format(volume))


if __name__ == '__main__':
    radius = 12
    obj = print_volume()
    obj.print_volume(radius)

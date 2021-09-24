class Name():

    def __init__(self, surname):
        self.surname = surname
        # self.name = name
        # self.lastname = lastname

    def brief_name(self):
        x = self.surname.split(' ')
        return f'{x[0]} {x[1]}'

    def initials(self):
        x = self.surname.split(' ')
        return f'{x[0]} {x[1][0]}.{x[2][0]}.'

    @staticmethod
    def strfname(znach1, znach2):
        fio = znach1.split(' ')
        y = {
            '%Ф': fio[0],
            '%ф': f"{fio[0][0]}.",
            '%И': fio[1],
            '%и': f"{fio[1][0]}.",
            '%О': fio[2],
            '%о': f"{fio[2][0]}.",
        }
        x = znach2.split(' ')
        print('{}'.format(' '.join([y[z] for z in x])))


a = Name('Иванов Иван Иванович')
print(a.brief_name())
print(a.initials())
Name.strfname('Иванов Иван Иванович', '%Ф %ф %о')

# m = 'Иванов Иван Иванович'
# x1 = y1.split(' ')
# y = {
#     '%Ф': x1[0],
#     '%ф': x1[0][0],
#     '%И': x1[1],
#     '%и':  x1[1][0],
#     '%О': x1[2],
#     '%о': x1[2][0]
# }
#
# y2 = '%Ф %О %о'
# x = y2.split(' ')
#
# h = [y[z] for z in x]
# h1 = ' '.join(h)
# print(h1)
#
# print(x)
# print(y)



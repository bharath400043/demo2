class Ipl:
    place = 'dubai'
    time = '8 clock'

    def __init__(self, team_name, captian, owner):
        self.team_name = team_name
        self.captian = captian
        self.owner = owner
        print('team name : ', self.team_name, self.captian, self.owner)

    def points_table(self):
        try:
            points = int(input('enter the points :'))
            if points <= 0 or points >= 21:
                return 'please enter valid number'
            elif points >= 0 and points <= 15:
                return 'Your not eligible for semifinals'
            elif points >= 16 and points <= 20:
                return 'Your eligible for semifinals'

        except Exception as er:
            print(er)


obj = Ipl("CSK", "Dhoni", "swaroop")
res = obj.points_table()
print('result : ', res)

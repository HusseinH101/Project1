class Player:
    def __init__(self, name):
        """""This function initializes the methods"""
        self.name = name
        self.total_score = 0
        self.current_score = 0

        

    def add_total_score(self, points):
        """""This function returns the totalscore of the
        currentuser """
        self.total_score += points
        return self.total_score
    
    def change_name(self, name_dict):
        """""This function chnages name of the current user by asking
        for the current name to change and changing it to the new name typed
        names are stored in the dictornary, current name gets removed and
        replace with the new one"""
        current_name = input('Enter current name: ')
        new_name = input('Enter new name: ')

        if current_name in name_dict:
            name_dict[new_name] = name_dict.pop(current_name)
            self.name = new_name
            print(f'Name changed to {new_name}')

        else:
            print(f'{current_name} not found')

    def reset_turn(self):
        """""This functions resets a drag, if the currentscore is 15
        it resets to 0"""
        self.current_score = 0
        print(f'{self.name}s turn has been reset. Current score is now {self.current_score}')

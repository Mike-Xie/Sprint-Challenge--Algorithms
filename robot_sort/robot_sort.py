class SortingRobot:
    def __init__(self, l):
        """
        SortingRobot takes a list and sorts it.
        """
        self._list = l          # The list the robot is tasked with sorting
        self._item = None       # The item the robot is holding
        self._position = 0      # The list position the robot is at
        self._light = "OFF"     # The state of the robot's light
        self._time = 0          # A time counter (stretch)

    def can_move_right(self):
        """
        Returns True if the robot can move right or False if it's
        at the end of the list.
        """
        return self._position < len(self._list) - 1

    def can_move_left(self):
        """
        Returns True if the robot can move left or False if it's
        at the start of the list.
        """
        return self._position > 0

    def move_right(self):
        """
        If the robot can move to the right, it moves to the right and
        returns True. Otherwise, it stays in place and returns False.
        This will increment the time counter by 1.
        """
        self._time += 1
        if self._position < len(self._list) - 1:
            self._position += 1
            return True
        else:
            return False

    def move_left(self):
        """
        If the robot can move to the left, it moves to the left and
        returns True. Otherwise, it stays in place and returns False.
        This will increment the time counter by 1.
        """
        self._time += 1
        if self._position > 0:
            self._position -= 1
            return True
        else:
            return False

    def swap_item(self):
        """
        The robot swaps its currently held item with the list item in front
        of it.
        This will increment the time counter by 1.
        """
        self._time += 1
        # Swap the held item with the list item at the robot's position
        self._item, self._list[self._position] = self._list[self._position], self._item

    def compare_item(self):
        """
        Compare the held item with the item in front of the robot:
        If the held item's value is greater, return 1.
        If the held item's value is less, return -1.
        If the held item's value is equal, return 0.
        If either item is None, return None.
        """
        if self._item is None or self._list[self._position] is None:
            return None
        elif self._item > self._list[self._position]:
            return 1
        elif self._item < self._list[self._position]:
            return -1
        else:
            return 0

    def set_light_on(self):
        """
        Turn on the robot's light
        """
        self._light = "ON"
    def set_light_off(self):
        """
        Turn off the robot's light
        """
        self._light = "OFF"
    def light_is_on(self):
        """
        Returns True if the robot's light is on and False otherwise.
        """
        return self._light == "ON"
    def light_is_off(self):
        return self._light == "OFF"

    def get_length(self):
        return len(self._list)

    def get_list(self):
        return self._list

    def sort(self):
        """
        Sort the robot's list using bubble sort
        More details in robot_uper.txt
        TL:DR this is like some sort of low level programming project
        """
        # light off means work to be done still

        while self.light_is_off():
            # unless light is set back off in a further branch
            # this causes the outer while loop to exit
            self.set_light_on()

            
            # iterate through the list going to the right
            while self.can_move_right():
                self.swap_item()
                self.move_right()
                # when element is bigger, swap them
                if self.compare_item() == 1:
                    # these four swap the thing and go back to where we were
                    self.swap_item()
                    self.move_left()
                    self.swap_item()
                    self.move_right()
                    # set light off again so the while loop repeats
                    self.set_light_off()
                # when element is smaller, put it back, go back where we were
                else:
                    self.move_left()
                    self.swap_item()
                    self.move_right()
            # reset all the way to the left, can't avoid iterating through twice
            # in bubble since you have to walk through again with no hitches L-R         
            while self.can_move_left():
                self.move_left()




if __name__ == "__main__":
    # Test our your implementation from the command line
    # with `python robot_sort.py`

    l = [99, 97, 58, 1]
    robot = SortingRobot(l)

    robot.sort()
    print(robot._list)
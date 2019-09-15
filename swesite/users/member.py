class Member:
    first_name = ""
    last_name = ""
    events = {}
    total_points = 0

    def __init__(self, first_name, last_name, total_points):
        self.first_name = first_name
        self.last_name = last_name
        self.total_points = total_points

    def __str__(self):
        """
            (assumes if there is nothing in the total column, member is an officer)
        """
        if self.total_points == "":
            return "{} {:>10}".format(self.full_name().strip(), "OFFICER")

        return "{} {:>10}".format(self.full_name(), self.total_points)

    def full_name(self):
        return "{} {}".format(self.first_name.strip(), self.last_name.strip())

    def set_events(self, events):
        self.events = events

    def get_events_attended_missed(self):
        """
            (assumes nothing in the event column is an event that hasn't happened yet)

            returns a dictionary of all events member has attended and missed
            in the format {'event name': points_earned}
            read as:
                for {'event_name', points_earned } pair in dict:
                    if points_earned is !="":
                        add this pair to dict that will be returned
       """
        return {k: v for k, v in self.events.items() if v != ""}

    def get_events_attended(self):
        """
            (assumes a 0 in the event column means member did not attend event)

            returns a dictionary of all events member has attended
            in the format {'event name': points_earned}
            read as:
                for {'event_name', points_earned } pair in dict:
                    if points_earned is !="" and !=0:
                        add this pair to dict that will be returned
       """
        return {k: v for k, v in self.events.items() if v != "" and v != 0}

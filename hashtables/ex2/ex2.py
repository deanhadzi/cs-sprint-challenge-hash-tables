#  Hint:  You may not need all of these.  Remove the unused functions.
class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    """
    YOUR CODE HERE
    """
    # creating an empty hashtable and our route container.
    flights = {}
    route = []

    # populate all tickets into our hash table.
    for ticket in tickets:
        flights[ticket.source] = ticket.destination

    # the starting location.
    curr = "NONE"

    # iterate through hashtable to sort the tickets.
    for _ in range(length):
        route.append(flights[curr])
        curr = flights[curr]

    return route

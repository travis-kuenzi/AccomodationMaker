import random;

#Host class 
class Host:
    def __init__(self, name, availability, keeping=None):
        self.name = name
        self.availability = availability
        self.keeping = keeping if keeping is not None else []

    #use isAvailable in this function!
    def assign_guest(self, guest):
        if self.availability > 0:
            self.keeping.append(guest)
            self.availability -= 1

    def is_available(self):
        if self.availability > 0:
            return True
        else:
            return False


Colton = Host("Colton", 4)
Travis = Host("Travis", 3)
Micah = Host("Micah", 5)

#create list of hosts
hosts = [Colton, Travis, Micah]

#list of potential guests
guests = ["Billy", "Bob", "Joe", "Tom", "Dick", "Harry", "John", "Sally", "Steve"]

#randomly assign the guests to the hosts

for guest in guests:
    available_hosts = []
    for host in hosts:
        if host.is_available():
            available_hosts.append(host)
    
    if available_hosts:
        host = random.choice(available_hosts)
        host.assign_guest(guest)

for host in hosts:
    print(host.name, ": ", end="")
    for guest in host.keeping:
        print(guest, end=" ")
    print()

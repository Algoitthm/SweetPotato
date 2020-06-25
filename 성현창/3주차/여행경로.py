import copy

def solution(tickets):
    answer = []
    path_dict = {}
    for ticket in tickets:
        start = ticket[0]
        end = ticket[1]
        if start not in path_dict.keys():
            path_dict[start] = [end]
        else:
            tmp = path_dict[start]
            tmp.append(end)
            path_dict[start] = tmp
    current_posit = "ICN"
    person = Person(current_posit, ["ICN"], len(tickets))
    person_list = [person]
    success_person = []
    while(True):
        if len(person_list) == 0:
            break
        person = person_list.pop(0)
        to_travel_list = path_dict[person.current_posit]
        for dest in to_travel_list:
            new_person = copy.deepcopy(person)
            suc_travler = new_person.travel(dest)
            if suc_travler:
                if new_person.check_all():
                    success_person.append(new_person)
                elif len(new_person.path) > len(tickets)+1:
                    continue
                else:
                    person_list.append(new_person)

    answer = success_person.pop(0).path
    for person in success_person:
        for i,j in zip(answer, person.path):
            if i > j:
                answer = person.path
                continue
            elif i != j:
                break

    return answer

class Person:
    def __init__(self, current_posit, path, ticket_number):
        self.current_posit = current_posit
        self.path = path
        self.ticket_number = ticket_number
        self.used_tickets = []

    def check_all(self):
        if len(self.used_tickets) == self.ticket_number:
            return True
        else:
            return False

    def travel(self, dest):
        self.path.append(dest)
        ticket = [self.current_posit, dest]
        if ticket in self.used_tickets:
            return False
        else:
            self.used_tickets.append([self.current_posit, dest])
            self.current_posit = dest
            return True
        

if __name__ == "__main__":
    # solution([["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"]])
    solution([["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL","SFO"]])
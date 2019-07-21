def generate_ticket(airline,source,destination,no_of_passengers):
    ticket_number_list = []
    i = 0
    if no_of_passengers < 5:
        while no_of_passengers != 0:
            ticket_number_list.append(airline + ":" + source[:3] + ":" + destination[:3] + ":" + str(101+i))
            i = i+1
            no_of_passengers = no_of_passengers - 1
    else:
        for i in range(5):
            ticket_number_list.append(airline + ":" + source[:3] + ":" + destination[:3] + ":" + str(100+no_of_passengers))
            i = i+1
            no_of_passengers = no_of_passengers - 1
        ticket_number_list = ticket_number_list[::-1]

    return ticket_number_list
if __name__=="__main__":
    airline=str(input())
    source=str(input())
    destination=str(input())
    no_of_passengers=int(input())
    print( generate_ticket(airline,source,destination,no_of_passengers))
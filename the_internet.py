"""
Comands include: 
create-server <server_name> <valid_IPAddress> 
    Ex: create-server facebook.com 104.233.42.193

create-connection <server_name> <server_name2> <time>
    Ex: create-conection facebook.com amazon.com 23

ping <server_name>
    Ex: ping facebook.com
set-server <server_name>
    Ex: set-server facebook.com
traceroute <servername>
    Ex: traceroute facebook.com
traceroute <valid_IPAddress>
    Ex: traceroute 104.233.42.193

traceroute <servername>
    Ex: traceroute facebook.com
traceroute <valid_IPAddress>
    Ex: traceroute 104.233.42.193

display-servers
ip-config
quit
"""
EXIT_STRING = 'quit'

def create_server(server_name, ip_v4_address, server_list):
    """
        This checks the server list and determines whether or not it already exists as a server
        if it doesnt it checks the ip to see whether or not it is a proper ip address
        if it is then it checks to see whether there is already a server with the inputted name
        or the inputted ip address.
    """
    is_it_a_new_server = True
    do_it = False
    ip_count = 0

    for i in server_list:
        if i == server_name:
            is_it_a_new_server = False
            print(f'This server already exists. {server_name}')
        elif server_list[i]['ipaddress'] == ip_v4_address:
            print(f'This IP address is already in use. {ip_v4_address}')
            is_it_a_new_server = False

    if is_it_a_new_server == True:
        check_ip = ip_v4_address.split('.')
        number_list = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        problem = False
        count = 0

        if len(check_ip) == 4:
            while problem == False and count != len(check_ip):
                for j in check_ip[count]:
                    if j not in number_list:
                        problem = True
                if count != len(check_ip):
                    count += 1

            if count == len(check_ip) and problem == False:
                for i in range(4):
                    if (int(check_ip[i]) >= 0):
                        if (int(check_ip[i]) <= 255):
                            ip_count += 1
                        else:
                            problem = True

            if ip_count == 4:
                print(f'Success: A server with name {server_name} was created at ip {ip_v4_address}')
                server_list[server_name] = {'ipaddress': ip_v4_address, 'is_server': False, 'connections_list': [], 'connect_time': []}

            if problem == True:
                print(f'Error: The IP address is invalid. {ip_v4_address}')
        else:
            print(f'Error: The IP address is invalid. {ip_v4_address}')


def create_connection(server_1, server_2, connect_time, server_list):
    """
        This code checks the connect time and determines whether or not
        the time input is proper and then checks to see the legitimacy of
        the existence of the two inputted servers and if they are not already
        connected it connects them
    """
    if server_1 == server_2:
        print('Error: You cannot connect a server to itself.')

    else:
        number_list = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        problem = False
        count_time = 0

        while problem == False and count_time != len(connect_time):
            for j in connect_time[count_time]:
                if j not in number_list:
                    problem = True
            if count_time != len(connect_time):
                count_time += 1
        if count_time == len(connect_time) and problem == False:
            server_here =  False
            add_or_not = True
            count = 0

            if server_1 not in server_list:
                print(f'Error: Server does not exist. {server_1}')
            if server_2 not in server_list:
                print(f'Error: Server does not exist. {server_2}')

            for i in server_list:
                if i == server_1:
                    count += 1
                elif i == server_2:
                    count += 1
            if count == 2:
                server_here = True
                if server_here == True:
                    if server_1 in server_list[server_2]['connections_list'] or server_2 in server_list[server_1]['connections_list']:
                        add_or_not = False
                        print(f'Error: Servers are already connected. {server_1} , {server_2}')

                    if add_or_not == True:
                        server_list[server_1]['connections_list'].append(server_2)
                        server_list[server_2]['connections_list'].append(server_1)

                        server_list[server_1]['connect_time'].append({server_2: connect_time})
                        server_list[server_2]['connect_time'].append({server_1: connect_time})

                        print(f'Success: {server_1} and {server_2} have been connected.')
        else:
            print(f'Error: Connect time is not a proper time. {connect_time}')

def set_server(server_or_ip, server_list):
    """
        Checks to see if the server exists checking both name
        and ip, if it does exist it switches all of the servers
        to false as being the main server and then it switches
        the one you selected if it exists to True
    """
    does_it_exist = False
    for i in server_list:
        if i == server_or_ip:
            does_it_exist = True
    if does_it_exist == False:
        for i in server_list:
            if server_list[i]['ipaddress'] == server_or_ip:
                does_it_exist = True

    if does_it_exist == True:
        for i in server_list:
            if server_list[i]['ipaddress'] == server_or_ip:
                server_list[i]['is_server'] = True
                print(f'Success: Server has been set at: {i}')
            elif i == server_or_ip:
                server_list[i]['is_server'] = True
                print(f'Success: Server has been set at: {i}')
            else:
                server_list[i]['is_server'] = False
    else:
        print('Error: Server does not exist.')

def ip_config(server_list):
    """
        This just prints the start server not too much here
    """
    count = 0
    for i in server_list:
        if server_list[i]['is_server'] == True:
            print(i, server_list[i]['ipaddress'])
        elif server_list[i]['is_server'] == False:
            count += 1
    if count == len(server_list):
        print('Error: You have not selected a server yet.')

def display_servers(server_list):
    """
        This displays the servers using the key of each thing and connection time etc
    """


    if server_list:
        for i in server_list:
            to_do = 0
            server_name = i
            if server_list[i]['connections_list'] == []:
                print('\t\t', i, '\t',  server_list[i]['ipaddress'])

            if server_list[i]['connections_list'] != []:
                print('\t\t', i, '\t', server_list[i]['ipaddress'])
                for j in range(len(server_list[i]['connections_list'])):
                    server = server_list[i]['connections_list'][j]
                    print('\t\t\t\t', server_list[i]['connections_list'][j], '\t', server_list[server]['ipaddress'], '\t', server_list[i]['connect_time'][j][server])
    else:
        print('Error: There are no servers to display')


def tracert(start_server_from, server_go_to, server_list):
    """
        This uses almost the same thing as spider web on the hw and it displays the route to get to a server if it can
    """
    been_to = []
    tracert_rec(start_server_from, server_go_to, server_list, been_to)

def tracert_rec(start_server_from, server_go_to, server_list, been_to):
    temp_server = server_list[start_server_from]['connections_list']
    been_to.append(start_server_from)

    for i in temp_server:
        if server_go_to in been_to:
               for i in range(len(been_to)):
                   if i != len(been_to):

                       print(i, server_list[been_to[i]]['ipaddress'], ''.join([been_to[i]]))
                   else:
                       pass

        else:
            if i not in been_to:
                tracert_rec(i, server_go_to, server_list, been_to)

def ping(start_server_from, server_go_to, server_list):
    """
        This uses almost the same thing as spider web on the hw and it displays the route to get to a server if it can
        its almost like tracert
    """
    been_to = []
    thing = 0
    thing = ping_rec(start_server_from, server_go_to, server_list, been_to)


def ping_rec(start_server_from, server_go_to, server_list, been_to):

    temp_server = server_list[start_server_from]['connections_list']
    been_to.append(start_server_from)


    for i in temp_server:
        if server_go_to in been_to:
            x = 0
            for i in range(len(been_to)):
                if i + 1 != len(been_to):
                    serv = server_list[been_to[i]]['connect_time'][i].get(been_to[i + 1], False)
                    serv = int(serv)
                    x += serv
                elif i + 1 == len(been_to):
                    print('Reply from', server_list[server_go_to]['ipaddress'], f'time = {x} ms')


        else:
            if i not in been_to:
                ping_rec(i, server_go_to, server_list, been_to)

def run_the_internet():
    """
        This is the main code for my work it just reads the commands and activates them
    """
    trace = ['tracert', 'traceroute']
    server_list = {}
    command = input('>>> ')
    while command != EXIT_STRING:
        action = command.split(' ')[0]
        if action == 'create-server':
            if len(command.split(' ')) == 3:
                server_name = command.split(' ')[1]
                ip_address = command.split(' ')[2]

                create_server(server_name,ip_address, server_list)

        elif action == 'create-connection':
            if len(command.split(' ')) == 4:
                server_1 = command.split(' ')[1]
                server_2 = command.split(' ')[2]
                connect_time = command.split(' ')[3]

                create_connection(server_1, server_2, connect_time, server_list)

        elif action == 'set-server':
            if len(command.split(' ')) == 2:
                 server_or_ip = command.split(' ')[1]
                 set_server(server_or_ip, server_list)

        elif action == 'ip-config':
            ip_config(server_list)

        elif action == 'display-servers':
            display_servers(server_list)

        elif action == 'ping':
            if len(command.split(' ')) == 2:
                server_or_ip = command.split(' ')[1]
                keep_going = False
                go_more = False

                for i in server_list:
                    if server_list[i]['is_server'] == True:
                        start_server_from = i
                        keep_going = True
                if keep_going == True:
                    for j in server_list:
                        if j == server_or_ip:
                            server_go_to = j
                            go_more = True
                        else:
                            if server_list[j]['ipaddress'] == server_or_ip:
                                server_go_to = j
                                go_more = True
                    if go_more == True:
                        if start_server_from == server_go_to:
                            print('Reply from', server_list[server_go_to]['ipaddress'], 'time = 0 ms')
                        else:
                            if server_go_to in server_list[start_server_from]['connections_list']:
                                for i in range(len(server_list[start_server_from]['connections_list'])):
                                    if server_list[start_server_from]['connections_list'][i] == server_go_to:
                                        to_go = i
                                time = server_list[start_server_from]['connect_time'][i][server_go_to]
                                print('Reply from', server_list[server_go_to]['ipaddress'], f'time = {time} ms')
                            elif server_list[server_go_to]['connections_list'] == []:
                                print(f'Error: Could not find a path to the server. {server_go_to}')
                            else:
                                ping(start_server_from, server_go_to, server_list)

                    else:
                        print('Error: Server you are trying to ping does not exist')
                else:
                    print('Error: You have not set the server yet')

        elif action in trace:
            if len(command.split(' ')) == 2:
                server_or_ip = command.split(' ')[1]
                keep_going = False
                go_more = False

                for i in server_list:
                    if server_list[i]['is_server'] == True:
                        start_server_from = i
                        keep_going = True
                if keep_going == True:
                    for j in server_list:
                        if j == server_or_ip:
                            server_go_to = j
                            go_more = True
                        else:
                            if server_list[j]['ipaddress'] == server_or_ip:
                                server_go_to = j
                                go_more = True
                    if go_more == True:
                        if start_server_from == server_go_to:
                            print('This is the starting server')
                        else:
                            if server_list[server_go_to]['connections_list'] == []:
                                print(f'Error: Could not find a path to the server. {server_go_to}')
                            else:
                                tracert(start_server_from, server_go_to, server_list)

                    else:
                        print('Error: Server you are trying to ping does not exist')
                else:
                    print('Error: You have not set the server yet')


        command = input('>>> ')

if __name__ == '__main__':
    run_the_internet()


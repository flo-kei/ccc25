
def validate(data):
    output = ''
    for idx, line in enumerate(data):
        time = 0
        position = 0

        for item in line:
            if item == '0':
                time += 1
            else:
                num = int(item)
                if num < 0:
                    position -= 1
                else:
                    position += 1
                time += abs(int(item))

            output += str(position) + ' ' + str(time) + '\n'

    return output


def print_grid(grid,grid_size,markerX, markerY):
    printstr = ''
    for x in range(grid_size):
        for y in range(grid_size):
            if markerX == x and markerY == y:
                printstr += 'X '
            else:
                printstr += (str(grid[x][y]) + ' ')
        printstr += '\n'

    print(printstr)


def run_dimension(line,total_steps,polarity,asteroid_coord):
    output = ''

    output += '0 '

    current_speed = 5

    nums = [5, 5, 4, 3, 2, 1]

    for current_pos in range(total_steps):
        output += str(current_speed * polarity) + ' '

        #eval_pos = current_pos if current_pos != 0 else 1

        if total_steps - (current_pos) <= nums[current_speed]:
            current_speed += 1
        elif total_steps - (current_pos+1) <= nums[current_speed]:
            current_speed = current_speed
        else:
            current_speed -= 1

        current_speed = min(current_speed, 5)
        current_speed = max(current_speed, 1)

    output += '0\n'

    return output


def find_path(grid, do_x, start_x, start_y, goal_x, goal_y):
    reward = 99999
    path = []

    x = start_x
    y = start_y

    x_move = 1 if x < goal_x else -1
    y_move = 1 if y < goal_y else -1

    while x <= len(grid)-1 and x >= 0 and y <= len(grid[0])-1 and y >= 0:
        print_grid(grid,len(grid),x,y)

        if grid[x][y] == reward:
            return path

        if x == goal_x and do_x == True:
            find_path(grid,False,start_x,start_y,goal_x,goal_y)

        if y == goal_y and do_x == False:
            find_path(grid,True,start_x,start_y,goal_x,goal_y)

        if grid[x][y] == -reward:
            res = find_path(grid,not do_x,x-x_move,y,goal_x,goal_y)


        if do_x:
            x += x_move
        else:
            y += y_move

        path.append((x,y))


    return []


def process(data):
    output = ''

    for idx in range(0,len(data)-1,2):
        station = data[idx]
        asteroid = data[idx+1][0].split(',')
        asteroid_x = int(asteroid[0])
        asteroid_y = int(asteroid[1])

        spacestation_coords = station[0].split(',')
        spacestation_pos_x = int(spacestation_coords[0])
        spacestation_pos_y = int(spacestation_coords[1])
        timelimit = station[1]

        total_steps_x = abs(int(spacestation_pos_x))
        total_steps_y = abs(int(spacestation_pos_y))
        polarity_x = 1 if int(spacestation_pos_x) >= 0 else -1
        polarity_y = 1 if int(spacestation_pos_y) >= 0 else -1

        max_x = max(spacestation_pos_x,asteroid_x)+1
        max_y = max(spacestation_pos_y,asteroid_y)+1

        grid_size = max(max_x,max_y)

        grid = [[0 for x in range(grid_size)] for y in range(grid_size)] # [[0]*grid_size]*grid_size
        reward = 99999

        # tile costs:
        grid[spacestation_pos_x][spacestation_pos_y] = reward

        # place asteroid
        for x in range(max(0,asteroid_x-1),min(grid_size,asteroid_x+1)+1):
            for y in range(max(0,asteroid_y-1),min(grid_size,asteroid_y+1)+1):
                grid[x][y] = -reward


        print_grid(grid,grid_size,0,0)

        path = find_path(grid,False,0,0,int(spacestation_pos_x),int(spacestation_pos_y))

        for idx in range(0,len(path)-1):
            output += path[idx][0] + ',' + path[idx][1] + '\n'

        # output_x = run_dimension(station,total_steps_x,polarity_x,asteroid_x)
        # output_y = run_dimension(station,total_steps_y,polarity_y,asteroid_y)

        #output+=output_x+output_y+'\n'



    return output

# idx = 0

def do_sublvl(idx):
    lvl = '5'
    example = False
    # sublvl = str(i)



    prefix = 'level'+lvl+'/inputs/'
    filenames = ['level'+lvl+'_0_example.in','level'+lvl+'_1_small.in','level'+lvl+'_2_large.in']

    # filestr = 'level'+lvl+'/inputs/level'+lvl+'_'
    # filestr += sublvl+'_'
    # if example:
    #     filestr+='example'
    #
    # filestr += '.in'

    f = open(prefix+filenames[idx] ,'r',encoding='utf8')

    data = f.readlines()

    data = data[1:]

    for idx,line in enumerate(data):
        data[idx] = str.split(str.replace(line,'\n',''),' ') 

    # print(data)

    output = process(data)


    outputfilename = 'level'+lvl+'/outputs/level'+lvl+'_'
    outputfilename += str(idx) + '_'
    if example:
        outputfilename+='example'

    outputfilename += '.out'

    outputfile = open(outputfilename,'w+',encoding='utf8')
    outputfile.write(output)

#do_sublvl(idx)

for i in range(0,3):
    print('Run '+str(i))
    do_sublvl(i)
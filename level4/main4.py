
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


def run_dimension(line,total_steps,polarity):
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


def process(data):
    output = ''

    for idx,line in enumerate(data):
        spacestation_coords = line[0].split(',')
        spacestation_pos_x = spacestation_coords[0]
        spacestation_pos_y = spacestation_coords[1]
        timelimit = line[1]

        total_steps_x = abs(int(spacestation_pos_x))
        total_steps_y = abs(int(spacestation_pos_y))
        polarity_x = 1 if int(spacestation_pos_x) >= 0 else -1
        polarity_y = 1 if int(spacestation_pos_y) >= 0 else -1

        output_x = run_dimension(line,total_steps_x,polarity_x)
        output_y = run_dimension(line,total_steps_y,polarity_y)

        output+=output_x+output_y+'\n'



    return output

# idx = 0

def do_sublvl(idx):
    lvl = '4'
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

def process(data):
    output = ''
    for idx,line in enumerate(data):
        #position = 0
        #time = len(line)
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


        output += str(position)+' '+str(time)+'\n'



    return output

idx = 2

def do_sublvl(idx):
    lvl = '2'
    example = False
    # sublvl = str(i)



    prefix = 'level'+lvl+'/inputs/'
    filenames = ['level2_0_example.in','level2_1_small.in','level2_2_large.in']

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

do_sublvl(idx)

# for i in range(1,6):
#     do_sublvl(i)
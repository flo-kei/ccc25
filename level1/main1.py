
def process(data):
    output = ''
    for idx,line in enumerate(data):
        linesum = 0
        for item in line:
            linesum += int(item)

        output += str(linesum)+'\n'

        # x = int(line[0])
        # y = int(line[1])

        # res = (x // 3) * y
        # output += str(res) + '\n'

    return output

idx = 2

def do_sublvl(idx):
    lvl = '1'
    example = False
    # sublvl = str(i)



    prefix = 'level1/inputs/'
    filenames = ['level1_0_example.in','level1_1_small.in','level1_2_large.in']

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
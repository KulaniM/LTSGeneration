from builtins import print, property
from transitions import State
from transitions.extensions import GraphMachine as Machine
import graphviz
import re

# LIFX system
#PIL0 = []
PIL1 = ['1','SD, *, wifi0', 'msg=(LifxWiFiBeacon,SSID,BSSID)', 'ACSeq=<(SD,send,{msg}),(CP,receive, {msg})>', 'ch=wifi0', 'rLC=-', 'BR={1}']
PIL2 = ['2', 'CP, SD, wifi0', 'msg=(SSID,OpenSystemAuthenticationRequest)', 'ACSeq =<(CP,send,{msg}),(SD,receive, {msg})>', 'ch=wifi0', 'rLC=-', 'BR={-}']
PIL3 = ['3', 'SD,CP,wifi0', 'msg=(AssociationResponse)', 'ACSeq =<(SD,send,{msg}),(CP,receive, {msg})>', 'ch=wifi0', 'rLC=-', 'BR={-}']
PIL4 = ['4','CP,SD,openwifi','msg=(GetService)', 'ACSeq=<(CP,send,{msg}),(SD,receive,{msg})>', 'ch=openwifi', 'rLC=-', 'BR={-}']
PIL5 = ['5', 'SD,CP,openwifi', 'msg=(StateService}', 'ACSeq=<(SD,send,{msg}),(CP,receive,{msg})>', 'ch=openwifi', 'rLC=-', 'BR={4,8,10,12,14}']
PIL6 = ['6', 'CP,SD,openwifi', 'msg=(Station,Username,Password)', 'ACSeq=<(CP,send,{msg}),(SD,receive, {msg})>','ch=openwifi', 'rLC=-', 'BR={-}']
PIL7 = ['7', 'SD,CP,openwifi', 'msg=(Station,Username,EncodedPassword)', 'ACSeq =<(SD,send,{msg}),(CP,receive,{msg})>' , 'ch=openwifi', 'rLC=-', 'BR={8}']
PIL8 = ['8', 'CP,SD,wifi', 'msg=(GetService)', 'ACSeq=<(CP,send,{msg}),(SD,receive,{msg})>', 'ch=wifi', 'rLC=-', 'BR={-}' ]
PIL9 = ['9','SD,CP,wifi','msg=(StateService,Configured)', 'ACSeq=<(SD,send,{msg}),(CP,receive, {msg})>', 'ch=wifi', 'rLC=-', 'BR={8,16,18,20}']
PIL10 = ['10', 'CP,SD,openwifi', 'msg=(SetPowerRequest)', 'ACSeq =<(CP,send,{msg}), (SD,receive,{msg}), (SD, executeCommand, {msg})>',  'ch=openwifi','rLC=-', 'BR={-}']
PIL11 = ['11','SD,CP,openwifi', 'msg=(Success)', 'ACSeq =<(SD, send,{msg}),(CP,receive,{msg})>', 'ch=openwifi', 'rLC=-', 'BR={10}']
PIL12 = ['12', 'CP,SD,openwifi', 'msg=(SetColorRequest)', 'ACSeq =<(CP,send,{msg}),(SD,receive,{msg}), (SD, executeCommand, {msg})>','ch=openwifi',  'rLC=-', 'R={-}']
PIL13 = ['13', 'SD,CP,openwifi', 'msg=(Success)', 'ACSeq =<(SD, send,{msg}),(CP,receive,{msg})>', 'ch=openwifi', 'rLC=-', 'BR={12}']
PIL14 = ['14', 'CP,SD,openwifi', 'msg=(GetLights)', 'ACSeq =<(CP, send,{msg}),(SD,receive,{msg})>', 'ch=openwifi', 'rLC=-', 'BR={-}']
PIL15 = ['15', 'SD,CP,openwifi', 'msg=(LightsState)', 'ACSeq =<(SD, send,{msg}),(CP,receive,{msg})>', 'ch=openwifi', 'rLC=-', 'BR={14}']
PIL16 = ['16', 'CP,SD,wifi', 'msg=(SetPowerRequest)', 'ACSeq =<(CP,send,{msg}),(SD,receive,{msg}),(SD, executeCommand, {msg})>', 'ch=wifi', 'rLC=-', 'BR={-}']
PIL17 = ['17', 'SD,CP,wifi', 'msg=(Success)', 'ACSeq =<(SD, send,{msg}),(CP,receive,{msg})>', 'ch=wifi', 'rLC=-', 'BR={16}']
PIL18 = ['18', 'CP,SD,wifi', 'msg=(SetColorRequest)', 'ACSeq =<(CP,send,{msg}),(SD,receive,{msg}),(SD, executeCommand, {msg})>', 'ch=wifi', 'rLC=-', 'BR={-}']
PIL19 = ['19', 'SD,CP,wifi', 'msg=(Success)', 'ACSeq =<(SD, send,{msg}),(CP,receive,{msg})>', 'ch=wifi', 'rLC=-', 'BR={18}']
PIL20 = ['20', 'CP,SD,wifi', 'msg=(GetLights)', 'ACSeq =<(CP, send,{msg}),(SD,receive,{msg})>', 'ch=wifi', 'rLC=-', 'BR={-}']
PIL21 = ['21', 'SD,CP,wifi', 'msg=(LightsState)', 'ACSeq =<(SD, send,{msg}),(CP,receive,{msg})>', 'ch=wifi', 'rLC=-', 'BR={20 }']


PIL  = [PIL1, PIL2, PIL3, PIL4, PIL5,PIL6,PIL7, PIL8,PIL9,PIL10,PIL11,PIL12,PIL13,PIL14,PIL15,PIL16,PIL17,PIL18,PIL19,PIL20,PIL21]

PIL_size = 21

#LTS0
class SD(object):
    pass

#LTS1
class CP(object):
    pass

sd = None
cp = None

# list of participants in the smart home system
participants = ['SD', 'CP']

# track source for transactions which are branches
branch_source = {}

# track destination for branches joining existing transactions
branch_dest = {}
branch_small_label= {}

# track the message content to use existing state as destination ex. success all joins together

# state machines
sd = SD()  # initialize the SD model
sdMachine1 = Machine(sd)
cp = CP()  # initialize the SD model
cpMachine1 = Machine(cp)
smachines = {'SD':[sdMachine1, 'a', 0], 'CP': [cpMachine1, 'b', 0]} # p, machine, label, counter

source = {}
dest = {}

#initialize the state diagram for each participant
for p in participants:
    source[p] = smachines[p][1] + str(smachines[p][2])
    smachines[p][0].add_states(State(source[p]))
    dest[p] = 'null'

# track the source state of a branch each participant
branch_source_values = []
branch_source_values2 = []
branch_dest_values = []
branch_dest_values2 = []
branch_label_values = []
branch_label_values2 = []
i = 0
while i <= PIL_size:
    branch_source_values.append('')
    branch_source_values2.append('')
    branch_dest_values.append('')
    branch_dest_values2.append('')
    branch_label_values.append('')
    branch_label_values2.append('')
    i+= 1

#for p in participants:
branch_source['SD'] =  branch_source_values
branch_source['CP'] =  branch_source_values2
branch_dest['SD'] = branch_dest_values
branch_dest['CP'] = branch_dest_values2
branch_small_label['SD'] = branch_label_values
branch_small_label['CP'] = branch_label_values2
# for p in participants:
#     branch_dest[p] =  []


cn = 0
q = 1 # PIL start from 1
for pil in PIL:
    id = pil[0]
    src = pil[1]
    msg = pil[2]
    acseq = pil[3]
    ch = pil[4]
    rlc = pil[5]
    br = pil[6]

    #create local action labels (line 6)
    if '-' in rlc:
        print('no local actions !')
    else:
        print('generating local actions ...')


    #generate a unique name for channel (line 7)
    cn += 1
    unq_channel_name = ch.split('=')[1] + str(cn)
    print(unq_channel_name)

    # Process Strings in ACSeq .............
    # prepare action sequence
    seq = acseq.split('=')
    seq = seq[1].replace('<','').replace('>','').replace('(','').replace(')','')
    splitseq = seq.split(',')
    checker = 0
    p = None
    a = None
    m = None
    acsequence = []
    for val in splitseq:#['SD', 'send', '{msg}', 'CP', 'receive', ' {msg}']
        # identify participant, action and msg
        checker += 1
        if checker % 3 == 0:
            m = val.replace('{','').replace('}','').strip()#'msg here'
            # add seq
            sq = (p,a,m)
            acsequence.append(sq)
            # reset
            checker = 0
            p = None
            a = None
            m = None
        elif checker % 2 == 0:
            a = val#'action'
        else:
            p = val#'participant'

    print(acsequence)#[('SD', 'send', 'msg'), ('CP', 'receive', 'msg')]

    # process actions (line 8)
    for ac in acsequence:
        print(ac)
        current_participant = ac[0].strip()
        action = ac[1].strip()
        message = ac[2].strip()

        if message == 'msg':
            message = msg.split('=')[1]

        # label (line 9)
        if action == 'send' or action == 'receive':
            if action == 'send':
                label = action + '(' + unq_channel_name + ',' + message + ')'
            elif action == 'receive':
                label = action + '(' + unq_channel_name + ',' + message + ')'

            # set source if exist (line 11)
            for p in participants:
                if current_participant == p:
                    source_list = branch_source[p]
                    if source_list[q]:
                        source[p] = source_list[q]
        else:
            label = action + message
        print(label)

        # destination (line 10)
        for p in participants:
            if current_participant == p:
                counter = smachines[p][2] + 1
                smachines[p][2] = counter
                dest[current_participant] = smachines[p][1] + str(smachines[p][2])


        # # add tranistions (lines 12-13)
        for p in participants:
            if current_participant == p:
                smachines[p][0].add_transition(label, source=source[current_participant], dest=dest[current_participant])
                source[p] = dest[p]
                if action == 'send' or action == 'receive':
                    branch_dest[current_participant][q] = dest[current_participant]
                    branch_small_label[current_participant][q] = label

        # if branches exist (line 15)
        if '-' not in br:
            print('branches !!!')
            brList = br.split('=')[1].replace('{', '').replace('}', '').strip().split(',')
            for b in brList:
                brValue = int(b)
                print(brValue)
                print(q)
                if q < brValue:
                    print('branch larger')
                    branch_source[current_participant][brValue] = dest[current_participant]
                    print(branch_source)


                elif q == brValue:
                    print('branch equal')
                    # add self recursions
                    for p in participants:
                        if current_participant == p:
                            smachines[p][0].add_transition(label, source=dest[current_participant], dest=dest[current_participant])

                elif q > brValue:
                    print('branch smaller')
                    if action == 'send' or action == 'receive':  ###
                        for p in participants:
                            if current_participant == p:
                                # dest
                                dest_list = branch_dest[p]
                                existingDestSD = dest_list[brValue]
                                # label
                                label_list = branch_small_label[p]
                                exLabel = label_list[brValue]
                                print(label)
                                print('SD: ' + dest[current_participant] + ', ' + existingDestSD)
                                for p in participants:
                                    if current_participant == p:
                                        smachines[p][0].add_transition(exLabel, source=dest[current_participant],
                                                                       dest=existingDestSD)


    print(branch_source)
    print(branch_dest)
    q += 1


# machine.add_transition('melt', source= , dest='liquid')
#
for p in participants:
    smachines[p][0].get_graph().draw('Gen_'+p+'.png', prog='dot')
    #/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
    # print full digraph
    print(smachines[p][0].get_combined_graph())
    # use graphviz library to get edges
    digraph = graphviz.Digraph()
    digraph = smachines[p][0].get_combined_graph()
    digraph_string = digraph.string()

    labels = re.findall("\[label=.*", digraph_string)
    edges = re.findall("[a-z][0-9][0-9] +->.[a-z][0-9][0-9]|[a-z][0-9] +->.[a-z][0-9]", digraph_string)

    c = 0
    for label in labels:
        label_value = re.findall('"[^"]*"',label)
        edge = edges[c]
        label_v =  label_value[0].replace('"','')
        print(edge)
        print(label_v)
        if 'send' in label_v:
            symbol = '!'
            label_v = label_v.replace('send', '')
        elif 'receive' in label_v:
            symbol = '?'
            label_v = label_v.replace('receive', '')

        label_value = re.findall('([^"]*)', label_v)
        print(label_value)

        #get channel



        c += 1





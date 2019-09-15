from builtins import print
from distutils.command.check import check

from transitions import State
from transitions.extensions import GraphMachine as Machine

#TODO
# Philips Hue system
#PIL0 = []
PIL1 = ['1','SD, ZFE, zigbee', 'msg=(BeaconRequest)', 'ACSeq=<(SD,send,{msg}),(ZFE,receive, {msg})>', 'ch=zigbee', 'rLC=-', 'BR={1,4}']
PIL2 = ['2', 'ZFE, SD, zigbee', 'msg=(PanID,HubID,AssoPermit)', 'ACSeq =<(ZFE,send,{msg}),(SD,receive, {msg})>', 'ch=zigbee', 'rLC=-', 'BR={2}']
PIL3 = ['3', 'SD,ZFE,zigbee', 'msg=(PanID,DeviceID)', 'ACSeq =<(SD,send,{msg}),(ZFE,receive, {msg})>', 'ch=zigbee', 'rLC=-', 'BR={12}']#12
PIL4 = ['4','ZFE,SD,zigbee','msg=(BeaconRequest)', 'ACSeq=<(ZFE,send,{msg}), (SD,receive, {msg})>', 'ch=zigbee', 'rLC=-', 'BR={-}']
PIL5 = ['5', 'SD,ZFE,zigbee', 'msg=(PanID,DeviceID,AssoPermit)', 'ACSeq=<(SD,send,{msg}),(ZFE,receive,{msg})>', 'ch=zigbee', 'rLC=-', 'BR={19}']#19
PIL6 = ['6', 'CP,HS,wifi', 'msg=(UPnPMsearchRequest)', 'ACSeq=<(CP,send,{msg}),(HS,receive,{msg})>', 'ch=wifi', 'rLC=-', 'BR={6}' ]
PIL7 = ['7','HS,CP,wifi','msg=(CPIP,ServName,HubIP,HubID)', 'ACSeq=<(HS,send,{msg}),(CP,receive, {msg})>', 'ch=wifi', 'rLC=-', 'BR={-}']
PIL8 = ['8', 'CP,HS,wifi', 'msg=(HubIP,x)', 'ACSeq=<(CP,newnonce,{x}),(CP,send,{msg}),(HS,receive, {msg})>','ch=wifi', 'rLC=-', 'BR={-}']
PIL9 = ['9', 'HS,CP,wifi', 'msg=(CPIP, hash(x))', 'ACSeq =<(HS,executeCommand,{LinkBTrue}),(HS,send,{msg}),(HS,executeCommand,{LinkBFalse}),(CP,receive,{msg})>' , 'ch=wifi', 'rLC=-', 'BR={10,17,24,26}']
PIL10 = ['10', 'CP,HS,wifi', 'msg=(HubIP,hash(x),SearchLightRequest)', 'ACSeq =<(CP,send,{msg}), (HS,receive,{msg})>',  'ch=wifi','rLC={ZFE}', 'BR={-}']
PIL11 = ['11','HS,CP,wifi', 'msg=(CPIP,RequestSuccess)', 'ACSeq =<(HS, send,{msg}),(CP,receive,{msg})>', 'ch=wifi', 'rLC=-', 'BR={10}']
PIL12 = ['12', 'ZFE,SD,zigbee', 'msg=(ScanRequest, PanID)', 'ACSeq =<(ZFE,send,{msg}),(SD,receive,{msg})>','ch=zigbee',  'rLC=-', 'R={-}']
PIL13 = ['13', 'SD,ZFE,zigbee', 'msg=(HubID,PanID,ScanResponse)', 'ACSeq =<(SD, send,{msg}),(ZFE,receive,{msg})>', 'ch=zigbee', 'rLC=-', 'BR={-}']
PIL14 = ['14', 'ZFE,SD,zigbee', 'msg=(DeviceID,IdentifyRequest)', 'ACSeq =<(ZFE, send,{msg}),(SD,receive,{msg}),(SD,executeCommand,{IdentifyRequest})>', 'ch=zigbee', 'rLC=-', 'BR={-}']
PIL15 = ['15', 'ZFE,SD,zigbee', 'msg=(DeviceID,PanID,NetworkJoinRequest)', 'ACSeq =<(ZFE, send,{msg}),(SD,receive,{msg})>', 'ch=zigbee', 'rLC=-', 'BR={-}']
PIL16 = ['16', 'SD,ZFE,zigbee', 'msg=(HubID,PanID,NetworkJoinResponse)', 'ACSeq =<(SD,send,{msg}),(ZFE,receive,{msg})>', 'ch=zigbee', 'rLC=-', 'BR={36}']
PIL17 = ['17', 'CP,HS,wifi', 'msg=(HubIP,hash(x),JoinNearestDeviceRequest)', 'ACSeq =<(CP, send,{msg}),(HS,receive,{msg})>', 'ch=wifi', 'rLC={ZFE}', 'BR={19}']
PIL18 = ['18', 'HS,CP,wifi', 'msg=(CPIP,Success)', 'ACSeq =<(HS,send,{msg}),(CP,receive,{msg})>', 'ch=wifi', 'rLC=-', 'BR={17}']
PIL19 = ['19', 'ZFE,SD,zigbee', 'msg=(LinkScanRequest,PanID)', 'ACSeq =<(ZFE, send,{msg}),(SD,receive,{msg})>', 'ch=zigbee', 'rLC=-', 'BR={-}']
PIL20 = ['20', 'SD, ZFE,zigbee', 'msg=(HubID,PandID,LinkScanReqeust)', 'ACSeq =<(SD, send,{msg}),(ZFE,receive,{msg})>', 'ch=zigbee', 'rLC=-', 'BR={-}']
PIL21 = ['21', 'ZFE, SD,zigbee', 'msg=(DeviceID,LinkIdentifyRequest)', 'ACSeq =<(ZFE, send,{msg}),(SD,receive,{msg}),(SD,executeCommand,{LinkIdentifyRequest})>', 'ch=zigbee', 'rLC=-', 'BR={-}']
PIL22 = ['22', 'ZFE, SD,zigbee', 'msg=(DeviceID,PanID,LinkNetworkJoinRequest)', 'ACSeq =<(ZFE,send,{msg}),(SD,receive,{msg})>', 'ch=zigbee', 'rLC=-', 'BR={-}']
PIL23 = ['23', 'SD, ZFE,zigbee', 'msg=(HubID,PandID,LinkNetworkJoinResponse)', 'ACSeq =<(SD, send,{msg}),(ZFE,receive,{msg})>', 'ch=zigbee', 'rLC=-', 'BR={39}']
PIL24 = ['24', 'CP,HS,wifi', 'msg=(HubIP,hash(x),RequestLightResult)', 'ACSeq =<(CP, send,{msg}),(HS,receive,{msg})>', 'ch=wifi', 'rLC=-', 'BR={-}']
PIL25 = ['25', 'HS, CP,wifi', 'msg=(CPIP,LightNo,LightName)', 'ACSeq =<(HS,send, {msg}),(CP,receive,{msg})>', 'ch=wifi', 'rLC=-', 'BR={24,34']
PIL26 = ['26', 'CP, HS,wifi', 'msg=(HubIP,hash(x),GetInfoRequest)', 'ACSeq =<(CP, send,{msg}),(HS,receive,{msg})>', 'ch=wifi', 'rLC=-', 'BR={-}']
PIL27 = ['27', 'HS, CP,wifi', 'msg=(CPIP,Configs,Lights,Whitelist)', 'ACSeq =<(HS, send,{msg}),(CP,receive,{msg}))>', 'ch=wifi', 'rLC=-', 'BR={26,28,30,32}']
PIL28 = ['28', 'CP, HS,wifi', 'msg=(HubIP,hash(x),DeleteLightRequest)', 'ACSeq =<(CP,send,{msg}),(HS,receive,{msg})>', 'ch=wifi', 'rLC=-', 'BR={-}']
PIL29 = ['29', 'HS, CP,wifi', 'msg=(CPIP,AdminSuccess)', 'ACSeq =<(HS,send,{msg}),(CP,receive, {msg}))>', 'ch=wifi', 'rLC=-', 'BR={28}']
PIL30 = ['30', 'CP, HS,wifi', 'msg=(HubIP,hash(x),DeleteUserIDRequest)', 'ACSeq =<(CP,send,{msg}),(HS,receive,{msg})>', 'ch=wifi', 'rLC=-', 'BR={-}']
PIL31 = ['31', 'HS, CP,wifi', 'msg=(CPIP,AdminSuccess)', 'ACSeq =<(HS,send,{msg}),(CP,receive, {msg}))>', 'ch=wifi', 'rLC=-', 'BR={30}']
PIL32 = ['32', 'CP, HS,wifi', 'msg=(HubIP,hash(x),LinkButtonTrue)', 'ACSeq =<(CP,send,{msg}),(HS,receive,{msg}),(HS,executeCommand,{LinkButtonTrue})>', 'ch=wifi', 'rLC=-', 'BR={-}']
PIL33 = ['33', 'HS, CP,wifi', 'msg=(CPIP,AdminSuccess)', 'ACSeq =<(HS,send,{msg}),(CP,receive, {msg}))>', 'ch=wifi', 'rLC=-', 'BR={32}']
PIL34 = ['34', 'CP, HS,wifi', 'msg=(HubIP,hash(x),Controlcmd)', 'ACSeq =<(CP,send,{msg}),(HS,receive,{msg})>', 'ch=wifi', 'rLC={ZFE}', 'BR={-}']
PIL35 = ['35','HS,CP,wifi', 'msg=(CPIP,RequestSuccess)', 'ACSeq =<(HS, send,{msg}),(CP,receive,{msg})>', 'ch=wifi', 'rLC=-', 'BR={34,38,41}']
PIL36 = ['36', 'ZFE,SD,zigbee', 'msg=(DeviceID,PanID,EncryptedControlcmd)', 'ACSeq =<(ZFE, send,{msg}),(SD,receive,{msg}),(SD,executeCommand,{EncryptedControlcmd})>', 'ch=zigbee', 'rLC=-', 'BR={-}']
PIL37 = ['37', 'SD,ZFE,zigbee', 'msg=(HubID,ACK)', 'ACSeq =<(SD,send,{msg}),(ZFE,receive,{msg})>', 'ch=zigbee', 'rLC={HS}', 'BR={36}']
PIL38 = ['38', 'HS, CP,wifi', 'msg=(CPIP,ControlcmdSuccess)', 'ACSeq =<(HS,send,{msg}),(CP,receive, {msg}))>', 'ch=wifi', 'rLC=-', 'BR={34}']
PIL39 = ['39', 'ZFE,SD,zigbee', 'msg=(DeviceID,PanID,EncryptedControlcmd)', 'ACSeq =<(ZFE, send,{msg}),(SD,receive,{msg}),(SD,executeCommand,{EncryptedControlcmd})>', 'ch=zigbee', 'rLC=-', 'BR={-}']
PIL40 = ['40', 'SD,ZFE,zigbee', 'msg=(HubID,ACK)', 'ACSeq =<(SD,send,{msg}),(ZFE,receive,{msg})>', 'ch=zigbee', 'rLC={HS}', 'BR={39}']
PIL41 = ['41', 'HS, CP,wifi', 'msg=(CPIP,ControlcmdSuccess)', 'ACSeq =<(HS,send,{msg}),(CP,receive, {msg}))>', 'ch=wifi', 'rLC=-', 'BR={34}']

#TODO
PIL  = [PIL1, PIL2, PIL3, PIL4, PIL5,PIL6,PIL7, PIL8,PIL9,PIL10,PIL11,PIL12,PIL13,PIL14,PIL15,PIL16,PIL17,PIL18,PIL19,PIL20,PIL21,PIL22,PIL23,PIL24,PIL25,PIL26,PIL27,PIL28,PIL29,PIL30,PIL31, PIL32, PIL33, PIL34, PIL35,PIL36,PIL37,PIL38,PIL39,PIL40,PIL41]
#set tge size the PIL list
PIL_size = 41

#TODO

# LTS0
class SD(object):
    pass


# LTS1
class CP(object):
    pass

# LTS2
class HS(object):
    pass

# LTS4
class ZFE(object):
    pass


sd = None
cp = None
#TODO
# list of participants in the smart home system
participants = ['CP', 'HS', 'ZFE','SD']

# track source for transactions which are branches
branch_source = {}

# track destination for branches joining existing transactions
branch_dest = {}
branch_small_label = {}

# track the message content to use existing state as destination ex. success all joins together

#TODO
# state machines
sd = SD()  # initialize the SD model
sdMachine1 = Machine(sd)
cp = CP()  # initialize the CP model
cpMachine1 = Machine(cp)
gs = HS()  # initialize the HS model
gsMachine1 = Machine(gs)
zf = ZFE()  # initialize the ZFE model
zfMachine1 = Machine(zf)
#TODO
smachines = {'SD': [sdMachine1, 'c', 0], 'CP': [cpMachine1, 'a', 0], 'HS': [gsMachine1, 'b', 0], 'ZFE': [zfMachine1, 'd', 0]}  # p, machine, label, counter

source = {}
dest = {}

# initialize the state diagram for each participant
for p in participants:
    source[p] = smachines[p][1] + str(smachines[p][2])
    smachines[p][0].add_states(State(source[p]))
    dest[p] = 'null'

#TODO
# track the source state of a branch each participant
branch_source_values = []
branch_source_values2 = []
branch_source_values3 = []
branch_source_values4 = []
branch_dest_values = []
branch_dest_values2 = []
branch_dest_values3 = []
branch_dest_values4 = []
branch_label_values = []
branch_label_values2 = []
branch_label_values3 = []
branch_label_values4 = []
i = 0
while i <= PIL_size:
    branch_source_values.append('')
    branch_source_values2.append('')
    branch_source_values3.append('')
    branch_source_values4.append('')
    branch_dest_values.append('')
    branch_dest_values2.append('')
    branch_dest_values3.append('')
    branch_dest_values4.append('')
    branch_label_values.append('')
    branch_label_values2.append('')
    branch_label_values3.append('')
    branch_label_values4.append('')
    i += 1
#TODO
# for p in participants:
branch_source['CP'] = branch_source_values
branch_source['HS'] = branch_source_values2
branch_source['ZFE'] = branch_source_values3
branch_source['SD'] = branch_source_values4
#TODO
# for p in participants:
#     branch_dest[p] = []
branch_dest['CP'] = branch_dest_values
branch_dest['HS'] = branch_dest_values2
branch_dest['ZFE'] = branch_dest_values3
branch_dest['SD'] = branch_dest_values4
#TODO
branch_small_label['CP'] = branch_label_values
branch_small_label['HS'] = branch_label_values2
branch_small_label['ZFE'] = branch_label_values3
branch_small_label['SD'] = branch_label_values4
#////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
cn = 0
q = 1  # PIL start from 1
for pil in PIL:
    id = pil[0]
    src = pil[1]
    msg = pil[2]
    acseq = pil[3]
    ch = pil[4]
    rlc = pil[5]
    br = pil[6]

    # create local action labels (line 6)
    if '-' in rlc:
        print('no local actions !')
    else:
        print('generating local actions ...')

    # generate a unique name for channel (line 7)
    cn += 1
    unq_channel_name = ch.split('=')[1] + str(cn)
    print(unq_channel_name)

    #define private channel
    unq_priv_channel_name = ''

    # Process Strings in ACSeq .............
    # prepare action sequence
    seq = acseq.split('=')
    seq = seq[1].replace('<', '').replace('>', '').replace('(', '').replace(')', '')
    splitseq = seq.split(',')
    checker = 0
    p = None
    a = None
    m = None
    acsequence = []
    for val in splitseq:  # ['SD', 'send', '{msg}', 'CP', 'receive', ' {msg}']
        # identify participant, action and msg
        checker += 1
        if checker % 3 == 0:
            m = val.replace('{', '').replace('}', '').strip()  # 'msg here'
            # add seq
            sq = (p, a, m)
            acsequence.append(sq)
            # reset
            checker = 0
            p = None
            a = None
            m = None
        elif checker % 2 == 0:
            a = val  # 'action'
        else:
            p = val  # 'participant'

    print(acsequence)  # [('SD', 'send', 'msg'), ('CP', 'receive', 'msg')]

    #update ACSeq to include local communication
    # extract participant from rlc
    if not rlc.__contains__('-'):
        rlc_p=rlc.split('=')[1].replace('{', '').replace('}', '').strip()
        print('local communication receiver: ' + rlc_p)
        if rlc_p:
            unq_priv_channel_name = 'priv' + str(cn)
            message = msg.split('=')[1]
            for ac in acsequence:
                if ac[1].strip().__eq__('receive'):
                    lc_s = (ac[0].strip(), 'sendPm', message)

            acsequence.append(lc_s)
            lc_r = (rlc_p, 'receivePm', message)
            acsequence.append(lc_r)


    # process actions (line 8)
    for ac in acsequence:
        print(ac)
        current_participant = ac[0].strip()
        action = ac[1].strip()
        message = ac[2].strip()

        if message == 'msg':
            message = msg.split('=')[1]

        # label (line 9)
        if action == 'sendPm' or action == 'receivePm':
            label = action + '(' + unq_priv_channel_name + ',' + message + ')'
            ## if local communication exists;
            # alter the branch source of the next transaction
            # and update the branch source of the local comm action
            for p in participants:
                if p.__eq__('ZFE'):
                    try:
                        nextTrSource = branch_source[p].__getitem__(q+ 2)
                        if nextTrSource:
                            letter = list(nextTrSource)[0]
                            index = int(nextTrSource.replace(letter, ''))
                            # update
                            branch_source[p][q] = nextTrSource
                            # branch_source[current_participant][int(trid) + 2] = letter + str(index + 1)
                            if branch_source[p][q]:
                                source[p] = branch_source[p][q]
                    except IndexError:
                        print("index not exist")




        elif action == 'send' or action == 'receive':
            label = action + '(' + unq_channel_name + ',' + message + ')'
            # set source if exist (line 11)
            for p in participants:
                if current_participant == p:
                    source_list = branch_source[p]
                    if source_list[q]:
                        source[p] = source_list[q]
        else:
            label = action +'(' +  message + ')'
        print(label)

        # destination (line 10)
        for p in participants:
            if current_participant == p:
                counter = smachines[p][2] + 1
                smachines[p][2] = counter
                dest[current_participant] = smachines[p][1] + str(smachines[p][2])
                if action == 'sendPm' or action == 'receivePm':
                    ## if local communication exists;
                    # change the source of the next action, as the detination of the private action
                    for p in participants:
                        if p.__eq__('ZFE'):
                                try:
                                    branch_source[current_participant][q + 2] = dest[current_participant]
                                except IndexError:
                                    print("index not exist")

        # # add tranistions (lines 12-13)
        for p in participants:
            if current_participant == p:
                smachines[p][0].add_transition(label, source=source[current_participant],
                                               dest=dest[current_participant])
                source[p] = dest[p]
                #edited to support PIL6 and PIL7 type of branches
                if action == 'send' or action == 'receive': # or action=='executeCommand' or action=='verify':
                    branch_dest[current_participant][q] = dest[current_participant]
                if action == 'send' or action == 'receive':
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
                    print('branch larger ' + b)
                    print('current participant ' + current_participant)
                    #check the branch source at transaction branch is already set
                    # check_state = branch_source[current_participant][brValue]
                    # if check_state and check_state != dest[current_participant]:
                    #     print('has set already: ' +check_state + 'cdest: ' +dest[current_participant])
                    branch_source[current_participant][brValue] = dest[current_participant]
                    print(branch_source)


                elif q == brValue:
                    print('branch equal')
                    # add self recursions
                    for p in participants:
                        if current_participant == p:
                            smachines[p][0].add_transition(label, source=dest[current_participant],
                                                           dest=dest[current_participant])

                elif q > brValue:
                    print('branch smaller')
                    if action == 'send' or action == 'receive': ###
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
    smachines[p][0].get_graph().draw('Gen_PhilipsHue_' + p + '.png', prog='dot')


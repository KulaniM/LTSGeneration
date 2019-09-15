from builtins import print
from transitions import State
from transitions.extensions import GraphMachine as Machine

#TODO
# Chromecast system
#PIL0 = []
PIL1 = ['1','SD, CP, wifi0', 'msg=(ChromecastWiFiBeacon,SSID,BSSID)', 'ACSeq=<(SD,send,{msg}),(CP,receive, {msg})>', 'ch=wifi0', 'rLC=-', 'BR={1}']
PIL2 = ['2', 'CP, SD, wifi0', 'msg=(SSID, OpenSystemAuthenticationRequest)', 'ACSeq =<(CP,send,{msg}),(SD,receive, {msg})>', 'ch=wifi0', 'rLC=-', 'BR={-}']
PIL3 = ['3', 'SD,CP,wifi0', 'msg=(AssociationResponse)', 'ACSeq =<(SD,send,{msg}),(CP,receive, {msg})>', 'ch=wifi0', 'rLC=-', 'BR={6,8,10,12,16}']
PIL4 = ['4','CP,SD,openwifi','msg=(GetEurekaInfo,SignRParam,VersionRParam,NameRParam,SetupStateRParam,EthernetConnectedRParam,IPaddressRParam,SsdpUdnRParam,Model NameRParam,DeviceCapabilitiesRParam,SSIDSuffixRParam,TosAcceptedRP aram,PublicKeyRParam,BSSIDRParam,x)', 'ACSeq=<(CP,newnonce,{x}), (CP,send,{msg}), (SD,receive, {msg})>', 'ch=openwifi', 'rLC=-', 'BR={-}']
PIL5 = ['5', 'SD,CP,openwifi', 'msg=(Version,Name,SetupState,EthernetConnected,IPaddress,SsdpUdn,ModelName,DeviceCapabilities,SSIDSuffix,TosAccepted,BSSID,PublickKey,Certificate, IntermediateCerts,SignedData,x)', 'ACSeq=<(SD,send,{msg}),(CP,receive,{msg})>', 'ch=openwifi', 'rLC=-', 'BR={4}']
PIL6 = ['6', 'CP,SD,openwifi', 'msg=(PostScanWifi)', 'ACSeq=<(CP,send,{msg}),(SD,receive,{msg}),(SD, executeCommand, {msg})>', 'ch=openwifi', 'rLC=-', 'BR={-}' ]
PIL7 = ['7','SD,CP,openwifi','msg=(SuccessScanRequest)', 'ACSeq=<(SD,send,{msg}),(CP,receive, {msg})>', 'ch=wifi', 'rLC=-', 'BR={6}']
PIL8 = ['8', 'CP,SD,openwifi', 'msg=(GetScanResults)', 'ACSeq=<(CP,send,{msg}),(SD,receive, {msg})>','ch=openwifi', 'rLC=-', 'BR={-}']
PIL9 = ['9', 'SD,CP,openwifi', 'msg=(HomeWifiSSID,HomeWifiBSSID,Frequency,SignalLevel,WPAAuth7, WPACiper4)', 'ACSeq =<(SD,send,{msg}),(CP,receive,{msg})>' , 'ch=openwifi', 'rLC=-', 'BR={8}']
PIL10 = ['10', 'CP,SD,openwifi', 'msg=(PostConnectWifi,SSID,aenc(Password,PublicKey),WPAAuth7,WPACiper4)', 'ACSeq =<(CP,send,{msg}), (SD,receive,{msg})>',  'ch=openwifi','rLC=-', 'BR={-}']
PIL11 = ['11','SD,CP,openwifi', 'msg=(SuccessConnectRequest, adec(aenc(Password,PublicKey),PrivateKey), PrivateKey))', 'ACSeq =<(SD, send,{msg}),(CP,receive,{msg})>', 'ch=openwifi', 'rLC=-', 'BR={-}']
PIL12 = ['12', 'CP,SD,openwifi', 'msg=(GetEurekaInfo,IPaddressRParam,VersionRParam,SetupStateRParam)', 'ACSeq =<(CP,send,{msg}),(SD,receive,{msg})>','ch=openwifi',  'rLC=-', 'R={-}']
PIL13 = ['13', 'SD,CP,openwifi', 'msg=(NewIPAddress,Version,NewSetupState)', 'ACSeq =<(SD, send,{msg}),(CP,receive,{msg})>', 'ch=openwifi', 'rLC=-', 'BR={12}']
PIL14 = ['14', 'CP,SD,openwifi', 'msg=(PostSetEurekaInfo,NewName,OptInStatusTrue)', 'ACSeq =<(CP, send,{msg}),(SD,receive,{msg})>', 'ch=openwifi', 'rLC=-', 'BR={-}']
PIL15 = ['15', 'SD,CP,openwifi', 'msg=(SuccessSetRequest)', 'ACSeq =<(SD, send,{msg}),(CP,receive,{msg})>', 'ch=openwifi', 'rLC=-', 'BR={14}']
PIL16 = ['16', 'CP,SD,openwifi', 'msg=(PostSaveWifi,ImmediateTrue)', 'ACSeq =<(CP,send,{msg}),(SD,receive,{msg})>', 'ch=openwifi', 'rLC=-', 'BR={-}']
PIL17 = ['17', 'SD,CP,openwifi', 'msg=(SuccessSaveRequest)', 'ACSeq =<(SD, send,{msg}),(CP,receive,{msg})>', 'ch=openwifi', 'rLC=-', 'BR={16}']
PIL18 = ['18', 'CP,SD,wifi', 'msg=(MDNSDiscoveryRequest)', 'ACSeq =<(CP,send,{msg}),(SD,receive,{msg})>', 'ch=wifi', 'rLC=-', 'BR={18}']
PIL19 = ['19', 'SD,CP,wifi', 'msg=(MDNSDiscoveryResponse)', 'ACSeq =<(SD, send,{msg}),(CP,receive,{msg})>', 'ch=wifi', 'rLC=-', 'BR={-}']
PIL20 = ['20', 'SD, GS,wifi', 'msg=(ValidScreenID)', 'ACSeq =<(SD, send,{msg}),(GS,receive,{msg})>', 'ch=wifi', 'rLC=-', 'BR={-}']
PIL21 = ['21', 'CP, SD,wifi', 'msg=(GetMdxSessionStatus)', 'ACSeq =<(CP, send,{msg}),(SD,receive,{msg})>', 'ch=wifi', 'rLC=-', 'BR={-}']
PIL22 = ['22', 'SD, CP,wifi', 'msg=(ScreenID)', 'ACSeq =<(SD,send,{msg}),(CP,receive,{msg})>', 'ch=wifi', 'rLC=-', 'BR={-}']
PIL23 = ['23', 'CP, GS,wifi', 'msg=(GetLoungToken,ScreenID)', 'ACSeq =<(CP, send,{msg}),(GS,receive,{msg})>', 'ch=wifi', 'rLC=-', 'BR={- }']
PIL24 = ['24', 'GS,CP,wifi', 'msg=(association(ScreenID),Expiration,ScreenID)', 'ACSeq =<(GS, send,{msg}),(GS, executeCommand, {SaveMapScreenIDandAssoc}),(CP,receive,{msg}),(CP,receive,{msg})>', 'ch=wifi', 'rLC=-', 'BR={25,27}']
PIL25 = ['25', 'CP, GS,wifi', 'msg=(GetScreenAvailability,association(ScreenID))', 'ACSeq =<(CP,send, {msg}),(GS,receive,{msg}),(GS,verify,{msg}),(GS,executeCommand,{msg})>', 'ch=wifi', 'rLC=-', 'BR={-}']
PIL26 = ['26', 'GS, CP,wifi', 'msg=(AvailabilityResponse,association(ScreenID))', 'ACSeq =<(GS, send,{msg}),(CP,receive,{msg})>', 'ch=wifi', 'rLC=-', 'BR={25}']
PIL27 = ['27', 'CP, GS,wifi', 'msg=(PostBindRequest,association(ScreenID),Device,ID,ControlPointName, AppName,MethodSetPlayList,VideoID)', 'ACSeq =<(CP, send,{msg}),(GS,receive,{msg}),(GS,verify,{assoc(ScreenID),ValidScreenID})>', 'ch=wifi', 'rLC=-', 'BR={-}']
PIL28 = ['28', 'GS, CP,wifi', 'msg=(CurrentVideoID,SID,GsessionID,LoungStatus,PlaylistModified, OnAutoplayModeChanged,OnPlaylistModeChanged)', 'ACSeq =<(GS,executeCommand,{StreamVideoID}),(GS,send,{msg}),(CP,receive,{msg})>', 'ch=wifi', 'rLC=-', 'BR={27,29}']
PIL29 = ['29', 'CP, GS,wifi', 'msg=(PostBindRequest,association(ScreenID),Device,ID,ControlPointName, AppName,MethodSetPlayList)', 'ACSeq =<(CP,send,{msg}),(GS,receive, {msg}),(GS,verify(association(ScreenID),ValidScreenID)))>', 'ch=wifi', 'rLC=-', 'BR={- }']
PIL30 = ['30', 'GS, CP,wifi', 'msg=(CurrentVideoID,SID,GsessionID,LoungStatus,PlaylistModified, OnAutoplayModeChanged,OnPlaylistModeChanged)', 'ACSeq =<(GS,send,{msg}),(CP,receive,{msg})>', 'ch=wifi', 'rLC=-', 'BR={29}']


#TODO
PIL  = [PIL1, PIL2, PIL3, PIL4, PIL5,PIL6,PIL7, PIL8,PIL9,PIL10,PIL11,PIL12,PIL13,PIL14,PIL15,PIL16,PIL17,PIL18,PIL19,PIL20,PIL21,PIL22,PIL23,PIL24,PIL25,PIL26,PIL27,PIL28,PIL29,PIL30]
#TODO
#set tge size the PIL list
PIL_size = 30

#TODO

# LTS0
class SD(object):
    pass


# LTS1
class CP(object):
    pass

# LTS2
class GS(object):
    pass



sd = None
cp = None
#TODO
# list of participants in the smart home system
participants = ['SD', 'CP', 'GS']

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
cp = CP()  # initialize the SD model
cpMachine1 = Machine(cp)
gs = GS()  # initialize the SD model
gsMachine1 = Machine(gs)
smachines = {'SD': [sdMachine1, 'a', 0], 'CP': [cpMachine1, 'b', 0], 'GS': [gsMachine1, 'c', 0]}  # p, machine, label, counter

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
branch_dest_values = []
branch_dest_values2 = []
branch_dest_values3 = []
branch_label_values = []
branch_label_values2 = []
branch_label_values3 = []
i = 0
while i <= PIL_size:
    branch_source_values.append('')
    branch_source_values2.append('')
    branch_source_values3.append('')
    branch_dest_values.append('')
    branch_dest_values2.append('')
    branch_dest_values3.append('')
    branch_label_values.append('')
    branch_label_values2.append('')
    branch_label_values3.append('')
    i += 1
#TODO
# for p in participants:
branch_source['SD'] = branch_source_values
branch_source['CP'] = branch_source_values2
branch_source['GS'] = branch_source_values3
#TODO
# for p in participants:
#     branch_dest[p] = []
branch_dest['SD'] = branch_dest_values
branch_dest['CP'] = branch_dest_values2
branch_dest['GS'] = branch_dest_values3
#TODO
branch_small_label['SD'] = branch_label_values
branch_small_label['CP'] = branch_label_values2
branch_small_label['GS'] = branch_label_values3
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
                    print('branch larger')
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
    smachines[p][0].get_graph().draw('Gen_Chromecast_' + p + '.png', prog='dot')


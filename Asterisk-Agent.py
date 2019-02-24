import sys
form1='''{0},,{1},novm,0,,,,,,,,,,,default,{2},sip,SIP/{3},fixed,{4},{5},,yes,yes,yes,yes,disabled,10,,,,alaw,no,device <{6}>,no,from-internal,0.0.0.0/0.0.0.0,all,rfc2833,no,no,dynamic,no,{7}@device,10,10,no,0.0.0.0/0.0.0.0,5060,yes,60,1234ab,pai,accept,chan_sip,"udp,tcp,tls",yes,friend,inherit,,,ENABLED,hunt-prim,20,,{8},0,"ext-local,{9},dest",,,0,0,Ring,7,novm,default,,yes'''
head='''extension,password,name,voicemail,ringtimer,noanswer,recording,outboundcid,sipname,noanswer_cid,busy_cid,chanunavail_cid,noanswer_dest,busy_dest,chanunavail_dest,mohclass,id,tech,dial,devicetype,user,description,emergency_cid,recording_in_external,recording_out_external,recording_in_internal,recording_out_internal,recording_ondemand,recording_priority,answermode,intercom,accountcode,allow,avpf,callerid,canreinvite,context,deny,disallow,dtmfmode,encryption,force_avp,host,icesupport,mailbox,namedcallgroup,namedpickupgroup,nat,permit,port,qualify,qualifyfreq,secret,sendrpid,sessiontimers,sipdriver,transport,trustrpid,type,videosupport,callgroup,pickupgroup,callwaiting_enable,findmefollow_strategy,findmefollow_grptime,findmefollow_grppre,findmefollow_grplist,findmefollow_annmsg_id,findmefollow_postdest,findmefollow_dring,findmefollow_needsconf,findmefollow_remotealert_id,findmefollow_toolate_id,findmefollow_ringing,findmefollow_pre_ring,findmefollow_voicemail,findmefollow_changecid,findmefollow_fixedcid,findmefollow_enabled'''
start1 = 7666 #put your int to start
end1 = 7809 #put your int to start
length_ext = 30
if start1 > end1:
    sys.exit()
f = open("auto-agent.csv", 'w')
f.write(head)
f.write("\n")
for i in range((start1),(end1+1)):
    #sys.stdout.write(form1.format(i,i,i,i,i,i,i,i,i,i))
    f.write(form1.format(i, i, i, i, i, i, i, i, i, i))
    f.write("\n")

f.close()
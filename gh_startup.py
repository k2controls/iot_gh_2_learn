''' gh_startup.py
Initializes greenhouse by starting gpio service 
and setting configuration values based on host name.
Host name formate: greenhouseXXYY where XX is group and YY is number

Keith E. Kelly
7/19/2021
'''
import pigpio
from iot_gh.GHgpio import GHgpio
from iot_gh.GHFan import GHFan

def startup():
    ''' Startup code called during IoT Greenhouse startup

    Turns off fan (currently active high and pull-up enables. Change in future versions)
    Tests pb switch. If depressed during startup, run board test.
    '''
    print("Starting gpio services...")
    pi = pigpio.pi()
    fan = GHFan(pi, GHgpio.FAN)
    fan.off()

    print("Setting configuration...\n")
    
    with open('/etc/hostname', 'r') as file1:
        gh_name = file1.readlines()[0][:-1]
        gh_group = gh_name[-4:-2]
        gh_num = gh_name[-2:]
        print("Your greenhouse name is {0}".format(gh_name))
        print("Your group ID is {0}".format(gh_group))
        print("your greenhouse number is {0}".format(gh_num))
        print()
        with open('./gh.conf', 'w') as file2:
            config = [
                "[IOT_GREENHOUSE]\n",
                "HOUSE_ID: {0}\n".format(gh_name),
                "GROUP_ID: {0}\n".format(gh_group),    
                "HOUSE_NUMBER: {0}".format(gh_num)
                ]
            file2.writelines(config)

    print("Done.")    

if __name__ == "__main__":
    startup()

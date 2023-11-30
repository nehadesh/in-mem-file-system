from file_system import FileSystem
from directory import Directory
from command_center import CommandCenter

 
class bcolors:
    PINK = '\033[95m'
    LAVENDER = '\033[94m'
    CYAN = '\033[96m'  
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
 
def main(): 
	''' 
	    A terminal environment interface to explore Neha's File System. 
	    This serves as the main entry point of the file system and the
		interface by which you, as the user can operate on the system.
	''' 
	
	print(bcolors.LAVENDER + '''
        ╭─━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━─╮
        │                                    │
        │    Welcome to your file system!    │
        │    Type help for command info.     │
        │                                    │
        ╰─━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━─╯
    ''' + bcolors.ENDC)
	
    # TODO: I would set this attribute when the user changes if I 
    # had time to work on the extension
	currentUser = 'poweruser'
	
	fs = FileSystem()
	command_interpreter = CommandCenter(fs)
	
	while True: 
		cli_prefix = bcolors.BOLD + " 👑 " + currentUser + " 📁 " + fs.get_pwd().get_name() + " % " + bcolors.ENDC
		args = input(cli_prefix)
		args = args.split(" ")
		
		# The following execution gracefully handles errors so that this while 
        # loop will contnue to run - simulating an infinite "terminal" environment.
		command_interpreter.execute_command(args)

        
	
if __name__ == "__main__": 
	main() 
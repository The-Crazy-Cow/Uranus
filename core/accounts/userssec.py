import os,sys,time,subprocess,shutil

from utils.UranusException import UserssecException
from utils.UranusUtils import add_date_suffixe,Mk_backup


def Mk_sudoers_file(sudoers_file):
    """Mk_sudoers_file - take a ready sudoers conf file 
         and put it in /etc/sudoers.d/ dir and check conf via
            visudo"""

    if not os.path.exists(sudoers_file):
        raise UserssecException(f"file {str(sudoers_file)} doesn't exist")
    if not os.path.isfile(sudoers_file):
        raise UserssecException(f"sudoers file {str(sudoers_file)} not file")

    sudoers_dir = "/etc/sudoers.d/"
    if not os.path.exists(sudoers_dir):os.mkdir(sudoers_dir)

    #file creation
    shutil.copy(sudoers_file,
                sudoers_dir,
                follow_symlinks=False
            )#by the other hand copy2 conserve metada but don't util here

    #success creation checking
    filename = os.path.basename(sudoers_file)
    filename = os.path.join(sudoers_dir,filename) 
    if not os.path.exists(filename): 
        raise UserssecException(f"failed to create sudoers file {filename}")

    #add the current date suffixe to the filename
    final_name = add_date_suffixe(filename=filename)
    
    if os.path.exists(final_name):
        Mk_backup(final_name)
    os.rename(filename,final_name)

    subprocess.run(['chmod','-R','0440',
                    sudoers_dir],
                    shell=False
                )
    subprocess.run(['chown','-R','root:root',sudoers_dir],
                    shell=False
                )
    visudo_c()

def visudo_c ():
    """execute visudo with -c option for check all
            sudoers file configuration"""

    p=subprocess.Popen(['visudo','-c'],
                        shell=False,
                        stdout=subprocess.PIPE,
                        stderr=subprocess.PIPE
                    )
    stdout,stderr=p.communicate()
    out = stderr.decode('utf-8')
    if len(out): raise UserssecException(out)

    pass


    
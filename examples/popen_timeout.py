import time
import subprocess

def run_command(cmd, timeout=0):
    """Description: call subprocess to run command with timeout
       @param cmd: command could be string or list
       @param timeout: set to 0 if no timeout limit
       @return returncode, output: return code and output of cmd executed
    """
    start_time = time.time()
    cmd_str = str(cmd)
    print("running command %s" % cmd_str
    df = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    while timeout and df.poll() == None:
        if time.time()-start_time >= timeout:
            df.kill()
            print("timeout in running command %s exceed %d seconds" % (cmd_str, timeout))
            return -1, ""
    output = '\n'.join(df.communicate()).strip()
    print("command %s return with code: %d output:\n%s" % (cmd_str, df.returncode, output))
    return df.returncode, output
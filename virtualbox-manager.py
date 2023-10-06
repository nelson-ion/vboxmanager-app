#!/bin/python3
import subprocess

def listVMs():
    ## start with a list of VMs ##
    p = subprocess.Popen("VBoxManage list vms", stdout=subprocess.PIPE, shell=True) 
    (output, err) = p.communicate() 
    ## Wait for VBoxManage to terminate. Get return returncode ##
    p_status = p.wait()

    # split output text in lines
    vmsList = output.decode().split('\n')
    
    vmCount = 0
    for vm in vmsList:
        vmNameAndCode = vm.split(" ")
        if len(vmNameAndCode) == 2:
            vmCount+=1
            print(vmCount,"\t", vmNameAndCode[0])

print("Welcome!")
listVMs()
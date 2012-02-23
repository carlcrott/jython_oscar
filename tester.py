# run with:
# jython tester.py

# examples pulled/modified from:
# https://bitbucket.org/wwmm/oscar4/wiki/Examples

import sys

def setClassPath():
  libDir = "/home/thrive/java_projects/JARs/"
  classPaths = [
    "commons-lang-2.1.jar",
    "modified.jar",
    "oscar4-all-4.1-with-dependencies.jar",
  ]
  for classPath in classPaths:
    sys.path.append(libDir + classPath)

def runJavaClass(process):
  from modified import Oscarizer
  inst = Oscarizer()

  inst.setProcess(process)
  codified = inst.oscarParse()

  print "PARSED: \n", codified


def main(process):
  setClassPath()
  runJavaClass(process)


process = "To a solution of 3-bromobenzophenone (1.00 g, 4 mmol) in MeOH (15 mL) was added sodium borohydride (0.3 mL, 8 mmol) portionwise at rt and the suspension was stirred at rt for 1-24 h. The reaction was diluted slowly with water and extracted with CH2Cl2. The organic layer was washed successively with water, brine, dried over Na2SO4, and concentrated to give the title compound as oil (0.8 g, 79%), which was used in the next reaction without further purification. MS (ESI, pos. ion) m/z: 247.1 (M-OH)."


main(process)


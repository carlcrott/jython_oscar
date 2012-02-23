# Example

1. Compress "Oscarizer.class" into "modified.jar"

2. Place modified.jar into local jar repository 
EX: "/home/thrive/java_projects/JARs/" in this project instance

3. Edit libDir in tester.py ln:10 to the above local jar repository
<pre>
def setClassPath():
  libDir = "/home/thrive/java_projects/JARs/"
  classPaths = [
    "commons-lang-2.1.jar",
    "modified.jar",
    "oscar4-all-4.1-with-dependencies.jar",
  ]
</pre>

4. Compile ( Note: modified classpath for non-IDE developers )
<pre>
$ javac -classpath /home/thrive/java_projects/JARs/commons-lang-2.1.jar:/home/thrive/java_projects/JARs/oscar4-all-4.1-with-dependencies.jar Oscarizer.java
</pre>

5. Run
<pre>
$ jython tester.py
</pre>



##### should see something like:

<pre>
PARSED:
3-bromobenzophenone
 
MeOH
[Structure:INCHI:InChI=1/CH4O/c1-2/h2H,1H3]
 
sodium borohydride
[Structure:INCHI:InChI=1/BH4.Na/h1H4;/q-1;+1]
 
1-
 
water
[Structure:INCHI:InChI=1/H2O/h1H2]
 
CH2Cl2
[Structure:INCHI:InChI=1/CH2Cl2/c2-1-3/h1H2]
 
water
[Structure:INCHI:InChI=1/H2O/h1H2]
 
brine
 
Na2SO4
[Structure:INCHI:InChI=1/2Na.H2O4S/c;;1-5(2,3)4/h;;(H2,1,2,3,4)/q2*+1;/p-2/f2Na.O4S/q2m;-2]
 
ion
 
M-OH

</pre>



.. ===============LICENSE_START=======================================================
.. Licensed to the Apache Software Foundation (ASF) under one or more
.. contributor license agreements.  See the NOTICE file distributed with
.. this work for additional information regarding copyright ownership.
.. The ASF licenses this file to You under the Apache License, Version 2.0
.. (the "License"); you may not use this file except in compliance with
.. the License.  You may obtain a copy of the License at
.. 
..     http://www.apache.org/licenses/LICENSE-2.0
.. 
.. Unless required by applicable law or agreed to in writing, software
.. distributed under the License is distributed on an "AS IS" BASIS,
.. WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
.. See the License for the specific language governing permissions and
.. limitations under the License.
.. 
.. Modifications Copyright © 2018 AT&T Intellectual Property.
.. ===============LICENSE_END=========================================================

=================================
Zeppelin Notebook Developer Guide
=================================

To develop and test spark job on Hadoop, follow below steps.
   1. Configure Livy interpreter by updating below properties
      zeppelin.livy.keytab: full qualified kerberos keytab file to access Hadoop
      zeppelin.livy.principal: Kerberos principal to access Hadoop
      zeppelin.livy.url: Livy server URL with port  
	
   2. Develop spark script in languages python, R or Scala. Example code in Python as below
      %livy.pyspark


      # use sklearn to predict value if digital images

      from sklearn import grid_search, datasets

      from sklearn.ensemble import RandomForestClassifier

      from sklearn.grid_search import GridSearchCV

      from sklearn import svm



      digits = datasets.load_digits()


      print(digits.data)

      clf = svm.SVC(gamma=0.001, C=100.)

      clf.fit(digits.data[:-1], digits.target[:-1])  

      clf.predict(digits.data[11:20])

   3. Click run button to test

To develop python job, flow below steps.
   1. Check python interpreter, to confirm zeppelin.python points to right python version.

   2. Develop python script with example as below
      %python


      import matplotlib.pyplot as plt

      plt.figure()

      x = [1, 2, 3, 4, 5, 6, 7, 8]

      y = [20, 21, 20.5, 20.81, 21, 21.48, 22, 21.89]


      plt.plot(x, y, linestyle='dashed', marker='o', color='red') 

   3. Click run button to test 
 
To browse file system on hadoop, follow below steps.
   1. Configure file interpreter by updating below property.
      hdfs.url: webhdfs url.

   2. Create script with example as below
      %file
      ls -ltr /apps
      #above command will explore /apps folder on configured HDFS cluster.

   3. Click run button to test.
 

# Databricks notebook source
pip install PGPy

# COMMAND ----------

pip install --upgrade pip

# COMMAND ----------

pip install python-gnupg

# COMMAND ----------

pip install GnuPG

# COMMAND ----------

import gnupg
import os 

gpg=gnupg.GPG('/Users/tannut.tawornsan@lotuss.com/')
gpg.encoding = 'utf-8'

key_input_data = gpg.gen_key_input(
    name_email = 'tannut.tawornsan@lotuss.com',
    passphrase = 'mypasspharse',
    key_type = 'RSA',
    key_length = 1024
    )

key = gpg.gen_key(key_input_data)


print(key)



# COMMAND ----------

import gnupg
import os 

gpg = gnupg.GPG('/Users/tannut.tawornsan@lotuss.com/')

# dbfs:/FileStore/shared_uploads/tannut.tawornsan@lotuss.com/emp_info_20220228.txt
# /FileStore/tables/emp_info_20220228.txt

path ='/dbfs/FileStore/shared_uploads/tannut.tawornsan@lotuss.com/'
testfile = '/emp_info_20220228.txt'

with open(path + testfile, 'rb') as f:
    status = gpg.encrypt(f, ['tannut.tawornsan@lotuss.com'], output= path + testfile + ".encrypted")
    
print(status.ok)
print(status.stderr)

# COMMAND ----------

import gnupg
import os 
import pandas as pd 
#Key pair created successfully.
#Fingerprint: DE532B5CBB2D4E75CAF1EF60C93F0D89414FF66C
gpg = gnupg.GPG('/Users/tannut.tawornsan@lotuss.com/')

# dbfs:/FileStore/shared_uploads/tannut.tawornsan@lotuss.com/emp_info_20220228.txt
# /FileStore/tables/emp_info_20220228.txt

#/dbfs/FileStore/shared_uploads/tannut.tawornsan@lotuss.com/emp_info2_20220228_txt.gpg

path ='/dbfs/FileStore/shared_uploads/tannut.tawornsan@lotuss.com/'
testfile = '/emp_info2_20220228_txt.gpg'

    
with open(path + testfile, 'rb') as fin:
    b_data = fin.read()
str_data = b_data.decode('utf8')
gpg.decrypt(str_data, passphrase = 'mypasspharse',output= path +'test.csv')

  #decrypted_data = gpg.decrypt(str(encrypted_ascii_data),passphrase="password")


# COMMAND ----------

dbutils.notebook.entry_point.getDbutils().notebook().getContext().notebookPath().get()

# COMMAND ----------

import os 
path = '/dbfs/FileStore/shared_uploads/tannut.tawornsan@lotuss.com/'
for directory in os.listdir(path):
    print(directory)

# COMMAND ----------

# MAGIC %fs ls

# COMMAND ----------

f = open("/dbfs/FileStore/shared_uploads/tannut.tawornsan@lotuss.com/emp_info_20220228.txt", "r")

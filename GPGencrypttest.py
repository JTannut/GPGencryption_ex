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



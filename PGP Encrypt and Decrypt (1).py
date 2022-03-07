# Databricks notebook source
!pip install python-gnupg==0.4.8

# COMMAND ----------

import gnupg

# COMMAND ----------

gpg = gnupg.GPG()

# COMMAND ----------

# generate key
input_data = gpg.gen_key_input(
    name_email='tannut.tawornsan@lotuss.com',
    passphrase='txnnxt',
)
key = gpg.gen_key(input_data)
print(key)

# COMMAND ----------

# create ascii-readable versions of pub / private keys
ascii_armored_public_keys = gpg.export_keys(key.fingerprint)
ascii_armored_private_keys = gpg.export_keys(
    keyids=key.fingerprint,
    secret=True,
    passphrase='txnnxt',
)

# COMMAND ----------

# export
with open('EncrypttionKeytest01.asc', 'w') as f:
    f.write(ascii_armored_public_keys)
    f.write(ascii_armored_private_keys)

# COMMAND ----------

# import
with open('EncrypttionKeytest01.asc') as f:
    key_data = f.read()
import_result = gpg.import_keys(key_data)

for k in import_result.results:
    print(k)

# COMMAND ----------

# encrypt file
# path : /dbfs/FileStore/shared_uploads/tannut.tawornsan@lotuss.com/emp_info_20220304.txt

with open('/dbfs/FileStore/shared_uploads/tannut.tawornsan@lotuss.com/emp_info_20220304.txt', 'rb') as f:
    status = gpg.encrypt_file(
        file=f,
        recipients=['tannut.tawornsan@lotuss.com'],
        output='/dbfs/FileStore/shared_uploads/tannut.tawornsan@lotuss.com/emp_info_20220304_encrypted.txt.gpg',
    )

print(status.ok)
print(status.status)
print(status.stderr)
print('~'*50)

# COMMAND ----------

dbutils.fs.ls("/FileStore/shared_uploads/tannut.tawornsan@lotuss.com/")

# COMMAND ----------

df = spark.read.text("dbfs:/FileStore/shared_uploads/tannut.tawornsan@lotuss.com/emp_info_20220304_encrypted.txt.gpg")

display(df)

# COMMAND ----------

# decrypt file
with open('/dbfs/FileStore/shared_uploads/tannut.tawornsan@lotuss.com/emp_info_20220304_encrypted.txt.gpg', 'rb') as f:
    status = gpg.decrypt_file(
        file=f,
        passphrase='txnnxt',
        output='/dbfs/FileStore/shared_uploads/tannut.tawornsan@lotuss.com/emp_info_20220304_Decrypted.txt',
    )

print(status.ok)
print(status.status)
print(status.stderr)

# COMMAND ----------

df = spark.read.text("dbfs:/FileStore/shared_uploads/tannut.tawornsan@lotuss.com/emp_info_20220304_Decrypted.txt")

display(df)

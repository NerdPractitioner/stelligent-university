#! /usr/bin/env ruby

require 'aws-sdk'

kms_key_id = '564ed848-813d-4cbf-a30e-4cfbac14d358'

s3 = Aws::S3::EncryptionV2::Client.new(
    kms_key_id: kms_key_id,
    key_wrap_schema: :kms_context,
    content_encryption_schema: :aes_gcm_no_padding,
    security_profile: :v2
)

myfile = File.basename 'encfile'

s3.put_object(bucket:'bucket-forlambda-holmes', key:'secret', body: myfile)
s3.get_object(bucket:'bucket-forlambda-holmes', key:'secret').body.read

#write to console
File.write("decrypt", File.read(s3.get_object(bucket:'bucket-forlambda-holmes', key:'secret').body.read) )